import socket
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(Fore.GREEN + f"[OPEN] Port {port}")
        sock.close()
    except Exception as e:
        print(Fore.RED + f"[ERROR] {e}")

def main():
    # ASCII Banner with colors
    print(Fore.CYAN + Style.BRIGHT + '''
██████╗  ██████╗ ██████╗ ████████╗    ███████╗███████╗███████╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝    ██╔════╝██╔════╝██╔════╝
██████╔╝██║   ██║██████╔╝   ██║       ███████╗█████╗  █████╗  
██╔═══╝ ██║   ██║██╔══██╗   ██║       ╚════██║██╔══╝  ██╔══╝  
██║     ╚██████╔╝██║  ██║   ██║       ███████║███████╗███████╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝╚══════╝╚══════╝
                                                        V 1.0
''')

    print(Fore.MAGENTA + "Author : " + Fore.YELLOW + "Saloni " +
          Fore.GREEN + "--> this tool helps to check open/closed ports ⚡\n")

    # Inputs
    target = input(Fore.CYAN + "🔷 Enter IP or domain: ")
    start_port = int(input(Fore.CYAN + "🔶 Start port: "))
    end_port = int(input(Fore.CYAN + "🔷 End port: "))

    print(Fore.LIGHTBLUE_EX + f"\n🔍 Scanning {target} from port {start_port} to {end_port}...\n")

    # Port scanning
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, target, port)

if __name__ == "__main__":
    main()
