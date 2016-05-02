from consumer import Consumer
from property import Property
from nyop import NYOP
from random import *

def run(numOfConsumer, conCoeffA, conCoeffB, numOfPro, proCoeffAList,
        proCoeffBList, maxSlot):
    consumerList = []
    for i in range(numOfConsumer):
        valueDict = {}
        valueDict[1] = randint(10,60)
        valueDict[2] = valueDict[1] + randint(10,60)
        valueDict[3] = valueDict[2] + randint(10,60)
        valueDict[4] = valueDict[3] + randint(10,60)
        valueDict[5] = valueDict[4] + randint(10,60)
        #print(valueDict)
        consumer = Consumer(i, valueDict)
        consumer.set_bidList(conCoeffA, conCoeffB)
        consumerList.append(consumer)
 
    propertyDict = {1:[], 2:[], 3:[], 4:[], 5:[]}
    numOfPro = 20
    for n in range(numOfPro):
        star = randint(1,5)
        if star == 1:
            cost = randint(10,40)
        elif star == 2:
            cost = randint(30,100)
        elif star == 3:
            cost = randint(50,160)
        elif star == 4:
            cost = randint(70, 220)
        elif star == 5:
            cost = randint(90,280)
        #print(cost)
        pro = Property(n, star, cost, randint(1,5))
        pro.set_priceList(proCoeffAList, proCoeffBList, maxSlot)
        propertyDict[star].append(pro)

    priceline = NYOP()
    priceline.compute(consumerList, propertyDict)
    #print("priceline's profit", priceline.profit)

    aveConU = sum(c.utility for c in consumerList)/numOfConsumer
    #print("average consumer utility", aveConU)

    sumProProfit = 0
    for k in propertyDict.keys():
        sumProProfit += sum(p.profit for p in propertyDict[k])
    aveProProfit = sumProProfit/numOfPro
    #print("average property profit", aveProProfit)

    return (priceline.profit, aveConU, aveProProfit)

def main():
    iterNum = 10
    print "iterate", iterNum, "times"
    numOfConsumer = 20
    numOfPro = 20
    print "number of consumer: ", numOfConsumer
    print "number of property: ", numOfPro

    #strategy of consumers
    #bid = value*a - b
    conCoeffA = 0.8
    conCoeffB = 0

    #strategy of properties
    #price = cost*a + b
    proCoeffAList = [1.1, 1.2, 1.3]
    proCoeffBList = [0, 0, 0]

    #maximum number of price the property can upload to priceline
    maxPriceSlot = 3
    
    pricelineProfit = 0
    sumConU = 0
    sumProU = 0
    for i in range(10):
        pp, ac, ap = run(numOfConsumer, conCoeffA, conCoeffB, numOfPro,
                         proCoeffAList, proCoeffBList, maxPriceSlot)
        pricelineProfit += pp
        sumConU += ac
        sumProU += ap

    print "average Priceline's profit", pricelineProfit/iterNum
    print "average consumer utility", sumConU/iterNum
    print "average property profit", sumProU/iterNum
           
main()
