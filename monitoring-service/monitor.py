import psutil
import time
import os
from datetime import datetime

while True:
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    log_message = f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"

    print(log_message)
    with open("logs/system.log", "a") as log:
        log.write(log_message + "\n")
    

    if cpu > 80:
        print("WARNING: High CPU Usage!")

    if memory > 80:
        print("WARNING: High Memory Usage!")

    if disk > 80:
        print("WARNING: High Disk Usage!")
        with open("logs/incidents.csv", "a") as log:
            log.write(f"{datetime.now()},Critical,High Disk Usage,Triggered\n"
    )
        print("\nTriggering AI Analysis Service...\n")
        os.system("python ai-analysis-service/analyze.py")
        print("\nTriggering Auto-Healing Service...\n")
        os.system("python auto-healing-service/heal.py")

    time.sleep(5)