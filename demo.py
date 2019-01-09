
def demo2(a):
    while True:
        if len(a)>3:
            a.pop()
            print("minus",a)
        else:
            break


def demo1(a):
    print(a)
    demo2(a)
    print(a)
a = [1,2,5,6,8,2]
demo1(a)