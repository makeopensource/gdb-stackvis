import gdb

class StackVis (gdb.Command):
  """Visualize the stack."""

  def __init__ (self):
    super (StackVis, self).__init__ ("stack-vis", gdb.COMMAND_USER)
    

  def invoke (self, arg, from_tty):
    frame = gdb.newest_frame()
    
    rbp = frame.read_register('rbp')
    rsp = frame.read_register('rsp')
    print(rbp)
    print(rsp)
    
    
    data = StackData(rbp, rsp)

    visualize(data)

class StackData:
    def __init__(self, rbp, rsp):
        self.rbp = rbp
        self.rsp = rsp

def visualize(data):
    height: int = int(data.rsp - data.rbp) // 8
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



StackVis ()
