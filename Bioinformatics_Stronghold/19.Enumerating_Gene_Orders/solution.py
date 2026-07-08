n = int(input())

basket = []
for i in range(1, n+1):
    basket.append(i)

def permutations(basekt):
    for i in range(len(basket)):
        print(' '.join(str(i) for i in basket))
        print(i)
    basket = basket[0] + basket[2] + basket[1]
    print(basket)