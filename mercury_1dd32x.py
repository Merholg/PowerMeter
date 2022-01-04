#!/usr/bin/env python3

import ctypes

c_uint8 = ctypes.c_uint8
c_uint32 = ctypes.c_uint32


class Byte1DD32x(ctypes.Union):
    class B1DD32X(ctypes.BigEndianStructure):
        """
        struct BYTE1DD32
        {
            unsigned char DirectAPower:1; // Направление активной мощности: 0 – прямое; 1 – обратное.
            unsigned char DirectRPower:1; // Направление реактивной мощности: 0 – прямое; 1 – обратное.
            unsigned char B1          :6; //байт 1
            unsigned char B3          :8; //байт 3
            unsigned char B2          :8; //байт 2
        };

        40 2D 02
        Значение коэффициента мощности по сумме фаз:
        Значение 1-го байта = 40 = 01000000 - направление активной мощности – прямое (0),
        направление реактивной мощности – обратное (1).
        N = 0x22D = 557
        """
        _pack_ = 1
        _fields_ = [
            ("direct_act", c_uint32, 1),
            ("direct_react", c_uint32, 1),
            ("b1", c_uint32, 6),
            ("b3", c_uint32, 8),
            ("b2", c_uint32, 8),
            ("b0", c_uint32, 8)
        ]

    _fields_ = [
        ("byte1dd32x", B1DD32X),
        ("bytes4", c_uint32)
    ]

    def __init__(self, inputbytearray=bytearray(), fourbytes=0):
        super().__init__()
        self.in_bytearray = inputbytearray
        self.bytes4 = fourbytes

    def unpack(self, inbytearray):
        self.in_bytearray = inbytearray
        self.bytes4 = int.from_bytes(inbytearray, byteorder='little', signed=False)
        return 1 if self.byte1dd32x.direct_act == 0 else -1, 1 if self.byte1dd32x.direct_react == 0 else -1, \
            int.from_bytes(bytearray([self.byte1dd32x.b1, self.byte1dd32x.b2, self.byte1dd32x.b3]),
                           byteorder='big', signed=False)


if __name__ == '__main__':
    sequence = Byte1DD32x()
    print(sequence.unpack(bytearray([0x40, 0x2D, 0x02])))
    print(hex(sequence.bytes4))
    print(sequence.byte1dd32x.direct_act)
    print(sequence.byte1dd32x.direct_react)
    print(hex(sequence.byte1dd32x.b0))
    print(hex(sequence.byte1dd32x.b1))
    print(hex(sequence.byte1dd32x.b2))
    print(hex(sequence.byte1dd32x.b3))
