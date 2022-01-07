#!/usr/bin/env python3

# import time
import serial
from serial import STOPBITS_ONE, PARITY_NONE, EIGHTBITS
from serial.tools import list_ports


class MercuryRTU(serial.Serial):
    """
    Критерием окончания любой последовательности (фрейма) является гарантированный тайм-аут,
    длительность которого зависит от выбранной скорости:
    − около 2 мс стандартная длительность тайм-аута для скорости равной и более 38400 бод;
    − около 3 мс стандартная длительность тайм-аута для скорости 19200 Бод;
    − около 5 мс стандартная длительность тайм-аута для скорости 9600 Бод;
    − около 10 мс стандартная длительность тайм-аута для скорости 4800 Бод;
    − около 20 мс стандартная длительность тайм-аута для скорости 2400 Бод;
    − около 40 мс стандартная длительность тайм-аута для скорости 1200 Бод;
    − около 80 мс стандартная длительность тайм-аута для скорости 600 Бод;
    − около 160 мс стандартная длительность тайм-аута для скорости 300 Бод.
    Запрос или ответ счетчика на запрос не могут быть посланы раньше тайм-аута, после
    окончания предыдущего запроса. Адресованный счетчик всегда отвечает на любые корректные
    запросы через время не менее тайм-аута и не более времени ожидания ответа:
    − около 150 мс стандартная длительность ожидания ответа для скорости равной и более 9600 бод;
    − около 180 мс стандартная длительность ожидания ответа для скорости 4800 Бод;
    − около 250 мс стандартная длительность ожидания ответа для скорости 2400 Бод;
    − около 400 мс стандартная длительность ожидания ответа для скорости 1200 Бод;
    − около 800 мс стандартная длительность ожидания ответа для скорости 600 Бод;
    − около 1600 мс стандартная длительность ожидания ответа для скорости 300 Бод.
    При использовании режима длинных ответов (поле данных ответа более 16 байт) длительность
    тайм-аута должна быть не менее 25 мс.
    9600[bit/s] / (EIGHTBITS + PARITY_NONE + STOPBITS_ONE) = 9600/9 = 1067[byte/s] , 1 byte for 1/1067 = 0,94 ms
    256 bytes for 240 ms , timeout<=25+240+150=415 ms
    16+3=19 bytes   19*0,94=17,86 ms 17,86*9600/300=571,52 ms
    """

    def __init__(self,
                 port=None,
                 baudrate=9600,
                 bytesize=EIGHTBITS,
                 parity=PARITY_NONE,
                 stopbits=STOPBITS_ONE,
                 timeout=0.415,
                 xonxoff=False,
                 rtscts=False,
                 write_timeout=0.572,
                 dsrdtr=False,
                 inter_byte_timeout=None,
                 exclusive=None,
                 quantity_repeat=3):
        super().__init__(port, baudrate, bytesize, parity, stopbits, timeout, xonxoff, rtscts, write_timeout, dsrdtr,
                         inter_byte_timeout, exclusive)
        self.quantity_repeat = quantity_repeat
        self.error_answer = dict({
            0x00: "Успешно.",
            0x01: "Недопустимая команда или параметр.",
            0x02: "Внутренняя ошибка счетчика.",
            0x03: "Не достаточен уровень доступа для удовлетворения запроса.",
            0x04: "Внутренние часы счетчика уже корректировались в течение текущих суток.",
            0x05: "Не открыт канал связи."
        })

    @staticmethod
    def modbus_crc(byte_sequence):
        """
        :param byte_sequence: байтовый массив для которого выполняется 'Быстрый расчет CRC c полиномом MODBUS'
                                как описано в M23x 236.8.0.0 234.9.0.0 rev2013.12.11.pdf
        :return: 2х байтовое целое в виде байтового массива из двух байт в big-endian порядке [::-1]
                (в протоколе нужен big-endian порядок)
        """

        crc_array = bytearray([0xFF, 0xFF])

        sr_crc_hi = bytes([
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x00, 0xC1, 0x81, 0x40, 0x01, 0xC0, 0x80, 0x41,
            0x01, 0xC0, 0x80, 0x41, 0x00, 0xC1, 0x81, 0x40
        ])

        sr_crc_lo = bytes([
            0x00, 0xC0, 0xC1, 0x01, 0xC3, 0x03, 0x02, 0xC2,
            0xC6, 0x06, 0x07, 0xC7, 0x05, 0xC5, 0xC4, 0x04,
            0xCC, 0x0C, 0x0D, 0xCD, 0x0F, 0xCF, 0xCE, 0x0E,
            0x0A, 0xCA, 0xCB, 0x0B, 0xC9, 0x09, 0x08, 0xC8,
            0xD8, 0x18, 0x19, 0xD9, 0x1B, 0xDB, 0xDA, 0x1A,
            0x1E, 0xDE, 0xDF, 0x1F, 0xDD, 0x1D, 0x1C, 0xDC,
            0x14, 0xD4, 0xD5, 0x15, 0xD7, 0x17, 0x16, 0xD6,
            0xD2, 0x12, 0x13, 0xD3, 0x11, 0xD1, 0xD0, 0x10,
            0xF0, 0x30, 0x31, 0xF1, 0x33, 0xF3, 0xF2, 0x32,
            0x36, 0xF6, 0xF7, 0x37, 0xF5, 0x35, 0x34, 0xF4,
            0x3C, 0xFC, 0xFD, 0x3D, 0xFF, 0x3F, 0x3E, 0xFE,
            0xFA, 0x3A, 0x3B, 0xFB, 0x39, 0xF9, 0xF8, 0x38,
            0x28, 0xE8, 0xE9, 0x29, 0xEB, 0x2B, 0x2A, 0xEA,
            0xEE, 0x2E, 0x2F, 0xEF, 0x2D, 0xED, 0xEC, 0x2C,
            0xE4, 0x24, 0x25, 0xE5, 0x27, 0xE7, 0xE6, 0x26,
            0x22, 0xE2, 0xE3, 0x23, 0xE1, 0x21, 0x20, 0xE0,
            0xA0, 0x60, 0x61, 0xA1, 0x63, 0xA3, 0xA2, 0x62,
            0x66, 0xA6, 0xA7, 0x67, 0xA5, 0x65, 0x64, 0xA4,
            0x6C, 0xAC, 0xAD, 0x6D, 0xAF, 0x6F, 0x6E, 0xAE,
            0xAA, 0x6A, 0x6B, 0xAB, 0x69, 0xA9, 0xA8, 0x68,
            0x78, 0xB8, 0xB9, 0x79, 0xBB, 0x7B, 0x7A, 0xBA,
            0xBE, 0x7E, 0x7F, 0xBF, 0x7D, 0xBD, 0xBC, 0x7C,
            0xB4, 0x74, 0x75, 0xB5, 0x77, 0xB7, 0xB6, 0x76,
            0x72, 0xB2, 0xB3, 0x73, 0xB1, 0x71, 0x70, 0xB0,
            0x50, 0x90, 0x91, 0x51, 0x93, 0x53, 0x52, 0x92,
            0x96, 0x56, 0x57, 0x97, 0x55, 0x95, 0x94, 0x54,
            0x9C, 0x5C, 0x5D, 0x9D, 0x5F, 0x9F, 0x9E, 0x5E,
            0x5A, 0x9A, 0x9B, 0x5B, 0x99, 0x59, 0x58, 0x98,
            0x88, 0x48, 0x49, 0x89, 0x4B, 0x8B, 0x8A, 0x4A,
            0x4E, 0x8E, 0x8F, 0x4F, 0x8D, 0x4D, 0x4C, 0x8C,
            0x44, 0x84, 0x85, 0x45, 0x87, 0x47, 0x46, 0x86,
            0x82, 0x42, 0x43, 0x83, 0x41, 0x81, 0x80, 0x40
        ])

        one_byte = bytearray(1)
        for i in range(len(byte_sequence)):
            one_byte[0] = crc_array[1] ^ byte_sequence[i]
            crc_array[1] = crc_array[0] ^ sr_crc_hi[one_byte[0]]
            crc_array[0] = sr_crc_lo[one_byte[0]]
        return crc_array[::-1]

    def port_exchange(self, send_sequence, len_recv_sequence):

        # if bytearray([0x80, 0x00, 0x60, 0x70]) == send_sequence:
        #     print(1, len_recv_sequence, send_sequence.hex(" "))
        #     return 0, "OK", bytearray([0x80, 0x00, 0x60, 0x70])
        # elif bytearray([0x80, 0x01, 0x01, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31, 0x48, 0xA8]) == send_sequence:
        #     print(2, len_recv_sequence, send_sequence.hex(" "))
        #     return 0, "OK", bytearray([0x80, 0x00, 0x60, 0x70])
        # else:
        #     print(3, len_recv_sequence, send_sequence.hex(" "))
        #     return -5, "OK", bytearray()

        if not super().isOpen():
            try:
                super().open()
            except serial.SerialException as e1:
                return -1, f"Unexpected{e1=}, {type(e1)=}. Error open serial port: " + str(e1), bytearray()

        try:
            super().reset_input_buffer()
            super().reset_output_buffer()
            super().write(send_sequence)
            recv_sequence = super().read(len_recv_sequence)
        except serial.SerialException as e2:
            super().close()
            return -2, f"Unexpected{e2=}, {type(e2)=}. Error operate for serial port: " + str(e2), bytearray()

        return 0, "OK", recv_sequence

    def conversion(self, address, send_sequence, len_recv_sequence):
        """
        Проверяет CRC у принятой последовательности при достижении последней ожидаемых размеров

        либо возвращает пустой массив если timeout или ошибка и ненулевой код ошибки
        :param address: однобайтовый адрес получателя
        :param send_sequence: байтовый массив передаваемой последовательности данных
        :param len_recv_sequence: спсиок содержащий ожидаемые размеры принимаемой последовательности данных
                                   без 2 байт CRC и 1 байта адреса
        :return: кортеж из кода ошибки и байтовой последовательности без CRC и адреса
        """
        len_recv_sequence = 1 if len_recv_sequence < 1 or len_recv_sequence > 255 else len_recv_sequence
        address = 0 if address < 1 or address > 253 else address
        send_sequence.insert(0, address)
        #        print(send_sequence.hex(" "))
        send_sequence.extend(self.modbus_crc(send_sequence))
        #        print(send_sequence.hex(" "))

        n = 0
        while n < 10:
            error_num, error_str, recv_sequence = self.port_exchange(send_sequence, len_recv_sequence + 3)
            if error_num < 0:
                return error_num, error_str, recv_sequence
            if len(recv_sequence) == 4 or len(recv_sequence) == (len_recv_sequence + 3):
                if recv_sequence[-2:] == self.modbus_crc(recv_sequence[:-2]):
                    if recv_sequence[0] == address:
                        if len(recv_sequence) == 4:
                            return recv_sequence[1], \
                                   "Unresolved error" if recv_sequence[1] > len(self.error_answer) \
                                   else self.error_answer[recv_sequence[1]], \
                                   recv_sequence[1:-2]
                        else:
                            return 0, self.error_answer[0], recv_sequence[1:-2]
            n += 1
            if n >= self.quantity_repeat:
                break

        return -3, f"Error read port for {n=} times: " + str(n), bytearray()

    def port_close(self):
        if super().isOpen():
            super().close()
        return


if __name__ == '__main__':
    # help(serial)

    """
    Пример:
            Проверить канал связи со счётчиком с сетевым адресом 80h.
            Запрос: 80 00 (CRC)
            Ответ: 80 00 (CRC) Тестирование канала связи прошло успешно.
    Пример:
            Запрос на открытие канала связи со счётчиком с сетевым адресом 80h, уровень доступа 1, пароль 111111.
            Запрос: 80 01 01 31 31 31 31 31 31 (CRC)
            Ответ: 80 00 (CRC)
            Канал связи открыт.
    """
    mercury_rtu = MercuryRTU()
    print(mercury_rtu.conversion(0x80, bytearray([0x00]), 0x01))  # must be [00]
    print(
        mercury_rtu.conversion(0x80, bytearray([0x01, 0x01, 0x31, 0x31, 0x31, 0x31, 0x31, 0x31]), 0x01))  # must be [00]

    print("Ports are:",list_ports.comports())
