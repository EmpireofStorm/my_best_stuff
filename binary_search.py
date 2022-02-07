from math import floor
a=input("Введите упорядоченный список чисел: ").split()
def binary_search(a, x, y, z):
    if x<=y:
        Mid=int(floor((x+y)/2))
        if int(a[Mid])==z:
            return Mid
        if int(a[Mid])>z:
            return binary_search(a, 0, Mid-1, z)
        if int(a[Mid])<z:
            return binary_search(a, Mid+1, y, z)
    return -1

z=int(input())
abc=binary_search(a, 0, int(len(a)-1), z)
print(abc)