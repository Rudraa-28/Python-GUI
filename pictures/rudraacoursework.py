from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox

# ---------------------------------FIRST WINDOW---------------------------------#
hello = Tk()
hello.title('WELCOME')
hello.iconbitmap('D:\jetbrains\pythonProject2\Python files-20230118\pictures/marvel-282124.ico')

answer = simpledialog.askstring("Input", "What is your first name?",
                                parent=hello)

messagebox.showinfo("welcome", "Hello, Welcome ☺️☺️☺️")
hello.destroy()

# ---------------------------------SECOND WINDOW---------------------------------#
window = Tk()
window.title('MARVEL SHOP ..〽️')

window.geometry('1275x689')
window.iconbitmap('D:\jetbrains\pythonProject2\Python files-20230118\pictures/marvel-282124.ico')
names = []
prices = []
basket_counter = IntVar(window, value=0)


# ---------------------------------ALL FUNCTIONS USED IN THIS CODE---------------------------------#

# ---------------------------------PRODUCTS ADDED AND REMOVING FUNCTIONS---------------------------------#
def add(element):
    names.append(element[0])
    prices.append(element[1])
    basket_counter.set(basket_counter.get() + 1)
    print(names)
    print(prices)


def remove(element):
    names.remove(element[0])
    prices.remove(element[1])
    basket_counter.set(basket_counter.get() - 1)
    print(names)
    print(prices)


# ---------------------------------BASKET WINDOW FUNCTIONS---------------------------------#
sv = StringVar()

# ---------------------------------FEEDBACK BUTTON---------------------------------#
def button():
    messagebox.askyesno("Question", " Do you like our shopping system?")
    xyz = messagebox.askquestion('Pay', 'Have you paid for your products ? 💵💵💵💵💵💵')
    if xyz != True:
        messagebox.showerror('error',
                             'I am sorry you have no payed for your products.\n'
                             'Please go back to the basket and select payment button for approving the payment.\n'
                             'Thank you..')
    else:
        messagebox.showinfo("Information", "THANK YOU !!! Have a good day...!!! ☺️☺️☺️")
        window.destroy()


# ---------------------------------PAYMENT BUTTON---------------------------------#
def payment():
    messagebox.showinfo("payment", "PAYMENT approved..!!✔️✔️")
    messagebox.showinfo("Information", "NOW WE ARE MOVING TO FEEDBACK..!!😁😁")
    messagebox.askyesno("Question", "Now we are at the end of shopping system. Do you like our shopping system?")
    messagebox.showinfo("Information", "THANK YOU !!! Have a good day...!!! ☺️☺️☺️")
    window.destroy()

# ---------------------------------BASKET WINDOW---------------------------------#

def show_basket():
    newWindow = Toplevel(master=window)
    newWindow.title("Basket")
    newWindow.iconbitmap(
        'D:\jetbrains\pythonProject2\Python files-20230118\pictures/marvel-282124.ico')
    newWindow.geometry('400x400')
    newWindow.configure(bg='pink')

    create_basket_text()
    basket_label = Label(newWindow, textvariable=sv)
    basket_label.pack()
    feedback = Button(master=newWindow, text='FEEDBACK', command=button, bg='#99b898', fg='black',
                      font=("Comic Sans MS", 18))
    feedback.pack()

    pay = Button(master=newWindow, text='CHECK OUT', command=payment, bg='#99b898', fg='black',
                 font=("Comic Sans MS", 18))
    pay.pack()


# ---------------------------------SELECTED ITEMS WITH TOTAL PURCHASE---------------------------------#

def create_basket_text():
    t = ''
    list_count = 1
    total = 0
    for i in range(len(names)):
        t = t + f"{list_count} --- {names[i]:20s}        £{prices[i]:4.1f} \n"
        list_count += 1
        total = total + prices[i]
    total = f"\n\n TOTAL:\t  £{total:4.1f} \n"
    sv.set(t + str(total))

    if sv.get() == '':
        sv.set('The basket is empty!')


# ------------------BASKET LABEL-----------------------------------#
lf_basket = LabelFrame(master=window, relief=RAISED, borderwidth=3, bg='#99b898')
lf_basket.grid(row=0, column=2)
basket_counter_label = Label(master=lf_basket, textvariable=basket_counter, bg='#99b898',cursor='star', height=3, width=10, font=14)
basket_counter_label.pack()

# ------------------BASKET BUTTON IN MAIN FRAME-----------------------------------#
lf_basket = Frame(master=window)
lf_basket.grid(row=2, column=2, padx=7, pady=7)
basket_show_button = Button(master=lf_basket, text='SHOW BASKET', command=show_basket, bg='#99b898', fg='black', cursor='exchange')
basket_show_button.pack()

# ----------------------------BASKET FRAME -------------------------------#
basket_fraem = LabelFrame(master=window)
basket_fraem.grid(row=1, column=4, padx=7, pady=7)


# ---------------------------------HOVER BUTTON FUNCTIONS---------------------------------#

def apple_frame_hover(event):
    l.configure(text='1. IRON MAN - This mask is of an American actor Robert Downey Jr. \n'
                     'who is famous for his suits and\n'
                     ' master brain in MCU.\n'
                     '2. CAPTIAN AMERICA - This shield is of an American actor\n'
                     ' Chris Evans who is famous for his \n'
                     'unbreakable shield in MCU.\n'
                     '3. BLACK PANTHER - These paws are of an American actor \n'
                     'Chadwick Boseman who is famous for his \n'
                     'wakanda and being black panther in MCU.\n')


def delete_text(event):
    l.configure(text='For description\nHover over the label\n')


def amazon_frame_hover(even):
    l.configure(text='4. SPIDER MAN - This spider sticker of an American actor\n'
                     ' Tom Holland who is famous for his \n'
                     'spider power in the MCU.\n'
                     '5. THOR - This hammer of an american actor Chris Hemsworth \n'
                     'who is famous for his \n'
                     'stormbreaker hammer in the MCU.\n'
                     '6. DOCTOR STRANGE - This Time stone one of the precious stone \n'
                     'gaurded by an american actor \n'
                     'Benedict Cumberbatch in the MCU.')


# --------------------------------WINDOW FIRST FRAME---------------------------------#

frame = LabelFrame(master=window, bg='#6c5b78', cursor='dot')
frame.grid(row=0, columnspan=3, padx=5, pady=5)

section = LabelFrame(master=frame, width=100, height=20, text='WELCOME', bg='#c06c84')
section.grid(row=0, columnspan=3, padx=30, pady=30)

l1 = Label(master=section, width=70, height=10, bg='pink')
k_label = Label(l1, text='HELLO WELCOME TO THIS MARVEL ANTIQUE SHOP ..!!🧸🧸🧸🧸', bg='#f8b195', font=("Comic Sans MS", 20),
                fg='black')
k_label.grid(row=0, column=0)
l1.pack()

# --------------------------------- WINDOW ROW 1 LEFT FRAME---------------------------------#


frame1 = LabelFrame(master=window, bg='#ff847c', cursor='plus')
frame1.grid(row=1, column=0, padx=5, pady=5)

section1 = LabelFrame(master=frame1, width=70, height=20, text='PRODUCTS', bg='#99b898')
section1.grid(row=0, column=0, padx=30, pady=30)

l2 = Label(master=section1, width=70, height=50, bg='#feceab')

# --------------------------------- IRON MAN PRODUCT ---------------------------------#

pan_image = PhotoImage(
    file="iron2.PNG")
pan_image = pan_image.subsample(2, 2)
pan_image_label = Label(l2, image=pan_image)
pan_image_label.grid(row=0, column=0)
pan_item = ['IRON MAN mask', 400]
pan_button = Button(l2, text='1. IRON MAN\n'
                             ' £ 400', command=lambda: add(pan_item), font=("Comic Sans MS", 11, 'bold'),
                    bg='red')  # , width=10, height=5)
pan_button.grid(row=0, column=1)
pan_button = Button(l2, text='REMOVE', command=lambda: remove(pan_item), font=("Comic Sans MS", 11, 'bold'),
                    bg='yellow')

pan_button.grid(row=0, column=2)

# --------------------------------- CAPTAIN AMERICA PRODUCT ---------------------------------#

chocolate_image = PhotoImage(
    file=r"captainamerica2.PNG")
chocolate_image = chocolate_image.subsample(2, 2)
chocolate_label = Label(l2, image=chocolate_image)
chocolate_label.grid(row=1, column=2)
chocolate_item = ['CAPTAIN AMERICA shield', 200]
chocolate_button = Button(l2, text='2. CAPTAIN AMERICA\n'
                                   ' £ 200', command=lambda: add(chocolate_item), font=("Comic Sans MS", 11, 'bold'),
                          bg='blue', fg='white')  # , width=10, height=5)
chocolate_button.grid(row=1, column=0)
chocolate_button = Button(l2, text='REMOVE', command=lambda: remove(chocolate_item), font=("Comic Sans MS", 11, 'bold'),
                          bg='white', )  # , width=10, height=5)
chocolate_button.grid(row=1, column=1)

# --------------------------------- BLACK PANTHER PRODUCT ---------------------------------#

kurkure_image = PhotoImage(
    file=r"blackpanther.png")
kurkure_image = kurkure_image.subsample(2, 2)
kurkure_label = Label(l2, image=kurkure_image)
kurkure_label.grid(row=3, column=0)
kurkure_item = ['BLACK PANTHER paws', 200]
kurkure_button = Button(l2, text='3. BLACK PANTHER\n'
                                 ' £ 200', command=lambda: add(kurkure_item), font=("Comic Sans MS", 11, 'bold'),
                        bg='black', fg='white')  # , width=10, height=5)
kurkure_button.grid(row=3, column=1)
kurkure_button = Button(l2, text='REMOVE', command=lambda: remove(kurkure_item), font=("Comic Sans MS", 11, 'bold'),
                        bg='purple', fg='white')  # , width=10, height=5)
kurkure_button.grid(row=3, column=2)

# --------------------------------- WINDOW ROW 1 LEFT HOVER BUTTON ---------------------------------#

l2.bind('<Enter>', apple_frame_hover)
l2.bind('<Leave>', delete_text)

l2.pack()

# --------------------------------- WINDOW ROW 1 RIGHT FRAME---------------------------------#


frame2 = LabelFrame(master=window, bg='#ff847c', cursor='plus')
frame2.grid(row=1, column=1, padx=5, pady=5)

section2 = LabelFrame(master=frame2, width=70, height=20, text='PRODUCTS', bg='#99b898')
section2.grid(row=1, column=1, padx=30, pady=30)

l3 = Label(master=section2, width=70, height=50, bg='#feceab')

# --------------------------------- SPIDERMAN PRODUCT ---------------------------------#

red_image = PhotoImage(
    file=r"spider2.png")
red_image = red_image.subsample(2, 2)
red_label = Label(l3, image=red_image)
red_label.grid(row=0, column=0)
red_item = ['SPIDERMAN sticker', 20]
red_button = Button(l3, text='4. SPIDER MAN\n'
                             ' £ 20', command=lambda: add(red_item), font=("Comic Sans MS", 11, 'bold'),
                    bg='red')
red_button.grid(row=0, column=1)
red_button = Button(l3, text='REMOVE', command=lambda: remove(red_item), font=("Comic Sans MS", 11, 'bold'), bg='blue',
                    fg='white')  # , width=10, height=5)
red_button.grid(row=0, column=2)

# --------------------------------- THOR PRODUCT ---------------------------------#

blue_image = PhotoImage(
    file=r"thor2.PNG")
blue_image = blue_image.subsample(2, 2)
blue_label = Label(l3, image=blue_image)
blue_label.grid(row=1, column=2)
blue_item = ['THOR hammer', 300]
blue_button = Button(l3, text='5. THOR\n'
                              ' £ 300', command=lambda: add(blue_item), font=("Comic Sans MS", 11, 'bold'),
                     bg='red')  # , width=10, height=5)
blue_button.grid(row=1, column=0)
blue_button = Button(l3, text='REMOVE', command=lambda: remove(blue_item), font=("Comic Sans MS", 11, 'bold'),
                     bg='grey', fg='white')  # , width=10, height=5)
blue_button.grid(row=1, column=1)

# --------------------------------- DOCTOR STRANGE PRODUCT ---------------------------------#

green_image = PhotoImage(
    file=r"doctor2.PNG")
green_image = green_image.subsample(2, 2)
green_label = Label(l3, image=green_image)
green_label.grid(row=3, column=0)
green_item = ['DOCTOR STRANGE stone', 600]
green_button = Button(l3, text='6. DOCTOR STRANGE\n'
                               ' £ 600', command=lambda: add(green_item), font=("Comic Sans MS", 11, 'bold'),
                      bg='lightgreen')  # , width=10, height=5)
green_button.grid(row=3, column=1)
green_button = Button(l3, text='REMOVE', command=lambda: remove(green_item), font=("Comic Sans MS", 11, 'bold'),
                      bg='blue', fg='white')  # , width=10, height=5)
green_button.grid(row=3, column=2)

# --------------------------------- WINDOW ROW 1 RIGHT HOVER BUTTON ---------------------------------#

l3.bind('<Enter>', amazon_frame_hover)
l3.bind('<Leave>', delete_text)

l3.pack()

# --------------------------------- DESCRIPTION FRAME ---------------------------------#

description_frame = LabelFrame(master=window, relief=RAISED, borderwidth=3, width=100, height=10,
                               font=("Comic Sans MS", 7, 'bold'), bg='yellow', cursor='man')
description_frame.grid(row=1, column=2, padx=7, pady=7)
l = Label(master=description_frame, text='For description\nHover over the label\n', width=53, height=15,
          font=("Comic Sans MS", 7, 'bold'), bg='lightblue')
l.pack()

window.configure(bg='black',cursor='spraycan')
window.mainloop()
