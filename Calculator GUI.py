# __Author__ __Lencof__
# Calculator GUI.py
from tkinter import * # use tkinter
from operator import add, sub, mul, truediv 
  
OPFUNC = {'+': add, '-': sub, '*': mul, '/': truediv} # create cortege
  
class ParseErr(Exception): # create class ParseErr(Exception)
    pass # empty block
  
screen = Tk() # cteare window TK() 
  
calc = StringVar(screen) # assing
calc.set("") # calc.set("")

  
  def lexer(s): # create def lexer(5)
  in_int = False # False
  current = [] 
  tokens = [] 
  for cur in s: 
      in in_int:
          if cur.isdigit():
              current.append(cur)
              continue
          else:
              tokens.append(int("".join(current)))
              in_int = False
              current = []
          if cur.isdigit():
              current.append(cur)
              in_int = True
          elif cur in ('+', '-', '*', '/'):
              tokens.append(cur)
          elif not cur.isspace():
              return f"Unexpected char '{cur}'"
  if in_int:
      tokens.append(int("".join(current)))
  return tokens
      
  
def parser(tokens): # create def parser(token)
    stack = []
    op_stack = []
    for tok in tokens:
        if isinstance(tok, int):
            stack.append(tok)
        else:
            while op_stack and not (tok in ('*', '/') and op_stack[-1] in ('+', '-')):
                right = stack.pop()
                stack.append(OPFUNC[op_stack.pop()](stack.pop(), right))
            op_stack.append(tok)
    for op in op_stack[::-1]:
        right = stack.pop()
        stack.append(OPFUNC[op](stack.pop(), right))
    return stack[0]


show = Frame(screen) # appropriated

entry = Entry(show, textvariable=calc, width="19", state="disable") # youe size
entry.grid(column=0, row=0) # your size

ac = Button(show, text='AC', width=4, height=2, command=lambda: calc.set("")) # your size
ac.grid(column=1, row=0) # your size

show.pack() # close

buttons = Frame(screen)

# figures
tab = ["789/", 
       "456*",
       "123+",
       "0.=-"]

for i, line in enumerate(tab):
    for j, case in enumerate(line):
        if case == "=":
            a = lambda x=case: calc.set(parser(lexer(calc.get().strip())))
        else:
            a = lambda x=case: calc.set(calc.get() + x)
        Button(buttons, text=case, width=4, height=2, command=a).grid(column=j, row=i)

buttons.pack() # close

screen.mainloop() # close
