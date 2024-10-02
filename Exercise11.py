number= int(input())

for x in range(number):
    text = " " * (x + number + (x*-2))
    for y in range(x + 1+ x):
        text+="*"
    print(text)




