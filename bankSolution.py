def bankSolution(balances, requests):
    for swi in range(len(requests)):
        tempReq = requests[swi].split(" ")
        if tempReq[0] == 'transfer':
            try:
                fromBalance = int(tempReq[1])-1
                toBalance = int(tempReq[2])-1
                totalBalance = int(tempReq[3])
                
                balances[fromBalance] -= totalBalance
                balances[toBalance] += totalBalance
                print(f'balances[fromBalance]: {balances[fromBalance]} and balances[toBalance]: {balances[toBalance]}')
                if balances[fromBalance] < 0:
                    return -(swi+1)
            except:
                return -(swi+1)
        elif tempReq[0] == 'withdraw':
            print(f'In Withdraw')
            try:
                print(f'balances[tempReq[1]]: {balances[int(tempReq[1])]} and int(tempReq[2]): {int(tempReq[2])}')
                if balances[int(tempReq[1])-1] < int(tempReq[2]):
                    return -(swi+1)
                balances[int(tempReq[1])-1] -= int(tempReq[2])
            except:
                return -(swi+1)
        else: # deposit
            print(f'In deposit')
            try:
                #print(f'balances[int(tempReq[1])]: {balances[int(tempReq[1])]} and int(tempReq[2]: {int(tempReq[2])}')
                num = int(tempReq[1])-1
                balances[num] += int(tempReq[2])
            except:
                return -(swi+1)

    return balances

balances = [10, 100, 20, 50, 30]
requests = ["withdraw 2 10", "transfer 5 1 20", "deposit 5 20", "transfer 3 4 15"]

balances = [20, 1000, 500, 40, 90]
requests = ["deposit 3 400", "transfer 1 2 30", "withdraw 4 50"]

print(bankSolution(balances, requests))