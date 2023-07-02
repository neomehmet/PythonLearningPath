
class Three():

    def __init__(self, liste):
        self.liste = liste
        print(self.liste)

    def get_res(self):
        res = []
        temp = []
        from itertools import combinations
        combi = combinations(self.liste,3)
        res = [i for i in combi if sum(i) == 0 ]
        return res
    
def main():
    a = [-18, -11, -7, -3, 3, 4, 8 ,10]
    test = Three( a)
    print(test.get_res())


main()