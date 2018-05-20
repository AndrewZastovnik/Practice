def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return c_lib*n
    else:
        group = [None]*n
        count = 0
        thing = {}
        for m in cities:
            if group[m[0]-1] == None and group[m[1]-1] == None:
                count += 1
                thing[count] = count
                group[m[0]-1] = count
                group[m[1]-1] = count
            else:
                if group[m[0]-1] == None:
                    group[m[0]-1] = group[m[1]-1]
                elif group[m[1]-1] == None:
                    group[m[1]-1] = group[m[0]-1]
                else:
                    if list(thing.values()).count(thing[group[m[0]-1]]) >1:
                        thing = updatedict(thing,thing[group[m[0]-1]],thing[group[m[1]-1]])
                    else:
                        thing[group[m[0]-1]] = thing[group[m[1]-1]]
        roads = 0
        libraries = 0
        for i in range(n):
            if group[i] == None:
                libraries +=1
            else:
                roads +=1
        groups = len(set(thing.values()))
        libraries += groups
        return c_lib*libraries+c_road*(roads- groups)

def updatedict(dict,value,replace):
    for key in dict.keys():
        if dict[key] == value:
            dict[key] = replace
    return dict
