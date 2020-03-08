dailyprice = [1,1,1,1,1,1,1,7,7,7,7,7,7,7]
#dailyprice = [7,8,8,11,9,7,5,6]

def weekly(dailyprice):
    res = []
    print(sum(dailyprice[0:7]))
    for i in range(len(dailyprice)-6):
        res.append("{0:.2f}".format((round(sum(dailyprice[i: i+7])/7,2))))
    print(res)
    
weekly(dailyprice)
