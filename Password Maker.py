import string, random, pyperclip
from tkinter import *
from tkinter import ttk

L_letters = string.ascii_lowercase
U_letters = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

def copy():
    pyperclip.copy(label_password['text'])
    label_success = Label(success_frame, text="Copy succeeded", fg="green", bg="#30d5c8", font=("Helvetica", 12))
    label_success.pack()
    label_success.after(1200, label_success.destroy)

def update_number_of_functions():
    return varL.get() + varU.get() + varN.get() + varS.get()

def Lbutton():
    global password
    if varL.get() == 0:
        password = [char for char in password if char not in L_letters]

def Ubutton():
    global password
    if varU.get() == 0:
        password = [char for char in password if char not in U_letters]

def Nbutton():
    global password
    if varN.get() == 0:
        password = [char for char in password if char not in numbers]

def Sbutton():
    global password
    if varS.get() == 0:
        password = [char for char in password if char not in symbols]

def distribute_remainder(remainder, options):
    for _ in range(remainder):
        choice = random.choice(options)
        password.append(random.choice(choice))

def Generator():
    global password
    password = []
    
    number_of_functions = update_number_of_functions()
    
    if number_of_functions == 0:
        label_password.config(text="Please select at least one option")
        return
    
    allAmount = pass_tall.get()
    for_each = allAmount // number_of_functions
    remainder = allAmount % number_of_functions
    
    if varL.get() == 1:
        password += random.choices(L_letters, k=for_each)
    if varU.get() == 1:
        password += random.choices(U_letters, k=for_each)
    if varN.get() == 1:
        password += random.choices(numbers, k=for_each)
    if varS.get() == 1:
        password += random.choices(symbols, k=for_each)
    
    options = []
    if varL.get() == 1:
        options.append(L_letters)
    if varU.get() == 1:
        options.append(U_letters)
    if varN.get() == 1:
        options.append(numbers)
    if varS.get() == 1:
        options.append(symbols)
    
    distribute_remainder(remainder, options)
    
    random.shuffle(password)
    password = "".join(password)
    label_password.config(text=password)

root = Tk()
root.geometry("555x440")
root.title("Password Maker")
root.config(bg="#30d5c8")
icon_photo = PhotoImage(file=r"Photos/unnamed (1).png")
root.iconphoto(True , icon_photo)

label_title = Label(root, text="One click --> Legendary password（⊙ｏ⊙）", font=("Helvetica", 16, "bold"), bg="#30d5c8")
label_title.grid(row=0, column=0, columnspan=4, sticky="WE", padx=20, pady=10)

label_password = Label(root, width=30, bd=5, foreground="white", highlightbackground="black", highlightthickness=5, bg="#FF0000", font=("Helvetica", 12))
label_password.grid(row=1, column=0, columnspan=4, sticky="WE", padx=20, pady=10)

Button_copy = Button(root, text="Copy", height=2, width=10, command=copy, bg="#2449FF", fg="white", font=("Helvetica", 10, "bold"))
Button_copy.grid(row=2, column=0, columnspan=4, pady=10)

success_frame = Frame(root , bg="#30d5c8")
success_frame.grid(row=3, column=0, columnspan=4, sticky="WE", padx=20)

label_settings_title = Label(root, text="Password Settings", font=("Helvetica", 14, "bold"), background="#30d5c8")
label_settings_title.grid(row=4, column=0, columnspan=4, sticky="WE", padx=20, pady=(20, 10))

varL = IntVar()
check_L = Checkbutton(root, text="Lowercase", variable=varL, font=("Helvetica", 12), command=Lbutton, bg="#30d5c8")
check_L.grid(row=6, column=0, padx=20, pady=5)

varU = IntVar()
check_U = Checkbutton(root, text="Uppercase", variable=varU, font=("Helvetica", 12), command=Ubutton, bg="#30d5c8")
check_U.grid(row=6, column=1, padx=20, pady=5)

varN = IntVar()
check_N = Checkbutton(root, text="Numbers", variable=varN, font=("Helvetica", 12), command=Nbutton, bg="#30d5c8")
check_N.grid(row=6, column=2, padx=20, pady=5)

varS = IntVar()
check_S = Checkbutton(root, text="Symbols", variable=varS, font=("Helvetica", 12), command=Sbutton, bg="#30d5c8")
check_S.grid(row=6, column=3, padx=20, pady=5)

Button_Generator = Button(root, text="GENERATE YOUR PASSWORD 🔥🔥", command=Generator, bg="#32cd32", fg="white", font=("Helvetica", 14, "bold"))
Button_Generator.grid(row=7, column=0, columnspan=4, sticky="WE", padx=20, pady=20)

label_passLength = ttk.Label(root, text="Password length >>>", font=("Helvetica", 10, "bold"), background="#30d5c8")
label_passLength.grid(row=5, column=0)

pass_tall = IntVar()
count_of_latters = Scale(root, from_=8, to=20, orient="horizontal", activebackground="#2dff00", variable=pass_tall)
count_of_latters.grid(row=5, column=1, columnspan=2, sticky="we", pady=5)

mainloop()
