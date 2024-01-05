p = "aaaabb"

def make_palindrome_list(p):
    def backtracking(start, path):
        if start == len(p):
            result.append(path[:])
            return
        
        for end in range(start + 1, len(p) + 1):
            a = p[start:end]
            if check(a):
                path.append(a)
                backtracking(end, path)
                path.pop()
        

    def check(p):
        return p == p[::-1]
    
    result = []
    backtracking(0,[])
    return result
    

print(make_palindrome_list(p))