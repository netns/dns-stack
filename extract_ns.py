import ipaddress
import re

pattern = re.compile(r'^(\S+)\s+\d+\s+(A|AAAA)\s+(\S+)$')

with open("named.root", "r") as f:
    for line in f:
        m = pattern.match(line.strip())
        if not m:
            continue

        name, record_type, ip = m.groups()

        try:
            ipaddress.ip_address(ip)
        except ValueError:
            continue

        print(f"master: {ip} # {name}")
