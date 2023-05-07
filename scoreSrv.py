import numpy
import time

while True:
    time.sleep(1)
    # Bonds, Cash, TBills, BAccnts, Stocks, RlEstate, MFunds, Options, Futures, Collectibles 
    weights = {"Bonds": 2, 
               "Cash": 1, 
               "TreasuryBills": 1, 
               "BankAccounts": 1,
               "Stocks": 4,
               "RealEstate": 1,
               "MutualFunds": 3,
               "Options": 10,
               "Futures": 10,
               "Collectibles": 8}
    message = open("message.txt","r+")
    # Erase contents then write random number to file
    if message.read() == "run":
        # Read asset types from column 1
        assetType = []
        data = open("data.txt","r+")
        lines = data.readlines()
        for line in lines:
            assetType.append(line.split()[0])
        size = len(assetType)
        data.close()
        
        amounts = numpy.loadtxt("data.txt", usecols = 1, dtype = float)
        # Multiply assets by risk factor and sum; Also sum amounts
        riskSum = 0
        amSum = 0
        for i in range(size):          
            riskSum += amounts[i] * weights[assetType[i]]
            amSum += amounts[i]
            
        if amSum == 0: amSum = 1         
        # Calculate score and return message
        score = riskSum//amSum
        
        if score < 1: 
            x = 'You are broke!'
        elif score == 1: 
            x = 'Low'
        elif score > 1 and score < 5: 
            x = 'Moderate'
        else: 
            x = 'High'
        
        message.truncate(0)
        message.seek(0)
        message.write(str(x))
        
    message.close()
    