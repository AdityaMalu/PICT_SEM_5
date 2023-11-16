class Job:
    def __init__(self, job_id, arrival_time, burst_time, priority):
        self.job_id = job_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.priority = priority

    def __str__(self):
        return f"Job {self.job_id}: Arrival Time={self.arrival_time}, Burst Time={self.burst_time}, Priority={self.priority}"

class Scheduler:
    def __init__(self):
        self.queue = []
        self.time = 0
        self.avg_waiting_time = 0
        self.total_burst_time = 0

    def add_job(self, job):
        self.queue.append(job)

    def fcfs(self):
        self.queue.sort(key=lambda job: job.arrival_time)

        total_waiting_time = 0
        for job in self.queue:
            total_waiting_time += self.time - job.arrival_time
            self.execute_job(job)
        self.avg_waiting_time = total_waiting_time / len(self.queue)
        self.calculate_total_burst_time()

    def sjf_preemptive(self):
        temp_queue = self.queue[:]
        temp_queue.sort(key=lambda job: (job.arrival_time, job.burst_time))

        while temp_queue:
            job = temp_queue[0]
            temp_queue = temp_queue[1:]

            if job.arrival_time > self.time:
                self.time = job.arrival_time

            time_executed = min(job.remaining_time, temp_queue[0].arrival_time - self.time) if temp_queue else job.remaining_time
            self.execute_job(job, time_executed)

            if job.remaining_time > 0:
                temp_queue.append(job)

    def priority_non_preemptive(self):
        self.queue.sort(key=lambda job: job.arrival_time)

        total_waiting_time = 0
        for job in self.queue:
            total_waiting_time += self.time - job.arrival_time
            self.execute_job(job)
        self.avg_waiting_time = total_waiting_time / len(self.queue)
        self.calculate_total_burst_time()

    def round_robin_preemptive(self, time_slice):
        temp_queue = self.queue[:]
        total_waiting_time = 0

        while temp_queue:
            job = temp_queue[0]
            temp_queue = temp_queue[1:]
            waiting_time = self.time - job.arrival_time
            total_waiting_time += waiting_time
            time_executed = min(time_slice, job.remaining_time)
            job.remaining_time -= time_executed
            self.time += time_executed

            if job.remaining_time > 0:
                temp_queue.append(job)
            else:
                self.print_job_completion(job)

        num_completed_jobs = len(self.queue) - len(temp_queue)
        self.avg_waiting_time = total_waiting_time / (num_completed_jobs if num_completed_jobs > 0 else 1)
        self.calculate_total_burst_time()

    def execute_job(self, job):
        self.time = max(self.time, job.arrival_time)
        self.print_job_execution(job)
        self.time += job.burst_time

    def print_job_execution(self, job):
        print(f"Time={self.time}, Executing {job}")

    def print_job_completion(self, job):
        print(f"Time={self.time}, Job {job.job_id} completed!")

    def calculate_total_burst_time(self):
        self.total_burst_time = sum(job.burst_time for job in self.queue)

def main():
    job1 = Job(1, 0, 8, 2)
    job2 = Job(2, 1, 4, 1)
    job3 = Job(3, 2, 9, 3)
    job4 = Job(4, 3, 5, 4)

    scheduler = Scheduler()
    scheduler.add_job(job1)
    scheduler.add_job(job2)
    scheduler.add_job(job3)
    scheduler.add_job(job4)

    print("FCFS:")
    scheduler.fcfs()
    print(f"Average Waiting Time: {scheduler.avg_waiting_time}")
    print(f"Total Burst Time: {scheduler.total_burst_time}")

    print("\nSJF Preemptive:")
    scheduler.sjf_preemptive()
    print(f"Average Waiting Time: {scheduler.avg_waiting_time}")
    print(f"Total Burst Time: {scheduler.total_burst_time}")

    print("\nPriority Non-Preemptive:")
    scheduler.priority_non_preemptive()
    print(f"Average Waiting Time: {scheduler.avg_waiting_time}")
    print(f"Total Burst Time: {scheduler.total_burst_time}")

    print("\nRound Robin Preemptive:")
    scheduler.round_robin_preemptive(3)
    print(f"Average Waiting Time: {scheduler.avg_waiting_time}")
    print(f"Total Burst Time: {scheduler.total_burst_time}")

if __name__ == "__main__":
    main()
