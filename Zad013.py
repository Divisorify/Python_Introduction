import datetime
wakeup_str = datetime.datetime(2022, 11, 28, 8, 55, 59)
print(wakeup_str)

now = datetime.datetime.now()

zostalo = wakeup_str - now

print(f'Do pobudki zostało: {zostalo}')
