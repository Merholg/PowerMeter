#!/usr/bin/env python3

# from mercury_rtu import MercuryRTU
from dataclasses import dataclass
from collections import namedtuple
import ctypes

c_uint8 = ctypes.c_uint8
c_uint32 = ctypes.c_uint32

StatusVar = namedtuple('StatusVar', 'Descript Volumes')
DecodedAnswer = namedtuple('DecodedAnswer', 'Descr StrVolume DigVolume')
Req0811xxh = namedtuple('Req0811xxh', 'ClassPTR Descr Factor')


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


class STATEWORD:
    """
    2.3.11 Чтение байт состояния.
    Команда предназначена для чтения слова состояния счетчика.
    Код параметра – 0Ah.
    Поле параметров отсутствует.
    Поле данных ответа состоит из 6 байт. Информация в слове состояния содержится в пози-
    ционном коде и, в основном, определяет наличие аппаратных или логических внутренних оши-
    бок счетчика. Структура слова состояния счетчиков приведена в Приложении А - Самодиагно-
    стика счётчика.
    Пример:
    Прочитать слово состояния счетчика с сетевым адресом 128.
    Запрос: 80 08 0A (CRC)
    Ответ: 80 00 00 00 00 04 00 (CRC)
    Ошибка «E-03» – нарушено функционирование UART1
    """

    class ByteX11111111(ctypes.Union):
        class X11111111(ctypes.BigEndianStructure):
            _pack_ = 1
            _fields_ = [
                ("BIT8", c_uint8, 1),
                ("BIT7", c_uint8, 1),
                ("BIT6", c_uint8, 1),
                ("BIT5", c_uint8, 1),
                ("BIT4", c_uint8, 1),
                ("BIT3", c_uint8, 1),
                ("BIT2", c_uint8, 1),
                ("BIT1", c_uint8, 1)
            ]

        _fields_ = [
            ("x11111111", X11111111),
            ("one_byte", c_uint8)
        ]

    @dataclass(frozen=True)
    class SWData:
        D = {
            "E01": "Напряжение батарейки ниже 2.2(В)",
            "E02": "Нарушено функционирование памяти2",
            "E03": "Нарушено функционирование UART",
            "E04": "Нарушено функционирование ADS",
            "E05": "Ошибка обмена с памятью1",
            "E06": "Неисправность часов",
            "E07": "Нарушено функционирование памяти3",
            "E08": "",
            "E09": "Ошибка КС ПО",
            "E10": "Ошибка калибровочных коэффициентов",
            "E11": "Ошибка регистров накопленной энергии",
            "E12": "Ошибка сетевого адреса",
            "E13": "Ошибка серийного номера",
            "E14": "Поврежден пароль",
            "E15": "Ошибка массива вариантов исполнения",
            "E16": "Поврежден флаг тарификатора",
            "E17": "Поврежден флаг отключения нагрузки",
            "E18": "Ошибка лимита мощности",
            "E19": "Ошибка лимита энергии",
            "E20": "Нарушение параметров UART",
            "E21": "Ошибка параметров индикации по тарифам",
            "E22": "Ошибка параметров индикации по периодам",
            "E23": "Повреждение множителя таймаута",
            "E24": "Поврежден байт программируемых флагов",
            "E25": "Повреждено расписание праздничных дней",
            "E26": "Повреждено тарифное расписание",
            "E27": "Поврежден массив таймера",
            "E28": "Ошибка сезонных переходов",
            "E29": "Ошибка местоположения прибора",
            "E30": "Повреждены коэффициенты трансформации",
            "E31": "Повреждены регистры накопления",
            "E32": "Ошибка параметров среза",
            "E33": "Повреждены регистры среза",
            "E34": "Ошибка указателей журнала событий",
            "E35": "Ошибка записи журнала событий",
            "E36": "Повреждение регистра учета технических потерь",
            "E37": "Ошибка мощностей технических потерь",
            "E38": "Ошибка регистров накопленной энергии потерь",
            "E39": "Повреждены регистры пофазного учета",
            "E40": "Флаг поступления широковещ. сообщения",
            "E41": "Повреждение указателей журнала ПКЭ",
            "E42": "Ошибка записи журнала ПКЭ",
            "E43": "",
            "E44": "",
            "E45": "",
            "E46": "",
            "E47": "Выполнение процедуры коррекции времени",
            "E48": "Напряжение батарейки ниже 2.65(В)"
        }

    m = 6

    def __init__(self, in_bytearray):
        super().__init__()
        if isinstance(in_bytearray, bytearray):
            self.n = len(in_bytearray)
            if self.n < STATEWORD.m:
                self.in_bytearray = in_bytearray[:]
                for i in range(STATEWORD.m - self.n):
                    self.in_bytearray.append(0)
            else:
                self.in_bytearray = in_bytearray[:STATEWORD.m]
        else:
            self.in_bytearray = bytearray([0] * STATEWORD.m)

        self.byte_b1 = self.ByteX11111111()
        self.byte_b2 = self.ByteX11111111()
        self.byte_b3 = self.ByteX11111111()
        self.byte_b4 = self.ByteX11111111()
        self.byte_b5 = self.ByteX11111111()
        self.byte_b6 = self.ByteX11111111()
        self.byte_b1.one_byte = self.in_bytearray[4]
        self.byte_b2.one_byte = self.in_bytearray[5]
        self.byte_b3.one_byte = self.in_bytearray[2]
        self.byte_b4.one_byte = self.in_bytearray[3]
        self.byte_b5.one_byte = self.in_bytearray[0]
        self.byte_b6.one_byte = self.in_bytearray[1]

        self.status_val = dict()
        self.status_val['E01'] = self.byte_b1.x11111111.BIT1
        self.status_val['E02'] = self.byte_b1.x11111111.BIT2
        self.status_val['E03'] = self.byte_b1.x11111111.BIT3
        self.status_val['E04'] = self.byte_b1.x11111111.BIT4
        self.status_val['E05'] = self.byte_b1.x11111111.BIT5
        self.status_val['E06'] = self.byte_b1.x11111111.BIT6
        self.status_val['E07'] = self.byte_b1.x11111111.BIT7
        self.status_val['E08'] = self.byte_b1.x11111111.BIT8
        self.status_val['E09'] = self.byte_b2.x11111111.BIT1
        self.status_val['E10'] = self.byte_b2.x11111111.BIT2
        self.status_val['E11'] = self.byte_b2.x11111111.BIT3
        self.status_val['E12'] = self.byte_b2.x11111111.BIT4
        self.status_val['E13'] = self.byte_b2.x11111111.BIT5
        self.status_val['E14'] = self.byte_b2.x11111111.BIT6
        self.status_val['E15'] = self.byte_b2.x11111111.BIT7
        self.status_val['E16'] = self.byte_b2.x11111111.BIT8
        self.status_val['E17'] = self.byte_b3.x11111111.BIT1
        self.status_val['E18'] = self.byte_b3.x11111111.BIT2
        self.status_val['E19'] = self.byte_b3.x11111111.BIT3
        self.status_val['E20'] = self.byte_b3.x11111111.BIT4
        self.status_val['E21'] = self.byte_b3.x11111111.BIT5
        self.status_val['E22'] = self.byte_b3.x11111111.BIT6
        self.status_val['E23'] = self.byte_b3.x11111111.BIT7
        self.status_val['E24'] = self.byte_b3.x11111111.BIT8
        self.status_val['E25'] = self.byte_b4.x11111111.BIT1
        self.status_val['E26'] = self.byte_b4.x11111111.BIT2
        self.status_val['E27'] = self.byte_b4.x11111111.BIT3
        self.status_val['E28'] = self.byte_b4.x11111111.BIT4
        self.status_val['E29'] = self.byte_b4.x11111111.BIT5
        self.status_val['E30'] = self.byte_b4.x11111111.BIT6
        self.status_val['E31'] = self.byte_b4.x11111111.BIT7
        self.status_val['E32'] = self.byte_b4.x11111111.BIT8
        self.status_val['E33'] = self.byte_b5.x11111111.BIT1
        self.status_val['E34'] = self.byte_b5.x11111111.BIT2
        self.status_val['E35'] = self.byte_b5.x11111111.BIT3
        self.status_val['E36'] = self.byte_b5.x11111111.BIT4
        self.status_val['E37'] = self.byte_b5.x11111111.BIT5
        self.status_val['E38'] = self.byte_b5.x11111111.BIT6
        self.status_val['E39'] = self.byte_b5.x11111111.BIT7
        self.status_val['E40'] = self.byte_b5.x11111111.BIT8
        self.status_val['E41'] = self.byte_b6.x11111111.BIT1
        self.status_val['E42'] = self.byte_b6.x11111111.BIT2
        self.status_val['E43'] = self.byte_b6.x11111111.BIT3
        self.status_val['E44'] = self.byte_b6.x11111111.BIT4
        self.status_val['E45'] = self.byte_b6.x11111111.BIT5
        self.status_val['E46'] = self.byte_b6.x11111111.BIT6
        self.status_val['E47'] = self.byte_b6.x11111111.BIT7
        self.status_val['E48'] = self.byte_b6.x11111111.BIT8

        self.volume_dict = dict()
        self.key = ''
        self.volume = 0
        for self.key, self.volume in self.status_val.items():
            if self.volume > 0:
                self.Descr = self.SWData.D[self.key] if self.key in self.SWData.D else 'undefined'
                self.volume_dict[self.key] = DecodedAnswer(Descr=self.Descr, StrVolume=format(self.volume),  # '.2f'),
                                                           DigVolume=self.volume)


class RELEASEVAR:
    """
    2.3.16 Чтение варианта исполнения.
    Поле данных ответа состоит из 6 байт: B4 E4 C2 96 03 00

    10110100:
    С1 A – 1,0%; 2 10
    С1 R – 2,0%; 3 11
    Uн = – 230В; 1 01
    Iн = – 5А.;  0 00

    11100100:
    число направлений – 1;   1 1
    температурный диапазон - 1-40°C;   1 1
    учёт профиля средних мощностей – да;   1 1
    число фаз - 3;   0 0
    постоянная счётчика – 1000 имп/квт⋅ч.   4 0100

    11000010:
    суммирование фаз – по модулю;
    тарификатор – внутренний;
    тип счётчика – AR (измерение активной и реактивной энергии);
    № варианта исполнения – 2.

    10010110:
    Память №3 – 131x8;
    модем PLM – нет;
    модем GSM – нет;
    оптопорт – есть;
    интерфейс – CAN;
    внешнее питание – есть;
    эл. пломба внешней крышки – нет.

    00000011:
    флаг наличия встроенного реле – нет;
    флаг наличия подсветки ЖКИ – нет;
    флаг потарифного учёта максимумов мощности – нет;
    флаг наличия эл. пломбы защитной крышки – нет;
    интерфейс 2 – нет;
    встроенное питание интерфейса 1 – нет;
    контроль ПКЭ – да;
    пофазный учёт энергии A+ - да.

    00000000:

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
                ("ClA", c_uint8, 2),
                ("ClR", c_uint8, 2),
                ("Un", c_uint8, 2),
                ("In", c_uint8, 2)
            ]

        _fields_ = [
            ("b1x2222", B1X2222),
            ("one_byte", c_uint8)
        ]

    class ByteB2X41111(ctypes.Union):
        class B2X41111(ctypes.BigEndianStructure):
            """
            BYTE MeterConst:4;
            // Постоянная счетчика имп/квт?ч 0 - 5000; 1 - 25000; 2 - 1250; 3 - 500; 4 - 1000; 5 - 250.
            BYTE NPhase:1;         // Число фаз 0 - 3, 1 - 1
            BYTE ProfMPower:1;     // Учет профиля средних мощностей 0 - нет, 1 - да
            BYTE TempRange:1;      // Температурный диапазон°C 0 – 20, 1 – 40
            BYTE NDirect:1;        // Число направлений 0 - 2, 1 - 1
            """
            _pack_ = 1
            _fields_ = [
                ("NDirect", c_uint8, 1),
                ("TempRange", c_uint8, 1),
                ("ProfMPower", c_uint8, 1),
                ("NPhase", c_uint8, 1),
                ("MeterConst", c_uint8, 4)
            ]

        _fields_ = [
            ("b2x41111", B2X41111),
            ("one_byte", c_uint8)
        ]

    class ByteB3X4211(ctypes.Union):
        class B3X4211(ctypes.BigEndianStructure):
            """
            BYTE NVarProd:4;       // No варианта исполнения
            1 - 57,7В(1)5А10А5000имп./кВт*ч 2 - 230В5А60А500имп./кВт*ч
            3 - 230В5А100А250имп./кВт*ч 4 - 230В(1)5А10А1000имп./кВт*ч
            BYTE MeterType:2;      // Тип счетчика 0 - AR, 1 - A
            BYTE Tarificator:1;    // Тарификатор 0 - внешний, 1 - внутренний
            BYTE SumPhase:1;       // Суммирование фаз 0 - с учетом знака, 1 - по модулю
            """
            _pack_ = 1
            _fields_ = [
                ("SumPhase", c_uint8, 1),
                ("Tarificator", c_uint8, 1),
                ("MeterType", c_uint8, 2),
                ("NVarProd", c_uint8, 4)
            ]

        _fields_ = [
            ("b3x4211", B3X4211),
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
                ("Mem3", c_uint8, 1),
                ("ModemPLM", c_uint8, 1),
                ("ModemGSM", c_uint8, 1),
                ("OPort", c_uint8, 1),
                ("IFace", c_uint8, 2),
                ("ExSupp", c_uint8, 1),
                ("EPlomb", c_uint8, 1)
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
                ("Relay", c_uint8, 1),
                ("Light", c_uint8, 1),
                ("TarMax", c_uint8, 1),
                ("CEPlomb", c_uint8, 1),
                ("IFace2", c_uint8, 1),
                ("SupIF1", c_uint8, 1),
                ("QPower", c_uint8, 1),
                ("PhCalcPower", c_uint8, 1)
            ]

        _fields_ = [
            ("b5x11111111", B5X11111111),
            ("one_byte", c_uint8)
        ]

    class ByteB6X11111111(ctypes.Union):
        class B6X11111111(ctypes.BigEndianStructure):
            """
            BYTE ExControl:1;
            // Флаг наличия аппаратных средств управления внешними устройствами отключения нагрузки, 0 - нет, 1 - есть
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
                ("Reserved2", c_uint8, 1),
                ("Reserved1", c_uint8, 1),
                ("IEC61107", c_uint8, 1),
                ("ModemPLC2", c_uint8, 1),
                ("Profile2", c_uint8, 1),
                ("BEPlomb", c_uint8, 1),
                ("VoltTarif", c_uint8, 1),
                ("ExControl", c_uint8, 1)
            ]

        _fields_ = [
            ("b6x11111111", B6X11111111),
            ("one_byte", c_uint8)
        ]

    @dataclass(frozen=True)
    class PVData:
        D = {
            'In': StatusVar(Descript='Iн - номинальный ток А', Volumes={0: '5', 1: '1', 2: '10'}),
            'Un': StatusVar(Descript='Uн - номинальное напряжение В', Volumes={0: '57,7', 1: '230'}),
            'ClR': StatusVar(Descript='Cl R класс точности по реактивной энергии %',
                             Volumes={0: '0,2', 1: '0,5', 2: '1,0', 3: '2,0'}),
            'ClA': StatusVar(Descript='Cl А класс точности по активной энергии %',
                             Volumes={0: '0,2', 1: '0,5', 2: '1,0', 3: '2,0'}),
            'MeterConst': StatusVar(Descript='Постоянная счетчика имп/квт?ч',
                                    Volumes={0: '5000', 1: '25000', 2: '1250', 3: '500', 4: '1000', 5: '250'}),
            'NPhase': StatusVar(Descript='Число фаз', Volumes={0: '3', 1: '1'}),
            'ProfMPower': StatusVar(Descript='Учет профиля средних мощностей', Volumes={0: 'нет', 1: 'да'}),
            'TempRange': StatusVar(Descript='Температурный диапазон°C', Volumes={0: '20', 1: '40'}),
            'NDirect': StatusVar(Descript='Число направлений', Volumes={0: '2', 1: '1'}),
            'NVarProd': StatusVar(Descript='No варианта исполнения',
                                  Volumes={1: '57,7В(1)5А10А5000имп./кВт*ч', 2: '230В5А60А500имп./кВт*ч',
                                           3: '230В5А100А250имп./кВт*ч', 4: '230В(1)5А10А1000имп./кВт*ч'}),
            'MeterType': StatusVar(Descript='Тип счетчика', Volumes={0: 'AR', 1: 'A'}),
            'Tarificator': StatusVar(Descript='Тарификатор', Volumes={0: 'внешний', 1: 'внутренний'}),
            'SumPhase': StatusVar(Descript='Суммирование фаз', Volumes={0: 'с учетом знака', 1: 'по модулю'}),
            'EPlomb': StatusVar(Descript='Эл. помба верхней крышки', Volumes={0: 'нет', 1: 'есть'}),
            'ExSupp': StatusVar(Descript='Внешнее питание', Volumes={0: 'нет', 1: 'есть'}),
            'IFace': StatusVar(Descript='Интерфейс', Volumes={0: 'CAN', 1: 'RS-485', 2: 'резерв', 3: 'нет'}),
            'OPort': StatusVar(Descript='оптопорт', Volumes={0: 'нет', 1: 'есть'}),
            'ModemGSM': StatusVar(Descript='Модем GSM', Volumes={0: 'нет', 1: 'есть'}),
            'ModemPLM': StatusVar(Descript='Модем PLM', Volumes={0: 'нет', 1: 'есть'}),
            'Mem3': StatusVar(Descript='Память No3', Volumes={0: '65.5x8', 1: '131x8'}),
            'PhCalcPower': StatusVar(Descript='Пофазный учет энергии A+', Volumes={0: 'нет', 1: 'да'}),
            'QPower': StatusVar(Descript='Контроль ПКЭ', Volumes={0: 'нет', 1: 'да'}),
            'SupIF1': StatusVar(Descript='Встроенное питание интерфейса 1', Volumes={0: 'нет', 1: 'да'}),
            'IFace2': StatusVar(Descript='Интерфейс 2', Volumes={0: 'нет', 1: 'да'}),
            'CEPlomb': StatusVar(Descript='Флаг наличия эл. пломбы защитной крышки',
                                 Volumes={0: 'нет', 1: 'есть'}),
            'TarMax': StatusVar(Descript='Флаг потарифного учета максимумов мощности',
                                Volumes={0: 'нет', 1: 'есть'}),
            'Light': StatusVar(Descript='Флаг наличия подсветки ЖКИ', Volumes={0: 'нет', 1: 'есть'}),
            'Relay': StatusVar(Descript='Флаг наличия встроенного реле', Volumes={0: 'нет', 1: 'есть'}),
            'ExControl':
                StatusVar(
                    Descript='Флаг наличия аппаратных средств управления внешними устройствами отключения нагрузки',
                    Volumes={0: 'нет', 1: 'есть'}),
            'VoltTarif': StatusVar(Descript='Флаг переключения тарифов внешним напряжением',
                                   Volumes={0: 'нет', 1: 'да'}),
            'BEPlomb': StatusVar(Descript='Флаг наличия эл.пломбы модульного отсека',
                                 Volumes={0: 'нет', 1: 'есть'}),
            'Profile2': StatusVar(Descript='Флаг наличия профиля 2', Volumes={0: 'нет', 1: 'есть'}),
            'ModemPLC2': StatusVar(Descript='Модем PLC2', Volumes={0: 'нет', 1: 'есть'}),
            'IEC61107': StatusVar(Descript='Флаг протокола IEC61107', Volumes={0: 'нет', 1: 'да'}),
            'Reserved1': StatusVar(Descript='Reserved1', Volumes={0: 'нет'}),
            'Reserved2': StatusVar(Descript='Reserved2', Volumes={0: 'нет'})
        }

    m = 6

    def __init__(self, in_bytearray):
        super().__init__()
        if isinstance(in_bytearray, bytearray):
            self.n = len(in_bytearray)
            if self.n < RELEASEVAR.m:
                self.in_bytearray = in_bytearray[:]
                for i in range(RELEASEVAR.m - self.n):
                    self.in_bytearray.append(0)
            else:
                self.in_bytearray = in_bytearray[:RELEASEVAR.m]
        else:
            self.in_bytearray = bytearray([0] * RELEASEVAR.m)

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

        self.status_val = dict()
        self.status_val['In'] = self.byte_b1.b1x2222.In
        self.status_val['Un'] = self.byte_b1.b1x2222.Un
        self.status_val['ClR'] = self.byte_b1.b1x2222.ClR
        self.status_val['ClA'] = self.byte_b1.b1x2222.ClA
        self.status_val['MeterConst'] = self.byte_b2.b2x41111.MeterConst
        self.status_val['NPhase'] = self.byte_b2.b2x41111.NPhase
        self.status_val['ProfMPower'] = self.byte_b2.b2x41111.ProfMPower
        self.status_val['TempRange'] = self.byte_b2.b2x41111.TempRange
        self.status_val['NDirect'] = self.byte_b2.b2x41111.NDirect
        self.status_val['NVarProd'] = self.byte_b3.b3x4211.NVarProd
        self.status_val['MeterType'] = self.byte_b3.b3x4211.MeterType
        self.status_val['Tarificator'] = self.byte_b3.b3x4211.Tarificator
        self.status_val['SumPhase'] = self.byte_b3.b3x4211.SumPhase
        self.status_val['EPlomb'] = self.byte_b4.b4x1121111.EPlomb
        self.status_val['ExSupp'] = self.byte_b4.b4x1121111.ExSupp
        self.status_val['IFace'] = self.byte_b4.b4x1121111.IFace
        self.status_val['OPort'] = self.byte_b4.b4x1121111.OPort
        self.status_val['ModemGSM'] = self.byte_b4.b4x1121111.ModemGSM
        self.status_val['ModemPLM'] = self.byte_b4.b4x1121111.ModemPLM
        self.status_val['Mem3'] = self.byte_b4.b4x1121111.Mem3
        self.status_val['PhCalcPower'] = self.byte_b5.b5x11111111.PhCalcPower
        self.status_val['QPower'] = self.byte_b5.b5x11111111.QPower
        self.status_val['SupIF1'] = self.byte_b5.b5x11111111.SupIF1
        self.status_val['IFace2'] = self.byte_b5.b5x11111111.IFace2
        self.status_val['CEPlomb'] = self.byte_b5.b5x11111111.CEPlomb
        self.status_val['TarMax'] = self.byte_b5.b5x11111111.TarMax
        self.status_val['Light'] = self.byte_b5.b5x11111111.Light
        self.status_val['Relay'] = self.byte_b5.b5x11111111.Relay
        self.status_val['ExControl'] = self.byte_b6.b6x11111111.ExControl
        self.status_val['VoltTarif'] = self.byte_b6.b6x11111111.VoltTarif
        self.status_val['BEPlomb'] = self.byte_b6.b6x11111111.BEPlomb
        self.status_val['Profile2'] = self.byte_b6.b6x11111111.Profile2
        self.status_val['ModemPLC2'] = self.byte_b6.b6x11111111.ModemPLC2
        self.status_val['IEC61107'] = self.byte_b6.b6x11111111.IEC61107
        self.status_val['Reserved1'] = self.byte_b6.b6x11111111.Reserved1
        self.status_val['Reserved2'] = self.byte_b6.b6x11111111.Reserved2

        self.volume_dict = dict()
        self.key = ''
        self.dig_volume = 0
        self.str_volume = ''
        # self.status_var = StatusVar()
        for self.key, self.dig_volume in self.status_val.items():
            self.status_var = self.PVData.D[self.key] if self.key in self.PVData.D else StatusVar(Descript='undefined',
                                                                                                  Volumes={0: 'нет'})
            self.descr = self.status_var.Descript
            self.str_volume = \
                self.status_var.Volumes[self.dig_volume] if self.dig_volume in self.status_var.Volumes else 'none'
            self.volume_dict[self.key] = DecodedAnswer(Descr=self.descr,
                                                       StrVolume=self.str_volume,
                                                       DigVolume=self.dig_volume)


class B1B2:
    """
    struct BYTE12
    {
        unsigned char B1          :8; //байт 1
        unsigned char B2          :8; //байт 2
    };
    """
    m = 2

    def __init__(self, in_bytearray):
        super().__init__()
        if isinstance(in_bytearray, bytearray):
            self.n = len(in_bytearray)
            if self.n < B1B2.m:
                self.in_bytearray = in_bytearray[:]
                for i in range(B1B2.m - self.n):
                    self.in_bytearray.append(0)
            else:
                self.in_bytearray = in_bytearray[:B1B2.m]
        else:
            self.in_bytearray = bytearray([0] * B1B2.m)

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
    m = 2

    def __init__(self, in_bytearray):
        super().__init__()
        if isinstance(in_bytearray, bytearray):
            self.n = len(in_bytearray)
            if self.n < B2B1.m:
                self.in_bytearray = in_bytearray[:]
                for i in range(B2B1.m - self.n):
                    self.in_bytearray.append(0)
            else:
                self.in_bytearray = in_bytearray[:B2B1.m]
        else:
            self.in_bytearray = bytearray([0] * B2B1.m)

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
    m = 3

    def __init__(self, in_bytearray):
        super().__init__()
        if isinstance(in_bytearray, bytearray):
            self.n = len(in_bytearray)
            if self.n < B1B3B2.m:
                self.in_bytearray = in_bytearray[:]
                for i in range(B1B3B2.m - self.n):
                    self.in_bytearray.append(0)
            else:
                self.in_bytearray = in_bytearray[:B1B3B2.m]
        else:
            self.in_bytearray = bytearray([0] * B1B3B2.m)

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
    m = 4

    def __init__(self, in_bytearray):
        super().__init__()
        if isinstance(in_bytearray, bytearray):
            self.n = len(in_bytearray)
            if self.n < B2B1B4B3.m:
                self.in_bytearray = in_bytearray[:]
                for i in range(B2B1B4B3.m - self.n):
                    self.in_bytearray.append(0)
            else:
                self.in_bytearray = in_bytearray[:B2B1B4B3.m]
        else:
            self.in_bytearray = bytearray([0] * B2B1B4B3.m)

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
    m = 3

    def __init__(self, in_bytearray):
        super().__init__()
        if isinstance(in_bytearray, bytearray):
            self.n = len(in_bytearray)
            if self.n < B1x2x6B3B2.m:
                self.in_bytearray = in_bytearray[:]
                for i in range(B1x2x6B3B2.m - self.n):
                    self.in_bytearray.append(0)
            else:
                self.in_bytearray = in_bytearray[:B1x2x6B3B2.m]
        else:
            self.in_bytearray = bytearray([0] * B1x2x6B3B2.m)
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
    m = 4

    def __init__(self, in_bytearray):
        super().__init__()
        if isinstance(in_bytearray, bytearray):
            self.n = len(in_bytearray)
            if self.n < B2B1x2x6B4B3.m:
                self.in_bytearray = in_bytearray[:]
                for i in range(B2B1x2x6B4B3.m - self.n):
                    self.in_bytearray.append(0)
            else:
                self.in_bytearray = in_bytearray[:B2B1x2x6B4B3.m]
        else:
            self.in_bytearray = bytearray([0] * B2B1x2x6B4B3.m)
        self.byte_ddb6 = ByteX2X6()

        self.byte_ddb6.one_byte = self.in_bytearray[1]
        self.direct_active = 1 if self.byte_ddb6.x2x6.direct_act == 0 else -1
        self.direct_reactive = 1 if self.byte_ddb6.x2x6.direct_react == 0 else -1
        self.volume = int.from_bytes(bytearray([self.byte_ddb6.x2x6.b1, self.in_bytearray[0], self.in_bytearray[3],
                                                self.in_bytearray[2]]), byteorder='big', signed=False)


class Request0811xxh:
    """
    2.3.15 Чтение вспомогательных параметров.
    Команда предназначена для чтения вспомогательных параметров: мгновенной активной, реактивной, полной мощности,
    напряжения тока, коэффициента мощности, частоты, угла между фазными напряжениями, коэффициента искажения
    синусоидальности фазных напряжений, температуры внутри корпуса прибора, а также даты и времени фиксации,
    зафиксированной энергии.
    Код параметров: 11h.
    Поле параметров – поле BWRI.
    """

    def __init__(self, in_bytearray, key, descr, physics):
        super().__init__()
        self.volume_dict = dict()
        self.volume = B1B3B2(in_bytearray).volume / physics
        self.volume_dict[key] = DecodedAnswer(Descr=descr,
                                              StrVolume=format(self.volume, '.2f'),
                                              DigVolume=self.volume)


@dataclass(frozen=True)
class Requests_0811xxh:
    D = {'VoltagePhase1': Req0811xxh(ClassPTR='Request0811xxh', Descr='Напряжение 1й фазы (В)', Factor=Physics.VOLTAGE)}


class VoltagePhaseI_081111h(Request0811xxh):
    """
    :param in_bytearray: возвращаемая при вызове запроса 081111h последовательность байт в виде байтмассива
    :return: volume_dict словарь с кортежем -  ключ = VoltagePhase1
                      с кортежем DecodedAnswer Descr='Напряжение 1й фазы (В)',
                                               StrVolume= напряжение строчного типа ,
                                               DigVolume= напряжение численного типа
    """

    def __init__(self, in_bytearray):
        super().__init__(in_bytearray, 'VoltagePhase1', 'Напряжение 1й фазы (В)', Physics.VOLTAGE)
        self.volume_dict = super().volume_dict


class VoltagePhaseII_081112h(Request0811xxh):
    """
    :param in_bytearray: возвращаемая при вызове запроса 081112h последовательность байт в виде байтмассива
    :return: volume_dict словарь с кортежем -  ключ = VoltagePhase2
                      с кортежем DecodedAnswer Descr='Напряжение 2й фазы (В)',
                                               StrVolume= напряжение строчного типа ,
                                               DigVolume= напряжение численного типа
    """

    def __init__(self, in_bytearray):
        super().__init__(in_bytearray, 'VoltagePhase2', 'Напряжение 2й фазы (В)', Physics.VOLTAGE)
        self.volume_dict = super().volume_dict


class VoltagePhaseIII_081113h(Request0811xxh):
    """
    :param in_bytearray: возвращаемая при вызове запроса 081113h последовательность байт в виде байтмассива
    :return: volume_dict словарь с кортежем -  ключ = VoltagePhase3
                      с кортежем DecodedAnswer Descr='Напряжение 3й фазы (В)',
                                               StrVolume= напряжение строчного типа ,
                                               DigVolume= напряжение численного типа
    """

    def __init__(self, in_bytearray):
        super().__init__(in_bytearray, 'VoltagePhase3', 'Напряжение 3й фазы (В)', Physics.VOLTAGE)
        self.volume_dict = super().volume_dict


class ApparentPowerS081408h:
    """
    Прочитать мгновенную полную мощность по сумме фаз для счетчика с сетевым адресом 128
    (используем запрос с номером 14h).
    Запрос: 80 08 14 08 (CRC)
    Ответ: 80 00 40 E7 29 00 40 E7 29 00 00 00 00 00 00 00 00 (CRC)
    Значение мгновенной полной мощности по сумме фаз - 4 BYTE
    Значение мгновенной полной мощности по 1-ой фазе - 4 BYTE
    Значение мгновенной полной мощности по 2-ой фазе - 4 BYTE
    Значение мгновенной полной мощности по 3-ей фазе - 4 BYTE

    Значение полной мощности по сумме фаз:
    Значение 1-го байта = 40 = 01000000 - направление активной мощности – прямое,
                                          направление реактивной мощности – обратное.
    N = 0029E7h = 10727d S = 10727/100 = 107,27 Вт
    N1 = 0029E7h = 10727d S1 = 10727/100 = 107,27 Вт
    фаза 0 - сумма фаз
    :param in_bytearray: возвращаемая при вызове запроса 0814h последовательность байт в виде байтмассива
    :return: словарь с кортежем -  фаза: (величина, направление активной мощности , направление реактивной мощности)
    """
    m = 16  # общая длина последовательности
    k = 4  # длина последовательности по каждой фазе

    @dataclass(frozen=True)
    class PhasePowers:
        D = {
            0: StatusVar(Descript='Значение мгновенной полной мощности по сумме фаз', Volumes='PowerPhaseSUM'),
            1: StatusVar(Descript='Значение мгновенной полной мощности по 1-ой фазе', Volumes='PowerPhaseI'),
            2: StatusVar(Descript='Значение мгновенной полной мощности по 2-ой фазе', Volumes='PowerPhaseII'),
            3: StatusVar(Descript='Значение мгновенной полной мощности по 3-ей фазе', Volumes='PowerPhaseIII')
        }

    def __init__(self, in_bytearray):
        super().__init__()
        self.volume_dict = dict()
        self.in_bytearray = bytearray([0] * ApparentPowerS081408h.m) if not isinstance(in_bytearray, bytearray) or (
                len(in_bytearray) < ApparentPowerS081408h.m) else in_bytearray[:ApparentPowerS081408h.m]
        self.i = 0
        for self.i in range(0, ApparentPowerS081408h.m, ApparentPowerS081408h.k):
            self.current_lenght = len(self.volume_dict)
            if self.current_lenght in ApparentPowerS081408h.PhasePowers.D:
                self.volume = B2B1x2x6B4B3(self.in_bytearray[self.i:self.i + ApparentPowerS081408h.k]).volume \
                              / Physics.POWER
                self.descr = ApparentPowerS081408h.PhasePowers.D[self.current_lenght].Descript
                self.key = ApparentPowerS081408h.PhasePowers.D[self.current_lenght].Volumes
                self.volume_dict[self.key] = DecodedAnswer(Descr=self.descr,
                                                           StrVolume=format(self.volume, '.2f'),
                                                           DigVolume=self.volume)


if __name__ == '__main__':
    print(VoltagePhaseI_081111h(bytearray([0x00, 0x2D, 0x02])).volume_dict)
    """
    Прочитать напряжения по 1-ой фазе для счетчика с сетевым адресом 128 (используем запрос с номером 11h).
    Запрос: 80 08 11 11 (CRC)
    Ответ: 80 00 5B 56 (CRC)
    Значение напряжения на 1-ой фазе
    N = 00565Bh = 22423d U = 22423/100 = 224,43 В
    """
    # must be {'VoltagePhase1': DecodedAnswer(Descr='Напряжение 1й фазы (В)', StrVolume='5.57', DigVolume=5.57)}

    print(ApparentPowerS081408h(bytearray([0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
                                           0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00])).volume_dict)
    # must be {0: RetAnswerFunctions(Volume=7158278.82, DirectActive=-1, DirectReactive=1),
    #          1: RetAnswerFunctions(Volume=3579139.41, DirectActive=1, DirectReactive=-1),
    #          2: RetAnswerFunctions(Volume=10737418.23, DirectActive=-1, DirectReactive=-1),
    #          3: RetAnswerFunctions(Volume=0.0, DirectActive=1, DirectReactive=1)}
    # must be {'PowerPhaseSUM': DecodedAnswer(Descr='Значение мгновенной полной мощности по сумме фаз',
    #                           StrVolume='7158278.82',
    #                           DigVolume=7158278.82),
    #          'PowerPhaseI':   DecodedAnswer(Descr='Значение мгновенной полной мощности по 1-ой фазе',
    #                           StrVolume='3579139.41',
    #                           DigVolume=3579139.41),
    #          'PowerPhaseII':  DecodedAnswer(Descr='Значение мгновенной полной мощности по 2-ой фазе',
    #                           StrVolume='10737418.23',
    #                           DigVolume=10737418.23),
    #          'PowerPhaseIII': DecodedAnswer(Descr='Значение мгновенной полной мощности по 3-ей фазе',
    #                           StrVolume='0.00',
    #                           DigVolume=0.0)}

    print(ApparentPowerS081408h(bytearray([0x00, 0x40, 0xE7, 0x29, 0x00, 0x40, 0xE7, 0x29,
                                           0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])).volume_dict)
    # must be {0: RetAnswerFunctions(Volume=107.27, DirectActive=1, DirectReactive=-1),
    #          1: RetAnswerFunctions(Volume=107.27, DirectActive=1, DirectReactive=-1),
    #          2: RetAnswerFunctions(Volume=0.0, DirectActive=1, DirectReactive=1),
    #          3: RetAnswerFunctions(Volume=0.0, DirectActive=1, DirectReactive=1)}
    # must be {'PowerPhaseSUM': DecodedAnswer(Descr='Значение мгновенной полной мощности по сумме фаз',
    #                           StrVolume='107.27',
    #                           DigVolume=107.27),
    #          'PowerPhaseI':   DecodedAnswer(Descr='Значение мгновенной полной мощности по 1-ой фазе',
    #                           StrVolume='107.27',
    #                           DigVolume=107.27),
    #          'PowerPhaseII':  DecodedAnswer(Descr='Значение мгновенной полной мощности по 2-ой фазе',
    #                           StrVolume='0.00',
    #                           DigVolume=0.0),
    #          'PowerPhaseIII': DecodedAnswer(Descr='Значение мгновенной полной мощности по 3-ей фазе',
    #                           StrVolume='0.00',
    #                           DigVolume=0.0)}
