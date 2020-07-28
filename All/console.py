import os

x = os.get_terminal_size().lines
y = os.get_terminal_size().columns

print(x)
print(y)