X = "12321"
Y = "42531"
# X = sorted(X,reverse = True)
# Y = sorted(Y,reverse = True)
list_ = [0 for i in range(10)]

# for i in range(10):
#     dict_1[i] = 0

for j in X:
    j = int(j)
    list_[j] += 1

# for k in range(len(Y)):
#     dict_1[Y[k]] += 1


print(list_)
