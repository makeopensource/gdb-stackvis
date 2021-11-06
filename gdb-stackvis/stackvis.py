import gdb


class StackVis (gdb.Command):
  """Visualize the stack."""

  def __init__ (self):
    super (StackVis, self).__init__ ("stack-vis", gdb.COMMAND_USER)
    

  def invoke (self, arg, from_tty):
    frame = gdb.newest_frame()

    rbp = frame.read_register('rbp')
    rsp = frame.read_register('rsp')

    data = StackData(rbp, rsp)

    visualize(data)

class StackData:
    def __init__(self, rbp, rsp):
        self.rbp = rbp
        self.rsp = rsp


StackVis ()
