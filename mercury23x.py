#!/usr/bin/env python3

import ctypes

c_uint8 = ctypes.c_uint8


class ByteDDB6(ctypes.Union):
    class DDB6(ctypes.BigEndianStructure):
        """
        struct BYTE1DDB6
        {
            unsigned char DirectAPower:1; // Направление активной мощности: 0 – прямое; 1 – обратное.
            unsigned char DirectRPower:1; // Направление реактивной мощности: 0 – прямое; 1 – обратное.
            unsigned char B1          :6; // байт 1
        };

        40
        Значение 1-го байта = 40 = 01000000 - направление активной мощности – прямое (0),
        направление реактивной мощности – обратное (1).

        """
        _pack_ = 1
        _fields_ = [
            ("direct_act", c_uint8, 1),
            ("direct_react", c_uint8, 1),
            ("b1", c_uint8, 6),
        ]

    _fields_ = [
        ("dd6b", DDB6),
        ("one_byte", c_uint8)
    ]


def sequence_ddb1b3b2(in_bytearray=bytearray([0, 0, 0])):
    if len(in_bytearray) < 3:
        return 0, 0, 0
    byte_ddb6 = ByteDDB6()
    byte_ddb6.one_byte = in_bytearray[0]
    direct_active = 1 if byte_ddb6.dd6b.direct_act == 0 else -1
    direct_reactive = 1 if byte_ddb6.dd6b.direct_react == 0 else -1
    volume = int.from_bytes(bytearray([byte_ddb6.dd6b.b1, in_bytearray[2], in_bytearray[1]]),
                            byteorder='big', signed=False)
    return direct_active, direct_reactive, volume


def sequence_b2ddb1b4b3(in_bytearray=bytearray([0, 0, 0, 0])):
    if len(in_bytearray) < 4:
        return 0, 0, 0
    byte_ddb6 = ByteDDB6()
    byte_ddb6.one_byte = in_bytearray[1]
    direct_active = 1 if byte_ddb6.dd6b.direct_act == 0 else -1
    direct_reactive = 1 if byte_ddb6.dd6b.direct_react == 0 else -1
    volume = int.from_bytes(bytearray([byte_ddb6.dd6b.b1, in_bytearray[0], in_bytearray[3], in_bytearray[2]]),
                            byteorder='big', signed=False)
    return direct_active, direct_reactive, volume


def answer_0811h(in_bytearray=bytearray([0, 0, 0])):
    """
    :param in_bytearray: возвращаемая при вызове запроса 11h последовательность байт в виде байтмассива
    :return: кортеж -  направление активной мощности , направление реактивной мощности, величина мощности
    """
    phase = list()
    phase.append(sequence_ddb1b3b2(in_bytearray))
    return phase


def answer_0814h(in_bytearray=bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])):
    """
    00 40 E7 29 00 40 E7 29 00 00 00 00 00 00 00 00
    Значение полной мощности по сумме фаз:
        Значение 1-го байта = 40 = 01000000 - направление активной мощности – прямое,
                                              направление реактивной мощности – обратное.
        N = 0029E7h = 10727d    S = 10727/100 = 107,27 Вт
        N1 = 0029E7h = 10727d   S1 = 10727/100 = 107,27 Вт
    :param in_bytearray:
    :return:
    """
    phase = list()
    if len(in_bytearray) >= 4:
        j = len(in_bytearray) if len(in_bytearray) < 16 else 16
        for i in range(0, j, 4):
            phase.append(sequence_b2ddb1b4b3(in_bytearray[i:i + 4]))
    j = len(phase)
    for i in range(j, 4):
        phase.append((0, 0, 0))
    return phase


if __name__ == '__main__':
    print(answer_0811h(bytearray([0x40, 0x2D, 0x02])))
    # must be [(1, -1, 557)]
    print(answer_0814h(bytearray([0x00, 0x40, 0xE7, 0x29, 0x00, 0x40, 0xE7, 0x29,
                                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])))
    # must be [(1, -1, 10727), (1, -1, 10727), (1, 1, 0), (1, 1, 0)]
