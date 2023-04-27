class Request0811xxh:
    """
    2.3.15 Чтение вспомогательных параметров.
    Команда предназначена для чтения вспомогательных параметров: мгновенной активной, реактивной, полной мощности,
    напряжения тока, коэффициента мощности, частоты, угла между фазными напряжениями, коэффициента искажения
    синусоидальности фазных напряжений, температуры внутри корпуса прибора, а также даты и времени фиксации,
    зафиксированной энергии.
    Код параметров: 11h.
    Поле параметров – поле BWRI.

    :param
    query_key:    символическое обозначение байтовой последовательности запроса - 081111h (напр)
    in_bytearray: возвращаемая при вызове запроса последовательность байт в виде байтмассива,
    :return
    volume_dict словарь с кортежем:
        ключ = 'VoltagePhase_I' символьное наименование возвращенной величины
        кортеж = DecodedAnswer(Descr='Напряжение 1й фазы (В)',
                               StrVolume= напряжение строчного типа ,
                               DigVolume= напряжение численного типа)
    q = lambda query_key, in_bytearray: Request0811xxh(query_key, in_bytearray)
    """
    m = 3

    @dataclass(frozen=True)
    class DetalVolumes:
        D = {
            '081111h': {'VolKey': 'VoltagePhase_I', 'Descript': 'Напряжение 1й фазы (В)', 'Factor': Physics.VOLTAGE},
            '081112h': {'VolKey': 'VoltagePhase_II', 'Descript': 'Напряжение 2й фазы (В)', 'Factor': Physics.VOLTAGE},
            '081113h': {'VolKey': 'VoltagePhase_III', 'Descript': 'Напряжение 3й фазы (В)', 'Factor': Physics.VOLTAGE}
        }

    def __init__(self, query_key, in_bytearray):
        super().__init__()
        self.volume_dict = dict()
        if isinstance(in_bytearray, bytearray) and \
                (len(in_bytearray) == Request0811xxh.m) and \
                (query_key in Request0811xxh.DetalVolumes.D):
            self.b1b3b2 = B1B3B2(in_bytearray)
            self.volume = self.b1b3b2.volume / Request0811xxh.DetalVolumes.D[query_key]['Factor']
            self.volume_dict[Request0811xxh.DetalVolumes.D[query_key]['VolKey']] = \
                DecodedAnswer(Descr=Request0811xxh.DetalVolumes.D[query_key]['Descript'],
                              StrVolume=format(self.volume, '.2f'),
                              DigVolume=self.volume)


class Request08140xh:
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
    class DetalPhasedVolumes:
        D = {
            '081408h': {
                'DirectA': 0,
                'DirectR': 0,
                'Phase':
                    {
                        0: {'VolKey': 'ApparentPowerPhase_SUM',
                            'Descript': 'Значение мгновенной полной мощности по сумме фаз'},
                        1: {'VolKey': 'ApparentPowerPhase_I',
                            'Descript': 'Значение мгновенной полной мощности по 1-ой фазе'},
                        2: {'VolKey': 'ApparentPowerPhase_II',
                            'Descript': 'Значение мгновенной полной мощности по 2-ой фазе'},
                        3: {'VolKey': 'ApparentPowerPhase_III',
                            'Descript': 'Значение мгновенной полной мощности по 3-ой фазе'}
                    }
            },
            '081404h': {
                'DirectA': 0,
                'DirectR': 1,
                'Phase':
                    {
                        0: {'VolKey': 'ReactivePowerPhase_SUM',
                            'Descript': 'Значение мгновенной реактивной мощности по сумме фаз'},
                        1: {'VolKey': 'ReactivePowerPhase_I',
                            'Descript': 'Значение мгновенной реактивной мощности по 1-ой фазе'},
                        2: {'VolKey': 'ReactivePowerPhase_II',
                            'Descript': 'Значение мгновенной реактивной мощности по 2-ой фазе'},
                        3: {'VolKey': 'ReactivePowerPhase_III',
                            'Descript': 'Значение мгновенной реактивной мощности по 3-ой фазе'}
                    }
            },
            '081400h': {
                'DirectA': 1,
                'DirectR': 0,
                'Phase':
                    {
                        0: {'VolKey': 'TruePowerPhase_SUM',
                            'Descript': 'Значение мгновенной активной мощности по сумме фаз'},
                        1: {'VolKey': 'TruePowerPhase_I',
                            'Descript': 'Значение мгновенной активной мощности по 1-ой фазе'},
                        2: {'VolKey': 'TruePowerPhase_II',
                            'Descript': 'Значение мгновенной активной мощности по 2-ой фазе'},
                        3: {'VolKey': 'TruePowerPhase_III',
                            'Descript': 'Значение мгновенной активной мощности по 3-ой фазе'}
                    }
            }
        }

    def __init__(self, query_key, in_bytearray):
        super().__init__()
        self.volume_dict = dict()
        if isinstance(in_bytearray, bytearray) and \
                (len(in_bytearray) == Request08140xh.m) and \
                (query_key in Request08140xh.DetalPhasedVolumes.D):
            self.i = 0
            self.b2b1x2x6b4b3 = dict()
            for self.i in range(0, Request08140xh.m, Request08140xh.k):
                self.current_lenght = len(self.volume_dict)
                if self.current_lenght in Request08140xh.DetalPhasedVolumes.D[query_key]:
                    self.b2b1x2x6b4b3[self.current_lenght] = \
                        B2B1x2x6B4B3(in_bytearray[self.i:self.i + Request08140xh.k])
                    self.factor = Request08140xh.DetalPhasedVolumes.D[query_key][self.current_lenght].Factor
                    self.descr = Request08140xh.DetalPhasedVolumes.D[query_key][self.current_lenght].Descript
                    self.vol_key = Request08140xh.DetalPhasedVolumes.D[query_key][self.current_lenght].VolKey
                    self.volume = self.b2b1x2x6b4b3[self.current_lenght].volume / self.factor
                    self.volume_dict[self.vol_key] = DecodedAnswer(Descr=self.descr,
                                                                   StrVolume=format(self.volume, '.2f'),
                                                                   DigVolume=self.volume)

    # print(Request0811xxh('081111h', bytearray([0x00, 0x5B, 0x56])).volume_dict)
    """
    Прочитать напряжения по 1-ой фазе для счетчика с сетевым адресом 128 (используем запрос с номером 11h).
    Запрос: 80 08 11 11 (CRC)
    Ответ: 80 00 5B 56 (CRC)
    Значение напряжения на 1-ой фазе
    N = 00565Bh = 22107d U = 22107/100 = 221,07 В
    """
    # must be {'VoltagePhase_I': DecodedAnswer(Descr='Напряжение 1й фазы (В)', StrVolume='221.07', DigVolume=221.07)}

    # print(Request08140xh('081408h', bytearray([0xAA, 0xAA, 0xAA, 0xAA, 0x55, 0x55, 0x55, 0x55,
                                               0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x00, 0x00])).volume_dict)
    # must be {'ApparentPowerPhase_SUM': DecodedAnswer(Descr='Значение мгновенной полной мощности по сумме фаз',
    #           StrVolume='7158278.82',
    #           DigVolume=7158278.82),
    #          'ApparentPowerPhase_I': DecodedAnswer(Descr='Значение мгновенной полной мощности по 1-ой фазе',
    #           StrVolume='3579139.41',
    #           DigVolume=3579139.41),
    #          'ApparentPowerPhase_II': DecodedAnswer(Descr='Значение мгновенной полной мощности по 2-ой фазе',
    #           StrVolume='10737418.23',
    #           DigVolume=10737418.23),
    #          'ApparentPowerPhase_III': DecodedAnswer(Descr='Значение мгновенной полной мощности по 3-ой фазе',
    #           StrVolume='0.00',
    #           DigVolume=0.0)}
    # print(Request08140xh('081408h', bytearray([0x00, 0x40, 0xE7, 0x29, 0x00, 0x40, 0xE7, 0x29,
                                               0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])).volume_dict)
    # must be {'ApparentPowerPhase_SUM': DecodedAnswer(Descr='Значение мгновенной полной мощности по сумме фаз',
    #           StrVolume='107.27',
    #           DigVolume=107.27),
    #          'ApparentPowerPhase_I': DecodedAnswer(Descr='Значение мгновенной полной мощности по 1-ой фазе',
    #           StrVolume='107.27',
    #           DigVolume=107.27),
    #          'ApparentPowerPhase_II': DecodedAnswer(Descr='Значение мгновенной полной мощности по 2-ой фазе',
    #           StrVolume='0.00',
    #           DigVolume=0.0),
    #          'ApparentPowerPhase_III': DecodedAnswer(Descr='Значение мгновенной полной мощности по 3-ой фазе',
    #           StrVolume='0.00',
    #           DigVolume=0.0)}
