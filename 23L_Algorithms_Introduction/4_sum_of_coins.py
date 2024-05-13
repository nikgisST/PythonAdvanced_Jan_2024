def choose_coins(coins, target):
    coins.sort(reverse=True)
    idx = 0
    used_coins = {}  # coin: times_used

    while target > 0 and idx < len(coins):   # прикл, когато не можем да върнем ресто(докато върнем ресто) или ни свършат монетите
        each_coin = coins[idx]
        count_current_coins = target // each_coin  # 4,50 => 1 * 4
        target = target % each_coin  # 4,50 % 1 => 0.50

        if count_current_coins > 0:
            used_coins[each_coin] = count_current_coins

        idx += 1

    if target != 0:
        return "Error"
    else:
        result = f"Number of coins to take: {sum(used_coins.values())}\n"

        for coin, count in used_coins.items():
            result += f"{count} coin(s) with value {coin}\n"

        return result


coins_for_def = [int(x) for x in input().split(", ")]
target_for_def = int(input())
print(choose_coins(coins_for_def, target_for_def))