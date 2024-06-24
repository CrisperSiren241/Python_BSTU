# При помощи вложенных циклов постройте фигуры:
# №1
#  + + + + + + + + + 
#  +               + 
#  +               + 
#  +               + 
#  +               + 
#  + + + + + + + + +   
# №2
#  + + + + + + + + + 
#  +       +       + 
#  + + + + + + + + + 
#  +       +       + 
#  + + + + + + + + + 
#  +       +       + 
#  + + + + + + + + + 

print("№1")
for i in range(6):
    for j in range(10):
        if i == 0 or i == 5 or j == 0 or j == 9:
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\n№2")
for i in range(7):
    for j in range(21):
        if (i % 3  == 0) or (j % 10 == 0):
            print("+", end=" ")
        else:
            print(" ", end=" ")
    print()



