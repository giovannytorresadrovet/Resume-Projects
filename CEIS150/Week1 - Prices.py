#Giovanny Torres Adrovet
#D41250849
#May 4th b w/u, 2024

#START
#Ini Variables
count = 0
sum_prices = 0

#Input Full Name
name = input("What is your full name: ")

#Input and convert min_price to float
min_price = float(input("Enter the minimum price: "))

#List of prices
price_list = [69.0, 71.0, 84.5, 91.0, 67.4, 81.2, 84.6, 58.8, 79.3, 101.2]

#Loop through price list
for price in price_list:
    #Add current price to sum
    sum_prices += price
    #If prices is > min_price
    if price > min_price:
        #Then add one
        count += 1

#Output
print("Hello",name,"the minimum price is ", min_price, ".")
print("There are",count,"prices greater than the minimum price.")

#END