def job_scheduling():
    n = int(input("Enter the number of jobs: "))
    jobs = []
    for i in range(n):
        name = input(f"Enter the name of job {i + 1}: ")
        deadline = int(input(f"Enter the deadline for job {i + 1}: "))
        profit = int(input(f"Enter the profit for job {i + 1}: "))
        jobs.append((name, deadline, profit))
    jobs.sort(key=lambda x: x[2], reverse=True)  #Sorts the profit in descending order
    
    schedule = [False] * (max(jobs, key=lambda x: x[1])[1] + 1)
    total_profit = 0
    job_sequence = []
    
    for job in jobs:
        for i in range(job[1], 0, -1):
            if not schedule[i]:
                schedule[i] = True
                total_profit += job[2]
                job_sequence.append(job[0])
                break
    
    print("Job sequence:", " -> ".join(job_sequence))
    print("Total profit:", total_profit)

job_scheduling()



link - https://www.linuxlookup.com/linux_iso
