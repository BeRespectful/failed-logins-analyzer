import csv

from pathlib import Path
failed_ip = {}
with open(Path(__file__).parent / "auth_logs.csv") as f:
    read = csv.DictReader(f)
    for row in read:
        if row["EventID"] == "4625":
            ip = row["SourceIP"]
            failed_ip[ip] = failed_ip.get(ip, 0) + 1
for ip, count in sorted(failed_ip.items(), key=lambda x: x[1], reverse=True):
    if not ip:
        continue
    print(f"{ip}: {count}")