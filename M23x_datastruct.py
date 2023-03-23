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


class B1B2:
    """
    struct BYTE12
    {
        unsigned char B1          :8; //байт 1
        unsigned char B2          :8; //байт 2
    };
    """

    def __init__(self, in_bytearray=bytearray([0] * 2)):
        super().__init__()
        m = 2
        if isinstance(in_bytearray, bytearray):
            n = len(in_bytearray)
            if n < m:
                self.in_bytearray = in_bytearray[:]
                for i in range(m - n):
                    self.in_bytearray.append(0)
            else:
                self.in_bytearray = in_bytearray[:m]
        else:
            self.in_bytearray = bytearray([0] * m)

        self.direct_active = 0
        self.direct_reactive = 0
        self.volume = int.from_bytes(bytearray([self.in_bytearray[0], self.in_bytearray[1]]),
                                     byteorder='big', signed=False)


class B2B1:
    """
    struct BYTE21
    {
        unsigned char B2          :8; //байт 2
        unsigned char B1          :8; //байт 1
    };
    """

    def __init__(self, in_bytearray=bytearray([0] * 2)):
        super().__init__()
        m = 2
        if isinstance(in_bytearray, bytearray):
            n = len(in_bytearray)
            if n < m:
                self.in_bytearray = in_bytearray[:]
                for i in range(m - n):
                    self.in_bytearray.append(0)
            else:
                self.in_bytearray = in_bytearray[:m]
        else:
            self.in_bytearray = bytearray([0] * m)

        self.direct_active = 0
        self.direct_reactive = 0
        self.volume = int.from_bytes(bytearray([self.in_bytearray[1], self.in_bytearray[0]]),
                                     byteorder='big', signed=False)


class B1B3B2:
    """
    struct BYTE132
    {
        unsigned char B1          :8; //байт 1
        unsigned char B3          :8; //байт 3
        unsigned char B2          :8; //байт 2
    };
    """

    def __init__(self, in_bytearray=bytearray([0] * 3)):
        super().__init__()
        m = 3
        if isinstance(in_bytearray, bytearray):
            n = len(in_bytearray)
            if n < m:
                self.in_bytearray = in_bytearray[:]
                for i in range(m - n):
                    self.in_bytearray.append(0)
            else:
                self.in_bytearray = in_bytearray[:m]
        else:
            self.in_bytearray = bytearray([0] * m)

        self.direct_active = 0
        self.direct_reactive = 0
        self.volume = int.from_bytes(bytearray([self.in_bytearray[0], self.in_bytearray[2], self.in_bytearray[1]]),
                                     byteorder='big', signed=False)


class B2B1B4B3:
    """
    struct BYTE2143
    {
        unsigned char B2          :8; //байт 2
        unsigned char B1          :8; //байт 1
        unsigned char B4          :8; //байт 4
        unsigned char B3          :8; //байт 3
    };
    """

    def __init__(self, in_bytearray=bytearray([0] * 4)):
        super().__init__()
        m = 4
        if isinstance(in_bytearray, bytearray):
            n = len(in_bytearray)
            if n < m:
                self.in_bytearray = in_bytearray[:]
                for i in range(m - n):
                    self.in_bytearray.append(0)
            else:
                self.in_bytearray = in_bytearray[:m]
        else:
            self.in_bytearray = bytearray([0] * m)

        self.direct_active = 0
        self.direct_reactive = 0
        self.volume = int.from_bytes(bytearray([self.in_bytearray[1], self.in_bytearray[0], self.in_bytearray[3],
                                                self.in_bytearray[2]]), byteorder='big', signed=False)


class B1x2x6B3B2:
    """
    struct BYTE1DD32
    {
        unsigned char B1          :6; //байт 1
        unsigned char DirectRPower:1; // Направление реактивной мощности: 0 – прямое; 1 – обратное.
        unsigned char DirectAPower:1; // Направление активной мощности: 0 – прямое; 1 – обратное.
        unsigned char B3          :8; //байт 3
        unsigned char B2          :8; //байт 2
    };
    """

    def __init__(self, in_bytearray=bytearray([0] * 3)):
        super().__init__()
        m = 3
        if isinstance(in_bytearray, bytearray):
            n = len(in_bytearray)
            if n < m:
                self.in_bytearray = in_bytearray[:]
                for i in range(m - n):
                    self.in_bytearray.append(0)
            else:
                self.in_bytearray = in_bytearray[:m]
        else:
            self.in_bytearray = bytearray([0] * m)
        self.byte_ddb6 = ByteX2X6()

        self.byte_ddb6.one_byte = self.in_bytearray[0]
        self.direct_active = 1 if self.byte_ddb6.x2x6.direct_act == 0 else -1
        self.direct_reactive = 1 if self.byte_ddb6.x2x6.direct_react == 0 else -1
        self.volume = int.from_bytes(bytearray([self.byte_ddb6.x2x6.b1, self.in_bytearray[2], self.in_bytearray[1]]),
                                     byteorder='big', signed=False)


class B2B1x2x6B4B3:
    """
    struct BYTE21DD43
    {
        unsigned char B2          :8; //байт 2
        unsigned char B1          :6; //байт 1
        unsigned char DirectRPower:1; // Направление реактивной мощности: 0 – прямое; 1 – обратное.
        unsigned char DirectAPower:1; // Направление активной мощности: 0 – прямое; 1 – обратное.
        unsigned char B4          :8; //байт 4
        unsigned char B3          :8; //байт 3
    };
    """

    def __init__(self, in_bytearray=bytearray([0] * 4)):
        super().__init__()
        m = 4
        if isinstance(in_bytearray, bytearray):
            n = len(in_bytearray)
            if n < m:
                self.in_bytearray = in_bytearray[:]
                for i in range(m - n):
                    self.in_bytearray.append(0)
            else:
                self.in_bytearray = in_bytearray[:m]
        else:
            self.in_bytearray = bytearray([0] * m)
        self.byte_ddb6 = ByteX2X6()

        self.byte_ddb6.one_byte = self.in_bytearray[1]
        self.direct_active = 1 if self.byte_ddb6.x2x6.direct_act == 0 else -1
        self.direct_reactive = 1 if self.byte_ddb6.x2x6.direct_react == 0 else -1
        self.volume = int.from_bytes(bytearray([self.byte_ddb6.x2x6.b1, self.in_bytearray[0], self.in_bytearray[3],
                                                self.in_bytearray[2]]), byteorder='big', signed=False)


def answer_081111h(in_bytearray=bytearray([0] * 3)):
    """
    Прочитать напряжения по 1-ой фазе для счетчика с сетевым адресом 128 (используем запрос с номером 11h).
    Запрос: 80 08 11 11 (CRC)
    Ответ: 80 00 5B 56 (CRC)
    Значение напряжения на 1-ой фазе
    N = 00565Bh = 22423d U = 22423/100 = 224,43 В
    фаза 0 - сумма фаз
    :param in_bytearray: возвращаемая при вызове запроса 0811h последовательность байт в виде байтмассива
    :return: словарь с кортежем -  фаза: (величина, направление активной мощности , направление реактивной мощности)
    """
    phase = dict()
    m = 3  # общая длина последовательности
    k = 3  # длина последовательности по каждой фазе
    if isinstance(in_bytearray, bytearray):
        n = len(in_bytearray)
        if n < m:
            trust_bytearray = in_bytearray[:]
            for i in range(m - n):
                trust_bytearray.append(0)
        else:
            trust_bytearray = in_bytearray[:m]
    else:
        trust_bytearray = bytearray([0] * m)

    j = 0
    for i in range(0, m, k):
        power = B1B3B2(trust_bytearray[i:i + k])
        phase[j] = (power.volume / Physics.VOLTAGE, 0, 0)
        j += 1

    return phase


def answer_081408h(in_bytearray=bytearray([0] * 16)):
    """
    Прочитать мгновенную полную мощность по сумме фаз для счетчика с сетевым адресом 128 (используем запрос с номером 14h).
    Запрос: 80 08 14 08 (CRC)
    Ответ: 80 00 40 E7 29 00 40 E7 29 00 00 00 00 00 00 00 00 (CRC)
    Значение мгновенной полной мощности по сумме фаз - 4 BYTE
    Значение мгновенной полной мощности по 1-ой фазе - 4 BYTE
    Значение мгновенной полной мощности по 2-ой фазе - 4 BYTE
    Значение мгновенной полной мощности по 3-ей фазе - 4 BYTE

    Значение полной мощности по сумме фаз:
    Значение 1-го байта = 40 = 01000000 - направление активной мощности – прямое, направление реактивной мощности – обратное.
    N = 0029E7h = 10727d S = 10727/100 = 107,27 Вт
    N 1 = 0029E7h = 10727d S 1 = 10727/100 = 107,27 Втфаза 0 - сумма фаз
    :param in_bytearray: возвращаемая при вызове запроса 0814h последовательность байт в виде байтмассива
    :return: словарь с кортежем -  фаза: (направление активной мощности , направление реактивной мощности, величина)
    """
    phase = dict()
    m = 16  # общая длина последовательности
    k = 4  # длина последовательности по каждой фазе
    if isinstance(in_bytearray, bytearray):
        n = len(in_bytearray)
        if n < m:
            trust_bytearray = in_bytearray[:]
            for i in range(m - n):
                trust_bytearray.append(0)
        else:
            trust_bytearray = in_bytearray[:m]
    else:
        trust_bytearray = bytearray([0] * m)

    j = 0
    for i in range(0, m, k):
        power = B2B1x2x6B4B3(trust_bytearray[i:i + k])
        phase[j] = (power.volume / Physics.POWER, power.direct_active, power.direct_reactive)
        j += 1

    return phase


if __name__ == '__main__':
    print(answer_081111h(bytearray([0x40, 0x2D, 0x02])))
    # must be {0: (1, -1, 557)}
    print(answer_081408h(bytearray([0x00, 0x40, 0xE7, 0x29, 0x00, 0x40, 0xE7, 0x29,
                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])))
    # must be {0: (1, -1, 10727), 1: (1, -1, 10727), 2: (1, 1, 0), 3: (1, 1, 0)}
