# given 50p, 20p, 10p, 5p, 2p, 1p find the number of coins to make change


def num_coins(to_change):
    coins = [50, 20, 10, 5, 2, 1]
    num_of_coins = 0
    for coin in coins:
        num_of_coins += to_change // coin
        to_change = to_change % coin
        if to_change == 0:
            break
    return num_of_coins


print(num_coins(83) == 5)
print(num_coins(48) == 5)
