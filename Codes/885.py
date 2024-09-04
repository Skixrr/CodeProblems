Ans = 0

def f(d): #returns the sorted value of d
    temp = str(d)
    def sort(array): #Sort the array by using quicksort
        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0]
            for x in array:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    greater.append(x)
            return sort(less)+equal+sort(greater)
        else:
            return array
    temp = sort(temp)
    val = int(''.join(map(str, temp)))
    return val

def s(n): #returns the sum of all f(d) where len(d) <= n
    val = 0
    for i in range(1,10**n):
        val = val + (f(i))
    return val

print(s(18))