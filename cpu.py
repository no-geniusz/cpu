from registers import Register
from registers import REG_WIDTH
from adders import RCAdder

reg1 = Register()
reg1.e = 0
reg2 = Register()
reg2.e = 0
adder = RCAdder()

print(reg1)
print(reg2)
print(adder)

while True:
    key = input("d/e")
    if key == 'e':
        reg1.e = not reg1.e
        reg2.e = not reg2.e

    for ch in range(1,5):
        if (str(ch) == key):
            reg1.d[REG_WIDTH - ch] = not reg1.d[REG_WIDTH - ch]
    for ch in range(5,9):
        if (str(ch) == key):
            reg2.d[REG_WIDTH - ch] = not reg2.d[REG_WIDTH - ch]

    reg1.eval()
    print(reg1)

    reg2.eval()
    print(reg2)

    for k in range(REG_WIDTH):
        adder.a[k] = reg1.q[k]
        adder.b[k] = reg2.q[k]
    adder.eval()
    print(adder)
