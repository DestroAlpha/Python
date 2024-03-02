from scipy import integrate

# Define the function
def f(x):
    return x**2

# Compute the integral from 0 to 1
integral, error = integrate.quad(f, 0, 1)

print("The integral is:", integral)
print("The absolute error is:", error)
