from tkinter import *

top = Tk()
top.geometry("600x350")
top.title("Equation Solver")

frame1 = Frame(top, highlightbackground="blue", highlightthickness=2)
frame1.pack(padx=50, pady=50)

#Make frame same size as window
frame1.pack_propagate(0)


# this will create a label widget
l1 = Label(frame1, text = "\u0394 = ")
l2 = Label(frame1, text = "L = ")
l3 = Label(frame1, text = "T = ")

l1.grid(row = 0, column = 0, sticky = W, padx=50, pady = 10)
l2.grid(row = 1, column = 0, sticky = W, padx=50, pady = 10)
l3.grid(row = 2, column = 0, sticky = W, padx=50, pady = 10)

e1 = Entry(frame1)
e2 = Entry(frame1)
e3 = Entry(frame1)

#make e1,e2,e3 responsive to the grid and move onto next row after entering a number
e1.bind("<Return>", lambda x: e2.focus_set())
e2.bind("<Return>", lambda x: e3.focus_set())
e3.bind("<Return>", lambda x: b1.focus_set())


# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)
e3.grid(row = 2, column = 1, pady = 2)


def solve(): 
    #show error Message is any value is missing
    if e1.get() == "" or e2.get() == "" or e3.get() == "": 
        l5 = Label(frame1, text = "Error: Missing Value")
        l5.grid(row = 4, column = 1, sticky = W, padx=50, pady = 10)
        #make label disappear after 2 seconds
        top.after(5000, l5.destroy)       
        return None
    delta = float(e1.get())
    L = float(e2.get())
    T = float(e3.get()) 

    #show error Message is any value is missing or T=0
    if T == 0:
        l5 = Label(frame1, text = "Error: T cannot be 0")
        l5.grid(row = 4, column = 1, sticky = W, padx=50, pady = 10)
        #make label disappear after 2 seconds
        top.after(5000, l5.destroy)
        return None
    

    solution = 1.7*L*T + (delta/T)
    return solution

def show():
    sol = solve() 
    l4 = Label(frame1, text = sol)
    l4.grid(row = 3, column = 1, sticky = W, pady = 2)
    top.after(5000, l4.destroy)


#make a textbox to calculate the solution   and show it
b1 = Button(frame1, text = "1.7LT + \u0394/T = ", command = show)
b1.grid(row = 3, column = 0, sticky = W, padx=50, pady = 10)


top.mainloop()

