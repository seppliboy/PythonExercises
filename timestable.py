#n = int(input("Enter your number: "))
#list1 = (list(range(1, n+1)))
#list2 = (list(range(2, n*2+1, 2)))
#list3 = (list(range(3, n*3+1, 3)))
#list4 = (list(range(4, n*4+1, 4)))

#print(list1)
#print(list2)
#print(list3)
#print(list4)

n = int(input("Enter your number: "))
line = ""

for row in range(1, n+1):
    for column in range(1, n+1):
        line = line + str(row*column) + "\t"
    line = line + "\n"
print(line)

