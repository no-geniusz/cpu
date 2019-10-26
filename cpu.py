from latches import RSLatch

rs = RSLatch()
print(rs)

while True:
    key = input("R/S")
    if key == 'r':
        rs.r = not rs.r
    elif key == 's':
        rs.s = not rs.s

    rs.eval()
    print(rs)

