def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return c_lib*n
    else:
        blocks = 0
        roads = 0
        notConnected = list(range(1,n+1))

        i = 1
        cities = cities
        group = [None]*n
        for m in range(n)
            
        while(len(notConnected) >0 ):
            l = [i]
            notConnected.remove(i)
            l,notConnected,cities = recshit(cities,l,i,notConnected)
            if len(notConnected) >0:
                i = notConnected[0]
            blocks+=1
            roads += len(l)-1
        return c_lib*blocks +c_road*roads
def recshit(cities,l,c,notConnected):
    for x in cities:
        if c in x:
            cities.remove(x)
            if x[0] not in l:
                l.append(x[0])
                notConnected.remove(x[0])
                l,notConnected,cities = recshit(cities,l,x[0],notConnected)
            if x[1] not in l:
                l.append(x[1])
                notConnected.remove(x[1])
                l,notConnected,cities = recshit(cities,l,x[1],notConnected)
    return l,notConnected,cities
