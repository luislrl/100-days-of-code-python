bill = float(input("Wellcome to the tip calculator!\nWhat was the total bill? "))
tip_per = int(input("How much tip would you like to give? 10, 12, or 15? "))
people_qnt = int(input("How many people to split the bill? "))

payment = (bill / ppl_qnt) * (1 + (tip_per/100))

print(f"Each person should pay ${round(payment, 2)}")