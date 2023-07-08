#!/usr/bin/python

### Project: 3L3Y3 Scanner
### Author: param373r pka belikeParamjot apka TheProJ4X0N

### Find me on following media:
###### Twitter: @param373r
###### Instagram: @param373r
###### Medium: @param373r

from socket import *
import optparse
from threading import *
from termcolor import colored


def connHost(THost, TPort, output=None):
	try:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.connect((THost,TPort))
		print colored('   [+]%d/tcp open', 'green') %TPort

		if output != None:
			file = open(output, 'a')		
   			file.write("[+]Port: %d is open\n" %TPort) 
   			file.close()
   	except:
		print colored('   [-]%d/tcp close', 'red') %TPort
	finally:
		sock.close()


def portScanner(THost,TPorts,output=None):
	try:
		hostIP= gethostbyname(THost)
	except:
		print ' Unknown host ' + THost

	try:
		hostName= gethostbyaddr(hostIP)
		print colored('\n[+]Scan results for ', 'blue') + colored(hostName, 'green')
	except:
		print colored('\n[+]Scan results for ', 'blue') + colored(hostIP, 'green')

	try:

		for TPort in TPorts:
			t= Thread(target = connHost , args = (THost,int(TPort), output))
			t.start()
			t.join()
		print colored('\n   [+] Scan Completed', 'magenta')
	except KeyboardInterrupt:
		print colored("\n   [+] Scan Finished", 'yellow')
		print "   Bye!!"
		exit(0)

def main():
	parser = optparse.OptionParser(' eli -H <targetHost> -p <targetPorts>')
	parser.add_option("-H", "--host", dest='THost', type= 'string', help = 'Enter Host IP or Host/Domain Name')
	parser.add_option("-p", "--ports", dest='TPorts', type= 'string', help = 'Enter the ports separated by \',\' (without spaces)')
	parser.add_option("-c", "--top200", dest='top200', action="store_false", help = 'To scan the Top 200 ports in Nmap\'s scan')
	parser.add_option("-a", "--all", dest='all', action="store_false", help = 'To scan the ALL 65535 ports on the host (This one\'s gonna be slow... a lot)')
	parser.add_option("-o", "--outfile", dest='filename', type= 'string', help = 'Output the open ports detected to a file')
	(options ,args) = parser.parse_args()

	THost = options.THost
	TPorts = str(options.TPorts).split(',')

	if (THost == None) | (TPorts == None):
		print colored('\n[x] Use -h flag to show options\n', 'yellow')
		exit(0)
	if(options.filename is not None):
		output = options.filename
		if (options.top200 is not None):
			portScanner(THost, top200, output)
		elif (options.all is not None):
			portScanner(THost, allports, output)
		else:
			portScanner(THost,TPorts, output)
	elif (options.top200 is not None):
		portScanner(THost, top200)
	elif (options.all is not None):
		portScanner(THost, allports)
	else:
		portScanner(THost,TPorts)


if __name__ == '__main__':
	top200 = [7, 9, 13, 17, 19, 21, 22, 23, 37, 42, 49, 53, 67, 68, 69, 80, 88, 111, 120, 123, 135, 136, 137, 138, 139, 158, 161, 162, 177, 192, 199, 389, 407, 427, 443, 445, 464, 497, 500, 514, 515, 517, 518, 520, 593, 623, 626, 631, 664, 683, 800, 989, 990, 996, 997, 998, 999, 1001, 1008, 1019, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1036, 1038, 1039, 1041, 1043, 1044, 1045, 1049, 1068, 1419, 1433, 1434, 1645, 1646, 1701, 1718, 1719, 1782, 1812, 1813, 1885, 1900, 2000, 2002, 2048, 2049, 2148, 2222, 2223, 2967, 3052, 3130, 3283, 3389, 3456, 3659, 3703, 4000, 4045, 4444, 4500, 4672, 5000, 5001, 5060, 5093, 5351, 5353, 5355, 5500, 5632, 6000, 6001, 6346, 7938, 9200, 9876, 10000, 10080, 11487, 16680, 17185, 19283, 19682, 20031, 22986, 27892, 30718, 31337, 32768, 32769, 32770, 32771, 32772, 32773, 32815, 33281, 33354, 34555, 34861, 34862, 37444, 39213, 41524, 44968, 49152, 49153, 49154, 49156, 49158, 49159, 49162, 49163, 49165, 49166, 49168, 49171, 49172, 49179, 49180, 49181, 49182, 49184, 49185, 49186, 49187, 49188, 49189, 49190, 49191, 49192, 49193, 49194, 49195, 49196, 49199, 49200, 49201, 49202, 49205, 49208, 49209, 49210, 49211, 58002, 65024]
	x = list()
	for i in range(1, 65536):
		x.append(i)
	allports = x
	main()
