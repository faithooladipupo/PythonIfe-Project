availableItems = {
    "1": {"Item": "Sugar", "quantity": "131", "price": "50"},
    "2": {"Item": "Bread (sliced)", "quantity": "311", "price": "200"},
    "3": {"Item": "Bread (unsliced)", "quantity": "229", "price": "150"},
    "4": {"Item": "Egg", "quantity": "545", "price": "50"},
    "5": {"Item": "Three crown (tin)", "quantity": "201", "price": "150"},
    "6": {"Item": "Peak milk (tin)", "quantity": "230", "price": "120"},
    "7": {"Item": "Peak milk (sachet)", "quantity": "791", "price": "50"},
    "8": {"Item": "Bournvita (sachet)", "quantity": "611", "price": "50"},
    "9": {"Item": "Milo (tin)", "quantity": "367", "price": "500"},
    "10": {"Item": "Peak milk (Large sachet)", "quantity": "889", "price": "700"},
    "11": {"Item": "Milo (Large sachet)", "quantity": "934", "price": "700"},
    "12": {"Item": "Bournvita (Large sachet)", "quantity": "758", "price": "100"},
    "13": {"Item": "Custard (small sachet)", "quantity": "383", "price": "200"},
    "14": {"Item": "Corn flakes (small sachet)", "quantity": "647", "price": "150"},
    "15": {"Item": "Golden morn (small sachet)", "quantity": "121", "price": "100"},
    "16": {"Item": "Detergent (small Wawu)", "quantity": "198", "price": "120"},
    "17": {"Item": "Detergent (small Aerial)", "quantity": "354", "price": "115"},
    "18": {"Item": "Detergent (Big Wawu)", "quantity": "323", "price": "200"},
    "19": {"Item": "Detergent (Big Aerial)", "quantity": "222", "price": "250"},
    "20": {"Item": "Corn flakes (Big sachet)", "quantity": "341", "price": "750"},
    "21": {"Item": "Golden morn (Large sachet)", "quantity": "458", "price": "650"},
    "22": {"Item": "Sprite (small)", "quantity": "134", "price": "80"},
    "23": {"Item": "Pepsi (small)", "quantity": "674", "price": "80"},
    "24": {"Item": "Fanta (small)", "quantity": "757", "price": "80"},
    "25": {"Item": "Lacasera (small)", "quantity": "127", "price": "80"},
    "26": {"Item": "Sprite (Big)", "quantity": "956", "price": "150"},
    "27": {"Item": "Pepsi (Big)", "quantity": "374", "price": "150"},
    "28": {"Item": "Fanta (Big)", "quantity": "267", "price": "150"},
    "29": {"Item": "Lacasera (Big)", "quantity": "786", "price": "150"},
    "30": {"Item": "Coke (Big)", "quantity": "546", "price": "150"}
}

#To change the price of any item in available items:
def changePrice(itemNo, new_price):
    availableItems[itemNo]["price"] = new_price
    return availableItems

#To add a new iem into the list of available items:
def addNewItem(itemNo, item, quantity, price):
    availableItems[itemNo] = {"Item": item, "quantity": quantity, "price": price}
    return availableItems


print("ITEMS AVAILABLE AND THEIR PRICES(N)")
print("NO      ITEM", "  ---  ", "PRICE(N)")
for x, y in availableItems.items():
    print(x, "  ", y["Item"], "---", y["price"])


buy = input("Do you want to buy an item, y/n? ")
if buy == "y".lower():
    purchase = "y".lower()
    while purchase == "y".lower():
        purchaseDict = {}
        def purchase(total, count):
            itemNo = input("Enter the NO of the item from the list of available items above: ")
            if itemNo not in availableItems:
                print("Item not available")       
            else:
                item = availableItems[itemNo]["Item"]
                price = availableItems[itemNo]["price"]
                print(item, "-", price)
                itemQuantity = int(input("Quantity (must be in number/digit): "))
                amount = int(price) * int(itemQuantity)
                print("Amount =", amount)
                total += amount
                count += 1
                purchaseDict[itemNo] = [item, itemQuantity, price, amount]
            keepbuying = input("Type 'y' to keep buying and 'n' to stop: ")
            if keepbuying == "y".lower():
                purchase(total, count)
            buy = input("Do you still want to buy an item, y/n? ")
            if buy == "n".lower():
                print("Transaction successful!")
                print("\n")
            else:
                print("Something went wrong! Transaction terminated.")
                print("\n")
            receipt = input("Proceed to print a receipt, y/n? ")
            if receipt == "y".lower():
                print("                      ", "RECEIPT")
                print("------------------------------------------------------------------")
                print("  ITEM --- QUANTITY       PRICE(N)  AMOUNT(N)")
                for itemNo in purchaseDict:
                    print(purchaseDict[itemNo][0], "---", purchaseDict[itemNo][1], "       ", purchaseDict[itemNo][2], " ", purchaseDict[itemNo][3])
                if count < 5:
                    VAT = (20/100)*total
                    print("20% VAT:", VAT)
                    Total = total - VAT
                    print("Total:  N", Total)
                elif count > 10:
                    VAT = (30/100)*total
                    print("30% VAT:  N", VAT)
                    Total = total - VAT
                    print("Total:", Total)
                elif count > 10 and purchaseDict[itemNo][3] >= 100:
                    VAT = (30/100)*total
                    print("30% VAT:", VAT)
                    discount = 800
                    print("Discount:  N", discount)
                    Total = total - VAT
                    print("Total:", Total)
                else:
                    print("Total amount of item purchased =  N", total)
                 
            elif receipt == "n".lower():
                print("Done!")
                print("Total amount of item purchased =  N", total)
            else:
                print("Wrong input! Transaction terminated.")
                print("Total amount of item purchased =  N", total) 
        break
        
else:
    pass
try:
    purchase(0, 0)
except:
    pass
































