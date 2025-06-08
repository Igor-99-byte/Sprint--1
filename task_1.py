times = '1h 45m,360s,25m,30m 120s,2h 60s'


all_minute = []
all_secund = []
all_hour = []

for time in times.split(','):
    for elements in time.split():
        if 'm' in elements[-1]:
            minute = int(elements.replace('m', ''))
            all_minute.append(minute)
            
        if 's' in elements[-1]:
            secund = (int(elements.replace('s', '')))
            all_secund.append((secund) // 60)

        if 'h' in elements[-1]:
            hour = int(elements.replace('h', ''))
            all_hour.append((hour) * 60)


all_time = sum(all_minute) + sum(all_hour) + sum(all_secund)
            
print(all_time)