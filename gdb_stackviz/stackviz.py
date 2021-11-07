import gdb
from typing import List

class StackViz (gdb.Command):
  """Visualize the stack."""

  def __init__ (self):
    super (StackViz, self).__init__ ("stackviz", gdb.COMMAND_USER)
    

  def invoke (self, arg, from_tty):
    try:
        frame = gdb.newest_frame()

        bp = int(frame.read_register('ebp'))
        sp = int(frame.read_register('esp'))

        visualize(bp, sp)

    except gdb.error:
        print('StackViz Error: program stack not initialized')

StackViz()


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



registers = ['ebp', 'eip', 'esp', 'eax', 'ebx', 'ecx', 'edx', 'edi', 'esi']

def visualize(bp, sp):
    if bp < sp or bp < 1000 or sp < 1000:
        print("No stack data found!")
    elif bp == sp:
        print(block(bp, ptrs=['ebp', 'esp']))
    else:
        for address in range(bp, sp-1, -4):
            # print(str.format('0x{:08X}', address))
            ptrs = []
            frame = gdb.newest_frame()
            
            for reg in registers:
                # print(reg, int(frame.read_register(reg)), address)
                if int(frame.read_register(reg)) == address:
                    ptrs.append(reg)

            print(block(address, ptrs))

