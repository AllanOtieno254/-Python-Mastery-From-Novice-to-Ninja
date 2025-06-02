# loop control statements : change loop execution from its normal sequence
#
# break: used to terminate loop entirely
# continue: skips to the next iteration of the loop
# pass: does nothing acts as a placeholder

while True:
    name=input("Enter your name: ")
    if  name !="":
        break

phone_num="123-456-7890"
for i in phone_num:
    if i =="-":
        continue
    print(i,end="")


for i in range(1,21):
    if i==13:
        pass
    else:
        print(i)