# Programer Name: Ani Ohanian
# Date:7/29/22
# Description: This program designs a consignment shop that accepts a product for sale and sets an initial price. 
# Each month that the item doesn’t sell, the price is reduced by 20 percent. When the item sells, the item’s owner 
# receives 60 percent of the sale price, and the shop gets 40 percent. Draw a flowchart and write pseudocode to 
# represent the logic of a program that allows the user to enter an original product price. The output is the sale price, 
# the owner’s cut, and the shop’s cut each month for the first three months the item is on sale.

originalProductPrice = float(input("Please enter the original product price: $"))

for numberOfMonth in range(3):

    month = numberOfMonth + 1
    originalProductPrice = originalProductPrice - (originalProductPrice * (0.2))
    ownerCut = originalProductPrice - (originalProductPrice * (0.6))
    shopCut = originalProductPrice - (originalProductPrice * (0.4))
    print("Month" + str(month) +"'s sales price of the product after 20% reduction is: $" + str(round(originalProductPrice,2)) 
    + "\nOwner's cut is 60% of the sales price of this month which is: $"+ str(round(ownerCut,2)) 
    + "\nShop's cut is 40% of the sales price of this month which is: $"+ str(round(shopCut,2))+"\n")
