from telnetlib import Telnet
import time
import re


def read(telnet_conn, sleep=1.5):
    time.sleep(sleep)
    data = telnet_conn.read_very_eager().decode()
    return data

def write(telnet_conn, data):
    byte_data = data.encode()
    telnet_conn.write(byte_data)


if __name__ == '__main__':
    host = "192.168.122.73"
    username = "hamza"

    # Create telnet connection
    tn = Telnet(host)

    d = read(tn)
    print(d)

if re.search(r'sername', d):
    write(tn, 'hamza\n')
    d = read(tn)
    print(d)