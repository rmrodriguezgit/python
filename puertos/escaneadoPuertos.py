import nmap
import sys


def nmap_ping_scan(network_prefix):
    # Crear una instancia de escaneo
    nm = nmap.PortScanner()
    # Configurar los parámetros de nmap
    ping_scan_raw_result = nm.scan(hosts=network_prefix, arguments='-v -n -sn')
    # Analice el resultado del escaneo y colóquelo en la lista de hosts
    host_list = [result['addresses']['ipv4'] for result in ping_scan_raw_result['scan'].values() if
                 result['status']['state'] == 'up']
    return host_list


if __name__ == '__main__':
    for host in nmap_ping_scan('www.rspt.org.cn'):
        print('%-20s %5s' % (host, 'is UP'))