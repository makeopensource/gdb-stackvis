import gdb
from typing import List

class StackVis (gdb.Command):
  """Visualize the stack."""

  def __init__ (self):
    super (StackVis, self).__init__ ("stack-vis", gdb.COMMAND_USER)
    

  def invoke (self, arg, from_tty):
    frame = gdb.newest_frame()

    rbp = int(frame.read_register('rbp'))
    rsp = int(frame.read_register('rsp'))

    print(rbp, rsp)
    visualize(rbp, rsp)

StackVis()


# hex formatter (0x{02X} per byte)
def fhex(number: int) -> str:
    hex_str = str.format('{:08X}', number)
    formatted_data = ' '.join(['0x' + hex_str[i:i+2] for i in range(0,len(hex_str),2)])
    return formatted_data


# generates a stack block
def block(address: int, ptrs: List[str]=[]) -> str:
    inferiors = gdb.inferiors()[0]
    # formatted = fhex(inferiors.read_memory(address, 8))
    formatted = fhex(address)

    return '\t'*4 + '|' + ' '*(len(formatted)+6) + '|\n' + \
           '\t'*2 + str.format('0x{:08X}', address) + '\t'*1 + '|' + ' '*3 + fhex(address) + ' '*3 + '|\n' + \
           '\t'*4 + '|' + ' '*(len(formatted)+6) + '|\n' + \
           '\t'*4 + '|' + '-'*(len(formatted)+6) + '|' + \
           ' '.join([f' <-- {x}' for x in ptrs])


def visualize(rbp, rsp):
    height: int = (rsp - rbp)
    if rbp > rsp or :
        print("No stack data found!")
    elif rbp == rsp:
        print(block(rbp, ptrs=['rbp', 'rsp']))
    else:
        for i in range(0,height,8):
            if i == 0:
                print(block(rbp + i, ptrs=['rbp']))
            elif i == height - 1:
                print(block(rbp + i, ptrs=['rsp']))
            else:
                print(block(rbp + i, []))

