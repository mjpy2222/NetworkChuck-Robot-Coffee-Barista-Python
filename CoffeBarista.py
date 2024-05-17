#Let's start a coffee shop together!!
#Let's build robot Barista!!

#Greet customer
print("Hello, Welcome to NetworkChuck Coffee!!!!!")
name = input("What is your name?\n")

#ask for customer's name
print("Hello " + name + ", thank you so much for coming in today.\n")

#Coffee menu
menu = "Black Coffee, Espresso, Latte, Cappucino"

#Ask customer for their order
order = input(name + ", what would you like from our menu today? Here is what we are serving:\n" + menu + "\n")

#Ask how many they would like
quantity = input("How many " + order + "s would you like?\n")

#coffee price
price = 8

total = price * int(quantity)

print("Thank you. Your total is $" + str(total)))

print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in a moment.")
