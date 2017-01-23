import os


def load(filename):
    from tools.VecMath import Vec2D
    import re
    if not os.path.isfile(filename):
        return []
    blockData = []
    f = open(filename)
    for line in f.readlines():
        line = line.strip()
        if line.startswith('#'):
            continue
        parts = re.split(r'\s+', line.strip())
        if len(parts) != 5:
            continue
        parts = [float(part) for part in parts]
        block = (Vec2D(parts[0], parts[1]), Vec2D(parts[2], parts[3]))
        blockData.append(block)
    return blockData


'''
x  y   b   h
20 10 200 100
20 10 200 100

[20.0, 10.0, 200.0, 100.0],[20.0, 10.0, 200.0, 100.0]

[Block(Vec2D(10, 10), Vec2D(20, 20)), Block(Vec2D(0,780), Vec2D(900,20))]
'''
