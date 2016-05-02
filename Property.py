class Property:
    def __init__(self, id, star, cost, availability):
        self.id = id
        self.star = star
        self.cost = cost
        self.priceList = []
        self.availability = availability
        self.profit = 0
        self.totalRound = 0
        self.successRound = 0
        
    def set_priceList(self, coeffAList, coeffBList, maxSlot):
        #price = cost*a + b
        for i in range(maxSlot):
            self.priceList.append(self.cost*coeffAList[i] + coeffBList[i])
        self.priceList.sort()
        self.priceList.reverse()

    def get_priceList(self):
        return self.priceList

    def transcation_occur(self, price):
        self.profit += price - self.cost
        self.availability -= 1
        self.totalRound += 1
        self.successRound += 1

    def firstRound_denial(self):
        self.totalRound += 1

    def get_successRate(self):
        if self.totalRound != 0:
            return float(self.successRound)/float(self.totalRound)
        else:
            return 0
        
        
