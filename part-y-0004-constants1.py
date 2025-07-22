premium_ratio_for_current_month = 11.20

premium_ratio_for_current_month = 10

premium_ratio_for_current_month = "Hi"

print(premium_ratio_for_current_month) # Hi

# But! We need constant premium_ratio

premium_ratio_for_two_months = (11.20, 10.15)

#premium_ratio_for_two_months[0] = 15 # Error! We can't change premium ratio

sales_amount = 22_500

print(f"Monthly premium $ {round(sales_amount * premium_ratio_for_two_months[0])}") # Monthly premium $ 252000
