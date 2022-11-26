def FA_Matcher(A, g, f):
    q = 0
    for i in (1, n+1):
        q = g(q, A[i])
        if(q == f):
            print("찾았다")