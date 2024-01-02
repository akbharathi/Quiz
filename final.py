import mysql.connector
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

db = mysql.connector.connect(host="localhost", user="root", passwd="Bharathi23$", database="quiz")
cursor = db.cursor()
cursor.execute("create table if not exists participants(Roll_no int auto_increment, Name varchar(20), Age int, Marks int, primary key(Roll_no));")

right = 0
right1 = 0
right2 = 0
right3 = 0
right4 = 0
right5 = 0
right6 = 0
right7 = 0


class QuizApp(Tk):

    # __init__ function 
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = Frame(self)
        container.pack(side=TOP, fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (quiz, Page1, Instruction, Page2, astronomy, ast1, ast2, ast3, ast4, ast5, ast6, ast7, ast8, ast9,
                  famous_persons, fp1, fp2, fp3, fp4, fp5, fp6, fp7, fp8, fp9, math, m1, m2, m3, m4, m5, m6, m7, m8,
                  m9, riddles, r1, r2, r3, r4, r5, r6, r7, r8, r9, current_affairs, ca1, ca2, ca3, ca4, ca5, ca6, ca7,
                  ca8, ca9, Literature, lit1, lit2, lit3, lit4, lit5, lit6, lit7, lit8, lit9, Sports, s1, s2, s3, s4,
                  s5, s6, s7, s8, s9, tourism, t1, t2, t3, t4, t5, t6, t7, t8, t9, ast_Results, fp_Results,
                  math_Results,
                  riddles_Results, ca_Results, lit_Results, sports_Results, tourism_Results):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(quiz)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        self.geometry("800x700")
        self.title("QUIZ")


class quiz(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.image = Image.open("Img//QUIZ.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        button = Button(self, text="LET'S START!", font=("Baskerville Old Face", 20), bg="black", fg="ivory",
                        command=lambda: controller.show_frame(Page1))
        button.place(x=650, y=680)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


# first window frame page1

class Page1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//quiz background.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.name_var = StringVar()
        self.age_var = StringVar()

        l1 = Label(self, text="Name :", font=("Lucida Calligraphy", 28), bg="black", fg="ivory")
        l1.place(x=400, y=200)
        input1 = Entry(self, textvariable=self.name_var, font=("Lucida Calligraphy", 20), bg="ivory", fg="black")
        input1.place(x=600, y=200)

        l2 = Label(self, text="Age :", font=("Lucida Calligraphy", 28), bg="black", fg="ivory")
        l2.place(x=440, y=400)
        input2 = Entry(self, textvariable=self.age_var, font=("Lucida Calligraphy", 20), bg="ivory", fg="black")
        input2.place(x=600, y=400)
        button1 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="ivory",
                         command=lambda: name_validation())
        button1.place(x=700, y=580)

        def name_validation():
            global name
            name = self.name_var.get()

            while True:
                try:
                    if len(name) == 0:
                        msg = 'Fill your name'
                        messagebox.showinfo('Info', msg)
                        break

                    if any(ch.isdigit() for ch in name):
                        msg = 'Name can\'t have numbers'
                        messagebox.showinfo('Info', msg)
                        break

                    if any(not c.isalnum() for c in name):
                        msg = 'Name can\'t have special characters'
                        messagebox.showinfo('Info', msg)
                        break

                    else:
                        age_validation()
                        break

                except Exception as ep:
                    messagebox.showerror('error', ep)
                    break

        def age_validation():
            global age
            age = self.age_var.get()

            while True:
                try:
                    if len(age) == 0:
                        msg = 'Fill your age'
                        messagebox.showinfo('Info', msg)
                        break

                    if int(age) <= 0:
                        msg = 'Age can\'t be negative or zero'
                        messagebox.showinfo('Info', msg)
                        break

                    if int(age) > 0:
                        controller.show_frame(Instruction)
                        break

                except:
                    msg = 'Age cannot be a string'
                    messagebox.showinfo('Info', msg)
                    break

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class Instruction(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//quiz background.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        message = '''
                        WELCOME TO THE QUIZ WORLD!

    You can choose any one of the 8 topics - Sports, Astronomy,

    Literature, Current Affairs, Famous persons, Simple Math,

    Tourism and Riddles. Each topic consists of 10 multiple

    choice 1 mark questions. You need to choose one from the 

    4 options given for each question. You can choose each

                                   topic only once.


                        SO, ARE YOU READY TO PLAY?'''

        text_box = Text(self, height=18, width=50, font=("Lucida Calligraphy", 18), bg="black", fg="ivory")
        text_box.place(x=400, y=100)
        text_box.insert('end', message)
        text_box.config(state='disabled')
        button1 = Button(self, text="LET'S GO!", font=("Baskerville Old Face", 20), bg="black", fg="ivory",
                         command=lambda: controller.show_frame(Page2))
        button1.place(x=720, y=670)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


# second window frame page2
class Page2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//quiz background.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        l1 = Label(self, text="Choose one Topic", font=("Lucida Calligraphy", 35), bg="black", fg="ivory")
        l1.place(x=510, y=0)
        bt1 = Button(self, text="Sports", font=("Lucida Calligraphy", 25), bg="black", fg="ivory",
                     command=lambda: [switch(bt1), controller.show_frame(Sports)])
        bt1.place(x=400, y=120)

        bt2 = Button(self, text="Literature", font=("Lucida Calligraphy", 25), bg="black", fg="ivory",
                     command=lambda: [switch(bt2), controller.show_frame(Literature)])
        bt2.place(x=400, y=250)

        bt3 = Button(self, text="Famous Persons", font=("Lucida Calligraphy", 25), bg="black", fg="ivory",
                     command=lambda: [switch(bt3), controller.show_frame(famous_persons)])
        bt3.place(x=400, y=380)

        bt4 = Button(self, text="Tourism", font=("Lucida Calligraphy", 25), bg="black", fg="ivory",
                     command=lambda: [switch(bt4), controller.show_frame(tourism)])
        bt4.place(x=400, y=510)

        bt5 = Button(self, text="Astronomy", font=("Lucida Calligraphy", 25), bg="black", fg="ivory",
                     command=lambda: [switch(bt5), controller.show_frame(astronomy)])
        bt5.place(x=850, y=120)

        bt6 = Button(self, text="Current Affairs", font=("Lucida Calligraphy", 25), bg="black", fg="ivory",
                     command=lambda: [switch(bt6), controller.show_frame(current_affairs)])
        bt6.place(x=850, y=250)

        bt7 = Button(self, text="Simple Math", font=("Lucida Calligraphy", 25), bg="black", fg="ivory",
                     command=lambda: [switch(bt7), controller.show_frame(math)])
        bt7.place(x=850, y=380)

        bt8 = Button(self, text="Riddles", font=("Lucida Calligraphy", 25), bg="black", fg="ivory",
                     command=lambda: [switch(bt8), controller.show_frame(riddles)])
        bt8.place(x=850, y=510)

        button1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="ivory",
                         command=lambda: controller.show_frame(Instruction))
        button1.place(x=700, y=650)

        def switch(btn):
            btn["state"] = DISABLED

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


# third window frame page2

class astronomy(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//Astronomy.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q1 = Label(self, text="1. Which galaxy is home to the solar system? ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q1.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Andromeda Galaxy", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Cygnus A", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Milkyway Galaxy", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Magellanic Clouds", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast1))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right
            right = right + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ast1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//Astronomy.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q2 = Label(self, text="2. Which object lost its status as a planet in 2006? ",
                   font=("Baskerville Old Face", 32), bg="black", fg="ivory")
        q2.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Uranus", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Neptune", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Mercury", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Pluto", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(astronomy))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast2))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right
            right = right + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ast2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//Astronomy.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q3 = Label(self, text="3. How many moons does Mars have? ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q3.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="1", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="2", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="3", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="4", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast1))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast3))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right
            right = right + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ast3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//Astronomy.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q4 = Label(self, text="4. Which planet has the largest moon in the solar system? ",
                   font=("Baskerville Old Face", 32), bg="black", fg="ivory")
        q4.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Venus", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Earth", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Jupiter", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Mars", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast2))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast4))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right
            right = right + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ast4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//Astronomy.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q5 = Label(self, text="5. How many terrestrial planets are there in the solar system?  ",
                   font=("Baskerville Old Face", 32), bg="black", fg="ivory")
        q5.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="5", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="6", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="4", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="1", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast3))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast5))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right
            right = right + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ast5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//Astronomy.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q6 = Label(self, text="6. Who was the first man to step on the moon? ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q6.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Neil Armstrong", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Buzz Aldrin", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Eugene Cernan", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Alan Bean", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast4))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast6))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right
            right = right + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ast6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//Astronomy.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q7 = Label(self, text="7. How many moons does Jupiter have? ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q7.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="76", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="79", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="69", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="80", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast5))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast7))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right
            right = right + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ast7(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//Astronomy.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q8 = Label(self, text="8. Which planet is called 'The Red planet'? ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q8.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Jupiter", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Saturn", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Venus", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Mars", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast6))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast8))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right
            right = right + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ast8(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//Astronomy.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q9 = Label(self, text="9. A group of stars that resemble an earthly object is called ",
                   font=("Baskerville Old Face", 32), bg="black", fg="ivory")
        q9.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="A constellation", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="A galaxy", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="A nebula", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="A coma stellata", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast7))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast9))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right
            right = right + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ast9(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//Astronomy.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q10 = Label(self, text="10. A light year is a measurement of  ", font=("Baskerville Old Face", 32),
                    bg="black", fg="ivory")
        q10.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Brightness", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Time", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Size", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Distance", font=("Lucida Calligraphy", 20), bg="black",
                           fg="RoyalBlue1", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast8))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="SUBMIT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ast_Results))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right
            right = right + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class famous_persons(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//famous.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q1 = Label(self, text="1. Who is the father of geometry?  ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q1.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Aristotle", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Euclid", font=("Lucida Calligraphy", 20), bg="dark goldenrod", fg="black",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Pythagoras", font=("Lucida Calligraphy", 20), bg="dark goldenrod", fg="black",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Kepler", font=("Lucida Calligraphy", 20), bg="dark goldenrod", fg="black",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

#        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
#                     command=lambda: controller.show_frame(Page2))
#        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp1))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right1
            right1 = right1 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class fp1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//famous.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q2 = Label(self, text="2. Who was known as the 'Iron man of India'?  ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q2.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Govind Ballabh Pant", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1,
                           value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Jawaharlal Nehru", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Subash Chandra Bose", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1,
                           value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Sardar Vallabhbhai Patel", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1,
                           value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(famous_persons))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp2))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right1
            right1 = right1 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class fp2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//famous.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q3 = Label(self, text="3. Which Indian beat the computers in mathematical wizardy?  ",
                   font=("Baskerville Old Face", 32), bg="black", fg="ivory")
        q3.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Ramanujan", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Raja Ramanna", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Shakuntala Devi", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Rina Panigrahi", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp1))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp3))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right1
            right1 = right1 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class fp3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//famous.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q4 = Label(self, text="4. Dr. M.S.Swaminathan has distinguished himself in which field?  ",
                   font=("Baskerville Old Face", 32), bg="black", fg="ivory")
        q4.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Agriculture", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Medicine", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Astrophysics", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Physics", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp2))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp4))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right1
            right1 = right1 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class fp4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//famous.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q5 = Label(self, text="5. R.K.Laxman is a renowned  ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q5.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Dance master", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Writer", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Cartoonist", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Journalist", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp3))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp5))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right1
            right1 = right1 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class fp5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//famous.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q6 = Label(self, text="6. The first woman in space was  ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q6.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Sally Ride", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Valentina Tereshkova", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1,
                           value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Kalpana Chawla", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Naidia Comenci", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp4))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp6))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right1
            right1 = right1 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class fp6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//famous.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q7 = Label(self, text="7. Who is known as the 'Flying Sikh of India'?  ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q7.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Mohinder Singh", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Ajit Pal Singh", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Joginder Singh", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Milka Singh", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp5))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp7))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right1
            right1 = right1 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class fp7(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//famous.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q8 = Label(self, text="8. Who is the creator of the Rock Garden in Chandigarh?  ",
                   font=("Baskerville Old Face", 32), bg="black", fg="ivory")
        q8.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Glen", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Nek Chand", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Pupal Jayakar", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Le Corbousier", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp6))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp8))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right1
            right1 = right1 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class fp8(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//famous.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q9 = Label(self, text="9. Who is known as the 'Lady with the Lamp'? ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q9.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Joan of Arc", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Indira Gandhi", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Florence Nightingale", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1,
                           value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Sarojini Naidu", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp7))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp9))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right1
            right1 = right1 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class fp9(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//famous.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q10 = Label(self, text="10. Who is known as the 'Missile Man of India'?  ", font=("Baskerville Old Face", 32),
                    bg="black", fg="ivory")
        q10.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Satish Dhawan", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="A.P.J.Abdul Kalam", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="K Sivan", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Vikram Sarabhai", font=("Lucida Calligraphy", 20), bg="dark goldenrod",
                           fg="black", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp8))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="SUBMIT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(fp_Results))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right1
            right1 = right1 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class math(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//maths2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q1 = Label(self, text="1. 50 times 5 is equal to ", font=("Baskerville Old Face", 32), bg="papaya whip")
        q1.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="2500", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="2500", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="250", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="500", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

#        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
#                     command=lambda: controller.show_frame(Page2))
#        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m1))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right2
            right2 = right2 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class m1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//maths2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q2 = Label(self, text="2. Find the product of 72 X 3 ", font=("Baskerville Old Face", 32),
                   bg="papaya whip")
        q2.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="226", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="216", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="246", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="256", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(math))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m2))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right2
            right2 = right2 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class m2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//maths2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q3 = Label(self, text="3. Arrange in ascending order: 15000, 2673, 8996, 54756, 88043 ",
                   font=("Baskerville Old Face", 32), bg="papaya whip")
        q3.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="88043, 54756, 15000, 8996, 2673", font=("Lucida Calligraphy", 20),
                           bg="papaya whip",
                           fg="firebrick4",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="2673, 8996, 15000, 54756, 88043", font=("Lucida Calligraphy", 20),
                           bg="papaya whip",
                           fg="firebrick4",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="15000, 8996, 54756, 2673, 88043", font=("Lucida Calligraphy", 20),
                           bg="papaya whip",
                           fg="firebrick4",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="None of these", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m1))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m3))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right2
            right2 = right2 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class m3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//maths2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q4 = Label(self, text="4. 20 has how many factors? ", font=("Baskerville Old Face", 32),
                   bg="papaya whip")
        q4.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="5", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="6", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="2", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="4", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m2))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m4))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right2
            right2 = right2 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class m4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//maths2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q5 = Label(self, text="5. What is the smallest four digit number? ", font=("Baskerville Old Face", 32),
                   bg="papaya whip")
        q5.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="1001", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="9999", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="1111", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="1000", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m3))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m5))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right2
            right2 = right2 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class m5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//maths2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q6 = Label(self, text="6. Simplify : 3 + 6 x (5 + 4) ÷ 3 - 7 ", font=("Baskerville Old Face", 32),
                   bg="papaya whip")
        q6.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="11", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="16", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="14", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="15", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)
        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m4))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m6))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right2
            right2 = right2 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class m6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//maths2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q7 = Label(self, text="7. The sum of the least number of three digits and largest number of two digits is ",
                   font=("Baskerville Old Face", 32), bg="papaya whip")
        q7.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="100", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="101", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="111", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="199", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m5))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m7))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right2
            right2 = right2 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class m7(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//maths2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q8 = Label(self, text="8. A number is divisible by 3 if the sum of its digits is divisible by ",
                   font=("Baskerville Old Face", 32), bg="papaya whip")
        q8.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="1", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="2", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="5", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="3", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m6))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m8))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right2
            right2 = right2 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class m8(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//maths2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q9 = Label(self, text="9. What is the largest two digits prime number?  ", font=("Baskerville Old Face", 32),
                   bg="papaya whip")
        q9.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="96", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="97", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="93", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="99", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m7))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m9))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right2
            right2 = right2 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class m9(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//maths2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q10 = Label(self, text="10. How many hours are there in 90 minutes? ", font=("Baskerville Old Face", 32),
                    bg="papaya whip")
        q10.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="1.30 hours", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="1.5 hours", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="1 hour", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="None of these", font=("Lucida Calligraphy", 20), bg="papaya whip",
                           fg="firebrick4", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(m8))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="SUBMIT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(math_Results))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right2
            right2 = right2 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class riddles(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//riddles2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q1 = Label(self, text="1. What has to be broken before you can use it? ",
                   font=("Baskerville Old Face", 32), bg="gray64", fg="firebrick2")
        q1.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Book", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Toy", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Egg", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Plant", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

#        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
#                     command=lambda: controller.show_frame(Page2))
#        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r1))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right3
            right3 = right3 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class r1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//riddles2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q2 = Label(self, text="2. I'm tall when I'm young, and I'm short when I'm old. What am I? ",
                   font=("Baskerville Old Face", 32), bg="gray64", fg="firebrick2")
        q2.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Human", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Alien", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Elephant", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Candle", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(riddles))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r2))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right3
            right3 = right3 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class r2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//riddles2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q3 = Label(self, text="3. What month of the year has 28 days? ",
                   font=("Baskerville Old Face", 32), bg="gray64", fg="firebrick2")
        q3.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="June", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="February", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="May", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="All months", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r1))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r3))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right3
            right3 = right3 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class r3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//riddles2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q4 = Label(self, text="4. What is always in front of you but cannot be seen? ",
                   font=("Baskerville Old Face", 32), bg="gray64", fg="firebrick2")
        q4.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Present", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Past", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Future", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Colour", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r2))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r4))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right3
            right3 = right3 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class r4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//riddles2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q5 = Label(self, text="5. What goes up but never comes down? ",
                   font=("Baskerville Old Face", 32), bg="gray64", fg="firebrick2")
        q5.place(x=0, y=0)

        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Age", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Time", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Balloon", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Bird", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r3))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r5))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right3
            right3 = right3 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class r5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//riddles2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q6 = Label(self, text="6. I have branches, but no fruit, trunk or leaves. What am I? ",
                   font=("Baskerville Old Face", 32), bg="gray64", fg="firebrick2")
        q6.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Banyan Tree", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Bank", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Insect", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Home", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r4))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r6))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right3
            right3 = right3 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class r6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//riddles2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q7 = Label(self, text="7. What has many keys but cannot open a single lock?",
                   font=("Baskerville Old Face", 32), bg="gray64", fg="firebrick2")
        q7.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Keychain", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Door", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Piano", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Flute", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r5))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r7))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right3
            right3 = right3 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class r7(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//riddles2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q8 = Label(self, text="8. What is black when it's clean and white when it's dirty?  ",
                   font=("Baskerville Old Face", 32), bg="gray64", fg="firebrick2")
        q8.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Wall", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Cloth", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="White board", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Black board", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r6))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r8))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right3
            right3 = right3 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class r8(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//riddles2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q9 = Label(self, text="9. Where does today come before yesterday? ",
                   font=("Baskerville Old Face", 32), bg="gray64", fg="firebrick2")
        q9.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Life", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Dictionary", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="World", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Fiction", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r7))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r9))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right3
            right3 = right3 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class r9(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//riddles2.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q10 = Label(self, text="10. It belongs to you but other people use it more than you do. What is it? ",
                    font=("Baskerville Old Face", 32), bg="gray64", fg="firebrick2")
        q10.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Height", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Age", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Fame", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Name", font=("Lucida Calligraphy", 20), bg="gray64", fg="firebrick2",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(r8))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="SUBMIT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(riddles_Results))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right3
            right3 = right3 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class current_affairs(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//current_affairs.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q1 = Label(self, text="1. Nancy Grace Roman Space Telescope is being developed by which country? ",
                   font=("Baskerville Old Face", 32), bg="black", fg="white")
        q1.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Japan", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="USA", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Russia", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Israel", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

#        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
#                     command=lambda: controller.show_frame(Page2))
#        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca1))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right4
            right4 = right4 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ca1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//current_affairs.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q2 = Label(self, text="2. Which state has introduced India’s first city sewage surveillance system? ",
                   font=("Baskerville Old Face", 32), bg="black", fg="white")
        q2.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Tamil Nadu", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Karnataka", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Maharashtra", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Uttar Pradesh", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(current_affairs))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca2))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right4
            right4 = right4 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ca2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//current_affairs.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q3a = Label(self, text="3. 'Sea snot' which is in the news, has been reported to accumulate",
                    font=("Baskerville Old Face", 32), bg="black", fg="white")
        q3a.place(x=0, y=0)
        q3b = Label(self, text="in the coast of which country?", font=("Baskerville Old Face", 32),
                    bg="black", fg="white")
        q3b.place(x=0, y=60)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="China", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=140)
        rad2 = Radiobutton(self, text="Turkey", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=220)
        rad3 = Radiobutton(self, text="Canada", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=300)
        rad4 = Radiobutton(self, text="Spain", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=380)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca1))
        bt1.place(x=0, y=460)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca3))
        bt2.place(x=500, y=460)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right4
            right4 = right4 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ca3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//current_affairs.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q4 = Label(self, text="4. Offshore patrol vessel 'Sajag' has been commissioned to which armed force? ",
                   font=("Baskerville Old Face", 32), bg="black", fg="white")
        q4.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Indian Coast Guard", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Indian Navy", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Indian army", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="CRPF", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca2))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca4))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right4
            right4 = right4 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ca4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//current_affairs.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q5a = Label(self, text="5.What is the name of the disinfection system launched in Telangana, to reuse",
                    font=("Baskerville Old Face", 32), bg="black", fg="white")
        q5a.place(x=0, y=0)
        q5b = Label(self, text=" the PPEs and other materials of healthcare workers? ",
                    font=("Baskerville Old Face", 32), bg="black", fg="white")
        q5b.place(x=0, y=60)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Vajra Kavach", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=140)
        rad2 = Radiobutton(self, text="RRR Kavach", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=220)
        rad3 = Radiobutton(self, text="Reuse Health", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=300)
        rad4 = Radiobutton(self, text="Suraksha Kavach", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=380)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca3))
        bt1.place(x=0, y=460)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca5))
        bt2.place(x=500, y=460)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right4
            right4 = right4 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ca5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//current_affairs.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q6 = Label(self, text="6. What is the theme of World Milk Day 2021, observed recently on 1st June? ",
                   font=("Baskerville Old Face", 32), bg="black", fg="white")
        q6.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Sustainability in the dairy sector", font=("Lucida Calligraphy", 20),
                           bg="navy", fg="IndianRed3", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Milk For All", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Leaving No one Behind", font=("Lucida Calligraphy", 20), bg="navy",
                           fg="IndianRed3", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Milk and SDG", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca4))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca6))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right4
            right4 = right4 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ca6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//current_affairs.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q7 = Label(self, text="7. In context with recent news of Goa, what does the abbreviation GIFT stand for? ",
                   font=("Baskerville Old Face", 32), bg="black", fg="white")
        q7.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Goa Institution For Future Transformation", font=("Lucida Calligraphy", 20),
                           bg="navy", fg="IndianRed3", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Goa Institution For Financial Transformation", font=("Lucida Calligraphy", 20),
                           bg="navy", fg="IndianRed3", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Goa Institution For Fin Tech", font=("Lucida Calligraphy", 20),
                           bg="navy", fg="IndianRed3", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Goa Institute of Foreign Affairs", font=("Lucida Calligraphy", 20),
                           bg="navy", fg="IndianRed3", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca5))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca7))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right4
            right4 = right4 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ca7(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//current_affairs.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q8a = Label(self, text="8. Which country has recently come up with a policy for three children,",
                    font=("Baskerville Old Face", 32), bg="black", fg="white")
        q8a.place(x=0, y=0)
        q8b = Label(self, text="as against the present two children limit? ", font=("Baskerville Old Face", 32),
                    bg="black", fg="white")
        q8b.place(x=0, y=60)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="India", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=140)
        rad2 = Radiobutton(self, text="USA", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=220)
        rad3 = Radiobutton(self, text="Japan", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=300)
        rad4 = Radiobutton(self, text="China", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=380)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca6))
        bt1.place(x=0, y=460)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca8))
        bt2.place(x=500, y=460)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right4
            right4 = right4 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ca8(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//current_affairs.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q9a = Label(self, text="9. 'Campaign Rabta Muhim', which was making news recently, is being ",
                    font=("Baskerville Old Face", 32), bg="black", fg="white")
        q9a.place(x=0, y=0)
        q9b = Label(self, text="implemented in which state? ", font=("Baskerville Old Face", 32),
                    bg="black", fg="white")
        q9b.place(x=0, y=60)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Rajasthan", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=140)
        rad2 = Radiobutton(self, text="Punjab", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=220)
        rad3 = Radiobutton(self, text="Haryana", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=300)
        rad4 = Radiobutton(self, text="Uttarakhand", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=380)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca7))
        bt1.place(x=0, y=460)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca9))
        bt2.place(x=500, y=460)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right4
            right4 = right4 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ca9(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//current_affairs.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q10 = Label(self, text="10. 'Red Tourism', which was seen in the news, is associated with which country? ",
                    font=("Baskerville Old Face", 32), bg="black", fg="white")
        q10.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Indonesia", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="India", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="China", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Sri Lanka", font=("Lucida Calligraphy", 20), bg="navy", fg="IndianRed3",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca8))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="SUBMIT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(ca_Results))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right4
            right4 = right4 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class Literature(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//literature.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q1 = Label(self, text="1. What is a funny poem of five lines called? ", font=("Baskerville Old Face", 32),
                   bg="DarkGoldenRod2")
        q1.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Quartet", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Limerick", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Palindrome", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Sextet", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

#        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
#                     command=lambda: controller.show_frame(Page2))
#        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit1))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right5
            right5 = right5 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class lit1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//literature.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q2 = Label(self, text="2. Who is the villain in Hamlet? ", font=("Baskerville Old Face", 32),
                   bg="DarkGoldenRod2")
        q2.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Horatio", font=("Lucida Calligraphy", 20), bg="DarkGoldenRod2",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Lago", font=("Lucida Calligraphy", 20), bg="DarkGoldenRod2",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Claudius", font=("Lucida Calligraphy", 20), bg="DarkGoldenRod2",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Yorick", font=("Lucida Calligraphy", 20), bg="DarkGoldenRod2",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(Literature))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit2))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right5
            right5 = right5 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class lit2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//literature.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q3 = Label(self, text="3. Who was the author of the famous storybook 'Alice's Adventures in Wonderland'? ",
                   font=("Baskerville Old Face", 32), bg="DarkGoldenRod2")
        q3.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Lewis Carroll", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="H G Wells", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="John Keats", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Rudyard Kipling", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit1))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit3))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right5
            right5 = right5 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class lit3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//literature.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q4 = Label(self, text="4. Which is the first Harry Potter book? ", font=("Baskerville Old Face", 32),
                   bg="DarkGoldenRod2")
        q4.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="HP and the Goblet of Fire", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="HP and the Philosopher's Stone", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="HP and the Chamber of Secrets", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="HP and the deathly hallows", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit2))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit4))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right5
            right5 = right5 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class lit4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//literature.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q5 = Label(self, text="5. Shakespeare's four greatest tragedies are Macbeth, Othello, Hamlet and _________?  ",
                   font=("Baskerville Old Face", 32), bg="DarkGoldenRod2")
        q5.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Twelfth Night", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Romeo and Juliet", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="King Lear", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Julius Caesar", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit3))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit5))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right5
            right5 = right5 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class lit5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//literature.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q6 = Label(self, text="6. What is the genre that deals with imaginative and futuristic concepts? ",
                   font=("Baskerville Old Face", 32), bg="DarkGoldenRod2")
        q6.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Science Fiction", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Fantasy", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Paranormal fiction", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1,
                           value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Dystopian fiction", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit4))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit6))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right5
            right5 = right5 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class lit6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//literature.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q7 = Label(self, text="7. In which novel of Roald Dahl, the character Willy Wonka can be found? ",
                   font=("Baskerville Old Face", 32), bg="DarkGoldenRod2")
        q7.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Matilda", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Fantastic Mr Fox", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="The BFG", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Charlie And The Chocolate Factory", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)
        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit5))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit7))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right5
            right5 = right5 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class lit7(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//literature.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q8 = Label(self, text="8. Who was the authoress of 'Pride and Prejudice'? ", font=("Baskerville Old Face", 32),
                   bg="DarkGoldenRod2")
        q8.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Emily Bronte", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Jane Austen", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Anne Bronte", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Harper Lee", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit6))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit8))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right5
            right5 = right5 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class lit8(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//literature.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q9 = Label(self, text="9. The character of Mustardseed was found in which Shakespearean play? ",
                   font=("Baskerville Old Face", 32), bg="DarkGoldenRod2")
        q9.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="A Midsummer Night's Dream", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Hamlet", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Othello", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Macbeth", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit7))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit9))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right5
            right5 = right5 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class lit9(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//literature.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q10a = Label(self, text="10. The use of words with humorous satirical intention so that the meaning is ",
                     font=("Baskerville Old Face", 32), bg="DarkGoldenRod2")
        q10a.place(x=0, y=0)
        q10b = Label(self, text="the direct opposite to what is actually said is known as?  ",
                     font=("Baskerville Old Face", 32), bg="DarkGoldenRod2")
        q10b.place(x=0, y=60)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Pun", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=140)
        rad2 = Radiobutton(self, text="Irony", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=220)
        rad3 = Radiobutton(self, text="Metaphor", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=300)
        rad4 = Radiobutton(self, text="Personification", font=("Lucida Calligraphy", 20),
                           bg="DarkGoldenRod2", variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=380)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit8))
        bt1.place(x=0, y=460)
        bt2 = Button(self, text="SUBMIT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(lit_Results))
        bt2.place(x=500, y=460)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right5
            right5 = right5 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class Sports(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//sports.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q1 = Label(self, text="1. Who won gold medal for India in 2020 Olympics? ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q1.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="P V Sindhu", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Neeraj Chopra", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Ravi Dahiya", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Mirabhai Chanu", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

#        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
#                     command=lambda: controller.show_frame(Page2))
#        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s1))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right6
            right6 = right6 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class s1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//sports.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q2 = Label(self, text="2. In which country was the first Olympic held? ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q2.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Germany", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="France", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Greece", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Tokyo", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(Sports))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s2))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right6
            right6 = right6 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class s2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//sports.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q3 = Label(self, text="3. How many holes does a standard golf course have? ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q3.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="18", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="15", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="10", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="8", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s1))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s3))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right6
            right6 = right6 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class s3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//sports.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q4 = Label(self, text="4. How many yards is a cricket pitch in length? ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q4.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="20 yards", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="22 yards", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="25 yards", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="18 yards", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s2))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s4))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right6
            right6 = right6 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class s4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//sports.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q5 = Label(self, text="5. Who was the first Indian fencer to qualify for Tokyo Olympic Games? ",
                   font=("Baskerville Old Face", 32), bg="black", fg="ivory")
        q5.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Kavitha Devi", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Daina Devi", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Bhavani Devi", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Kaushik Vedika", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s3))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s5))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right6
            right6 = right6 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class s5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//sports.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q6 = Label(self, text="6. FIFA is the global regulatory body of which sports? ",
                   font=("Baskerville Old Face", 32), bg="black", fg="ivory")
        q6.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Football", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Hockey", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Cricket", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Tennis", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s4))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s6))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right6
            right6 = right6 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class s6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//sports.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q7 = Label(self, text="7. What is the full form of IPL? ", font=("Baskerville Old Face", 32),
                   bg="black", fg="ivory")
        q7.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Indo-Pakistan League", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="International Premier League", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Indian Players League", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Indian Premier League", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s5))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s7))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right6
            right6 = right6 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class s7(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//sports.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q8 = Label(self, text="8. Thomas Cup and Uber Cup are prestigious trophies of- ",
                   font=("Baskerville Old Face", 32), bg="black", fg="ivory")
        q8.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Lawn Tennis", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Badminton", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Table Tennis", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Golf", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s6))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s8))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right6
            right6 = right6 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class s8(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//sports.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q9 = Label(self, text="9. How many medals did India won in Tokyo Olympics 2020? ",
                   font=("Baskerville Old Face", 32), bg="black", fg="ivory")
        q9.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="7", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="5", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="8", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="6", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s7))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s9))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right6
            right6 = right6 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class s9(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//sports.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q10 = Label(self, text="10. Who was India's first football captain? ", font=("Baskerville Old Face", 32),
                    bg="black", fg="ivory")
        q10.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="P K Banerjee", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Talimeren Ao", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="SC Goswami", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Shalein Manna", font=("Lucida Calligraphy", 20), bg="steel blue",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(s8))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="SUBMIT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(sports_Results))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right6
            right6 = right6 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class tourism(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//tourism.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q1 = Label(self, text="1. One of the seven wonders of the world, the 'Taj Mahal' is located where? ",
                   font=("Baskerville Old Face", 32),
                   bg="light sky blue", fg="ivory")
        q1.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Bangalore", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Delhi", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Agra", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Lucknow", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

#        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
#                     command=lambda: controller.show_frame(Page2))
#        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t1))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 3:
            global right7
            right7 = right7 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class t1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//tourism.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q2 = Label(self, text="2. Which Indian hill station is known as the 'Queen of the Hills'? ",
                   font=("Baskerville Old Face", 32),
                   bg="light sky blue", fg="ivory")
        q2.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Mussoorie", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Darjeeling", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Shimla", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Shillong", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(tourism))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t2))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right7
            right7 = right7 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class t2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//tourism.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q3 = Label(self, text="3. What is the Indian state famous for boating activities on its backwaters? ",
                   font=("Baskerville Old Face", 32),
                   bg="light sky blue", fg="ivory")
        q3.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Kerala", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Karnataka", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Jammu and Kashmir", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Odisha", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t1))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t3))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right7
            right7 = right7 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class t3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//tourism.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q4 = Label(self, text="4. This World Heritage Site in India houses the holy remains of St. Xavier. Name it. ",
                   font=("Baskerville Old Face", 32),
                   bg="light sky blue", fg="ivory")
        q4.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="St.Francis Xavier Church, Cochin", font=("Lucida Calligraphy", 20),
                           bg="light sky blue",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Basilica of Bom Jesus, Goa", font=("Lucida Calligraphy", 20),
                           bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="St.Blaise Church, Mumbai", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="St.James Mar Thomas Church, Delhi", font=("Lucida Calligraphy", 20),
                           bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t2))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t4))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right7
            right7 = right7 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class t4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//tourism.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q5 = Label(self, text="5. Which is the tallest mountain in the Indian territory? ",
                   font=("Baskerville Old Face", 32),
                   bg="light sky blue", fg="ivory")
        q5.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Kanchenjunga", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Mount Godwin Austen(K2)", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Mount Everest", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Nanga Parbat", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t3))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t5))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right7
            right7 = right7 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class t5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//tourism.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q6a = Label(self, text="6. The southernmost point of the Indian mainland, Kanyakumari, ",
                    font=("Baskerville Old Face", 32),
                    bg="light sky blue", fg="ivory")
        q6a.place(x=0, y=0)
        q6b = Label(self, text="houses which center for meditation?", font=("Baskerville Old Face", 32),
                    bg="light sky blue", fg="ivory")
        q6b.place(x=0, y=60)

        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Vivekananda Rock", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=140)
        rad2 = Radiobutton(self, text="Netaji Yogic Institute", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=220)
        rad3 = Radiobutton(self, text="Gandhi Institute for Meditation", font=("Lucida Calligraphy", 20),
                           bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=300)
        rad4 = Radiobutton(self, text="Yogananda Memorial", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=380)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t4))
        bt1.place(x=0, y=460)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t6))
        bt2.place(x=500, y=460)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right7
            right7 = right7 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class t6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//tourism.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q7 = Label(self, text="7. Where is the largest museum in India located? ", font=("Baskerville Old Face", 32),
                   bg="light sky blue", fg="ivory")
        q7.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Kolkata", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Bangalore", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="New Delhi", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Mumbai", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t5))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t7))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 1:
            global right7
            right7 = right7 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class t7(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//tourism.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q8a = Label(self, text="8. What is the port town of India, where the Portuguese first reached ",
                    font=("Baskerville Old Face", 32),
                    bg="light sky blue", fg="ivory")
        q8a.place(x=0, y=0)
        q8b = Label(self, text="in search of an alternate trade route to India", font=("Baskerville Old Face", 32),
                    bg="light sky blue", fg="ivory")
        q8b.place(x=0, y=60)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Calcutta", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=140)
        rad2 = Radiobutton(self, text="Bombay", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=220)
        rad3 = Radiobutton(self, text="Madras", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=300)
        rad4 = Radiobutton(self, text="Calicut", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=380)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t6))
        bt1.place(x=0, y=460)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t8))
        bt2.place(x=500, y=460)

    def correct(self):
        if int(self.var1.get()) == 4:
            global right7
            right7 = right7 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class t8(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//tourism.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q9 = Label(self, text="9. Which city is known as the Silicon Valley of India? ",
                   font=("Baskerville Old Face", 32),
                   bg="light sky blue", fg="ivory")
        q9.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Hyderabad", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Bangalore", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Mumbai", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Chennai", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t7))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t9))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right7
            right7 = right7 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class t9(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//tourism.jpg")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        q10 = Label(self, text="10. The famous cricket stadium with the largest seating capacity in India is named "
                               "what? ", font=("Baskerville Old Face", 32),
                    bg="light sky blue", fg="ivory")
        q10.place(x=0, y=0)
        self.var1 = IntVar()
        rad1 = Radiobutton(self, text="Feroz Shah Kotla, Delhi", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black", variable=self.var1, value=1, command=self.correct)
        rad1.place(x=0, y=80)
        rad2 = Radiobutton(self, text="Eden Gardens, Kolkata", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=2, command=self.correct)
        rad2.place(x=0, y=160)
        rad3 = Radiobutton(self, text="Chepauk, Chennai", font=("Lucida Calligraphy", 20), bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=3, command=self.correct)
        rad3.place(x=0, y=240)
        rad4 = Radiobutton(self, text="Chinnaswamy Stadium, Bangalore", font=("Lucida Calligraphy", 20),
                           bg="light sky blue",
                           fg="black",
                           variable=self.var1, value=4, command=self.correct)
        rad4.place(x=0, y=320)

        bt1 = Button(self, text="BACK", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(t8))
        bt1.place(x=0, y=400)
        bt2 = Button(self, text="NEXT", font=("Baskerville Old Face", 20), bg="black", fg="white",
                     command=lambda: controller.show_frame(tourism_Results))
        bt2.place(x=500, y=400)

    def correct(self):
        if int(self.var1.get()) == 2:
            global right7
            right7 = right7 + 1

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ast_Results(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//quiz background.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.image2 = Image.open("Img//ast_answers.png")
        self.background_image2 = ImageTk.PhotoImage(self.image2)
        self.background2 = Label(self, image=self.background_image2)
        self.background2.place(x=400, y=200)

        self.text = IntVar()
        self.text.set("")
        label = Label(self, text='', textvariable=self.text, font=("Baskerville Old Face", 35), bg="black", fg="white")
        label.place(x=800, y=100)

        label1 = Label(self, text="SCOREBOARD", font=("Baskerville Old Face", 35), bg="black", fg="white")
        label1.place(x=600, y=0)
        l2 = Label(self, text="Marks:", font=("Baskerville Old Face", 35), bg="black", fg="white")
        l2.place(x=650, y=100)
        button = Button(self, text="Show marks", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                        command=lambda: [switch(button), self.total(), submit()])
        button.place(x=500, y=650)

        button1 = Button(self, text="Play Again", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                         command=lambda: controller.show_frame(Page2))
        button1.place(x=850, y=650)

        def switch(btn):
            btn["state"] = DISABLED

        def submit():
            marks = right
            cursor.execute("insert into participants(Name,Age,Marks) values('{}',{}, {});".format(name, age, marks))
            db.commit()

    def total(self):
        self.text.set(right)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class fp_Results(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//quiz background.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.image2 = Image.open("Img//fp_answers.png")
        self.background_image2 = ImageTk.PhotoImage(self.image2)
        self.background2 = Label(self, image=self.background_image2)
        self.background2.place(x=400, y=200)

        self.text = IntVar()
        self.text.set("")
        label = Label(self, text='', textvariable=self.text, font=("Baskerville Old Face", 35), bg="black", fg="white")
        label.place(x=800, y=100)

        label1 = Label(self, text="SCOREBOARD", font=("Baskerville Old Face", 35), bg="black", fg="white")
        label1.place(x=600, y=0)
        l2 = Label(self, text="Marks:", font=("Baskerville Old Face", 35), bg="black", fg="white")
        l2.place(x=650, y=100)
        button = Button(self, text="Show marks", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                        command=lambda: [switch(button), self.total(), submit()])
        button.place(x=500, y=650)

        button1 = Button(self, text="Play Again", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                         command=lambda: controller.show_frame(Page2))
        button1.place(x=850, y=650)

        def switch(btn):
            btn["state"] = DISABLED

        def submit():
            marks = right1
            cursor.execute("insert into participants(Name,Age,Marks) values('{}',{}, {});".format(name, age, marks))
            db.commit()

    def total(self):
        self.text.set(right1)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class math_Results(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//quiz background.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.image2 = Image.open("Img//math_answers.png")
        self.background_image2 = ImageTk.PhotoImage(self.image2)
        self.background2 = Label(self, image=self.background_image2)
        self.background2.place(x=400, y=200)

        self.text = IntVar()
        self.text.set("")
        label = Label(self, text='', textvariable=self.text, font=("Baskerville Old Face", 35), bg="black", fg="white")
        label.place(x=800, y=100)

        label1 = Label(self, text="SCOREBOARD", font=("Baskerville Old Face", 35), bg="black", fg="white")
        label1.place(x=600, y=0)
        l2 = Label(self, text="Marks:", font=("Baskerville Old Face", 35), bg="black", fg="white")
        l2.place(x=650, y=100)
        button = Button(self, text="Show marks", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                        command=lambda: [switch(button), self.total(), submit()])
        button.place(x=500, y=650)

        button1 = Button(self, text="Play Again", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                         command=lambda: controller.show_frame(Page2))
        button1.place(x=850, y=650)

        def switch(btn):
            btn["state"] = DISABLED

        def submit():
            marks = right2
            cursor.execute("insert into participants(Name,Age,Marks) values('{}',{}, {});".format(name, age, marks))
            db.commit()

    def total(self):
        self.text.set(right2)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class riddles_Results(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//quiz background.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.image2 = Image.open("Img//riddles_answers.png")
        self.background_image2 = ImageTk.PhotoImage(self.image2)
        self.background2 = Label(self, image=self.background_image2)
        self.background2.place(x=400, y=200)

        self.text = IntVar()
        self.text.set("")
        label = Label(self, text='', textvariable=self.text, font=("Baskerville Old Face", 35), bg="black", fg="white")
        label.place(x=800, y=100)

        label1 = Label(self, text="SCOREBOARD", font=("Baskerville Old Face", 35), bg="black", fg="white")
        label1.place(x=600, y=0)
        l2 = Label(self, text="Marks:", font=("Baskerville Old Face", 35), bg="black", fg="white")
        l2.place(x=650, y=100)
        button = Button(self, text="Show marks", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                        command=lambda: [switch(button), self.total(), submit()])
        button.place(x=500, y=650)

        button1 = Button(self, text="Play Again", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                         command=lambda: controller.show_frame(Page2))
        button1.place(x=850, y=650)

        def switch(btn):
            btn["state"] = DISABLED

        def submit():
            marks = right3
            cursor.execute("insert into participants(Name,Age,Marks) values('{}',{}, {});".format(name, age, marks))
            db.commit()

    def total(self):
        self.text.set(right3)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class lit_Results(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//quiz background.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.image2 = Image.open("Img//lit_answers.png")
        self.background_image2 = ImageTk.PhotoImage(self.image2)
        self.background2 = Label(self, image=self.background_image2)
        self.background2.place(x=400, y=200)

        self.text = IntVar()
        self.text.set("")
        label = Label(self, text='', textvariable=self.text, font=("Baskerville Old Face", 35), bg="black", fg="white")
        label.place(x=800, y=100)

        label1 = Label(self, text="SCOREBOARD", font=("Baskerville Old Face", 35), bg="black", fg="white")
        label1.place(x=600, y=0)
        l2 = Label(self, text="Marks:", font=("Baskerville Old Face", 35), bg="black", fg="white")
        l2.place(x=650, y=100)
        button = Button(self, text="Show marks", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                        command=lambda: [switch(button), self.total(), submit()])
        button.place(x=500, y=650)

        button1 = Button(self, text="Play Again", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                         command=lambda: controller.show_frame(Page2))
        button1.place(x=850, y=650)

        def switch(btn):
            btn["state"] = DISABLED

        def submit():
            marks = right5
            cursor.execute("insert into participants(Name,Age,Marks) values('{}',{}, {});".format(name, age, marks))
            db.commit()

    def total(self):
        self.text.set(right5)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class ca_Results(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//quiz background.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.image2 = Image.open("Img//ca_answers.png")
        self.background_image2 = ImageTk.PhotoImage(self.image2)
        self.background2 = Label(self, image=self.background_image2)
        self.background2.place(x=400, y=200)

        self.text = IntVar()
        self.text.set("")
        label = Label(self, text='', textvariable=self.text, font=("Baskerville Old Face", 35), bg="black", fg="white")
        label.place(x=800, y=100)

        label1 = Label(self, text="SCOREBOARD", font=("Baskerville Old Face", 35), bg="black", fg="white")
        label1.place(x=600, y=0)
        l2 = Label(self, text="Marks:", font=("Baskerville Old Face", 35), bg="black", fg="white")
        l2.place(x=650, y=100)
        button = Button(self, text="Show marks", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                        command=lambda: [switch(button), self.total(), submit()])
        button.place(x=500, y=650)

        button1 = Button(self, text="Play Again", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                         command=lambda: controller.show_frame(Page2))
        button1.place(x=850, y=650)

        def switch(btn):
            btn["state"] = DISABLED

        def submit():
            marks = right4
            cursor.execute("insert into participants(Name,Age,Marks) values('{}',{}, {});".format(name, age, marks))
            db.commit()

    def total(self):
        self.text.set(right4)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class sports_Results(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//quiz background.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.image2 = Image.open("Img//sports_answers.png")
        self.background_image2 = ImageTk.PhotoImage(self.image2)
        self.background2 = Label(self, image=self.background_image2)
        self.background2.place(x=400, y=200)

        self.text = IntVar()
        self.text.set("")
        label = Label(self, text='', textvariable=self.text, font=("Baskerville Old Face", 35), bg="black", fg="white")
        label.place(x=800, y=100)

        label1 = Label(self, text="SCOREBOARD", font=("Baskerville Old Face", 35), bg="black", fg="white")
        label1.place(x=600, y=0)
        l2 = Label(self, text="Marks:", font=("Baskerville Old Face", 35), bg="black", fg="white")
        l2.place(x=650, y=100)
        button = Button(self, text="Show marks", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                        command=lambda: [switch(button), self.total(), submit()])
        button.place(x=500, y=650)

        button1 = Button(self, text="Play Again", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                         command=lambda: controller.show_frame(Page2))
        button1.place(x=850, y=650)

        def switch(btn):
            btn["state"] = DISABLED

        def submit():
            marks = right6
            cursor.execute("insert into participants(Name,Age,Marks) values('{}',{}, {});".format(name, age, marks))
            db.commit()

    def total(self):
        self.text.set(right6)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


class tourism_Results(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.image = Image.open("Img//quiz background.png")
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        self.image2 = Image.open("Img//tourism_answers.png")
        self.background_image2 = ImageTk.PhotoImage(self.image2)
        self.background2 = Label(self, image=self.background_image2)
        self.background2.place(x=400, y=200)

        self.text = IntVar()
        self.text.set("")
        label = Label(self, text='', textvariable=self.text, font=("Baskerville Old Face", 35), bg="black", fg="white")
        label.place(x=800, y=100)

        label1 = Label(self, text="SCOREBOARD", font=("Baskerville Old Face", 35), bg="black", fg="white")
        label1.place(x=600, y=0)
        l2 = Label(self, text="Marks:", font=("Baskerville Old Face", 35), bg="black", fg="white")
        l2.place(x=650, y=100)
        button = Button(self, text="Show marks", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                        command=lambda: [switch(button), self.total(), submit()])
        button.place(x=500, y=650)

        button1 = Button(self, text="Play Again", font=("Lucida Calligraphy", 20), bg="black", fg="ivory",
                         command=lambda: controller.show_frame(Page2))
        button1.place(x=850, y=650)

        def switch(btn):
            btn["state"] = DISABLED

        def submit():
            marks = right7
            cursor.execute("insert into participants(Name,Age,Marks) values('{}',{}, {});".format(name, age, marks))
            db.commit()

    def total(self):
        self.text.set(right7)

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


# Driver Code


app = QuizApp()
app.mainloop()
