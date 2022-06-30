def tri_area(base, height): # it just needed to write the formula and return it
    area = (base * height) / 2 
    return area

base = int(input("Input the base : "))
height = int(input("Input the height : "))
print(tri_area(base, height))

