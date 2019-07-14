value=float(input('Enter the value:'))
unit=input('Enter the unit:')
if unit=="inch":
    print("%finch=%fcm"%(value,value*2.54))
elif unit=="cm":
    print("%fcm=%finch"%(value,value/2.54))
else:
    print("Please enter the valid unit")
