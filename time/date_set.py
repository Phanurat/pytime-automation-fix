from datetime import datetime, timedelta
import pytz
import time

# กำหนดเขตเวลา
tz = pytz.timezone('Asia/Bangkok')

# เวลาปัจจุบันในเขตเวลาที่กำหนด
now = datetime.now(tz)

# กำหนดเวลา main break และ end main break
main_break_start = now.replace(hour=21, minute=31, second=0, microsecond=0)
main_break_end = now.replace(hour=7, minute=0, second=0, microsecond=0) + timedelta(days=1)

# run and break intervals for the next day
first_run_start = now.replace(hour=7, minute=1, second=0, microsecond=0) + timedelta(days=1)
first_run_end = now.replace(hour=8, minute=30, second=0, microsecond=0) + timedelta(days=1)

first_break_start = now.replace(hour=8, minute=31, second=0, microsecond=0) + timedelta(days=1)
first_break_end = now.replace(hour=9, minute=0, second=0, microsecond=0) + timedelta(days=1)

run_two_start = now.replace(hour=9, minute=1, second=0, microsecond=0) + timedelta(days=1)
run_two_end = now.replace(hour=10, minute=30, second=0, microsecond=0) + timedelta(days=1)

break_two_start = now.replace(hour=10, minute=31, second=0, microsecond=0) + timedelta(days=1)
break_two_end = now.replace(hour=11, minute=0, second=0, microsecond=0) + timedelta(days=1)

three_run_start = now.replace(hour=11, minute=1, second=0, microsecond=0) + timedelta(days=1)
three_run_end = now.replace(hour=12, minute=59, second=0, microsecond=0) + timedelta(days=1)

break_three_start = now.replace(hour=13, minute=0, second=0, microsecond=0) + timedelta(days=1)
break_three_end = now.replace(hour=14, minute=0, second=0, microsecond=0) + timedelta(days=1)

four_run_start = now.replace(hour=14, minute=1, second=0, microsecond=0) + timedelta(days=1)
four_run_end = now.replace(hour=15, minute=30, second=0, microsecond=0) + timedelta(days=1)

break_four_start = now.replace(hour=15, minute=31, second=0, microsecond=0) + timedelta(days=1)
break_four_end = now.replace(hour=16, minute=0, second=0, microsecond=0) + timedelta(days=1)

five_run_start = now.replace(hour=16, minute=1, second=0, microsecond=0) + timedelta(days=1)
five_run_end = now.replace(hour=17, minute=30, second=0, microsecond=0) + timedelta(days=1)

break_five_start = now.replace(hour=17, minute=31, second=0, microsecond=0) + timedelta(days=1)
break_five_end = now.replace(hour=18, minute=0, second=0, microsecond=0) + timedelta(days=1)

six_run_start = now.replace(hour=18, minute=1, second=0, microsecond=0) + timedelta(days=1)
six_run_end = now.replace(hour=19, minute=30, second=0, microsecond=0) + timedelta(days=1)

break_six_start = now.replace(hour=19, minute=31, second=0, microsecond=0) + timedelta(days=1)
break_six_end = now.replace(hour=20, minute=0, second=0, microsecond=0) + timedelta(days=1)

seven_run_start = now.replace(hour=20, minute=1, second=0, microsecond=0) + timedelta(days=1)
seven_run_end = now.replace(hour=21, minute=30, second=0, microsecond=0) + timedelta(days=1)

# ลูปที่ตรวจสอบว่าเวลาปัจจุบันถึงเวลาเป้าหมายแล้วหรือยัง
while True:
    now = datetime.now(tz)
    
    # ตรวจสอบว่าปัจจุบันอยู่ในช่วง main break หรือไม่
    if main_break_start == now or now < main_break_end:
        print("main break")
        print(f"{now.hour}:{now.minute}")

    elif first_run_start <= now < first_run_end:
        print("Running 1")
        print(f"{now.hour}:{now.minute}")
    
    elif first_break_start <= now < first_break_end:
        print("Mini Break 1")
        print(f"{now.hour}:{now.minute}")
    
    elif run_two_start <= now < run_two_end:
        print("Running 2")
        print(f"{now.hour}:{now.minute}")
    
    elif break_two_start <= now < break_two_end:
        print("Mini Break 2")
        print(f"{now.hour}:{now.minute}")
    
    elif three_run_start <= now < three_run_end:
        print("Running 3")
        print(f"{now.hour}:{now.minute}")
    
    elif break_three_start <= now < break_three_end:
        print("Mini Break 3")
        print(f"{now.hour}:{now.minute}")
    
    elif four_run_start <= now < four_run_end:
        print("Running 4")
        print(f"{now.hour}:{now.minute}")
    
    elif break_four_start <= now < break_four_end:
        print("Mini Break 4")
        print(f"{now.hour}:{now.minute}")
    
    elif five_run_start <= now < five_run_end:
        print("Running 5")
        print(f"{now.hour}:{now.minute}")
    
    elif break_five_start <= now < break_five_end:
        print("Mini Break 5")
        print(f"{now.hour}:{now.minute}")
    
    elif six_run_start <= now < six_run_end:
        print("Running 6")
        print(f"{now.hour}:{now.minute}")
    
    elif break_six_start <= now < break_six_end:
        print("Mini Break 6")
        print(f"{now.hour}:{now.minute}")
    
    elif seven_run_start <= now < seven_run_end:
        print("Running 7")
        print(f"{now.hour}:{now.minute}")

    time.sleep(10)  # หยุดโปรแกรมเป็นเวลา 10 วินาทีเพื่อประหยัดพลังงาน
