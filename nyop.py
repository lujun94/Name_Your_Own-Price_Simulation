import random

class NYOP:
    def __init__(self):
        self.profit = 0
    
    #WeightedPick() is cited from
    #http://stackoverflow.com/questions/2570690/python-algorithm-to-randomly-select-a-key-based-on-proportionality-weight
    def weightedPick(d):
    r = random.uniform(0, sum(d.itervalues()))
    s = 0.0
    for k, w in d.iteritems():
        s += w
        if r < s: return k
    return k

    def compute(self, consumerList, propertyDict):
        for consumer in consumerList:
            bidList = consumer.get_sortedBidList()
            findADeal = False
            for utility, star in bidList:
                visited = []
                #get all the qualified properties
                qualifiedProperty = propertyList[star]
                
                while True:
                    firstRoundPro = random.choice(qualifiedProperty)
                    if firstRoundPro.availability > 0:
                        break
                    else:
                        visited.append(firstRoundPro)
                    
                firstRoundProPrice = firstRoundPro.get_priceList()
                #if there is a property price below consumer bid price
                #pick the highest price below consumer bid price
                if min(firstRoundProPrice) < consumer.bidDict[star]:
                    findPrice = False
                    while True:
                        for price in firstRoundProPrice:
                            if price < consumer.bidDict[star]
                                findPrice = price
                                break
                    #transation occurs
                    firstRoundPro.transaction_occur(findPrice)
                    consumer.transcation_occur()
                    self.profit += consumer.bidDict[star] - findPrice
                    findADeal = True
                    
                    #break the for utility, star in bidList when find a deal
                    break
                        
                                
                else:
                    firstRoundPro.firstRound_denial()
                    #remove the first round property from the list
                    visited.append(firstRoundPro)
                    #keep doing second Round if matches not found
                    while len(visited) < len(qualifiedProperty):
                    #Randomly select one based on their past success rate
                        dictWithWeight = {}
                        for p in qualifiedProperty:
                            if p not in visited:
                                if p.availability > 0:
                                    dictWithWeight[p] = p.get_successRate()*100
                                else:
                                    visited.append(p)
                        pickedPro = weightedPick(dictWithWeight)
                        pickedProPrice = pickedPro.get_priceList()
                        
                        #if there is a property price below consumer bid price
                        #pick the highest price below consumer bid price
                        if min(pickedProPrice) < consumer.bidDict[star]:
                           findPrice = False
                           while True:
                                for price in pickedProPrice:
                                    if price < consumer.bidDict[star]
                                        findPrice = price
                                    break
                           #transation occurs
                           prickedPro.transaction_occur(findPrice)
                           consumer.transcation_occur()
                           self.profit += consumer.bidDict[star] - findPrice
                           findADeal = True
                           break
                        else:
                           visited.append(pickedPro)
                           
                    #break the for utility, star in bidList when find a deal
                    if findADeal = True:
                        break
            
                    
                    
                
