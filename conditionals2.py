mark = int(input("Enter a number: "))

if mark > 85:
    print("Distinction")
elif mark >= 65 and mark <= 85:
    print("Pass")
else:
    print("Fail")

#with elif ^

if mark >= 65:
    if mark >= 85:
    print("Distinction")
    else:
    print("Pass")
else:
    print("Fail")

#without elif ^