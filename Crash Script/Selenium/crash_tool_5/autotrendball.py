import play
import tkinter as tk

def main():
    root = tk.Tk()
    ex = play.auto_run(root)
    root.mainloop()
    play.auto_run()

if __name__ == "__main__":
    main()