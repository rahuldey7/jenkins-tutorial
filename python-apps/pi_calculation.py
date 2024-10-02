from decimal import Decimal, getcontext

# Set the precision level higher to store and display more digits
getcontext().prec = 50  # Increase precision to 50 decimal places

def calculate_pi(iterations):
    pi_approx = Decimal(0)
    for i in range(iterations):
        # Leibniz series: alternating sum of 1/(2n + 1) using Decimal
        pi_approx += Decimal((-1) ** i) / Decimal(2 * i + 1)
    
    # Multiply the result by 4 to get the approximation of pi
    return 4 * pi_approx

# Example: calculating pi with 50 iterations
iterations = 50
pi_value = calculate_pi(iterations)
print(f"Approximated value of pi after {iterations} iterations: {pi_value}")
