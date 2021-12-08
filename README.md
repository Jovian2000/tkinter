# Tkinter
## F1.7.01.O1
Repo aangemaakt
## F1.7.01.O2
Lichtschakelaar gemaakt
```python
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
```
