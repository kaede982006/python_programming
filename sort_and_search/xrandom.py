import random

class XRandom:
    def randint(self, num, n, m):
        data = []
        if n>m:
            for i in range(num):
                data.append(0)
        else:
            for i in range(num):
                data.append(random.randint(n, m))
        return data
    def random(self, num, n, m):
        data = []
        if n>m:
            for i in range(num):
                data.append(0)
        else:
            for i in range(num):
                data.append(n+(m-n)*random.random())
        return data
