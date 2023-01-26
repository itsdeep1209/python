def process(start,stop,increment=1,*args,**kwds):
    print(start,stop,increment)
    print(args,type(args))
    print(kwds, type(kwds))
    for key in kwds:
        print(key, kwds[key])

process(10,20,2,1,2,3,4,id=1,name="guido",age=66.3,married=True)