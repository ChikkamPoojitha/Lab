class movierelease:
    def __init__(self):
        self.movies={"salar":"12-3-2023","kgf":"13-4-2023","dollar":"23-5-2023"}
    def getrelease(self,moviename):
        if moviename in self.movies:
            return self.movies[moviename]
        else:
            return f"{moviename} not found"
n1=movierelease()
mname="kgf"
date=n1.getrelease(mname)
print(f"the relese date of {mname} is {date}")
