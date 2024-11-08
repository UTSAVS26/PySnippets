class Job:
    def __init__(self, id, dead, profit):
        self.id = id  # Job ID
        self.dead = dead  # Deadline for job completion
        self.profit = profit  # Profit if job is completed before or on deadline

def compare(job):
    return job.profit

def min_num(num1, num2):
    return num2 if num1 > num2 else num1

def job_sequencing(jobs, n):
    # Sort jobs by profit in descending order
    jobs.sort(key=compare, reverse=True)

    # List to store the result (sequence of job IDs)
    result = [-1] * n
    # Boolean list to keep track of occupied time slots
    slot = [False] * n

    # Iterate through all jobs
    for i in range(n):
        # Find a free slot for this job, checking from the last possible slot
        for j in range(min_num(n, jobs[i].dead) - 1, -1, -1):
            if not slot[j]:  # If slot is free
                result[j] = i  # Assign this job to the slot
                slot[j] = True  # Mark the slot as occupied
                break

    # Get the sequence of job IDs for maximum profit
    job_sequence = [jobs[result[i]].id for i in range(n) if slot[i]]
    return job_sequence
  
# Example
if __name__ == "__main__"
    n = 4
    jobs = [
        Job('a', 4, 20),
        Job('b', 1, 10),
        Job('c', 1, 40),
        Job('d', 1, 30)
    ]
    
    # Display the sequence of jobs that maximize profit
    print("Following is the maximum profit sequence of jobs:")
    print(" ".join(job_sequencing(jobs, n)))
