from latches import DLatch

d_latch = DLatch()
print(d_latch)

while True:
    key = input("d/e")
    if key == 'd':
        d_latch.d = not d_latch.d
    elif key == 'e':
        d_latch.e = not d_latch.e

    d_latch.eval()
    print(d_latch)

