from registers import ShiftRegister

reg = ShiftRegister()
for i in range(ShiftRegister.size):
    reg.data[i] = False
reg.e = False
reg.d = False

print(reg)

while True:
    key = input("d/e")
    if key == 'e':
        reg.e = not reg.e
    elif key == 'd':
        reg.d = not reg.d

    reg.eval()
    print(reg)

