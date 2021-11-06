def Visualize(data):
    height: int = (data.rsp - data.rbp) // 8
    print(height)
    if data.rbp == data.rsp:
        print("No stack data found!")
        return
    for i in range(height):
        if i == 0:
            print(f"                |---------------------------------------------|\n")
            print(f"                |                                             |\n")
            print(f" {hex(data.rbp)} |   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00   |\n")
            print(f"                |                                             |\n")
            print(f"                |---------------------------------------------| <--- rbp\n")
        #big loopy
        data.rbp = data.rbp + 0x4
        print(f"                |                                             |\n")
        print(f" {hex(data.rbp)} |   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00   |\n")
        print(f"                |                                             |\n")
        print(f"                |---------------------------------------------|\n")

        if i == height - 1:
            print(f"                |                                             |\n")
            print(f" {hex(data.rsp)} |   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00   |\n")
            print(f"                |                                             |\n")
            print(f"                |---------------------------------------------| <-- rsp\n")
