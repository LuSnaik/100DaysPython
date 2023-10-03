# # calculadora de gorjeta

# # greetings
# print("Welcome to the tip calculator")

# # a conta total
bill = float(input("What was the total bill? $"))

# # percentagem de gorjeta, tem 10, 12, e 15
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip_perc = tip / 100

# # divisão da conta
div = int(input("How many people to split the bill? "))

# calculos

## percentagem
bill_p = bill * tip_perc
bill += bill_p
#bill = round(bill)
## div
#div = round((bill / div), 2)
div = f"{(bill / div):.2f}"

message = f"Each person should pay: ${div}"

print(message)