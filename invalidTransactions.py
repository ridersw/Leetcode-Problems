#conditions:
	# amount > $1000
	#transactions occurs within 60 mins with same name and different cities

def invalidTransactions(transactions):

	tr = transactions[0].split(",")
	name 	= []
	name.append(tr[0])
	time	= []
	time.append(tr[1])
	amount 	= []
	amount.append(tr[2])
	city 	= []
	city.append(tr[3])
	
	invalidTransaction = []
	
	transactions.sort()
	
	for swi in range(1, len(transactions)):
		tr = transactions[swi].split(",")
		name.append(tr[0])
		time.append(tr[1])
		amount.append(tr[2])
		city.append(tr[3])
		
		if int(tr[2]) > 1000:
			invalidTransaction.append(transactions[swi])
			return invalidTransaction
		
		if name[swi] == name[swi-1] and city[swi] != city[swi-1] and int(amount[swi]) - int(amount[swi-1]) < 60:
			invalidTransaction.append(transactions[swi])
			invalidTransaction.append(transactions[swi-1])
			return invalidTransaction 
	
if __name__ == "__main__":
	#print(invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,100,beijing"]))
	#print(invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]))
	#print(invalidTransactions(transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]))
	print(invalidTransactions(transactions = ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,frankfurt"]))
	
	
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
You are given an array of strings transaction where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

 

#Example 1:

#Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
#Output: ["alice,20,800,mtv","alice,50,100,beijing"]
#Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
#Example 2:

#Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
#Output: ["alice,50,1200,mtv"]
#Example 3:

#Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
#Output: ["bob,50,1200,mtv"]
 
#Constraints:

#transactions.length <= 1000
#Each transactions[i] takes the form "{name},{time},{amount},{city}"
#Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
#Each {time} consist of digits, and represent an integer between 0 and 1000.
#Each {amount} consist of digits, and represent an integer between 0 and 2000.
