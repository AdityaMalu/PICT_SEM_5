from typing import List

class Process:
    def __init__(self, name, burst, AT, priority=None):
        self.name = name
        self.BT = burst
        self.WT = 0
        self.AT = AT
        self.CT = 0
        self.TAT = 0
        self.remBT = burst
        self.priority = priority
        self.flag = False

    def display(self):
        print(f"{self.name}\t{self.BT}\t{self.AT}\t{self.CT}\t{self.TAT}\t{self.WT}\t{self.priority}")

def sortByArrival(processes):
    return sorted(processes, key=lambda x: x.AT)

def sortByPriority(processes):
    return sorted(processes, key=lambda x: x.priority)

class FCFS:
    def execute(self, processes):
        processes.sort(key=lambda x: x.AT)

        total_waiting_time = 0
        for process in processes:
            total_waiting_time += process.CT - process.AT
            process.CT += process.BT
            process.TAT = process.CT - process.AT
            process.WT = process.TAT - process.BT
            if process.WT < 0:
                process.WT = 0
            process.display()

        avg_waiting_time = total_waiting_time / len(processes)
        avg_TAT = sum(process.TAT for process in processes) / len(processes)
        print(f"Average Waiting Time: {avg_waiting_time}")
        print(f"Average TAT: {avg_TAT}")

class SJF:
    def execute(self, processes):
        processes.sort(key=lambda x: (x.AT, x.remBT))

        time = 0
        total_waiting_time = 0
        count = 0
        min_remBT = float('inf')

        print("\n\nPRNo\tBT\tAT\tCT\tTAT\tWT")
        print("============================================================================================")

        while count < len(processes):
            for i, process in enumerate(processes):
                if process.AT <= time and 0 < process.remBT < min_remBT:
                    min_remBT = process.remBT
                    shortest = i

            if min_remBT == float('inf'):
                time += 1
                continue

            processes[shortest].remBT -= 1
            min_remBT = processes[shortest].remBT

            if min_remBT == 0:
                min_remBT = float('inf')
                count += 1
                sum_time = time + 1
                processes[shortest].CT = sum_time
                processes[shortest].TAT = processes[shortest].CT - processes[shortest].AT
                processes[shortest].WT = processes[shortest].TAT - processes[shortest].BT

                total_waiting_time += processes[shortest].WT
                processes[shortest].display()
                
            time += 1

        avg_waiting_time = total_waiting_time / len(processes)
        avg_TAT = sum(process.TAT for process in processes) / len(processes)
        print(f"Average Waiting Time: {avg_waiting_time}")
        print(f"Average TAT: {avg_TAT}")

class PriorityNonPreemptive:
    def execute(self, processes):
        processes.sort(key=lambda x: x.priority)

        total_waiting_time = 0
        print("\n\nPRNo\tBT\tAT\tCT\tTAT\tWT\tPR")
        print("============================================================================================")

        for process in processes:
            process.CT += process.BT
            process.TAT = process.CT - process.AT
            process.WT = process.TAT - process.BT

            total_waiting_time += process.WT
            process.display()

        avg_waiting_time = total_waiting_time / len(processes)
        avg_TAT = sum(process.TAT for process in processes) / len(processes)
        print(f"Average Waiting Time: {avg_waiting_time}")
        print(f"Average TAT: {avg_TAT}")

class RoundRobin:
    def execute(self, processes, quantum):
        processes.sort(key=lambda x: x.AT)

        time = 0
        total_waiting_time = 0

        print("\n\nPRNo\tBT\tAT\tCT\tTAT\tWT\tPR")
        print("============================================================================================")

        while True:
            done = True
            for process in processes:
                if 0 < process.remBT and process.AT <= time:
                    done = False

                    if process.remBT > quantum:
                        time += quantum
                        process.remBT -= quantum
                        print(f"Running Process {process.name} from {time - quantum} to {time}")
                    else:
                        time += process.remBT
                        print(f"Running Process {process.name} from {time - process.remBT} to {time}")

                        process.remBT = 0
                        process.CT = time
                        process.TAT = process.CT - process.AT
                        process.WT = process.TAT - process.BT
                        total_waiting_time += process.WT
                        print(f"Completed Process {process.name}")
                        process.display()

            if done:
                break

        avg_waiting_time = total_waiting_time / len(processes)
        avg_TAT = sum(process.TAT for process in processes) / len(processes)
        print(f"Average Waiting Time: {avg_waiting_time}")
        print(f"Average TAT: {avg_TAT}")

def main():
    processes = []
    ch = 0

    while ch != -1:
        print("CPU SCHEDULING ALGORITHMS")
        print("\n 1.FCFS\n 2.SJF\n 3.PriorityNonPreemptive\n 4.Round Robin\n-1.Exit\nENTER: ")
        ch = int(input())

        try:
            if ch == 1:
                fcfs = FCFS()
                fcfs.execute(processes)
            elif ch == 2:
                sjf = SJF()
                sjf.execute(processes)
            elif ch == 3:
                pr = PriorityNonPreemptive()
                pr.execute(processes)
            elif ch == 4:
                rr = RoundRobin()
                quantum = int(input("Enter Quantum Time: "))
                rr.execute(processes, quantum)
            elif ch == -1:
                break
            else:
                raise ValueError("Unexpected value: " + str(ch))
        except Exception as e:
            print(f"Unexpected Value: {e}")

if __name__ == "__main__":
    main()
