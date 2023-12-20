from tkinter import *
from tkinter.ttk import Combobox

def btn_click():
    mark = 0
    selected_answer_q3 = cb.get()
    selected_options_q6 = listbox_q6.curselection()
    correct_options_q6 = [1]

    if v1.get() == 1 and v2.get() == 0 and v3.get() == 1 and v4.get() == 0:
        mark += 4
    elif v1.get() == 1 and v2.get() == 0 and v3.get() == 0 and v4.get() == 0:
        mark += 2
    elif v1.get() == 0 and v2.get() == 0 and v3.get() == 1 and v4.get() == 0:
        mark += 2

    if v5.get() == 2:
        mark += 2

    if selected_answer_q3 == "SSD":
        mark += 2

    if scale_var.get():
            mark += 2

    for index in selected_options_q6:
        if index in correct_options_q6:
            mark += 2

    if mark > 7:
        lbl5["fg"] = "green"
    else:
        lbl5["fg"] = "red"
    v6.set("Ваша оцінка: "+str(mark))


tk = Tk()

# Title
tk.title("Тест з інформатики")
font_title = ("Arial", 14, "bold")
font_q = ("Arial", 12, "bold")

# Send Button
btn = Button(tk, text="Відповісти", command=btn_click, font=font_q)
v6 = StringVar()
lbl5 = Label(tk, text='', textvariable=v6, font=font_title)

# Student
qstn_title0 = Label(tk, text="Тест з Архітектури ПК", font=font_title)
qstn0 = Label(tk, text="Введіть своє ім'я", font=font_q)
v0 = StringVar()
entry_q0 = Entry(tk, textvariable=v0)


# Question 1
qstn_title1 = Label(tk, text="Питання №1", font=font_title)
qstn1 = Label(tk, text="Які існують виробники процесорів?", font=font_q)
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
chb1 = Checkbutton(tk, text="AMD", variable=v1, onvalue=1, offvalue=0)
chb2 = Checkbutton(tk, text="Logitech", variable=v2, onvalue=1, offvalue=0)
chb3 = Checkbutton(tk, text="Intel", variable=v3, onvalue=1, offvalue=0)
chb4 = Checkbutton(tk, text="NVIDIA", variable=v4, onvalue=1, offvalue=0)

# Question 2
qstn_title2 = Label(tk, text="Питання №2", font=font_title)
qstn2 = Label(tk, text="Скільки материнських плат може бути в системному блоці?", font=font_q)
v5 = IntVar()
rbt1 = Radiobutton(tk, text="Дві", variable=v5, value=1)
rbt2 = Radiobutton(tk, text="Тільки одна", variable=v5, value=2)
rbt3 = Radiobutton(tk, text="Одна, але за потреби можна встановити дві", variable=v5, value=3)
rbt4 = Radiobutton(tk, text="Дві й більше", variable=v5, value=4)

# Question 3
qstn_title3 = Label(tk, text="Питання №3", font=font_title)
qstn3 = Label(tk, text="Що швидше SSD чи HDD?", font=font_title)
qstn3_data = ("SSD", "Однаково", "HDD", "Не знаю")
cb = Combobox(tk, values=qstn3_data)


# Question 5
qstn_title5 = Label(tk, text="Питання №5", font=font_title)
qstn5 = Label(tk, text="Оцініть своє знання з інформатики від 1 до 10:", font=font_q)
scale_var = IntVar()
scale_q5 = Scale(tk, from_=1, to=10, orient=HORIZONTAL, variable=scale_var)

# Question 6
qstn_title6 = Label(tk, text="Питання №6", font=font_title)
qstn6 = Label(tk, text="Оберіть зайве:", font=font_q)

# Options for Listbox (you can customize these options)
listbox_options_q6 = ["Процесор", "Флеш-накопичувач", "Відеокарта", "Жорсткий диск", "Материнська плата", "Блок живлення"]

listbox_var_q6 = StringVar()
listbox_q6 = Listbox(tk, listvariable=listbox_var_q6, selectmode=MULTIPLE, height=len(listbox_options_q6))

# Set the list of options for the listbox_var_q6
listbox_var_q6.set(tuple(listbox_options_q6))


# Q0Place
qstn0.pack()
entry_q0.pack()

# Q1Place
qstn_title1.pack()
qstn1.pack()
chb1.pack()
chb2.pack()
chb3.pack()
chb4.pack()

# Q2Place
qstn_title2.pack()
qstn2.pack()
rbt1.pack()
rbt2.pack()
rbt3.pack()
rbt4.pack()

# Q3Place
qstn_title3.pack()
qstn3.pack()
cb.pack()

# Q5Place
qstn_title5.pack()
qstn5.pack()
scale_q5.pack()

# Q6Place
qstn_title6.pack()
qstn6.pack()
listbox_q6.pack()


btn.pack()
lbl5.pack()

tk.mainloop()
