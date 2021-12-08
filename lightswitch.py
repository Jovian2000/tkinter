import tkinter as tk
window = tk.Tk()
window.config(bg="black")
button = tk.Button(text='Switch light off', bg="white", fg="black")
button.pack(pady = 50, padx = 100)

# schijf hier tussen je code
def buttonPress(event):
    if button.config('text')[-1] == 'Switch light on':
        button.config(text='Switch light off',bg="white",fg="black")
        window.config(bg="black")  
        print("light is off")    
    else:
        button.config(text='Switch light on',bg="white",fg="blue")
        window.config(bg="yellow")      
        print("light is on")
button.bind('<Button>', buttonPress)
# schijf hier tussen je code

window.mainloop()