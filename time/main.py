from datetime import datetime, timedelta
import pytz
import time

# กำหนดเขตเวลา
tz = pytz.timezone('Asia/Bangkok')

# เวลาปัจจุบันในเขตเวลาที่กำหนด
now = datetime.now(tz)

# กำหนดเวลา main break และ end main break
main_break = now.replace(hour=21, minute=31, second=0, microsecond=0)
end_main_break = now.replace(hour=7, minute=0, second=0, microsecond=0) + timedelta(days=1)

#run 07:01 - 08:30
first_run = now.replace(hour=7, minute=1, second=0, microsecond=0) + timedelta(days=1)
first_run_end = now.replace(hour=8, minute=30, second=0, microsecond=0) + timedelta(days=1)

#mini break 08:31 - 09.00
first_break = now.replace(hour=8, minute=31, second=0, microsecond=0) + timedelta(days=1)
first_break_end = now.replace(hour=9, minute=0, second=0, microsecond=0) + timedelta(days=1)

#run 09.01 - 10.30
run_two = now.replace(hour=9, minute=1, second=0, microsecond=0) + timedelta(days=1)
end_run_two = now.replace(hour=10, minute=30, second=0, microsecond=0) + timedelta(days=1)

#mini break 10.31 - 11.00
break_two = now.replace(hour=10, minute=31, second=0, microsecond=0) + timedelta(days=1)
end_break_two = now.replace(hour=11, minute=0, second=0, microsecond=0) + timedelta(days=1)

#run 11.01 - 12.59
three_run = now.replace(hour=11, minute=1, second=0, microsecond=0) + timedelta(days=1)
end_three_run = now.replace(hour=12, minute=59, second=0, microsecond=0) + timedelta(days=1)

#mini break 13.00 - 14.00
break_three = now.replace(hour=13, minute=0, second=0, microsecond=0) + timedelta(days=1)
end_break_three = now.replace(hour=14, minute=0, second=0, microsecond=0) + timedelta(days=1)

#run 14.01 - 15.30
four_run = now.replace(hour=14, minute=1, second=0, microsecond=0) + timedelta(days=1)
end_four_run = now.replace(hour=15, minute=30, second=0, microsecond=0) + timedelta(days=1)

#mini break 15.31 - 16.00
break_four = now.replace(hour=15, minute=31, second=0, microsecond=0) + timedelta(days=1)
end_break_four = now.replace(hour=16, minute=0, second=0, microsecond=0) + timedelta(days=1)

#run 16.01 - 17.30
five_run = now.replace(hour=16, minute=1, second=0, microsecond=0) + timedelta(days=1)
end_five_run = now.replace(hour=17, minute=30, second=0, microsecond=0) + timedelta(days=1)

#mini break 17.31 - 18.00
break_five = now.replace(hour=17, minute=31, second=0, microsecond=0) + timedelta(days=1)
end_break_five = now.replace(hour=18, minute=0, second=0, microsecond=0) + timedelta(days=1)

#run 18.01 - 19.30
six_run = now.replace(hour=18, minute=1, second=0, microsecond=0) + timedelta(days=1)
end_six_run = now.replace(hour=19, minute=30, second=0, microsecond=0) + timedelta(days=1)

#mini break 19.31 - 20.00
break_six = now.replace(hour=19, minute=31, second=0, microsecond=0) + timedelta(days=1)
end_break_six = now.replace(hour=20, minute=0, second=0, microsecond=0) + timedelta(days=1)

#run 20.01 - 21.30
seven_run = now.replace(hour=20, minute=1, second=0, microsecond=0) + timedelta(days=1)
end_seven_run = now.replace(hour=21, minute=30, second=0, microsecond=0) + timedelta(days=1)

# ลูปที่ตรวจสอบว่าเวลาปัจจุบันถึงเวลาเป้าหมายแล้วหรือยัง
while True:
    now = datetime.now(tz)
    
    # ตรวจสอบว่าปัจจุบันอยู่ในช่วง main break หรือไม่
    if main_break <= now < end_main_break:
        print("main break")
        print(f"{now.hour}:{now.minute}")

    elif first_run <= now < first_run_end:
        print("Running 1")
        print(f"{now.hour}:{now.minute}")
    
    elif first_break <= now < first_break_end:
        print("Mini Break 1")
        print(f"{now.hour}:{now.minute}")
    
    elif run_two <= now < end_run_two:
        print("Running 2")
        print(f"{now.hour}:{now.minute}")
    
    elif break_two <= now < end_break_two:
        print("Mini Break 2")
        print(f"{now.hour}:{now.minute}")
    
    elif three_run <= now < end_three_run:
        print("Running 3")
        print(f"{now.hour}:{now.minute}")
    
    elif break_three <= now < end_break_three:
        print("Mini Break 3")
        print(f"{now.hour}:{now.minute}")
    
    elif four_run <= now < end_four_run:
        print("Running 4")
        print(f"{now.hour}:{now.minute}")
    
    elif break_four <= now < end_break_four:
        print("Mini Break 4")
        print(f"{now.hour}:{now.minute}")
    
    elif five_run <= now < end_five_run:
        print("Running 5")
        print(f"{now.hour}:{now.minute}")
    
    elif break_five <= now < end_break_five:
        print("Mini Break 5")
        print(f"{now.hour}:{now.minute}")
    
    elif six_run <= now < end_six_run:
        print("Running 6")
        print(f"{now.hour}:{now.minute}")
    
    elif break_six <= now < end_break_six:
        print("Mini Break 6")
        print(f"{now.hour}:{now.minute}")
    
    elif seven_run <= now < end_seven_run:
        print("Running 7")
        print(f"{now.hour}:{now.minute}")

    time.sleep(10)  # หยุดโปรแกรมเป็นเวลา 10 วินาทีเพื่อประหยัดพลังงาน
