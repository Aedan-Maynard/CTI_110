#Aedan Maynard
#9-26-26
#P2LAB1
#Asking the user for input on the radius of a circle then calculating diameter, circumference, and area.

#Input question and creation of radius to be used in calculations
radius = float(input("what is the radius of the circle? "))
#Creation of diameter variable and calculation
diameter = 2 * radius
#Creation of circumference variable and calculation
circumference = 2 * 3.14159 * radius
#Creation of area variable and calculation
area = 3.14159 * radius ** 2
#print statements for the Diameter, Circumference, and Area

print(f"What is the diameter of the circle? {diameter:.1f}")
print(f"What is the circumference of the circle? {circumference:.2f}")
print(f"What is the area of the circle? {area:.3f}")