class Consumer:
    def __init__(self, id, valueDict):
        self.id = id
        self.valueDict = valueDict
        self.bidDict = {}
        self.sortedBidList = []

    def valueList(self):
        return self.valueDict

    def set_bidList(self, bidCoeffA, bidCoeffB):
        for star in self.valueDict.keys():
            # bid = value*a - b
            self.bidDict[star] = self.valueDict[star]*bidCoeffA + bidCoeffB

    def get_bidList(self):
        return self.bidDict

    def set_sortedbidList(self):
        expectedUList = []
        for star in self.valueDict.keys():
            expectedU = self.valueDict[star] - self.bidDict[star]
            expectedUList.append((expectedU, star))
        self.sortedBidList = sorted(expectedUList)

        
            
            
        
        
        
    
                
        
        
        
