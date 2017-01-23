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
        block = {
            'pos': Vec2D(parts[0], parts[1]),
            'size': Vec2D(parts[2], parts[3]),
            'enemy': parts[4]
        }
        blockData.append(block)
    return blockData

