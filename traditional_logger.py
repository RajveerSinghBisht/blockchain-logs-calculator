import time

LOG_FILE = "traditional.log"

def write_log(message):
    start = time.time()
    
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.time()} - {message}\n")
    
    end = time.time()
    return end - start

def tamper_log(index):
    with open(LOG_FILE, "r") as f:
        logs = f.readlines()
    
    logs[index] = "TAMPERED LOG ENTRY\n"
    
    with open(LOG_FILE, "w") as f:
        f.writelines(logs)

def verify_log(index):
    # Traditional system has no integrity check
    return False