class Pass1:
    def __init__(self):
        self.mdt = ""
        self.pp = 0
        self.kp = 0
        self.mnt = ""
        self.mdtp = 0
        self.start = False
        self.name = False
        self.macro_name = ""
        self.macro_count = 0
        self.lc = 0

    def process(self):

        file = open("/workspaces/PICT_SEM_5/input.asm" , "r")
        for lines in file:
            word = lines.replace("\n", "").replace(
                "'", "").replace(",", "").split(" ")
            if word[0]=="MACRO":
                pntab = []
                self.macro_count+=1
                self.start = True
                self.name = True
                self.mdtp = self.lc+1
            
            elif word[0] == "MEND":
                self.start = False
            else:
                if self.name == True:
                    self.mnt += f"\n{word[0]}"
                    for i in range(1,len(word)):
                        pntab.append(word[i].replace("&",""))
                        self.pp+=1
                    self.name = False
                else:
                    for i in range(len(word)):
                        if word[i] in pntab:
                            self.mdt+=f"(P,{pntab.index(word[i]) + 1})\n"
                        else:
                            self.mdt += f"{word[i]}\t"
            self.lc+=1
            



        self.mnt += f"\t{self.pp}\t{self.kp}\t{self.mdtp}"
        print("MNT",self.mnt)
        print()
        print("MDT\n",self.mdt)
        print()
            # print("Name",self.name)
        print("Pntab\n",pntab)
            # print(word)

obj = Pass1()
obj.process()
