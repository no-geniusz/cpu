from latches import RSLatch

latch = RSLatch()
latch.r = True
latch.s = False

print(latch)

while True:
    key = input("r/s")
    if key == 'r':
        latch.r = not latch.r
    elif key == 's':
        latch.s = not latch.s

    latch.eval()
    print(latch)

