class Pass2:
    def __init__(self) -> None:
        self.symtab = []
        self.littab = []
        self.machine = ""
        self.lc = 0
        pass

    def readFiles(self):
        with open("/home/pict/31148/pass2/Symtab.txt", "r") as File:
            data = File.readlines()
            for line in data:
                word = line.split()
                self.symtab.append(int(word[2][:-1]))
        with open("/home/pict/31148/pass2/Littab.txt", "r") as File:
            data = File.readlines()
            for line in data:
                word = line.split()
                self.littab.append(int(word[2][:-1]))

    def LiteralORSymbol(self, word):
        # print(word[3:-1])
        index = int(word[3:-1])
        if word.find('L') != -1:
            return (self.littab[index-1])
        else:
            return (self.symtab[index-1])

    def process(self):
        with open("/home/pict/31148/pass2/IC.txt", "r") as file:
            data = file.readlines()
            for line in data:
                word = line.replace("\n", "").strip().split()
                if word[0].find('AD') != -1 or word[0].find('DL,02') != -1:
                    if word[0].find('AD') != -1:
                        if word[0][4:-1] == "01":
                            self.lc = int(word[1][3:-1])
                        elif word[0][4:-1] == "03":
                            # print(word[1][:-2])
                            # print(self.LiteralORSymbol(word[1][:-2]))
                            location = int(self.LiteralORSymbol(word[1][:-2]))
                            add = int(word[1][-1])
                            self.lc = location+add
                        self.machine += '\n'
                            
                    if word[0].find('DL') != -1:
                        self.machine += f"\n{self.lc}"
                        self.lc += int(word[1][3:-1])
                    print()
                elif word[0].find("DL,01") != -1:
                    self.machine += f"\n{self.lc}\t00\t0\t{word[1][3:-1]}"
                    print(f"{self.lc}\t00\t0\t{word[1][3:-1]}")
                    self.lc+=1
                    pass
                elif word[0].find('IS,00') != -1:
                    self.machine += f"\n{self.lc}\t00\t0\t000"
                    print(f"{self.lc}\t00\t0\t000")
                    self.lc+=1
                elif word[0].find('IS,10') != -1:
                    code = self.LiteralORSymbol(word[1])
                    self.machine += f"\n{self.lc}\t10\t0\t{code}"
                    print(f"{self.lc}\t10\t0\t{code}")
                    self.lc+=1
                elif word[0].find('IS') != -1:
                    code1 = word[0][4:6]
                    code2 = word[1][1]
                    # print(word[2])
                    code3 = self.LiteralORSymbol(word[2])
                    # print(code3)
                    self.machine += f"\n{self.lc}\t{code1}\t{code2}\t{code3}"
                    print(f"{self.lc}\t{code1}\t{code2}\t{code3}")
                    self.lc+=1
                else:
                    self.machine += "f\n{self.lc}"
                    self.lc+=1
                    print()

            file.close()
        # print(self.machine)

        with open("machine_code.txt", 'w') as File:
            for i in self.machine:
                File.write(i)
        
        file.close()


test = Pass2()
test.readFiles()
test.process()