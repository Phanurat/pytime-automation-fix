import subprocess

processes = [
    subprocess.Popen(["python", "file1.py"]),
    subprocess.Popen(["python", "file2.py"]),
    subprocess.Popen(["python", "file3.py"]),
    subprocess.Popen(["python", "file4.py"])
]

for process in processes:
    process.wait()