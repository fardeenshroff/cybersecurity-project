class Firewall:
    def _init_(self):
        self.allowed_ips = ['192.168.1.10', '192.168.1.20']
        self.allowed_ports = [80, 443]

    def filter_traffic(self, ip, port):
        if ip in self.allowed_ips and port in self.allowed_ports:
            return "Traffic allowed"
        else:
            return "Traffic blocked"
