def run_fcfs(processes):
    # Sort processes primarily by Arrival Time
    sorted_p = sorted(processes, key=lambda x: x[1])
    t = 0
    results = {}
    
    for pid, at, bt in sorted_p:
        if t < at:
            t = at
        t += bt
        ct = t
        tat = ct - at
        wt = tat - bt
        results[pid] = {'AT': at, 'BT': bt, 'CT': ct, 'TAT': tat, 'WT': wt}
        
    return results

def run_sjf(processes):
    t = 0
    done = []
    results = {}
    
    while len(done) < len(processes):
        # Filter processes that have arrived by time 't' and are not yet completed
        available = [x for x in processes if x[1] <= t and x not in done]
        
        if not available:
            t = min(x[1] for x in processes if x not in done)
            continue
            
        # Select process with the shortest Burst Time
        selected = min(available, key=lambda x: x[2])
        pid, at, bt = selected
        
        t += bt
        ct = t
        tat = ct - at
        wt = tat - bt
        
        results[pid] = {'AT': at, 'BT': bt, 'CT': ct, 'TAT': tat, 'WT': wt}
        done.append(selected)
        
    return results

# Standardized Test Dataset: (Process ID, Arrival Time, Burst Time)
dataset = [('P1', 2, 5), ('P2', 3, 1), ('P3', 0, 2), ('P4', 1, 3), ('P5', 1, 6)]

# Execute Algorithms
fcfs_metrics = run_fcfs(dataset)
sjf_metrics = run_sjf(dataset)

# Display Comparison
print("=" * 65)
print(f"{'CPU SCHEDULING ALGORITHM COMPARISON':^65}")
print("=" * 65)

def display_table(title, metrics):
    print(f"\n--- {title} ---")
    print(f"{'PID':<8}{'AT':<8}{'BT':<8}{'CT':<8}{'TAT':<8}{'WT':<8}")
    print("-" * 48)
    tot_tat = tot_wt = 0
    for pid in sorted(metrics.keys()):
        m = metrics[pid]
        tot_tat += m['TAT']
        tot_wt += m['WT']
        print(f"{pid:<8}{m['AT']:<8}{m['BT']:<8}{m['CT']:<8}{m['TAT']:<8}{m['WT']:<8}")
    
    n = len(metrics)
    avg_tat = tot_tat / n
    avg_wt = tot_wt / n
    print("-" * 48)
    print(f"Average Turnaround Time (TAT) : {avg_tat:.2f}")
    print(f"Average Waiting Time (WT)    : {avg_wt:.2f}")
    return avg_tat, avg_wt

fcfs_avg_tat, fcfs_avg_wt = display_table("1. FCFS Algorithm", fcfs_metrics)
sjf_avg_tat, sjf_avg_wt = display_table("2. SJF (Non-Preemptive) Algorithm", sjf_metrics)

print("\n" + "=" * 65)
print(f"{'SUMMARY & VERDICT':^65}")
print("=" * 65)
print(f"FCFS Avg WT : {fcfs_avg_wt:.2f} | SJF Avg WT : {sjf_avg_wt:.2f}")
print(f"FCFS Avg TAT: {fcfs_avg_tat:.2f} | SJF Avg TAT: {sjf_avg_tat:.2f}")

if sjf_avg_wt < fcfs_avg_wt:
    print("\nVERDICT: SJF is BETTER because it minimizes the Average Waiting Time.")
elif fcfs_avg_wt < sjf_avg_wt:
    print("\nVERDICT: FCFS performed better for this specific dataset.")
else:
    print("\nVERDICT: Both algorithms yielded identical performance.")
print("=" * 65)
