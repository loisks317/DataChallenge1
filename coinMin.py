def min_coins(change):
 	 #
   # user inputs amount to determine minimum number of 
   # coins to make change
   # return dictionary - minCoins - with number of coins affiliated with each coin (vague?) 
   # {'quarter': 2, 'dime':0, 'nickel':3, 'penny':0}
   #
   changeTotal=0
   minCoin={}
   coinList=['quarter', 'dime', 'nickel', 'penny']
   for ii in range(len(coinList)):
     minCoin[coinList[ii]]=0
   coinValue=[0.25, .10, .05, .01]
   
   for iCoin in range(len(coinList)):
    while True:
    	changeTotal += coinValue[iCoin]       
        if change >= changeTotal:
    	  minCoin[coinList[iCoin]]+=1
        else:
          changeTotal -= coinValue[iCoin]
          break
   
   numberofCoins=0
   for jj in coinList:
      numberofCoins+=minCoin[jj]
   
   return(minCoin, numberofCoins) 
