# Enter deposit data
s = float(input())  # Initial amount in rubles
p = float(input())  # Interest rate in percent
t = float(input())  # Deposit term in years
d = float(input())  # Frequency of interest calculation in months

# Calculate the number of interest periods
n = t * 12 / d

# Calculate the effective interest rate for the period
i = p / 100 / 12 * d

# We calculate the deposit amount at the end of the term using the compound interest formula
f = s * (1 + i) ** n

# Round the amount to two decimal places
f = round(f, 2)

# Display the amount on the screen
print("Deposit amount at the end of the term:", f, "usa dollar.")
