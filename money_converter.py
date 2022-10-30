amount = int(input("Enter the amount to convert:"+" "))
print("")
convert = {"Enter Your Choice" : ['dollar','euro','yen']}
print(convert)
currency = input(f"Enter the currency to convert from choice :"+" ")
print(" ")
if currency.lower() == "dollar":
     dollar =float(amount*0.01338)
     format_dollar="{:.2f}".format(dollar)
     print(" ")
     print(f"{amount}INR = {format_dollar} in dollar")
elif currency.lower() == "euro":
     euro =float(amount*0.012)
     format_euro="{:.2f}".format(euro)
     print(" ")
     print(f"{amount}INR = {format_euro} in euro")
elif currency.lower() == "yen":
     yen =float(amount*1.54)
     format_yen = "{:.2f}".format(yen)
     print(" ")
     print(f"{amount}INR = {format_yen} in yen")
else:
     print(" ")
     print("Enter from given choice")

