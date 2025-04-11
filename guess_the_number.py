import tkinter as tk
from tkinter import messagebox
import random
import time

class GuessNumberGame:
    def __init__(self, master):
        self.master = master
        master.title("猜数字游戏 🎮")
        master.geometry("400x300")

        self.number_to_guess = random.randint(1, 100)
        self.guess_count = 0
        self.start_time = time.time()

        self.label = tk.Label(master, text="我选了 1 到 100 之间的一个数字，猜猜看！", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 14))
        self.entry.pack()

        self.result_label = tk.Label(master, text="", font=("Arial", 12), fg="blue")
        self.result_label.pack(pady=5)

        self.hint_label = tk.Label(master, text="", font=("Arial", 12), fg="green")
        self.hint_label.pack()

        self.submit_button = tk.Button(master, text="提交", command=self.check_guess, font=("Arial", 12))
        self.submit_button.pack(pady=10)

        self.reset_button = tk.Button(master, text="再来一次", command=self.reset_game, font=("Arial", 12))
        self.reset_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="请输入一个有效的整数！", fg="red")
            return

        self.guess_count += 1

        if guess < self.number_to_guess:
            self.result_label.config(text="太小了！", fg="orange")
            self.give_hint(guess)
        elif guess > self.number_to_guess:
            self.result_label.config(text="太大了！", fg="orange")
            self.give_hint(guess)
        else:
            end_time = time.time()
            time_used = int(end_time - self.start_time)
            messagebox.showinfo("恭喜！", f"你猜对了！数字是 {self.number_to_guess} 🎉\n"
                                          f"你共猜了 {self.guess_count} 次\n"
                                          f"用时 {time_used} 秒")
            self.reset_game()

    def give_hint(self, guess):
        if abs(guess - self.number_to_guess) <= 10:
            self.hint_label.config(text="🔥 很接近了！", fg="green")
        elif guess < self.number_to_guess:
            self.hint_label.config(text="提示：数字更大哦 📈", fg="gray")
        else:
            self.hint_label.config(text="提示：数字更小哦 📉", fg="gray")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.guess_count = 0
        self.start_time = time.time()
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.hint_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessNumberGame(root)
    root.mainloop()
