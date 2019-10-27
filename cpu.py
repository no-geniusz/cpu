from registers import Register
from registers import REG_WIDTH

reg = Register()
for i in range(REG_WIDTH):
    reg.d[i] = False
reg.e = False

print(reg)

while True:
    key = input("d/e")
    if key == 'e':
        reg.e = not reg.e

    for ch in range(1,5):
        if (str(ch) == key):
            reg.d[REG_WIDTH - ch] = not reg.d[REG_WIDTH - ch]

    reg.eval()
    print(reg)

