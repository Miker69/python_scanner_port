import os
import socket
from multiprocessing import Process


def port_scan(x, z):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((x, z))
        print(f"{x} Port: {z} is open", end='\n')
    except socket.error:
        pass
    finally:
        s.close()

try:
    host = input('Enter host:')
    delete_words = ('http://', 'https://', '/')
    for i in delete_words:
         host = host.replace(i, '')
    host = socket.gethostbyname(host)
except:
    print('Ошибка в название хоста' )
    os.system(exit())

print('Start scan...')
my_list = []
for port in range(65536):
    mult = Process(target=port_scan, args=(host, port))
    my_list.append(mult)
    mult.start()

for my_thread in my_list:
    my_thread.join()
print('Scan completed!')
