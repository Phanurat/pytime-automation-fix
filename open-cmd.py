import subprocess
import time

# คำสั่งเพื่อเปิด Command Prompt ใหม่
command = 'start cmd /k "echo Hello, World!"'

# รันคำสั่ง
subprocess.run(command, shell=True)
