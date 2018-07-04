def number_of_numbers(N, S, d=None):
    if S < 0:
        return 0
    if N == 0:
        return 0
    if N == 1:
        if 0<=S<=9:
            return 1
        else:
            return 0
    if d is None:
        d = {}
    if (N,S) in d:
        return d[(N,S)]
    r = 0   
    for i in range(10):
        r += number_of_numbers(N-1, S-i, d)
    d[(N,S)] = r
    return r

def lucky_numbers(N,S):
    if S % 2 == 1:
        return 0
    else:
        return number_of_numbers(N,S//2)**2

if __name__ == "__main__":
    inp = input()
    n1,s1 = inp.split(" ")
    n = int(n1)
    s = int(s1)
    print(lucky_numbers(n, s))