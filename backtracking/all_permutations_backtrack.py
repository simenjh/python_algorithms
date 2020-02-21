# Python program to generate all permutations of a list

def toString(List): 
    return ''.join(List)

# This function takes three parameters: 
# 1. a: List
# 2. l: Starting index of the list
# 3. r: Length of the list
def permute(a, l, r): 
    if l==r: 
        print(toString(a))
    else: 
            for i in range(l, r):
                a[l], a[i] = a[i], a[l] 
                permute(a, l+1, r) 
                a[l], a[i] = a[i], a[l] # backtrack 

                
# Driver program to test the above function 
string = "ABC"
n = len(string) 
a = list(string) 
permute(a[:], 0, len(a))
