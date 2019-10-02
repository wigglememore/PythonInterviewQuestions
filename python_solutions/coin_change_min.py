# given 50p, 20p, 10p, 5p, 2p, 1p find the min number of coins to make change


def greedy_coins(to_change, coins):
    num_of_coins = 0
    for coin in coins:
        num_of_coins += to_change // coin
        to_change = to_change % coin
        if to_change == 0:
            break
    return num_of_coins


def min_coins(to_change):
    coins = [25, 10, 1]
    current_min = 100
    for c in coins:
        current_min = min(current_min, greedy_coins(to_change, coins))
        coins.remove(c)
    return current_min


print(min_coins(1000) == 40)
