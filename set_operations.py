def num_set():
    num=int(input("enter toatl value:"))
    s=set()
    for i in range(num):
        value=int(input(f"value {i+1}:"))
        s.add(value)
    return s
set1=num_set()
set2=num_set()
print("set1=",set1)
print("set2=",set2)
print("\n**mathematical operations**")
print("1.union")
print("2.intersection")
print("3.difference")
print("4.symmetric difference")
x=int(input("Enter number 1 to 4:"))
if x==1:
    print("union:",set1.union(set2))
elif x==2:
    print("intersection:",set1.intersection(set2))
elif x==3:
    print("difference:",set1.difference(set2))
elif x==4: 
    print("symmetric difference:",set1.symmetric_difference(set2))
else:
    print("invalid")








