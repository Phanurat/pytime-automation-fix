import concurrent.futures
import subprocess

# ฟังก์ชันเพื่อรันไฟล์ Python
def run_script(script_name):
    subprocess.run(["python", script_name])

# รันไฟล์ Python พร้อมกัน
scripts = ["file1.py", "file2.py", "file3.py", "file4.py"]

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(run_script, scripts)
