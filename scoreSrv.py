import numpy
import time

while True:
    time.sleep(1)
    # Bonds, Cash, TBills, BAccnts, Stocks, RlEstate, MFunds, Options, Futures, Collectibles 
    weights = [2, 1, 1, 1, 4, 1, 3, 10, 10, 8]
    message = open("message.txt","r+")
    # Erase contents then write random number to file
    if message.read() == "run":
        assets = numpy.loadtxt("data.txt", usecols = 0, dtype = float)
        amounts = numpy.loadtxt("data.txt", usecols = 1, dtype = float)
        # Multiply assets by risk factor and sum; Also sum amounts
        asSum = 0
        amSum = 0
        for i in range(10):
            assets[i] *= weights[i]
            asSum += assets[i]
            amSum += amounts[i]
            
        if amSum == 0: amSum = 1         
        # Calculate score and return message
        score = asSum//amSum
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
    