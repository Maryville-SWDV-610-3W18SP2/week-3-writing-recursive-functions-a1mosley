def maximum(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0],maximum(L[1:]))
def minimum(L):
    if len(L) == 1:
        return L[0]
    else:
        return min(L[0],minimum(L[1:]))
    
def backWards (n):
        if not n: return []
        return [n.pop()] + backWards(n)