from datetime import datetime, timedelta

def parse_to_utc(s):
    date_part, tz_part = s.split(' UTC')
    y, m, d = map(int, date_part.split('-'))
    sign = 1 if tz_part[0] == '+' else -1
    h, mn = map(int, tz_part[1:].split(':'))
    return datetime(y, m, d) - timedelta(hours=sign*h, minutes=sign*mn)

d1 = parse_to_utc(input().strip())
d2 = parse_to_utc(input().strip())

diff = abs((d1 - d2).total_seconds())
print(int(diff // 86400))
