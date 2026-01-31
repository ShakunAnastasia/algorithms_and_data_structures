def a(n, k):
    k += 1              # 4
    i = n               # 2
    while i > 0:        # 3 * (n + 1)
        i -= 1          # 4 * n

# sum = 7n + 9

def b(n, k):
    i = n               # 2
    while i > 1:        # 3 * (log2(n) + 1)
        k += 1          # 4 * log2(n)
        i //= 2         # 4 * log2(n)

# sum = 11*log2(n) + 52

def c(n, k):
    i = 0               # 2
    while i < n:        # 3 * (n/2 + 1)
        j = 0           # 2 * (n/2)
        while j < n:    # 3 * (n/2) * (n/2 + 1)
            k += 1      # 4 * (n^2 / 4)
            j += 2      # 4 * (n^2 / 4)
        i += 2          # 4 * (n/2)

# sum = 2.75n^2 + 6n + 5

def d(n, k):
    i = 0               # 2
    while i < n:        # 3 * (n + 1)
        j = 0           # 2 * n
        while j < i*i:  # 5 * (n^3/3 - n^2/2 + n/6 + n)
            k += 1      # 4 * (n^3/3 - n^2/2 + n/6)
            j += 1      # 4 * (n^3/3 - n^2/2 + n/6)
        i += 1          # 4 * n

# sum = 4.33*n^3 - 6.5*n^2 + 16.17*n + 5

def e(n, k):
    i = 1               # 2
    while i < n:        # 3 * (log2(n) + 1)
        j = 1           # 2 * log2(n)
        while j < n:    # 3 * log2(n) * (log2(n) + 1)
            k += 1      # 4 * (log2(n)^2)
            j *= 2      # 4 * (log2(n)^2)
        i *= 2          # 4 * log2(n)

# sum = 11*(log2(n)^2) + 12*log2(n) + 5

def f(n, k):
    i = 1               # 2
    while i < n:        # 3 * (log2(n) + 1)
        j = i           # 2 * log2(n)
        while j < n:    # 3 * (log2(n)*(log2(n)+1)/2 + log2(n))
            k += 1      # 4 * (log2(n)*(log2(n)+1)/2)
            j *= 2      # 4 * (log2(n)*(log2(n)+1)/2)
        i *= 2          # 4 * log2(n)

# sum = 5.5*(log2(n)^2) + 17.5*log2(n) + 5
