import gdb
from typing import List

class StackVis (gdb.Command):
  """Visualize the stack."""

  def __init__ (self):
    super (StackVis, self).__init__ ("stack-vis", gdb.COMMAND_USER)
    

  def invoke (self, arg, from_tty):
    frame = gdb.newest_frame()

    bp = int(frame.read_register('ebp'))
    sp = int(frame.read_register('esp'))

    print(bp, sp)
    visualize(bp, sp)

StackVis()


# hex formatter (0x{02X} per byte)
def fhex(number: int) -> str:
    hex_str = str.format('{:08X}', number)
    formatted_data = ' '.join(['0x' + hex_str[i:i+2] for i in range(0,len(hex_str),2)])
    return formatted_data


# generates a stack block
def block(address: int, ptrs: List[str]=[]) -> str:
    inferiors = gdb.inferiors()[0]
    memory: bytes = inferiors.read_memory(address, 4)

    int_mem: int = int.from_bytes(memory, 'little')
    formatted = fhex(int_mem)

    return '\t'*4 + '|' + ' '*(len(formatted)+6) + '|\n' + \
           '\t'*2 + str.format('0x{:08X}', address) + '\t'*1 + '|' + ' '*3 + formatted + ' '*3 + '|\n' + \
           '\t'*4 + '|' + ' '*(len(formatted)+6) + '|\n' + \
           '\t'*4 + '|' + '-'*(len(formatted)+6) + '|' + \
           ' '.join([f' <-- {x}' for x in ptrs])


def visualize(bp, sp):
    height: int = (bp - sp)
    if bp < sp or bp < 1000 or sp < 1000:
        print("No stack data found!")
    elif bp == sp:
        print(block(bp, ptrs=['ebp', 'esp']))
    else:
        for i in range(0, height+1, 8):
            if i == 0:
                print(block(bp - i, ptrs=['ebp']))
            elif i >= height-1:
                print(block(bp - i, ptrs=['esp']))
            else:
                print(block(bp - i, []))

