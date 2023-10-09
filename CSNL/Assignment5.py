import time
import math

class FlowControl:
    def __init__(self, m):
        self.mb = m
        self.fs = 0

    def frame_size(self):
        self.fs = 2 ** self.mb - 1
        print("Frame Size ---->", self.fs)

    def go_back(self):
        i = 0
        x = 0
        cnt = 1
        while self.mb != 0:
            j = 0
            k = 0
            v = [0] * self.fs
            while k != self.fs:
                print("Frame", i, "Sent ---->")
                time.sleep(1)
                v[k] = i
                k += 1
                i += 1
            v2 = [0] * self.fs
            while j != self.fs:
                if x == 5 and cnt == 1:
                    v2[j] = -1
                    j += 1
                    x += 1
                    cnt += 1
                    continue
                print("Frame", x, "Received ---->")
                time.sleep(1)
                v2[j] = x
                j += 1
                x += 1
            flag = 0
            for z in range(self.fs):
                if v[z] == v2[z]:
                    time.sleep(1)
                    print("ACKNOWLEDGEMENT Received", v[z], "-->")
                else:
                    print("Retransmit From", v[z], "")
                    i = v[z]
                    x = v[z]
                    flag = 1
                    break
            if flag:
                pass
            else:
                print("Window Slided")
                self.mb -= 1

    def selective(self):
        i = 0
        x = 0
        cnt = 1
        while self.mb != 0:
            j = 0
            k = 0
            v = [0] * self.fs
            while k != self.fs:
                print("Frame", i, "Sent ---->")
                time.sleep(1)
                v[k] = i
                k += 1
                i += 1
            v2 = [0] * self.fs
            while j != self.fs:
                if x == 5 and cnt == 1:
                    v2[j] = -1
                    j += 1
                    x += 1
                    cnt += 1
                    continue
                print("Frame", x, "Received ---->")
                time.sleep(1)
                v2[j] = x
                j += 1
                x += 1
            flag = 0
            c = 0
            for z in range(self.fs):
                if v[z] == v2[z]:
                    time.sleep(1)
                    print("ACKNOWLEDGEMENT Received", v[z], "-->")
                else:
                    c = 1
            if c == 1:
                print("Retransmit", 5, "")
                time.sleep(1)
                print("Frame", 5, "SENT---->")
                time.sleep(1)
                print("Frame", 5, "RECEIVED---->")
                time.sleep(1)
                print("ACKNOWLEDGEMENT", 5, "SENT---->")
            if flag:
                pass
            else:
                print("Window Slided")
                self.mb -= 1

while True:
    a = int(input("Enter Number of Bits--\n"))
    f = FlowControl(a)
    print("YOU WANT TO PERFORM\n1. GO BACK N\n2. SELECTIVE REPEAT\n3. Exit")
    choice = int(input("Enter your choice (1/2/3): "))
    if choice == 1:
        f.frame_size()
        f.go_back()
    elif choice == 2:
        f.frame_size()
        f.selective()
    elif choice == 3:
        break
