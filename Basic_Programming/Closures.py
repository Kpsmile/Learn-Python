def startAt(start):
    def incrementBy(inc):
        return start + inc
    return incrementBy

f = startAt(10)
g = startAt(100)

print f(1), g(2)