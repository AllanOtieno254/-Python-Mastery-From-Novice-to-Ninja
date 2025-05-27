# logical operators(and,or,not): used to check if 2 or more conditional statements are met or true

temp=int(input("What is the temperature outside? "))
if temp >= 0 and temp <= 30:
    print("The temp is good today. Go outside")

elif temp <0 or temp>30:
    print("The temp is bad today.stay inside")


if not(temp >= 0 and temp <= 30):
    print("temp is not good stay at home")