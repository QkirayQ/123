Dual = []
One = []
Guest = ["Ilay Zahar", "Scot Jon", "Ricki Swader", "Kate Huge", "Noah Jon", "William Davis", "Michael Brown", "Murphy Swader"]
while len(Guest)!=0:
    x = Guest.pop(0)
    a = x.split()
    for y in Guest:
        b = y.split()
        if a[1] == b[1]:
            Guest.remove(y)
            a = a.pop(0)
            Dual.append(a+" and "+ y+ "'s")
            break
    else:
        One.append(x+",")
print(Dual[0], Dual[1],"and" ,One[0],One[1],One[2],One[3], "Willcome to the party")
