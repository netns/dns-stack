import sys
from pathlib import Path
import ipaddress
import re

pattern = re.compile(r"^(\S+)\s+\d+\s+(A|AAAA)\s+(\S+)$")

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} <named.root path>")
    sys.exit(1)

named_file = Path(sys.argv[1]).expanduser().resolve()

if not named_file.exists() or not named_file.is_file():
    print("invalid file")
    sys.exit(1)

with open(named_file, "r") as f:
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
