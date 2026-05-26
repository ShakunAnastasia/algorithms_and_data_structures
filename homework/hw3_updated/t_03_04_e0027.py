def get_max_rotation(num):
    if num == 0:
        return 0

    size = num.bit_length()
    ans = num
    x = num
    mask = (1 << size) - 1

    for _ in range(size - 1):
        x = ((x << 1) & mask) | (x >> (size - 1))
        if x > ans:
            ans = x

    return ans


if __name__ == "__main__":
    n = int(input())
    print(get_max_rotation(n))
