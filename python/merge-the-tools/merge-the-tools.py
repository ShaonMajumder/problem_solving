

def merge_the_tools(string, k):
    # your code goes here
    chunks, chunk_size = len(string), k
    subsquent_strings = [ string[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
    
    for s in subsquent_strings:
        temp = ""
        for c in s:
            print
            if c not in temp:
              temp = temp + c
        print(temp)


    

if __name__ == '__main__':
    string = input("String ?")
    k = int(input("k ?"))
    merge_the_tools(string, k)
