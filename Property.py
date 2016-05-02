class Property:
    def __init__(self, id, star, cost, availability):
        self.id = id
        self.star = star
        self.cost = cost
        self.priceList = []
        self.availability = availability
        self.profit = 0
        
    def set_priceList(self, coeffAList, coeffBList, maxSlot):
        #price = cost*a + b
        for i in range(maxSlot):
            self.priceList.append(self.cost*coeffAList[i] + coeffBList[i])

    def get_priceList(self):
        return self.priceList

    def transcation_occur(self, price):
        self.profit += price - cost
        self.availability -= 1
