def find(string, character):
    pos = []
    for i, ch in enumerate(string):
        if ch == character:
            pos.append(i)
    return pos
print(find("rehab", "a"))