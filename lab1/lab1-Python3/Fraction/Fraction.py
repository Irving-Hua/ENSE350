# Python3 program to reduce a fraction x/y 
# to its lowest form 
from math import gcd 

# Function to reduce a fraction 
# to its lowest form 
def reduceFraction(x, y) : 
	
	d = gcd(x, y); 

	x = x // d; 
	y = y // d; 

	print("x =", x, ", y =", y); 

# Driver Code 
if __name__ == "__main__" : 

	x = 16; 
	y = 10; 

	reduceFraction(x, y); 

# This code is contributed by Ryuga 

