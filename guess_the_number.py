import random

def guess_the_number():
    print("欢迎来到猜数字游戏！")
    print("我已经选好了一个 1 到 100 之间的数字，你来猜猜看！")

    # 随机生成一个 1 到 100 之间的数字
    number_to_guess = random.randint(1, 100)
    guesses_taken = 0

    while True:
        # 获取玩家输入
        try:
            player_guess = int(input("请输入你的猜测："))
        except ValueError:
            print("请输入一个有效的数字！")
            continue
        
        guesses_taken += 1

        if player_guess < number_to_guess:
            print("太小了！再试试吧。")
        elif player_guess > number_to_guess:
            print("太大了！再试试吧。")
        else:
            print(f"恭喜你！你猜对了，数字是 {number_to_guess}。")
            print(f"你猜了 {guesses_taken} 次。")
            break

if __name__ == "__main__":
    guess_the_number()
