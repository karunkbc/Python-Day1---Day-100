print("Welcome to the tip calculator.")
bill=float(input("What  was your total bill ? RS "))
tip=int(input("What percentage tip would you like to give ? 10, 12 or 15 ? "))
people=int(input("How many people to split the bill ? "))
bill_with_tip=tip/100 *bill
total_bill=bill+bill_with_tip
bill_per_person=total_bill/people
final_amount=round(bill_per_person ,2 )
print(f"Each preson should pay :RS {final_amount}")
