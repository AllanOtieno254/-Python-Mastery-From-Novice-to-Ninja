# nested loops: The inner loop will finish all of its iteration befoe
#                 finishing one iteration of outer loop

rows=int(input("How many rows"))
columns=int(input("How many columns"))
symbol=input("Enter symbol to use")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="") # we use end to prevent moving to next tine
    print()
