from datetime import datetime
now =  datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(now.year)
print(now.month)
print(now.day) #day가 날짜입니다.
print(now.hour) 
print(now.minute) 
print(now.second) 
print(f"요일 = {now.weekday()}") #월 0 화 1 수 2
print(f"요일 = {now.isoweekday()}") #일 0 월 1 화 2 수 3

today = datetime.now()
xmas =  datetime(2025,12,25)
remain = xmas - today
print(f"크리스마스까지 남은 날짜는 {remain.days}")