#Remove multiple elements from a list in Python 
mylist = [10, 20, 30, 40, 50, 60]
x = [10, 20]
for number in mylist[:]:
    if number in x:
        mylist.remove(number)
print(mylist)
