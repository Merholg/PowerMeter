#!/usr/bin/env python3

# from mercury_rtu import MercuryRTU
from dataclasses import dataclass
from collections import namedtuple
import ctypes

c_uint8 = ctypes.c_uint8
c_uint32 = ctypes.c_uint32

RetAnswerFunctions = namedtuple('RetAnswerFunctions', 'Volume DirectActive DirectReactive')


@dataclass(frozen=True)
class Physics:
    VOLTAGE: int = 100
    CURRENT: int = 1000
    POWER: int = 100
    POWERFACTOR: int = 1000
    FREQUENCY: int = 100
    PHASEANGLE: int = 100
    NOSINRATIO: int = 100
    TEMPERATURE: int = 1


class ByteX2X6(ctypes.Union):
    """
    40
    Значение 1-го байта = 40 = 01000000 -   направление активной мощности – прямое (0),
                                            направление реактивной мощности – обратное (1).
    """

    class X2X6(ctypes.BigEndianStructure):
        """
        struct BYTE1DDB6
        {
            unsigned char DirectAPower:1; // Направление активной мощности: 0 – прямое; 1 – обратное.
            unsigned char DirectRPower:1; // Направление реактивной мощности: 0 – прямое; 1 – обратное.
            unsigned char B1          :6; // байт 1
        };
        """
        _pack_ = 1
        _fields_ = [
            ("direct_act", c_uint8, 1),
            ("direct_react", c_uint8, 1),
            ("b1", c_uint8, 6)
        ]

    _fields_ = [
        ("x2x6", X2X6),
        ("one_byte", c_uint8)
    ]


class B1B2B3B4B5B6:
    """
    //2.3.16 Чтение варианта исполнения. PRODUCTIONVAR
    //Поле данных ответа состоит из 6 байт
    struct PRODUCTIONVAR
    {
        //---------------------------------
        //---------------------------------
        //---------------------------------
        //---------------------------------
        //---------------------------------
    };
    """

    class ByteB1X2222(ctypes.Union):
        class B1X2222(ctypes.BigEndianStructure):
            """
            BYTE In:2;  // Iн : 0 - 5; 1 - 1; 2 - 10.
    	    BYTE Un:2;  // Uн Uн - номинальное напряжение В: 0 - 57,7; 1 - 230.
    	    BYTE ClR:2; // Cl R класс точности по реактивной энергии %: 0 - 0,2; 1 - 0,5; 2 - 1,0; 3 - 2,0.
    	    BYTE ClA:2; // Cl А класс точности по активной энергии %: 0 - 0,2; 1 - 0,5; 2 - 1,0; 3 - 2,0.
            """
            _pack_ = 1
            _fields_ = [
                ("In", c_uint8, 2),
                ("Un", c_uint8, 2),
                ("ClR", c_uint8, 2),
                ("ClA", c_uint8, 2)
            ]

        _fields_ = [
            ("b1x2222", B1X2222),
            ("one_byte", c_uint8)
        ]

    class ByteB2X41111(ctypes.Union):
        class B2X41111(ctypes.BigEndianStructure):
            """
            BYTE MeterConst:4;     // Постоянная счетчика имп/квт?ч 0 - 5000; 1 - 25000; 2 - 1250; 3 - 500; 4 - 1000; 5 - 250.
	        BYTE NPhase:1;         // Число фаз 0 - 3, 1 - 1
	        BYTE ProfMPower:1;     // Учет профиля средних мощностей 0 - нет, 1 - да
	        BYTE TempRange:1;      // Температурный диапазон°C 0 – 20, 1 – 40
	        BYTE NDirect:1;        // Число направлений 0 - 2, 1 - 1
            """
            _pack_ = 1
            _fields_ = [
                ("MeterConst", c_uint8, 4),
                ("NPhase", c_uint8, 1),
                ("ProfMPower", c_uint8, 1),
                ("TempRange", c_uint8, 1),
                ("NDirect", c_uint8, 1)
            ]

        _fields_ = [
            ("b2x41111", B2X41111),
            ("one_byte", c_uint8)
        ]

    class ByteB3X4211(ctypes.Union):
        class B3X4211(ctypes.BigEndianStructure):
            """
            BYTE NVarProd:4;       // No варианта исполнения 1 - 57,7В(1)5А10А5000имп./кВт*ч 2 - 230В5А60А500имп./кВт*ч 3 - 230В5А100А250имп./кВт*ч 4 - 230В(1)5А10А1000имп./кВт*ч
	        BYTE MeterType:2;      // Тип счетчика 0 - AR, 1 - A
	        BYTE Tarificator:1;    // Тарификатор 0 - внешний, 1 - внутренний
	        BYTE SumPhase:1;       // Суммирование фаз 0 - с учетом знака, 1 - по модулю
            """
            _pack_ = 1
            _fields_ = [
                ("NVarProd", c_uint8, 4),
                ("MeterType", c_uint8, 2),
                ("Tarificator", c_uint8, 1),
                ("SumPhase", c_uint8, 1)
            ]

        _fields_ = [
            ("x2x2x2x2", B3X4211),
            ("one_byte", c_uint8)
        ]

    class ByteB4X1121111(ctypes.Union):
        class B4X1121111(ctypes.BigEndianStructure):
            """
            BYTE EPlonb:1;         // Эл. помба верхней крышки 0 - нет, 1 - есть
	        BYTE ExSupp:1;         // Внешнее питание 0 - нет, 1 - есть
	        BYTE IFace:2;          // Интерфейс 0 - CAN, 1 - RS-485, 2 - резерв, 3 - нет
	        BYTE OPort:1;          // оптопорт 0 - нет, 1 - есть
	        BYTE ModemGSM:1;       // Модем GSM 0 - нет, 1 - есть
	        BYTE ModemPLM:1;       // Модем PLM 0 - нет, 1 - есть
	        BYTE Mem3:1;           // Память No3 0 - 65.5x8, 1 - 131x8
            """
            _pack_ = 1
            _fields_ = [
                ("EPlonb", c_uint8, 1),
                ("ExSupp", c_uint8, 1),
                ("IFace", c_uint8, 2),
                ("OPort", c_uint8, 1),
                ("ModemGSM", c_uint8, 1),
                ("ModemPLM", c_uint8, 1),
                ("Mem3", c_uint8, 1)
            ]

        _fields_ = [
            ("b4x1121111", B4X1121111),
            ("one_byte", c_uint8)
        ]

    class ByteB5X11111111(ctypes.Union):
        class B5X11111111(ctypes.BigEndianStructure):
            """
    	    BYTE PhCalcPower:1;    // Пофазный учет энергии A+ 0 - нет, 1 - да
    	    BYTE QPower:1;         // Контроль ПКЭ 0 - нет, 1 - да
	        BYTE SupIF1:1;         // Встроенное питание интерфейса 1 0 - нет, 1 - да
	        BYTE IFace2:1;         // Интерфейс 2 0 - нет, 1 - да
    	    BYTE CEPlomb:1;        // Флаг наличия эл. пломбы защитной крышки, 0 - нет, 1 - есть
	        BYTE TarMax:1;         // Флаг потарифного учета максимумов мощности, 0 - нет, 1 - есть
	        BYTE Light:1;          // Флаг наличия подсветки ЖКИ, 0 - нет, 1 - есть
	        BYTE Relay:1;          // Флаг наличия встроенного реле, 0 - нет, 1 - есть
            """
            _pack_ = 1
            _fields_ = [
                ("PhCalcPower", c_uint8, 1),
                ("QPower", c_uint8, 1),
                ("SupIF1", c_uint8, 1),
                ("IFace2", c_uint8, 1),
                ("CEPlomb", c_uint8, 1),
                ("TarMax", c_uint8, 1),
                ("Light", c_uint8, 1),
                ("Relay", c_uint8, 1)
            ]

        _fields_ = [
            ("b5x11111111", B5X11111111),
            ("one_byte", c_uint8)
        ]

    class ByteB6X11111111(ctypes.Union):
        class B6X11111111(ctypes.BigEndianStructure):
            """
	        BYTE ExControl:1;      // Флаг наличия аппаратных средств управления внешними устройствами отключения нагрузки, 0 - нет, 1 - есть
	        BYTE VoltTarif:1;      // Флаг переключения тарифов внешним напряжением, 0 - нет, 1 - да
	        BYTE BEPlomb:1;        // Флаг наличия эл.пломбы модульного отсека, 0 - нет, 1 - есть
	        BYTE Profile2:1;       // Флаг наличия профиля 2 0 - нет, 1 - есть
	        BYTE ModemPLC2:1;      // Модем PLC2, 0 - нет, 1 - есть
	        BYTE IEC61107:1;       // Флаг протокола IEC61107, 0 - нет, 1 - да
	        BYTE Reserved1:1;      // Reserved
	        BYTE Reserved2:1;      // Reserved
            """
            _pack_ = 1
            _fields_ = [
                ("ExControl", c_uint8, 1),
                ("VoltTarif", c_uint8, 1),
                ("BEPlomb", c_uint8, 1),
                ("Profile2", c_uint8, 1),
                ("ModemPLC2", c_uint8, 1),
                ("IEC61107", c_uint8, 1),
                ("Reserved1", c_uint8, 1),
                ("Reserved2", c_uint8, 1)
            ]

        _fields_ = [
            ("b6x11111111", B6X11111111),
            ("one_byte", c_uint8)
        ]

    @dataclass(frozen=True)
    class PVData:
        D = {
            {'In': {'Descript': 'Iн - номинальный ток А', 'Volumes': {0: '5', 1: '1', 2: '10'}}},
            {'Un': {'Descript': 'Uн - номинальное напряжение В', 'Volumes': {0: '57,7', 1: '230'}}},
            {'ClR': {'Descript': 'Cl R класс точности по реактивной энергии %',
                     'Volumes': {0: '0,2', 1: '0,5', 2: '1,0', 3: '2,0'}}},
            {'ClA': {'Descript': 'Cl А класс точности по активной энергии %',
                     'Volumes': {0: '0,2', 1: '0,5', 2: '1,0', 3: '2,0'}}},
            {'MeterConst': {'Descript': 'Постоянная счетчика имп/квт?ч',
                            'Volumes': {0: '5000', 1: '25000', 2: '1250', 3: '500', 4: '1000', 5: '250'}}},
            {'NPhase': {'Descript': 'Число фаз', 'Volumes': {0: '3', 1: '1'}}},
            {'ProfMPower': {'Descript': 'Учет профиля средних мощностей', 'Volumes': {0: 'нет', 1: 'да'}}},
            {'TempRange': {'Descript': 'Температурный диапазон°C', 'Volumes': {0: '20', 1: '40'}}},
            {'NDirect': {'Descript': 'Число направлений', 'Volumes': {0: '2', 1: '1'}}},
            {'NVarProd': {'Descript': 'No варианта исполнения',
                          'Volumes': {1: '57,7В(1)5А10А5000имп./кВт*ч', 2: '230В5А60А500имп./кВт*ч',
                                      3: '230В5А100А250имп./кВт*ч', 4: '230В(1)5А10А1000имп./кВт*ч'}}},
            {'MeterType': {'Descript': 'Тип счетчика', 'Volumes': {0: 'AR', 1: 'A'}}},
            {'Tarificator': {'Descript': 'Тарификатор', 'Volumes': {0: 'внешний', 1: 'внутренний'}}},
            {'SumPhase': {'Descript': 'Суммирование фаз', 'Volumes': {0: 'с учетом знака', 1: 'по модулю'}}},
            {'EPlomb': {'Descript': 'Эл. помба верхней крышки', 'Volumes': {0: 'нет', 1: 'есть'}}},
            {'ExSupp': {'Descript': 'Внешнее питание', 'Volumes': {0: 'нет', 1: 'есть'}}},
            {'IFace': {'Descript': 'Интерфейс', 'Volumes': {0: 'CAN', 1: 'RS-485', 2: 'резерв', 3: 'нет'}}},
            {'OPort': {'Descript': 'оптопорт', 'Volumes': {0: 'нет', 1: 'есть'}}},
            {'ModemGSM': {'Descript': 'Модем GSM', 'Volumes': {0: 'нет', 1: 'есть'}}},
            {'ModemPLM': {'Descript': 'Модем PLM', 'Volumes': {0: 'нет', 1: 'есть'}}},
            {'Mem3': {'Descript': 'Память No3', 'Volumes': {0: '65.5x8', 1: '131x8'}}},
            {'PhCalcPower': {'Descript': 'Пофазный учет энергии A+', 'Volumes': {0: 'нет', 1: 'да'}}},
            {'QPower': {'Descript': 'Контроль ПКЭ', 'Volumes': {0: 'нет', 1: 'да'}}},
            {'SupIF1': {'Descript': 'Встроенное питание интерфейса 1', 'Volumes': {0: 'нет', 1: 'да'}}},
            {'IFace2': {'Descript': 'Интерфейс 2', 'Volumes': {0: 'нет', 1: 'да'}}},
            {'CEPlomb': {'Descript': 'Флаг наличия эл. пломбы защитной крышки', 'Volumes': {0: 'нет', 1: 'есть'}}},
            {'TarMax': {'Descript': 'Флаг потарифного учета максимумов мощности',
                        'Volumes': {0: 'нет', 1: 'есть'}}},
            {'Light': {'Descript': 'Флаг наличия подсветки ЖКИ', 'Volumes': {0: 'нет', 1: 'есть'}}},
            {'Relay': {'Descript': 'Флаг наличия встроенного реле', 'Volumes': {0: 'нет', 1: 'есть'}}},
            {'ExControl': {
                'Descript': 'Флаг наличия аппаратных средств управления внешними устройствами отключения нагрузки',
                'Volumes': {0: 'нет', 1: 'есть'}}},
            {'VoltTarif': {'Descript': 'Флаг переключения тарифов внешним напряжением',
                           'Volumes': {0: 'нет', 1: 'да'}}},
            {'BEPlomb': {'Descript': 'Флаг наличия эл.пломбы модульного отсека', 'Volumes': {0: 'нет', 1: 'есть'}}},
            {'Profile2': {'Descript': 'Флаг наличия профиля 2', 'Volumes': {0: 'нет', 1: 'есть'}}},
            {'ModemPLC2': {'Descript': 'Модем PLC2', 'Volumes': {0: 'нет', 1: 'есть'}}},
            {'IEC61107': {'Descript': 'Флаг протокола IEC61107', 'Volumes': {0: 'нет', 1: 'да'}}},
            {'Reserved1': {'Descript': 'Reserved1', 'Volumes': {0: 'нет'}}},
            {'Reserved2': {'Descript': 'Reserved2', 'Volumes': {0: 'нет'}}}
        }

    def __init__(self, in_bytearray):
        super().__init__()
        m = 6
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

        self.byte_b1 = self.ByteB1X2222()
        self.byte_b2 = self.ByteB2X41111()
        self.byte_b3 = self.ByteB3X4211()
        self.byte_b4 = self.ByteB4X1121111()
        self.byte_b5 = self.ByteB5X11111111()
        self.byte_b6 = self.ByteB6X11111111()

        self.byte_b1.one_byte = self.in_bytearray[0]
        self.byte_b2.one_byte = self.in_bytearray[1]
        self.byte_b3.one_byte = self.in_bytearray[2]
        self.byte_b4.one_byte = self.in_bytearray[3]
        self.byte_b5.one_byte = self.in_bytearray[4]
        self.byte_b6.one_byte = self.in_bytearray[5]

        self.volume = int.from_bytes(self.byte_b1.b1x2222.In)
        self.PVvar = self.PVData.D.get('In', {'Descript': 'Unknown', 'Volumes': {0: 'None'}})

        # self.volume = int.from_bytes(bytearray([self.in_bytearray[0], self.in_bytearray[1]]),
        #                              byteorder='big', signed=False)


class B1B2:
    """
    struct BYTE12
    {
        unsigned char B1          :8; //байт 1
        unsigned char B2          :8; //байт 2
    };
    """

    def __init__(self, in_bytearray):
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

    def __init__(self, in_bytearray):
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

    def __init__(self, in_bytearray):
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

    def __init__(self, in_bytearray):
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

    def __init__(self, in_bytearray):
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

    def __init__(self, in_bytearray):
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


def answer_081111h(in_bytearray):
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
    trust_bytearray = in_bytearray[:] if isinstance(in_bytearray, bytearray) and (
            len(in_bytearray) == m) else bytearray([0] * m)

    for i in range(0, m, k):
        power = B1B3B2(trust_bytearray[i:i + k])
        phase[len(phase)] = RetAnswerFunctions(Volume=(power.volume / Physics.VOLTAGE),
                                               DirectActive=0, DirectReactive=0)

    return phase


def answer_081408h(in_bytearray):
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
    N1 = 0029E7h = 10727d S1 = 10727/100 = 107,27 Вт
    фаза 0 - сумма фаз
    :param in_bytearray: возвращаемая при вызове запроса 0814h последовательность байт в виде байтмассива
    :return: словарь с кортежем -  фаза: (величина, направление активной мощности , направление реактивной мощности)
    """
    phase = dict()
    m = 16  # общая длина последовательности
    k = 4  # длина последовательности по каждой фазе
    trust_bytearray = in_bytearray[:] if isinstance(in_bytearray, bytearray) and (
            len(in_bytearray) == m) else bytearray([0] * m)

    for i in range(0, m, k):
        power = B2B1x2x6B4B3(trust_bytearray[i:i + k])
        phase[len(phase)] = RetAnswerFunctions(Volume=(power.volume / Physics.POWER),
                                               DirectActive=power.direct_active, DirectReactive=power.direct_reactive)

    return phase


if __name__ == '__main__':
    print(answer_081111h(bytearray([0x00, 0x2D, 0x02])))
    # must be {0: RetAnswerFunctions(Volume=5.57, DirectActive=0, DirectReactive=0)}
    print(answer_081408h(bytearray([0x00, 0x40, 0xE7, 0x29, 0x00, 0x40, 0xE7, 0x29,
                                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])))
    # must be {0: RetAnswerFunctions(Volume=107.27, DirectActive=1, DirectReactive=-1),
    #          1: RetAnswerFunctions(Volume=107.27, DirectActive=1, DirectReactive=-1),
    #          2: RetAnswerFunctions(Volume=0.0, DirectActive=1, DirectReactive=1),
    #          3: RetAnswerFunctions(Volume=0.0, DirectActive=1, DirectReactive=1)}
