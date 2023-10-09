import math

def check_class(IP):
    print("Your IP class:", end=" ")
    first_oct = IP.find('.')
    f_oct = IP[:first_oct]

    if 0 <= int(f_oct) <= 127:
        print("Class A")
        print("Default subnetMask: 255.0.0.0")
    elif 128 <= int(f_oct) <= 191:
        print("Class B")
        print("Default subnetMask: 255.255.0.0")
    elif 192 <= int(f_oct) <= 224:
        print("Class C")
        print("Default subnetMask: 255.255.255.0")
    elif 225 <= int(f_oct) <= 239:
        print("Class D")
        print("Default subnetMask: not defined")
    elif 240 <= int(f_oct) <= 255:
        print("Class E")
        print("Default subnetMask: not defined")

def count_bits(n):
    count = 0
    while n:
        count += 1
        n >>= 1
    return count

def create_subnet(IP, n):
    # Only for class C
    bit_to_transfer = math.ceil(math.log(n, 2))

    subnetted_mask = 0

    for i in range(7, 7 - bit_to_transfer, -1):
        subnetted_mask += 2**i

    print("SubnettedMask:", f"255.255.255.{subnetted_mask}")

    range_to_add = 2**(8 - bit_to_transfer)
    print(range_to_add)
    var_num = 0
    print("\nYour range-->>")
    third_dot = IP.rfind('.')
    
    three_oct = IP[:third_dot]
    i = 0
    for i in range(n):
        print(f"{three_oct}.{var_num} - {three_oct}.{var_num + range_to_add - 1}")
        var_num += range_to_add
        var_num += 1

    print("Unused subnets:")
    for i in range(2**bit_to_transfer):
        print(f"{three_oct}.{var_num} - {three_oct}.{var_num + range_to_add - 1}")
        var_num += range_to_add
        var_num += 1

if __name__ == "__main__":
    no_subnet = int(input("How many subnets to mask?\n"))
    IP = input("Enter the IP: ")

    check_class(IP)
    create_subnet(IP, no_subnet)

    print()
    print()
    
    cmd = f"ping {IP}"
    import os
    os.system(cmd)
