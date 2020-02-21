# Python program to generate all derangements of a list

def toString(List): 
    return ''.join(List) 


def derangements(input_array):
    def permute(a, l, r):
        if l == r:
            print(toString(a))
        else:
            for i in range(l, r):
                if not (a[i] == input_array[l]):
                    a[l], a[i] = a[i], a[l] 
                    permute(a, l+1, r) 
                    a[l], a[i] = a[i], a[l] # backtrack 
    permute(input_array[:], 0, len(input_array))

                
# Driver program to test the above function 
string = "ABC"
n = len(string) 
a = list(string) 
derangements(a)
