print("Welcome to the tip calculator!\n")

bill = float(input("What was the total bill?\n$"))
percentage_tip = int(input("\nWhat is the percentage tip you'd like to leave? 15, 18, 20 or 25 \n"))
num_of_people = int(input("\nHow many people are in your party?\n"))

tip_as_percent = percentage_tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = round(bill + total_tip_amount, 2)
total_bill_per_person = "{:.2f}".format(round(total_bill / num_of_people, 2))

print(f"\nTotal Bill with tip is ${total_bill}\n")
print(f"Bill Per person is ${total_bill_per_person}")