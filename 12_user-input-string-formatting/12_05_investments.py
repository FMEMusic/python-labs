# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

investment = int(input("Investment Amount: $ "))
interest = int(input("Interest rate %: "))
years = int(input("Number of years to invest:"))

print(f"The total value of your investment is $ {int(investment*(1+ interest/100)*years)}.00")