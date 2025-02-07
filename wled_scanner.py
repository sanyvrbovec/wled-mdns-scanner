from zeroconf import ServiceBrowser, Zeroconf
import time

class WLEDListener:
    def __init__(self):
        self.wled_ip = None

    def remove_service(self, *args):
        pass

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info and b"wled" in name.lower().encode():
            self.wled_ip = info.parsed_addresses()[0]
            print(f"Pronađen WLED uređaj: {self.wled_ip}")

    def update_service(self, *args):
        pass

# Pokreni mDNS pretragu
zeroconf = Zeroconf()
listener = WLEDListener()
browser = ServiceBrowser(zeroconf, "_wled._tcp.local.", listener)  # Promijenjen servis

# Čekajte maksimalno 10 sekundi
timeout = 10
start_time = time.time()
try:
    while listener.wled_ip is None and (time.time() - start_time) < timeout:
        time.sleep(0.1)
finally:
    zeroconf.close()

if listener.wled_ip:
    print(f"WLED IP adresa: {listener.wled_ip}")
else:
    print("WLED uređaj nije pronađen. Provjerite mrežu i WLED konfiguraciju.")