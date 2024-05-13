def recursive_drawing(n):   # n=1
    if n == 0:
        return

    print("*" * n)
    recursive_drawing(n - 1)   # когато n==0, влиза в if-а и донася тук return n спря последно, когато беше 1
    print("#" * n)


n = int(input())    #2
recursive_drawing(n)
