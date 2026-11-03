import sys
from collections import Counter

contador = Counter()
with open(sys.argv[1]) as arquivo:
    for linha in arquivo:
        if "Failed password" in linha:
            ip = linha.split(" from ")[1].split()[0]
            contador[ip] += 1

for ip, total in contador.most_common():
    print(f"{ip}: {total} failed attempts.")
