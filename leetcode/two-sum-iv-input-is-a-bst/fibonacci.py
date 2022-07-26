def fibonnaci(m):
    if m <= 2:
        return 1
    return fibonnaci(m-1) + fibonnaci(m-2)

print( fibonnaci(5) )