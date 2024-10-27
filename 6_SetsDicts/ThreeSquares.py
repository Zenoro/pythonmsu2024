if __name__ == '__main__':
    nums = set(eval(input()))
    M = max(nums)
    sqr_sums = {i*i + j*j + k*k for i in range(1, int(M**0.5) + 1)
                for j in range(i, int((M - i*i) ** 0.5) + 1)
                for k in range(j, int((M - i*i - j*j) ** 0.5) + 1)}
    print(len(nums & sqr_sums))
