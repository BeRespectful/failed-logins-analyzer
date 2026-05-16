# failed-logins-analyzer

A Python tool for SOC analysts to identify brute force login attempts from Windows authentication logs.

## What it does

- Parses Windows authentication log CSVs
- Identifies failed login events (Event ID 4625)
- Counts failures per source IP
- Surfaces top brute force candidates, sorted by failure count descending

## MITRE ATT&CK Mapping

Detects [T1110.001 — Brute Force: Password Guessing](https://attack.mitre.org/techniques/T1110/001/)

## Sample Output

```
203.0.113.42: 23
198.51.100.7: 8
10.0.1.47: 7
10.0.1.70: 6
45.33.17.92: 5
...
```

External IPs with elevated failure counts are flagged as top brute force candidates for SOC triage.

## How to Run

```bash
python3 failed_logins.py
```

The script expects `auth_logs.csv` in the same directory. A sample dataset is included.

## Detection Logic

1. Reads CSV authentication logs
2. Filters for EventID 4625 (failed login)
3. Aggregates by SourceIP, skipping rows with missing IP data
4. Sorts by failure count, descending
5. Outputs ranked list ready for analyst triage

## Roadmap

- [x] Step 1: CSV parsing and total failure counting
- [x] Step 2: Per-IP aggregation and sorted output
- [ ] Step 3: Time-window burst detection (5+ failures from same IP in 60 seconds)
- [ ] Step 4: KQL detection rule translation for Microsoft Sentinel

## Author

Muhammad Bilal Ahmed — Building toward a Microsoft Sentinel / Defender XDR SOC role.
