#!/usr/bin/env python3

import time
import serial


def conversion(send_sequence, len_recv_sequence_list, timeout):
    """
    Проверяет CRC у принятой последовательности при достижении последней ожидаемых размеров и
    возвращает последовательность без CRC и 0 в коде ошибки
    либо возвращает пустой массив если timeout или ошибка и ненулевой код ошибки
    :param send_sequence: байтовый массив передаваемой последовательности данных
    :param len_recv_sequence_list: спсиок содержащий ожидаемые размеры принимаемой последовательности данных без 2 байт CRC
    :param timeout:
    :return:
    """
    # import serial, time
    # initialization and open the port
    # configure the serial connections (the parameters differs on the device you are connecting to)
    # ser = serial.Serial(
    #    port='/dev/ttyUSB1',
    #    baudrate=9600,
    #    parity=serial.PARITY_ODD,
    #    stopbits=serial.STOPBITS_TWO,
    #    bytesize=serial.SEVENBITS
    # )

    # possible timeout values:
    #    1. None: wait forever, block call
    #    2. 0: non-blocking mode, return immediately
    #    3. x, x is bigger than 0, float allowed, timeout block call

    ser = serial.Serial()
    ser.port = "/dev/ttyUSB0"
    # ser.port = "/dev/ttyUSB7"
    # ser.port = "/dev/ttyS2"
    ser.baudrate = 9600
    ser.bytesize = serial.EIGHTBITS  # number of bits per bytes
    ser.parity = serial.PARITY_NONE  # set parity check: no parity
    ser.stopbits = serial.STOPBITS_ONE  # number of stop bits
    # ser.timeout = None          #block read
    ser.timeout = 0  # non-block read
    # ser.timeout = 2              #timeout block read
    ser.xonxoff = False  # disable software flow control
    ser.rtscts = False  # disable hardware (RTS/CTS) flow control
    ser.dsrdtr = False  # disable hardware (DSR/DTR) flow control
    ser.writeTimeout = 2  # timeout for write

    try:
        ser.open()
    except Exception as e:
        print("error open serial port: " + str(e))
        exit()

    if ser.isOpen():

        try:
            ser.flushInput()  # flush input buffer, discarding all its contents
            ser.flushOutput()  # flush output buffer, aborting current output
            # and discard all that is in buffer

            # write data
            ser.write("AT+CSQ")
            print("write data: AT+CSQ")

            time.sleep(0.5)  # give the serial port sometime to receive the data

            # while ser.inWaiting() > 0:
            #   out += ser.read(1)

            numOfLines = 0

            while True:
                response = ser.readline()
                print("read data: " + response)
                numOfLines = numOfLines + 1
                if numOfLines >= 5:
                    break

            ser.close()

        except Exception as e1:
            print("error communicating...: " + str(e1))

    else:
        print("cannot open serial port ")


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
#    print(conversion(bytes([0x80, 0x00, 0x70, 0x60])).hex(' '))  # must be [80 00 60 70]


