
class sample(object):

    def __call__(self):
        List1 = [89, 67, 54, 32, 21, 9, 98]
        List2 = [54, 67, 76, 89, 66, 90]
        List3 = []
        for a in List1:
            for b in List2:
                if a == b:
                    List3.append(b)
        print(List3)


obj = sample()

obj()


