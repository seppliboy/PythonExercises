from html.entities import name2codepoint


count = 0
name1 = str(input("What is the first name?: "))
name2 = str(input("What is the second name?: "))
name3 = str(input("What is the third name?: "))
name4 = str(input("What is fourth name?: "))
name5 = str(input("What is fifth name?: "))

print(name1, "is awesome!")
print(name2, "is awesome!")
print(name3, "is awesome!")
print(name4, "is awesome!")
print(name5, "is awesome!")

for i in range(10, 21, 2):
    print(i)

#my way ^
#correct way v

count = 0 

while count < 5:
    name = input("Please enter your name: ")
    print(f"{name} is awesome")
    count += 1