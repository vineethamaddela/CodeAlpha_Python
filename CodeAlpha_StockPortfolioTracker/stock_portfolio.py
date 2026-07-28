# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total_investment = 0

n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment
    else:
        print("Stock not found!")

print("\nTotal Investment Value: ₹", total_investment)

# Optional: Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value: ₹" + str(total_investment))

print("Result saved in portfolio.txt")
