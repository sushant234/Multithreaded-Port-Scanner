Multithreaded Port Scanner

A Python script that scans TCP and UDP ports using multithreading.

Usage

To use the port scanner, first clone this repository to your local machine:

git clone https://github.com/your_username/your_repository.git
Then navigate to the cloned directory:

cd your_repository
Next, install the required dependencies using pip:

pip install -r requirements.txt
Finally, run the port scanner with the following command:

python port_scanner.py TARGET_IP [--tcp-ports TCP_PORTS] [--udp-ports UDP_PORTS]

Replace TARGET_IP with the IP address of the target you want to scan. The --tcp-ports and --udp-ports options are optional and allow you to specify lists of TCP and UDP ports to scan, respectively. If these options are not specified, the script will scan ports 1-1023 for both TCP and UDP.

For more information on how to use the port scanner, run the following command:

python port_scanner.py --help
License

This project is licensed under the MIT License - see the LICENSE file for details.
