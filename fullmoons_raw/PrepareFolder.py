from fullmoons1900to2050 import fullmoons

buckets=100
bucketSize=int(len(fullmoons)/buckets)+1
for startIndex in range(0, len(fullmoons), bucketSize):
    endIndex=min(startIndex+bucketSize,len(fullmoons)-1)
    fileName=f"from{str(fullmoons[startIndex])}to{str(fullmoons[endIndex])}.py"
    with open("..//fullmoons//"+fileName,"w") as f:
        f.write(f"fullmoons={str(fullmoons[startIndex:endIndex+1])}")
    

