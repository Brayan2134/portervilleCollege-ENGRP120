# The givenFunction is x^3 +3x + 2
def givenFunc(x):
	return (x ** 3) + 3 * x + 2

# Bisection Algo
def bisection(a,b):

    # Control Statement
	if (givenFunc(a) * givenFunc(b) >= 0): # Low * high must be positive, or root cannot be found
		print("You have not assumed right a and b\n")
		return

    # Assume midpoint is a
	c = a

    # O(n) where n = iterations on while loop
	while ((b - a) >= 0.001): # while midpoint is not given max, rerun conditional

		# Find middle point
		c = (a + b)/2

		# Check if middle point is root
		if (givenFunc(c) == 0.0):
			break

		# Decide the side to repeat the steps
		if (givenFunc(c)*givenFunc(a) < 0):
			b = c
		else:
			a = c
			
	print("The value of root is : ","%.4f"%c) # Memory address
	

if __name__ == "__main__":
    a = eval(input("Enter a low guess for a: "))
    b = eval(input("Enter high value for b: "))
    bisection(a,b)