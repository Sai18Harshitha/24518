fruits=["mango","apple","mango","grapes","grapes","mango"]
print(f"{fruits}")
def getDup(data):
    Duplicates=[]
    print("\nmy duplicate items")

    for i in data:
        if data.count(i)>1:
            Duplicates.append(i)
    print(set(Duplicates))
def getUQ(data):
    UQ=[]
    print("\n my unique items")
    for i in data:
        if data.count(i)==1:
            UQ.append(i)
    print(UQ)
getDup(fruits)
getUQ(fruits)
def getSumUQ(data):
    USum=0
    print(f"\n sumof uniques- ")
    for i in data:
        if data.count(i)==1:
            USum+=1