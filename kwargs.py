# kwargs: parameter that will pack all arguments into a dictionary
#         useful so that a function can accept a varying amount of keyword_arguments

def hello(**kwargs):
    print("Hello " + kwargs["first"] + " " + kwargs["last"])

hello(first="Allan", middle="Akumu", last="Otieno")

def hello(**kwargs):
    print("Hello ")
    for key,value in kwargs.items():
        print(value,end="")

hello(title="Mr.",first="Allan",middle=" Otieno",last=" Akumu")












