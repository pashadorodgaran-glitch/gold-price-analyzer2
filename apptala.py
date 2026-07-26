prices = []
for i in range(3):
    x = int(input("قیمت را وارد کنید"))
    prices.append(x)


bishtarin = prices[0]
jam = 0
kamtarin = prices[0]


for price in prices :
    if kamtarin > price :
        kamtarin = price
    
    if bishtarin < price:
        bishtarin = price

    jam += price 

miangin = jam / len(prices)
   

print(prices)
print(kamtarin,"کمترین")
print(bishtarin,"بیشترین")
print(miangin,"میانگین")