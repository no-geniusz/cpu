from latches import DLatch

latch = DLatch()
latch.d = True
latch.e = False

print(latch)

while True:
    key = input("d/e")
    if key == 'e':
        latch.e = not latch.e
    elif key == 'd':
        latch.d = not latch.d

    latch.eval()
    print(latch)

