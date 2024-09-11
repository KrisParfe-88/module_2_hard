def shifr(n):
    result = ''
    for i in range(1, 21):
        for j in range(i + 1, 21):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result


for k in range(3, 21):
    print(k, '-', int(shifr(k)))
