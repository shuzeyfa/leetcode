dis,tr,v,g,r = map(int,input().split())
count = tr/v
summ = g+r
if count<=0:
    summ = dis/v
    print("%.7f" % (summ))
else:
    rem = r-count
    first = tr/v
    sec = (dis-tr) / v
    summ = first+sec+rem
    print("%.10f" % (summ))