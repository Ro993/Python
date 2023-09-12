#list mutable data type seprated by commaa(,), collection of ordered data, have an index position
mylist=[10,20,30]
print(mylist[0])
mylist[0]=20
print(mylist)
mylist.append(100)
print(mylist)
mylist.extend("hii")
print(mylist)
mylist.extend(["hii", 40, 50])
print(mylist)
mylist.pop()    # by default delete last value
print(mylist)
del mylist[0]
print(mylist)

