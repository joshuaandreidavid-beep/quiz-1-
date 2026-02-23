import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

cp = "X"
bts = []

def c_winner():
    win = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    
    for pos in win:
        if (buttons[pos[0]]["text"] ==
            buttons[pos[1]]["text"] ==
            buttons[pos[2]]["text"] != ""):
            return True
    return False

def c_draw():
    return all(bt["text"] != "" for bt in bts)

def bt_click(index):
    global cp
    
    if bts[index]["text"] == "":
        bts[index]["text"] = cp
        
        if c_winner():
            messagebox.showinfo("Game Over", f"Player {cp} wins!")
            reset()
            return
        
        if c_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset()
            return
        
        cp = "O" if cp == "X" else "X"

def reset():
    global cp
    cp = "X"
    for bt in bts:
        bt["text"] = ""

for i in range(9):
    bt = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                       command=lambda i=i: bt_click(i))
    bt.grid(row=i//3, column=i%3)
    bts.append(bt)

root.mainloop()
