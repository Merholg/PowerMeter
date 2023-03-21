#!/usr/bin/env python3

# from mercury_rtu import MercuryRTU
from enum import Enum
import ctypes

c_uint8 = ctypes.c_uint8
c_uint32 = ctypes.c_uint32


# class Mercury23x:
#     """
#
#     """
#
#     def __init__(self):
#         self.meters = dict()
#
#     def get_meter(self, address):
#         pass
#
#    def search_meters(self, begin_address, end_address):
#        begin_address = MercuryRTU.Address.BROADCAST if begin_address < MercuryRTU.Address.BEGIN or \
#                                                        begin_address > MercuryRTU.Address.END else begin_address
#        if begin_address == MercuryRTU.Address.BROADCAST:
#            end_address = MercuryRTU.Address.BROADCAST
#        else:
#            end_address = MercuryRTU.Address.END if end_address < MercuryRTU.Address.BEGIN or \
#                                                    end_address > MercuryRTU.Address.END else end_address
#        if end_address >= begin_address:
#            address = begin_address
#            while address <= end_address:
#                error_num, error_str, recv_sequence, recv_address = MercuryRTU.conversion(address, bytearray[0x00], 1)
#                if 0 == error_num and not (recv_address in self.meters):
#                    self.meters[recv_address] = (0, bytearray[0x00], bytearray[0x00, 0x00, 0x00, 0x00, 0x00, 0x00])


class Physics(Enum):
    VOLTAGE = 100
    CURRENT = 1000
    POWER = 100
    POWERFACTOR = 1000
    FREQUENCY = 100
    PHASEANGLE = 100
    NOSINRATIO = 100
    TEMPERATURE = 1


class ByteX2X6(ctypes.Union):
    class X2X6(ctypes.BigEndianStructure):
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
        ("x2x6", X2X6),
        ("one_byte", c_uint8)
    ]


class B1x2x6B3B2:
    def __init__(self, in_bytearray=bytearray([0, 0, 0])):
        super().__init__()
        if len(in_bytearray) < 3:
            self.in_bytearray = bytearray([0, 0, 0])
        elif len(in_bytearray) > 3:
            self.in_bytearray = in_bytearray[:3]
        else:
            self.in_bytearray = in_bytearray[:]
        self.byte_ddb6 = ByteX2X6()

        self.byte_ddb6.one_byte = self.in_bytearray[0]
        self.direct_active = 1 if self.byte_ddb6.x2x6.direct_act == 0 else -1
        self.direct_reactive = 1 if self.byte_ddb6.x2x6.direct_react == 0 else -1
        self.volume = int.from_bytes(bytearray([self.byte_ddb6.x2x6.b1, self.in_bytearray[2], self.in_bytearray[1]]),
                                     byteorder='big', signed=False)


def sequence_b2ddb1b4b3(in_bytearray=bytearray([0, 0, 0, 0])):
    if len(in_bytearray) < 4:
        return 0, 0, 0
    byte_ddb6 = ByteX2X6()
    byte_ddb6.one_byte = in_bytearray[1]
    direct_active = 1 if byte_ddb6.dd6b.direct_act == 0 else -1
    direct_reactive = 1 if byte_ddb6.dd6b.direct_react == 0 else -1
    volume = int.from_bytes(bytearray([byte_ddb6.dd6b.b1, in_bytearray[0], in_bytearray[3], in_bytearray[2]]),
                            byteorder='big', signed=False)
    return direct_active, direct_reactive, volume


def answer_0811h(in_bytearray=bytearray([0, 0, 0])):
    """
    фаза 0 - сумма фаз
    :param in_bytearray: возвращаемая при вызове запроса 0811h последовательность байт в виде байтмассива
    :return: словарь с кортежем -  фаза: (направление активной мощности , направление реактивной мощности, величина)
    """
    phase = dict()
    phase[0] = sequence_ddb1b3b2(in_bytearray)
    return phase


def answer_0814h(in_bytearray=bytearray([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])):
    """
    00 40 E7 29 00 40 E7 29 00 00 00 00 00 00 00 00
    Значение полной мощности по сумме фаз:
        Значение 1-го байта = 40 = 01000000 - направление активной мощности – прямое,
                                              направление реактивной мощности – обратное.
        N = 0029E7h = 10727d    S = 10727/100 = 107,27 Вт
        N1 = 0029E7h = 10727d   S1 = 10727/100 = 107,27 Вт
    фаза 0 - сумма фаз
    :param in_bytearray: возвращаемая при вызове запроса 0814h последовательность байт в виде байтмассива
    :return: словарь с кортежем -  фаза: (направление активной мощности , направление реактивной мощности, величина)
    """
    phase = dict()
    if len(in_bytearray) >= 4:
        j = len(in_bytearray) if len(in_bytearray) < 16 else 16
        for i in range(0, j, 4):
            k = len(phase)
            phase[k] = sequence_b2ddb1b4b3(in_bytearray[i:i + 4])
    j = len(phase)
    for i in range(j, 4):
        k = len(phase)
        phase[k] = (0, 0, 0)
    return phase


if __name__ == '__main__':
    print(answer_0811h(bytearray([0x40, 0x2D, 0x02])))
    # must be {0: (1, -1, 557)}
    print(answer_0814h(bytearray([0x00, 0x40, 0xE7, 0x29, 0x00, 0x40, 0xE7, 0x29,
                                  0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])))
    # must be {0: (1, -1, 10727), 1: (1, -1, 10727), 2: (1, 1, 0), 3: (1, 1, 0)}
