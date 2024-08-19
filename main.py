def rp(list, i, z, p=[]):
    if len(p) >= 2:
        return p
    if list[i:z] == list[i+z:z+z]:
        p.append(list[i:z])
        i += 1
        z += 1
        rp(list, i, z, p)
    else:
        if z == len(list)/2 + 1:
            return p
        z += 1
        rp(list, i, z, p)
    return p

i = 0
z = 1
n = [1,2,3,4,5,1,2,3,4,5]
print(rp(n, i, z))
