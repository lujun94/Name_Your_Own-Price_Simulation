class Consumer:
    def __init__(self, id, valueDict):
        self.id = id
        self.valueDict = valueDict
        self.bidDict = {}
        self.sortedBidList = []
        self.utility = 0

    def valueList(self):
        return self.valueDict

    def set_bidList(self, bidCoeffA, bidCoeffB):
        for star in self.valueDict.keys():
            # bid = value*a - b
            self.bidDict[star] = self.valueDict[star]*bidCoeffA + bidCoeffB
        self.set_sortedBidList()

    def get_bidList(self):
        return self.bidDict

    def set_sortedBidList(self):
        expectedUList = []
        for star in self.valueDict.keys():
            expectedU = self.valueDict[star] - self.bidDict[star]
            expectedUList.append((expectedU, star))
        #sort the list in the order to expected utility
        self.sortedBidList = sorted(expectedUList)

    def get_sortedBidList(self):
        return self.sortedBidList

    def transcation_occur(self, star, price):
        self.utility += self.valueDict[star] - price

    

        
            
            
        
        
        
    
                
        
        
        
