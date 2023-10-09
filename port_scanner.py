#For more information on socket module go here: https://realpython.com/python-sockets/
import socket
from colorama import Fore
#colors as global variables
GREEN = Fore.GREEN
GRAY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET

def portScanner(host, port):
    #creates an object of class socket
    sock = socket.socket()
    try: 
        sock.connect((host,port))
        sock.settimeout(.2)
    #if connection fails
    except: 
        return False
    #If it succeeds 
    else: 
        return True
    
#Determine the host
def runner():
    #Use your localhost IP: 127.0.0.1 
    host = input("Please enter the host to scan: ")
    for port in range(1, 1000):
        
        if (portScanner(host, port)):
            print(f"{GREEN}[+]The port {port} was open on {host}! {RESET}")
        else:
            print(f"{GRAY}[-]Port is closed!{RESET}", end="\r")

if __name__ == "__main__":
    runner()

#we can open ports to test our script on your local host, open the terminal and use the following commands: 
#sudo nc -lvnp 80 & 
#sudo nc -lvnp 99 & ..and so on

#verify how many ports you have open by using the following command:
#sudo netstat -ntlpa | grep -i listen 

