from telnetlib import Telnet
import time


def read(telnet_conn, sleep=1.5):
    time.sleep(sleep)
    data = telnet_conn.read_very_eager().decode()
    return data


if __name__ == '__main__':
    host = "192.168.122.73"
    username = "hamza"

    # Create telnet connection
    tn = Telnet(host)

    d = read(tn)
    print(d)