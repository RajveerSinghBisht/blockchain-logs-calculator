import time
import os
import pandas as pd
import subprocess
subprocess.run(["python", "deploy_contract.py"])
from traditional_logger import write_log as t_write
from blockchain_logger import write_log as b_write
from blockchain_logger import verify_log
overall_start = time.time()

#WORKLOADS = [100,1000,10000]
WORKLOADS = [100, 1000]

results = []

for workload in WORKLOADS:
    run_id = int(time.time())
    workload_start = time.time()
    print(f"Running workload: {workload}")
    
    #clear logs before each workload
    open("traditional.log", "w").close()
    open("blockchain.log", "w").close()
    
    # Traditional
    t_times = []
    start_t = time.time()

    for i in range(workload):
        t = t_write(f"log {i}")
        t_times.append(t)

    end_t = time.time()
    total_time_t = end_t - start_t
    
    # Blockchain
    b_times = []
    gas_used = []
    
    start_b = time.time()

    for i in range(workload):
        t, gas = b_write(f"log {i}")
        b_times.append(t)
        gas_used.append(gas)
        if i % 5000 == 0:
            print(f"Blockchain progress: {i}/{workload}")

    end_b = time.time()
    total_time_b = end_b - start_b

    # measure verification time (sample first 100 logs or less)
    v_times = []

    for i in range(min(100, workload)):
        result, t = verify_log(i)
        v_times.append(t)

    avg_verification_time = sum(v_times) / len(v_times)
    
    workload_end = time.time()
    total_workload_time = workload_end - workload_start
    print(f"Completed {workload} logs in {total_workload_time:.2f} seconds")
    
    results.append({
        "workload": workload,
        "t_latency": sum(t_times)/len(t_times),
        "b_latency": sum(b_times)/len(b_times),
        "t_throughput": workload / total_time_t,
        "b_throughput": workload / total_time_b,
        "total_gas": sum(gas_used),
        "verification_time": avg_verification_time,
        "run_id": run_id
    })

print("\n--- Tampering Experiment ---")

from blockchain_logger import tamper_log, verify_log

# Choose an index safely (must exist)
test_index = 5

print(f"Tampering log at index {test_index}...")
tamper_log(test_index)

print("Verifying tampered log...")
result, t = verify_log(test_index)

print(f"Tampering detected: {not result}")
print(f"Verification time: {t}")

overall_end = time.time()
print(f"\nTotal experiment time: {overall_end - overall_start:.2f} seconds")

df = pd.DataFrame(results)
file_exists = os.path.isfile("results.csv")

df.to_csv(
    "results.csv",
    mode='a',          # append mode
    header=not file_exists,  # write header only if file doesn't exist
    index=False
)
