import math
pi = math.pi
nope = "We're sorry. You did not chose one of the options."
def formula():
	f = input('\nPress "F" to get all the Formulas. Press enter to quit ')
	f.lower()

	if f == 'f': 
		watform = input("Do you want to see the Circumference, Area, or Volume Formula? ")
		watform.lower()
	
		if watform == 'circumference' or watform == 'cir':
			print("\nThe formula for Circumference of a circle is 2 x Pi (3.1415...) x the radius (r).")
			print("The formula for Circumference of a sphere is the exact same as for Circle and Cylinder")
		
		elif watform == 'area':
			print("\nThe Area of a Circle is Pi x Radius (r) to the power of 2 (^2).")
		
		elif watform == 'volume':
			print("\nThe Volume of a Sphere is 4/3 of Pi x Radius (r) Cubed (^3).")
			print("The Volume of a Cylinder is Pi x r ^2 x Height (h). (Basically, the Area of a circle x the Height)")
			print("The Volume of a Cone is Pi x r ^2 x h / 3 (Basically, 1/3 of the Volume of a cylinder).")
		else:
			print(nope)
	input("Goodbye.")

cva = input('Would you like to find the CIRCUMFERENCE, AREA or VOLUME? ')
cva.lower()

if cva == 'cir' or cva == 'circumference':
	csc = input('Do you want to find the Circumference of a Sphere, Cylinder, or Circle? ')
	csc.lower()
	if csc == 'circle':
		r = input ("\nWhat is the radius of your circle? ")
		r = float(r)
		result = 2 * pi * r
	
	elif csc == 'sphere':
		r = input ("\nWhat is the radius of your sphere? ")
		r = float(r)
		result = 2*pi*r

	elif csc == 'cylinder':
		r = input ("\nWhat is the radius of your cylinder? ")
		r = float(r)
		result = 2*pi*r
	else:
		print(nope)

elif cva == 'volume':
	scc = input('Do you want to find the volume of a Sphere, Cylinder, or Cone? ')
	scc.lower()
	r = input('\nWhat is the Radius? ')
	r = float(r) 

	if scc == 'sphere':
		result = (4/3)*pi*r**3

	elif scc == 'cylinder':
		h = input('What is the Height? ')
		h = float(h)
		result = pi * r ** 2 * h

	elif scc == 'cone':
		h = input('What is the Height? ')
		h = float(h)
		result = (pi * r ** 2 * h)/3
	else:
		print(nope)

elif cva == 'area':
	r = input("\nWhat is the radius of your circle? ")
	r = float(r)
	result = pi * r ** 2
	print("\nThe Area of your circle is roughly", result)
	input()

else:
	input(nope)
	formula();
print("The", cva, "is roughly", result)
input()
formula();

