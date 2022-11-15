import os

class fullmoons:
    def __init__(self):
        dir_path = __file__[:__file__.rfind("/")]
        files=os.listdir(dir_path)
        files=list(filter(lambda f: f.startswith('from'), files))
        self.firstfullmoon=None
        self.lastfullmoon=None
        self.ranges=[]
        allVals=[]
        for aFile in files:
            vals=aFile.replace("from","").replace(".py","").split("to")
            vals=[int(vals[0]),int(vals[1])]
            allVals+=vals
            if self.firstfullmoon==None:
                self.firstfullmoon=vals[0]
                self.lastfullmoon=vals[1]
            else:
                self.firstfullmoon=min(self.firstfullmoon,vals[0])
                self.lastfullmoon=max(self.lastfullmoon,vals[1])
        allVals.sort()
        for i in range(0, len(allVals), 2):
            self.ranges.append(allVals[i:i+2])
    def getCurrentMoonRange(self,time):
        nextFullMoon=prevFullMoon=None
        if time<self.firstfullmoon:#pre-1900
            nextFullMoon=self.firstfullmoon
        elif time>self.lastfullmoon:#post-2050
            prevFullMoon=self.lastfullmoon
        else: #1900-2050
            for index, moonRange in enumerate(self.ranges):
                if time < moonRange[1]:
                    if time < moonRange[0]:
                        nextFullMoon=moonRange[0]
                        prevFullMoon=self.ranges[index-1][1]
                        break
                    else:
                        targetFile=f"from{str(moonRange[0])}to{str(moonRange[1])}"
                        fullmoons = __import__(f"fullmoons.{targetFile}", None, None, [None])
                        for fullmoonindex, fullmoon in enumerate(fullmoons.fullmoons):
                            if time < fullmoon:
                                prevFullMoon=fullmoons.fullmoons[fullmoonindex-1]
                                nextFullMoon=fullmoon
                                break
                        break
        return([prevFullMoon,nextFullMoon])
        

if __name__=='__main__':
    f=fullmoons()
    print(f.getCurrentMoonRange(1668456182))


