# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
# "101" => rotate by 180o => "101"
# "6, 1, 0, 9, 8"
# "606" => "909" "686" 
# "101", "609" => "609", "181", "906" => "906"


def computeAllPossiblities(n):
    ## output: list of str
    
    count = 0
    ans = []
    candidate = []
    
    def recursive(path, n):
        if len(path) == n:
            candidate.append(path)
            return     

        for i in ['0', '1', '6', '8', '9']:
            if i in ['0', '1', '8']:
                recursive(i + path + i, n)
            elif i == '6':
                recursive(i + path + '9', n)
            else:
                recursive(i + path + '6', n)
    
    if n%2 == 0:
        recursive("", n)
        for i in candidate:
            if i and i[0] != '0':
                ans.append(i)
    else:
        recursive("", n-1)
        for i in candidate:
            if i and i[0] != '0':
                for j in ['0', '1', '8']:
                    ans.append( i[:(n-1)//2] + j + i[(n-1)//2:] )
                    
    return ans

def computeAllPossibilitiesSmallerOrEqualTo(n):
    ans = []
    
    for i in range(1, n+1):
        ans.extend(computeAllPossiblities(i))
        
    return ans
    
    
    
    
print(computeAllPossibilitiesSmallerOrEqualTo(3))


        