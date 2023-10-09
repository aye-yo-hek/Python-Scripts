# Pseudo code for a simple port scanner
import socket
from colorama import Fore

# Define colors as global variables
GREEN = Fore.GREEN
GRAY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET

# Function to perform port scanning
def portScanner(host, port):
    # Create a socket object
    sock = socket.socket()
    
    try:
        # Attempt to connect to the host and port
        sock.connect((host, port))
        sock.settimeout(0.2)
    except:
        # If the connection fails, the port is closed
        return False
    else:
        # If the connection succeeds, the port is open
        return True

# Function to scan ports on a given host
def runner():
    host = input("Please enter the host to scan: ")
    
    for port in range(1, 1000):
        if portScanner(host, port):
            print(f"{GREEN}[+] The port {port} is open on {host}! {RESET}")
        else:
            print(f"{GRAY}[-] Port {port} is closed! {RESET}", end="\r")

if __name__ == "__main__":
    runner()

# You can open ports for testing the script using commands like:
# sudo nc -lvnp 80 &
# sudo nc -lvnp 99 &
# ...and so on

# To verify how many ports you have open, use the following command:
# sudo netstat -ntlpa | grep -i listen
