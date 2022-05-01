def highesteven(mylist):
    def iseven(myinteger):
        return myinteger % 2 == 0

    for num in sorted(mylist, reverse=True):
        if iseven(num):
            return num
