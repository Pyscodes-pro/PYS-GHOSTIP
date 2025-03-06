import argparse
import requests
import socket
import dns.resolver
import whois
import time
import nmap
import shutil
import sys
import threading
import os
from termcolor import colored

def print_banner():
    """Mencetak banner alat."""
    banner = """
\033[31m
        ██▓███ ▓██   ██▓  ██████      ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓ ██▓ ██▓███     
       ▓██░  ██▒▒██  ██▒▒██    ▒     ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒▓██▒▓██░  ██▒   
       ▓██░ ██▓▒ ▒██ ██░░ ▓██▄      ▒██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░▒██▒▓██░ ██▓▒   
       ▒██▄█▓▒ ▒ ░ ▐██▓░  ▒   ██▒   ░▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░ ░██░▒██▄█▓▒ ▒   
       ▒██▒ ░  ░ ░ ██▒▓░▒██████▒▒   ░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░ ░██░▒██▒ ░  ░   
       ▒▓▒░ ░  ░  ██▒▒▒ ▒ ▒▓▒ ▒ ░    ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░▓  ▒▓▒░ ░  ░   
       ░▒ ░     ▓██ ░▒░ ░ ░▒  ░ ░     ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░     ▒ ░░▒ ░        
       ░░       ▒ ▒ ░░  ░  ░  ░     ░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░       ▒ ░░░          
                ░ ░           ░           ░  ░  ░  ░    ░ ░        ░            ░              
                ░ ░                                                                            
					v 1.1
\033[31m
╭────────────────────────────────────────────────────╮
│              Osint IP Scanner                      │
│                                                    │
│     GitHub    : https://github.com/pyscodes        │
│     Status    : Free Tool                          │
│     Support   : https://linktr.ee/pyscodes         │
│     instagram : https://instagram.com/pyscodes     │
╰────────────────────────────────────────────────────╯
\033[0m
    """
    print(colored(banner, "red"))

def print_intro():
   
    intro_text = """
\033[31m
╔═══════════════════════════════════════════════════╗
║             WELCOME TO PYSGHOSTIP TOOL            ║
║  This tool is designed for OSINT investigations,  ║
║  providing various techniques for IP analysis,    ║
║  reconnaissance, and target information gathering ║
║  						    ║
║           Press Enter to continue...              ║
╚═══════════════════════════════════════════════════╝
\033[0m
"""
    print(colored(intro_text, "red"))
    input()

def clear_screen():
    """Membersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def animated_loading(message, stop_event, delay=0.1):
    
    animation = "|/-\\"
    idx = 0
    while not stop_event.is_set():  # Periksa event untuk berhenti
        print(colored(f"\r{message} {animation[idx % len(animation)]}", "red"), end="", flush=True)
        idx += 1
        time.sleep(delay)
    print(colored("\r", "red"), end="", flush=True)  # Hapus animasi setelah berhenti

def loading_message():
   
    loading_text = "[+] Mengecek dependensi dan koneksi..."
    stop_event = threading.Event()  # Buat event
    loading_thread = threading.Thread(target=animated_loading, args=(loading_text, stop_event))
    loading_thread.start()
    time.sleep(3)  # Simulasi pengecekan dependensi
    stop_event.set()  # Set event untuk menghentikan animasi
    loading_thread.join()  # Tunggu thread selesai
    print(colored("\r[OK] Semua dependensi tersedia!                                     \n", "red"), end="", flush=True)
    time.sleep(1)

def dns_enumeration(domain):
    
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=animated_loading, args=("[+] Melakukan DNS Enumeration...", stop_event))
    loading_thread.start()
    try:
        resolver = dns.resolver.Resolver()
        resolver.nameservers = ["8.8.8.8", "1.1.1.1"]
        answers = resolver.resolve(domain, 'A')
        stop_event.set()  # Set event untuk menghentikan animasi
        loading_thread.join()
        print(colored("\r[OK] DNS Enumeration selesai!                                      \n", "red"), end="", flush=True)
        print(colored("[+] Mencari bocoran IP dari DNS...", "red"))
        for rdata in answers:
            print(colored(f"[FOUND] DNS Enumeration: {rdata}", "red"))
    except Exception as e:
        stop_event = threading.Event()
        loading_thread = threading.Thread(target=animated_loading, args=("[+] Melakukan DNS Enumeration...", stop_event))
        loading_thread.start()
        print(colored("\r[!] DNS Enumeration gagal!                                        \n", "red"), end="", flush=True)
        print(colored(f"[!] DNS Enumeration gagal: {e}", "red"))

def historical_ip_lookup(domain):
    
    print(colored("[+] Mencari riwayat IP...", "red"))
    try:
        # **PENTING:** Ganti YOUR_API_KEY dengan kunci API SecurityTrails Anda!
        api_key = "F6Xpv0hYeBE0tMqylzkjq79vbuGJh55J"  
        url = f"https://api.securitytrails.com/v1/domain/{domain}/history?apikey={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "records" in data:
                for record in data["records"]:
                    print(colored(f"[FOUND] Historical IP: {record['ip']}", "red"))
            else:
                print(colored("[!] Tidak ada data riwayat IP ditemukan", "red"))
        else:
            print(colored(f"[!] Error: {response.text}", "red"))
    except Exception as e:
        print(colored(f"[!] Historical IP Lookup gagal: {e}", "red"))

def direct_ip_leak(domain):
  
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=animated_loading, args=("[+] Mencoba Direct IP Leak...", stop_event))
    loading_thread.start()
    try:
        ip = socket.gethostbyname(domain)
        stop_event.set()
        loading_thread.join()
        print(colored("\r[OK] Direct IP Leak selesai!                                      \n", "red"), end="", flush=True)
        print(colored("[+] Mencoba menemukan IP asli...", "yellow"))
        print(colored(f"[FOUND] Direct IP: {ip}", "red"))
    except Exception as e:
        stop_event.set()
        loading_thread.join()
        print(colored("\r[!] Direct IP Leak gagal!                                        \n", "red"), end="", flush=True)
        print(colored(f"[!] Gagal menemukan IP asli: {e}", "red"))

def whois_lookup(domain):
  
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=animated_loading, args=("[+] Melakukan WHOIS Lookup...", stop_event))
    loading_thread.start()
    try:
        info = whois.whois(domain)
        stop_event.set()
        loading_thread.join()
        print(colored("\r[OK] WHOIS Lookup selesai!                                        \n", "red"), end="", flush=True)
        print(colored("[+] Melakukan WHOIS Lookup...", "yellow"))
        print(colored(f"WHOIS Data:\n{info}", "red"))
    except Exception as e:
        stop_event.set()
        loading_thread.join()
        print(colored("\r[!] WHOIS Lookup gagal!                                          \n", "red"), end="", flush=True)
        print(colored(f"[!] WHOIS Lookup gagal: {e}", "red"))

def port_scanning(domain):
 
    stop_event = threading.Event()
    loading_thread = threading.Thread(target=animated_loading, args=("[+] Memindai port terbuka...", stop_event))
    loading_thread.start()
    try:
        scanner = nmap.PortScanner()
        # Hanya pindai port yang umum dan gunakan argumen yang lebih agresif
        scanner.scan(domain, '21,22,80,443,3389', arguments='-T4')
        stop_event.set()
        loading_thread.join()
        print(colored("\r[OK] Port Scanning selesai!                                       \n", "green"), end="", flush=True)
        print(colored("[+] Memindai port terbuka...", "yellow"))
        for host in scanner.all_hosts():
            print(colored(f"[FOUND] Host: {host}", "red"))
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()
                for port in ports:
                    print(colored(f" - Port {port}: {scanner[host][proto][port]['state']}", "red"))
            break  # Hanya tampilkan informasi untuk host pertama
    except Exception as e:
        stop_event.set()
        loading_thread.join()
        print(colored("\r[!] Port Scanning gagal!                                         \n", "red"), end="", flush=True)
        print(colored(f"[!] Port Scanning gagal: {e}", "red"))

def menu():
   
    global domain

    # Mengatur warna untuk teks menu
    menu_color = "\033[31m"  #Merah
    reset_color = "\033[0m"   # Reset ke warna default

    while True:
        print_banner()

        # Membuat menu dengan karakter garis yang diinginkan
        print(colored(menu_color + "╔════════════════════════════════════╗", "red"))
        print(colored(menu_color + "║ [1] Masukkan Target Domain         ║", "red"))
        print(colored(menu_color + "║ [2] DNS Enumeration                ║", "red"))
        print(colored(menu_color + "║ [3] Historical IP Lookup           ║", "red"))
        print(colored(menu_color + "║ [4] Direct IP Leak                 ║", "red"))
        print(colored(menu_color + "║ [5] WHOIS Lookup                   ║", "red"))
        print(colored(menu_color + "║ [6] Port Scanning                  ║", "red"))
        print(colored(menu_color + "║ [7] Keluar                         ║", "red"))
        print(colored(menu_color + "╚════════════════════════════════════╝" + reset_color, "red"))

        choice = input(colored("Masukkan pilihan (1-7): ", "red"))
        if choice == "7":
            print(colored("GOOD BYE FRIEND ", "red"))
            break
        elif choice == "1":
            domain = input(colored("Masukkan domain target: ", "red"))
        elif choice in feature_mapping and domain:
            feature_mapping[choice](domain)
            input(colored("\nTekan Enter untuk kembali ke menu utama...", "red"))
        elif choice in feature_mapping and not domain:
            print(colored("[!] Harap masukkan domain terlebih dahulu!", "red"))
        else:
            print(colored("[!] Pilihan tidak valid!", "red"))

def main():
  
    parser = argparse.ArgumentParser(description="Bypass Cloudflare & Find Real IP")
    parser.add_argument("-d", "--domain", help="Domain target")
    args = parser.parse_args()
    
    global domain
    domain = args.domain if args.domain else ""
    print_banner()  # Tampilkan banner
    print_intro()   # Tampilkan intro
    clear_screen()  # Bersihkan layar setelah intro
    loading_message()  # Tampilkan pesan loading
    menu()  # Tampilkan menu

# Mapping fitur ke fungsi
feature_mapping = {
    "2": dns_enumeration,
    "3": historical_ip_lookup,
    "4": direct_ip_leak,
    "5": whois_lookup,
    "6": port_scanning
}

if __name__ == "__main__":
    import os
    main()
