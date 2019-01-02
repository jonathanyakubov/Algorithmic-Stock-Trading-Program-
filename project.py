			
def date_extraction():

	import csv

	apple_stock_data=open('AAPL.csv')

	apple_stock_data_f=csv.reader(apple_stock_data)

	Date_list=[]
	
	for row in apple_stock_data_f:
		Date,Open, High, Low, Close, Adj_close, Volume =row
		Date_list.append(Date)

	Date_list.pop(0)
	
	return Date_list
	
		
def opening_extraction():
	
	import csv
	apple_stock_data=open('AAPL.csv')
	apple_stock_data_f=csv.reader(apple_stock_data)	
	
	Open_list=[]
		
	for row in apple_stock_data_f:
		Date,Open, High, Low, Close, Adj_close, Volume =row	
		Open_list.append(Open)
	
	Open_list.pop(0)
	
	for i in range(len(Open_list)):
		Open_list[i]=float(Open_list[i])
	
	return Open_list
	

def high_extraction():
	
	import csv
	apple_stock_data=open('AAPL.csv')
	apple_stock_data_f=csv.reader(apple_stock_data)	
	
	High_list=[]
		
	for row in apple_stock_data_f:
		Date,Open, High, Low, Close, Adj_close, Volume =row	
		High_list.append(High)	
	
	High_list.pop(0)
	
	for i in range(len(High_list)):
		High_list[i]=float(High_list[i])
	

	return High_list
	
def low_extraction():
	
	import csv
	apple_stock_data=open('AAPL.csv')
	apple_stock_data_f=csv.reader(apple_stock_data)	
	
	Low_list=[]	
		
	for row in apple_stock_data_f:
		Date,Open, High, Low, Close, Adj_close, Volume =row	
		Low_list.append(Low)	
		
	Low_list.pop(0)
	
	for i in range(len(Low_list)):
		Low_list[i]=float(Low_list[i])	
		
	
	return Low_list

		
def close_extraction():
	import csv
	
	apple_stock_data=open('AAPL.csv')
	apple_stock_data_f=csv.reader(apple_stock_data)	
	
	Close_list=[]
	
	for row in apple_stock_data_f:
		Date,Open, High, Low, Close, Adj_close, Volume =row	
		Close_list.append(Close)
		
	Close_list.pop(0)
	
	for i in range(len(Close_list)):
		Close_list[i]=float(Close_list[i])	


	return Close_list


def close_adj_extraction():
	
	import csv
	apple_stock_data=open('AAPL.csv')
	apple_stock_data_f=csv.reader(apple_stock_data)	
	
	Close_adj_list=[]
	
	for row in apple_stock_data_f:
		Date,Open, High, Low, Close, Adj_close, Volume =row	
		Close_adj_list.append(Adj_close)	

	Close_adj_list.pop(0)
	
	for i in range(len(Close_adj_list)):
		Close_adj_list[i]=float(Close_adj_list[i])	
		
	return Close_adj_list

		
def volume_extraction():
	
	import csv
	apple_stock_data=open('AAPL.csv')
	apple_stock_data_f=csv.reader(apple_stock_data)	
	
	Volume_list=[]
	
	for row in apple_stock_data_f:
		Date,Open, High, Low, Close, Adj_close, Volume =row	
		Volume_list.append(Volume)
		
	Volume_list.pop(0)
	
	for i in range(len(Volume_list)):
		Volume_list[i]=int(Volume_list[i])		

	
	return Volume_list

def return_value(filename,col,day):		
	from sys import exit
	
	if filename == "MSFT.csv":
		print("You need to update the 'open functions' to extract from the correct CSV,",
			   "We are currently using AAPL.csv. For everywhere you see AAPL.csv in the code",
			   	"update to MSFT.csv and whereever there is an MSFT.csv, update to AAPL.csv")
		exit(0)
	
	if filename=="AAPL.csv":
		if "date" in col:
			date_list=date_extraction()
			col_date=date_list[day-1]
			return col_date
		elif "open" in col:
			open_list=opening_extraction()
			col_open=open_list[day-1]
			return col_open
		elif "high" in col:
			high_list=high_extraction()
			col_high=high_list[day-1]
			return col_high
		elif "low" in col:
			low_list=low_extraction()
			col_low=low_list[day-1]
			return col_low
		elif "close" in col and not "adj" in col:
			close_list=close_extraction()
			col_close=close_list[day-1]
			return col_close
		elif "adj" in col and "close" in col:
			close_adj_list=close_adj_extraction()
			col_close_adj=close_adj_list[day-1]
			return col_close_adj 
		elif "volume" in col:
			volume_list=volume_extraction()
			col_volume=volume_list[day-1]
			return col_volume
		else:
			print("What you entered is gibberish. Please try agin.")
			exit(0)		 

def test_data(filename,col, day):

	"""A test function to query the data you loaded into your program.
	
	Args:
		filename: A string for the filename containing the stock data, 
				  in CSV format.
		
		col: A string of either "data", "open", "high", "low", "close", 
			"volume", or "adj_close" for the column of stock market data to 
			look into. 
		
			The string arguments MUST be LOWERCASE!
		
		day: An integer reflecting the absolute number of the day in the data to look up, 
			 e.g. day 1, 15, or 1200 is row 1, 15, or 1200 in the file. 
		
		Returns:
			A value selected for the stock on some particular day, in some column col. The 
			returned value *must* be of the appropriate type, such as float, int or str. 
			"""

	
	price=return_value(filename,col,day)
	
	return price

def transact(funds, stocks, qty, price, buy=False, sell=False):

	from sys import exit 

	"""A bookkeeping function to help make stock transactions. 
	
	Args:
		funds: An account balance, a float,; it is a value of how much money you have, 
			   currently.
		
		stocks: An int, representing the number of stock you currently own. 
		
		qty: An int, representing how many stock you wish to buy or sell.
		
		price: A float reflecting a price of a single stock
		
		buy: This option parameter, if set to true, will initiate the buy. 
		
		sell: This option parameter, if set to true, will inititate a sell. 
		
	Returns:
		Two values *must* be returned. The first (a float) is the new 
		account balance (funds) as the transaction is completed. The second
		is the number of stock now owned (an int) after the transaction is complete.
		
		Error condition #1: If the 'buy' and 'sell' keyword parameters are both set to true,
		or both false, you *must* print an error message, and then return 
		the 'funds' and 'stocks' parameter unaltered. This is an ambiguous 
		transaction request!
		
		Error condition #2: If you 'buy' and 'sell' without enough funds or 
		stocks to sell, repectively, you *must* print an error message, and then
		return the 'funds' and 'stock' parameters unaltered. This is an 
		ambiguous transaction request!
		"""
		
	if buy == False and sell == False:
		print("This is an ambiguous transaction request!")
		return funds, stocks
	elif buy==True and sell==True:
		print("This is an ambiguous transaction request!")
		return funds,stocks 
	elif buy==True and sell==False:
		cost=price*qty
		if cost > funds:
			print("Insufficient Funds: Purchase of",qty,"at $",price, "requires",
				  "a total of $",cost,"but $",funds, "available")
			return funds, stocks 
		else:
			account_balance=float(funds-(cost))
			stocks+= qty
			return account_balance,stocks
	elif buy==False and sell==True:
		sell_amount=qty*price 
		if qty>stocks:
			print("Insufficient stock: ",stocks,"stocks owned, but selling", qty)
			
			return funds, stocks
		else:
			account_balance=float(funds+sell_amount)
			stocks-=qty
			return account_balance, stocks
	else:
		print("Please try again.")
		exit(0)
				
cash_balance=1000
stocks_owned=25
price=return_value("AAPL.csv", "close", 42)
			
cash_balance, stocks_owned=transact(cash_balance, stocks_owned, 3, price, sell=True, )
print(cash_balance, stocks_owned)	
	

		
def alg_moving_average(filename):

    """This function implements the moving average stock trading algorithm.

    Using the CSV stock data that should be loaded into your program, use
    that data to make decisions using the moving average algorithm.

    Any bookkeeping setup from Milestone I should be called/used here.

    You must buy stock if the current day price is 20% lower than the moving average.
    You must sell stock if the current day price is 20% higher than the moving average.

    Args:
        A filename, as a string.

    Returns:
        Two values, stocks and balance OF THE APPROPRIATE DATA TYPE.

    Prints:
        Nothing.
    """
    col="close"
    day=1
    price=close_extraction()
		
    
    qty=10 #the amt of stocks that will be sold or bought 
    funds=1000 #initialize cash balance 
    day_stock=20 #really the 21st day [1,2,3,4,5]
    x=0
    stocks_owned=400  #initialize stocks owned
    while day_stock<len(price):
    	day_price=price[day_stock]
#     	price=return_value(filename,col,day_stock+1)
    	average=(sum(price[x:day_stock]))/20
    	buy_option=(1-(day_price/average))
    	sell_option=abs((1-(average/day_price)))
    	if day_stock+1==len(price):
    		funds, stocks_owned=transact(funds, stocks_owned, stocks_owned, day_price, buy=False, sell=True)
    		break	
    	elif buy_option<.05:
    		funds, stocks_owned=transact(funds, stocks_owned, qty, day_price, True, sell=False)
    		print(funds,day_price,stocks_owned)
    	elif buy_option >.05:
    		funds, stocks_owned=transact(funds, stocks_owned, qty, day_price, buy=False, sell=True)
    		print(funds,day_price,stocks_owned)
    	x+=1
    	day_stock+=1	
    		
    # Last thing to do, return two values: one for the number of stocks you end up
#     owning after the simulation, and the amount of money you have after the simulation.
#     Remember, all your stocks should be sold at the end!
    print("The results are...in the following order: stocks_owned, funds")
    print(stocks_owned,funds)
    return stocks_owned, funds


def main():
    # My testing will use AAPL.csv or MSFT.csv
    filename = input("Enter a filename for stock data (CSV format): ")

    # Call your moving average algorithm, with the filename to open.
    alg1_stocks, alg1_balance = alg_moving_average(filename)

    # Print results of the moving average algorithm, returned above:
	
if __name__=='__main__':
	main()
	

		
		
		
		
		
	