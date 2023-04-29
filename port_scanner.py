import argparse
import threading
import socket

# Define a function for scanning TCP ports
def scan_tcp(target_ip, port):
    try:
        # Create a TCP socket and attempt to connect to the port
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_sock.settimeout(1)
        tcp_sock.connect((target_ip, port))
        print 'TCP port %d is open' % port
        tcp_sock.close()
    except:
        pass

# Define a function for scanning UDP ports
def scan_udp(target_ip, port):
    try:
        # Create a UDP socket and send a dummy message to the port
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_sock.settimeout(1)
        udp_sock.sendto(b'Dummy Message', (target_ip, port))
        response, _ = udp_sock.recvfrom(1024)
        print 'UDP port %d is open' % port
        udp_sock.close()
    except:
        pass

# Define a function for scanning all TCP and UDP ports using multithreading
def scan_ports(target_ip, tcp_ports, udp_ports):
    # Create a list of threads for TCP port scanning
    tcp_threads = []
    for port in tcp_ports:
        t = threading.Thread(target=scan_tcp, args=(target_ip, port))
        tcp_threads.append(t)
    
    # Create a list of threads for UDP port scanning
    udp_threads = []
    for port in udp_ports:
        t = threading.Thread(target=scan_udp, args=(target_ip, port))
        udp_threads.append(t)

    # Start all TCP threads
    for t in tcp_threads:
        t.start()

    # Start all UDP threads
    for t in udp_threads:
        t.start()

    # Wait for all threads to finish
    for t in tcp_threads + udp_threads:
        t.join()

# Define a function for parsing command line arguments
def parse_args():
    parser = argparse.ArgumentParser(description='Multithreaded port scanner')
    parser.add_argument('target_ip', type=str, help='Target IP address')
    parser.add_argument('--tcp-ports', type=int, nargs='+', default=range(1, 1024), help='TCP ports to scan (default: 1-1023)')
    parser.add_argument('--udp-ports', type=int, nargs='+', default=range(1, 1024), help='UDP ports to scan (default: 1-1023)')
    args = parser.parse_args()
    return args

# Define a function for printing the usage information
def print_usage():
    print 'Usage: python port_scanner.py target_ip [--tcp-ports TCP_PORTS] [--udp-ports UDP_PORTS]'
    print ''
    print 'Options:'
    print '  --tcp-ports TCP_PORTS  TCP ports to scan (default: 1-1023)'
    print '  --udp-ports UDP_PORTS  UDP ports to scan (default: 1-1023)'

if __name__ == '__main__':
    # Parse command line arguments
    args = parse_args()

    # Scan ports using multithreading
    scan_ports(args.target_ip, args.tcp_ports, args.udp_ports)
