def nonDivisibleSubset(k, S):
    mod = []
    for n in range(len(S)):
        mod.append((S[n]%k))
    remove = 0
    for x in set(mod):
        for y in set(mod):
            if x+y == k:
                if mod.count(x) < mod.count(y):
                    remove += mod.count(x)
                elif mod.count(x) == mod.count(y) and (mod.count(x) != 1 or x!=y):
                    remove += mod.count(x)-1/mod.count(y)
            elif x+y == 0:
                print(x,y,mod.count(x),mod.count(y))
                remove += mod.count(x)-1
    return len(S) - int(remove)
