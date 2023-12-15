import tkinter
from tkinter import *
import random
from PIL import Image, ImageTk
import os
import pygame
import webbrowser



def delete3():
  root4.destroy()

def delete2():
  root3.destroy()

def delete4():
  root5.destroy()

def saved ():
  root10 = Toplevel(root)
  root10.title = ("Info")
  root10.geometry("100x100")
  Label(root10, text="Saved succesful").pack()

def save():
  filename= raw_filename.get()
  notes = raw_notes.get()
  data = open(filename, "w")
  data.write(notes)
  data.close()

  saved()

def create_notes():
  global raw_filename
  raw_filename = StringVar()
  global raw_notes
  raw_notes = StringVar()

  root9 = Toplevel(root)
  root9.title = ("Info")
  root9.geometry("300x250")
  Label(root9, text = "Please enter a filename where you want to store the question").pack()
  Entry(root9, textvariable = raw_filename).pack()
  Label(root9, text="Please enter the question that you want to add:").pack()
  Entry(root9, textvariable=raw_notes).pack()
  Button(root9, text="save", command = save).pack()

def view_notes1():
    filename1 = raw_filename1.get()
    data = open(filename1, "r")
    data1 = data.read()
    root12 = Toplevel(root)
    root12.title = ("Notes")
    root12.geometry("400x400")
    Label(root12, text=data1).pack()

def view_notes():
    root11 = Toplevel(root)
    root11.title = ("Info")
    root11.geometry("250x250")
    all_files = os.listdir()
    Label(root11, text="Please use one the filename below").pack()
    Label(root11, text = all_files).pack()
    global raw_filename1
    raw_filename1= StringVar()
    Entry(root11, textvariable = raw_filename1).pack()
    Button(root11, command = view_notes1, text = "OK").pack()

def delete_note1():
    filename3 = raw_filename2.get()
    os.remove(filename3)
    root14 = Toplevel(root)
    root14.title = ("Notes")
    root14.geometry("400x400")
    Label(root14, text=filename3+" removed").pack()

def delete_notes():
    root13 = Toplevel(root)
    root13.title = ("Info")
    root13.geometry("250x250")
    all_files = os.listdir()
    Label(root13, text="Please type the file you want to delete").pack()
    Label(root13, text=all_files).pack()
    global raw_filename2
    raw_filename2 = StringVar()
    Entry(root13, textvariable=raw_filename2).pack()
    Button(root13, command=delete_note1, text="OK").pack()

def session():
  root8=Toplevel(root)
  root8.title=("Dashboard")
  root8.geometry("400x400")
  Label(root8,text = "Welcome to the dashboard").pack()
  Button(root8, text="Add  question",command = create_notes).pack()
  Button(root8, text="View question", command = view_notes).pack()
  Button(root8, text="Delete question", command = delete_notes).pack()

def login_sucess():
  #session()
  global root3
  root3 = Toplevel(root)
  root3.title=("Success")
  root3.geometry("250x250")
  Label (root3,text= "Log in success").pack()
  Button(root3,text="Procced", command = session).pack()

def password_not_recgonised():
  global root4
  root4 = Toplevel(root)
  root4.title = ("Success")
  root4.geometry("150x100")
  Label(root4, text="Password Error").pack()
  Button(root4, text="OK", command=delete3).pack()

def user_not_found():
  global root5
  root5 = Toplevel(root)
  root5.title = ("Success")
  root5.geometry("150x100")
  Label(root5, text="User not Found").pack()
  Button(root5, text="OK", command=delete4).pack()

def register_user():
  username_info = username.get()
  password_info = password.get()

  file = open(username_info,"w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()

  username_entry.delete(0,END)
  password_entry.delete(0,END)

  Label(root1,text = "Registration Success", fg = "green", font = ("Calibri",11)).pack()

def login_verify():
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)


  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1,"r")
    verify = file1.read().splitlines()
    if password1 in verify:
      login_sucess()
    else:
      password_not_recgonised()
  else:
      user_not_found()

def register():
  global root1
  root1=Toplevel(root)
  root1.title("Register ")
  root1.geometry("300x250")

  global username
  global password
  global username_entry
  global password_entry

  username = StringVar()
  password = StringVar()

  Label(root1, text="Please enter details below").pack()
  Label(root1, text="").pack()
  Label(root1, text="Username *").pack()
  username_entry = Entry(root1,textvariable = username)
  username_entry.pack()
  Label(root1,text="Password *").pack()
  password_entry = Entry(root1,textvariable = password)
  password_entry.pack()
  Label(root1, text="").pack()
  Button(root1, text="Register", width = 10, height = 1, command = register_user).pack()

def login():
  global root2
  root2=Toplevel(root)
  root2.title("Login")
  root2.geometry("300x250")
  Label(root2, text="Please enter details below to login").pack()
  Label(root2, text="").pack()

  global username_verify
  global password_verify
  username_verify = StringVar()
  password_verify = StringVar()

  global username_entry1
  global password_entry1

  Label(root2, text="Username *").pack()
  username_entry1=Entry(root2, textvariable=username_verify)
  username_entry1.pack()
  Label(root2, text="").pack()
  Label(root2, text="Password *").pack()
  password_entry1 = Entry(root2, textvariable=password_verify)
  password_entry1.pack()
  Label(root2, text="").pack()
  Button(root2, text = "Login",width=10,height=1,command=login_verify).pack()



#-----------------------------------------------------------------------------------------------

questions_22 = [
    "The Pilgrims left England seeking religious freedom. ",
    "Nazis were socialists.",
    "Cowboys worked the plains alone.",
    "USSR dictator Joseph Stalin is responsible for more deaths than Adolf Hitler.",
    "A woman established the first-ever birth control clinic.",
    "In 1775, Paul Revere took a long ride yelling to warn people that the British army was coming.",
    "Vlad the Impaler inspired Bram Stoker's Dracula.",
    "The Emancipation Proclamation freed all the southern slaves.",
    "Cleopatra was the last Pharaoh of Egypt.",
    "Doctors used to not give women painkillers during birth.",
    "Vikings wore horned helmets.",
    "The Mongol Empire was the largest continuous land empire ever.",
    "George Washington was the only US president to not belong to any political party.",
    "Julius Caesar was the first baby to be delivered via C-section.",
    "Napoleon Bonaparte was short.",
    "Benjamin Franklin invented bifocals.",
    "Gjergj Kastrioti Skënderbeu, known as Skanderbeg, was an old Albanian president",

]

answer_choice_22 = [
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
    ["TRUE", "FALSE", ],
]

answer2_22 = [1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, ]

user_answer_22 = []

indexe_22 = []

def gen_22():
    global indexe_22
    while (len(indexe_22) < 16):  # nr of questions_22
        y = random.randint(0, 15)  # form to
        if y in indexe_22:
            continue
        else:
            indexe_22.append(y)

def showresult_22(score_22):
    lblQuestion_22.destroy()
    r1_22.destroy()
    r2_22.destroy()

    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score_22 >= 12:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice1)
        buttonclaim.pack(pady=5)
    elif (score_22 >= 6 and score_22 < 12):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice1)
        buttonclaim.pack(pady=5)
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a worst Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice)
        buttonclaim.pack(pady=5)

def calc_22():
    global indexe_22, user_answer_22, answer2_22
    y = 0
    score_22 = 0
    for i in indexe_22:
        if user_answer_22[y] == answer2_22[i]:
            score_22 = score_22 + 1
        y += 1
    print(score_22)
    showresult_22(score_22)

ques2 = 1

def selected_22():
    global radiovar_22, user_answer_22
    global lblQuestion_22, r1_22, r2_22
    global ques2
    y = radiovar_22.get()
    user_answer_22.append(y)
    radiovar_22.set(-1)
    # print(y)
    if ques2 < 16:  # nr of questions_22
        lblQuestion_22.config(text=questions_22[indexe_22[ques2]])
        r1_22['text'] = answer_choice_22[indexe_22[ques2]][0]
        r2_22['text'] = answer_choice_22[indexe_22[ques2]][1]
        ques2 += 1
    else:
        calc_22()

def startQuiz_22():
    global lblQuestion_22, r1_22, r2_22, r3, r4
    lblQuestion_22 = Label(
        root,
        text=questions_22[indexe_22[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion_22.pack(pady=(100, 30))

    global radiovar_22
    radiovar_22 = IntVar()
    radiovar_22.set(-1)

    r1_22 = Radiobutton(
        root,
        text=answer_choice_22[indexe_22[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar_22,
        command=selected_22,
        background="#ffffff",
    )
    r1_22.pack(pady=5)

    r2_22 = Radiobutton(
        root,
        text=answer_choice_22[indexe_22[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar_22,
        command=selected_22,
        background="#ffffff",
    )
    r2_22.pack(pady=5)

def lvl2history():
    lvl1buton.destroy()
    lvl2buton.destroy()
    lvl3buton.destroy()
    backbutton1.destroy()
    gen_22()
    startQuiz_22()

#-----------------------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------------------
questions = [
    "In America, slavery was only ever in the southern states. ",
    " Over the course of history, roughly 600,000 people were put to death for being witches.",
    "Early feminists were mostly concerned with sexual liberation.",
    "Due to China's one-child policy, many little girls were abandoned every year",
    "America has always operated as a democracy.",
    "The Salem Witch Trials caused by hallucinogenic fungus infecting the people of Salem.",
    "English was the first European language spoken in America.",
    "Dentures used to be made with human teeth.",
    "Christopher Columbus discovered America.",
    "Our founding fathers signed the Declaration of Independence on July 4, 1776.",
    "The Aztecs made human sacrifices.",
    "Stonehenge was used as a cemetery.",
    "The Great Chicago Fire was started when a cow knocked over a lantern.",
    "America was the first country to develop nuclear weapons.   ",
    "The radio broadcast of H.G. Wells  War of the Worlds caused mass hysteria all over America.",
    "For decades, the Australian government took Aboriginal children from their parents.",
]

answers_choice = [
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
    ["TRUE", "FALSE",],
]

answers = [ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0,]

user_answer = []

indexes = []

def gen():
    global indexes
    while (len(indexes) < 16):  # nr of questions
        x = random.randint(0, 15) #form to
        if x in indexes:
            continue
        else:
            indexes.append(x)
    # print(indexes)

def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    #r3.destroy()
    #r4.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score >= 12:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice1)
        buttonclaim.pack(pady=5)
    elif (score >= 6 and score < 12):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice)
        buttonclaim.pack(pady=5)
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a worst Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice)
        buttonclaim.pack(pady=5)

def calc():
    global indexes, user_answer, answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 1
        x += 1
    print(score)
    showresult(score)

ques = 1

def selected():
    global radiovar, user_answer
    global lblQuestion, r1, r2 #r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    # print(x)
    if ques < 16:  # nr of questions
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        #r3['text'] = answers_choice[indexes[ques]][2]
        #r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        calc()

def startQuiz():
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        root,
        text=questions[indexes[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=5)
"""
    r3 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Times", 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Times", 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r4.pack(pady=5)
"""

def lvl3history():
    #labelimage.destroy()
    #labeltext.destroy()
    #lblInstruciton.destroy()
    #lblRules.destroy()
    #btnStart.destroy()
    #my_canvas.destroy()
    lvl1buton.destroy()
    lvl2buton.destroy()
    lvl3buton.destroy()
    backbutton1.destroy()
    gen()
    startQuiz()

#-----------------------------------------------------------------------------------------------------------------






#---------------------------------------------------------------------------------------------------------------

questions11 = [
    "(13 + 7) x (5 - 3) / 4 x (1 + 1) = Which operation would the young mathematician do first?",
    "One of the most basic properties of math is demonstrated here. What is it called?   2 + 3 = 3 + 2",
    "The student is taught another property of mathematic operations. Which property is it? (5 + 2) + 7 = 5 + (2 + 7)",
    "Which mathematical property is demonstrated below?   3 + 0 = 3",
    "Which property of math is the student learning with the following equation? 3 x (4 + 7) = (3 x 4) + (3 x 7)",
    "What is the correct order of operation for the following equation, written as such?     5 + 2 x 8 / 4 - 3 =",
    "Which of the following DOES NOT indicate multiplication of the number 4 and the variable, 'Y'?",
    "When multiplying two negative numbers, what kind of number does one always get for an answer?",
    "Generally speaking, dividing some non-zero number by zero yields what result?",
    "How many digits are in the number 1002004?",
    "What is 109,786,865 rounded to the nearest ten million?",
    "Write Two hundred one million, five hundred six thousand, twelve in standard form.",
    "Order from least to greatest the numbers   0.99, 0.099 , 9.9 , 0.9.",
    "Round 312.92 to the nearest whole number.",
    "Which one of these numbers rounds to 100,000?",
    "How is 23,456 rounded to obtain 23,500?",
    "If you switch the positions of the digits 3 and 5 in the number 3256, which statement is correct?",
]

answer_choice11 = [
    ["The division", "Those inside parentheses","The multiplication", "The subtraction",],
    ["Identity Property", "Mirror Property","Commutative Property", "Associative Property",],
    ["Commutative Property", "Additive Property"," Identity Property", "Associative Property",],
    ["Indemnify Property", "Idiocy Property","Idolatry Property", "Identity Property",],
    ["Cross-multiplicative Property", "Distributive Property","Numerative Property", "Denominative Property",],
    ["+, *, /, *", "*, /, +, -", "/, -, +, *", "-, /, *, +",],
    ["4(Y)", "4Y","4 x Y", "4%Y",],
    [" Negative number", "Zero","Depends on the numbers", "Positive number",],
    ["Zero", "Undefined or infinity","The original non-zero number", "The original non-zero number times two",],
    ["3", "5","6", "7",],
    ["110,000,000", "100,000,000","111,000,000", "109,770,000",],
    ["210,560,012", "201,560,120","201,506,012", "201,506,120",],
    ["0.99, 0.099, 9.9, 0.9", "0.99, 9.9, 0.099, 0.9","9.9, 0.9, 0.99, 0.099", "9.9, 0.99, 0.9, 0.099",],
    ["313", "312","312.9", "300",],
    ["99,999", "94,789","150,000", "90,000",],
    ["to the nearest ten", "to the nearest hundred","to the nearest thousand", "to the nearest ten thousand",],
    ["the number does not change", "the number increases","the number decreases", "the number has more digits",],
]

answer_11 = [1, 2, 3, 3, 1, 1, 3, 3, 1, 3,  0, 2, 3, 0, 0, 1, 1,]

user_answer_11 = []

indexe11 = []

def gen11():
    global indexe11
    while (len(indexe11) < 16):  # nr of questions11
        x11 = random.randint(0, 16) #form to
        if x11 in indexe11:
            continue
        else:
            indexe11.append(x11)

def showresult_11(score_11):
    lblQuestion_11.destroy()
    r1_11.destroy()
    r2_11.destroy()
    r3_11.destroy()
    r4_11.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score_11 >= 12:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice)
        buttonclaim.pack(pady=5)
    elif (score_11 >= 6 and score_11 < 12):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice)
        buttonclaim.pack(pady=5)
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a worst Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice)
        buttonclaim.pack(pady=5)

def calc_11():
    global indexe11, user_answer_11, answer_11
    x11 = 0
    score_11 = 0
    for i in indexe11:
        if user_answer_11[x11] == answer_11[i]:
            score_11 = score_11 + 1
        x11 += 1
    print(score_11)
    showresult_11(score_11)

ques_11 = 1

def selected_11():
    global radiovar_11, user_answer_11
    global lblQuestion_11, r1_11, r2_11 ,r3_11, r4_11
    global ques_11
    x11 = radiovar_11.get()
    user_answer_11.append(x11)
    radiovar_11.set(-1)

    if ques_11 < 16:  # nr of questions11
        lblQuestion_11.config(text=questions11[indexe11[ques_11]])
        r1_11['text'] = answer_choice11[indexe11[ques_11]][0]
        r2_11['text'] = answer_choice11[indexe11[ques_11]][1]
        r3_11['text'] = answer_choice11[indexe11[ques_11]][2]
        r4_11['text'] = answer_choice11[indexe11[ques_11]][3]
        ques_11 += 1
    else:
        calc_11()

def startQuiz_11():
    global lblQuestion_11, r1_11, r2_11, r3_11, r4_11
    lblQuestion_11 = Label(
        root,
        text=questions11[indexe11[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion_11.pack(pady=(100, 30))

    global radiovar_11
    radiovar_11 = IntVar()
    radiovar_11.set(-1)

    r1_11 = Radiobutton(
        root,
        text=answer_choice11[indexe11[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar_11,
        command=selected_11,
        background="#ffffff",
    )
    r1_11.pack(pady=5)

    r2_11 = Radiobutton(
        root,
        text=answer_choice11[indexe11[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar_11,
        command=selected_11,
        background="#ffffff",
    )
    r2_11.pack(pady=5)

    r3_11 = Radiobutton(
        root,
        text=answer_choice11[indexe11[0]][2],
        font=("Times", 12),
        value=2,
        variable=radiovar_11,
        command=selected_11,
        background="#ffffff",
    )
    r3_11.pack(pady=5)

    r4_11 = Radiobutton(
        root,
        text=answer_choice11[indexe11[0]][3],
        font=("Times", 12),
        value=3,
        variable=radiovar_11,
        command=selected_11,
        background="#ffffff",
    )
    r4_11.pack(pady=5)

def lvl1math():
    lvl1buton.destroy()
    lvl2buton.destroy()
    lvl3buton.destroy()
    backbutton1.destroy()
    gen11()
    startQuiz_11()

#----------------------------------------------------------------------------------------------------------------




#---------------------------------------------------------------------------------------------------------------

questions12 = [
    "What percent of a circle is 75 degrees?",
    "Which expression represents the use of the distributive property on 3(a + b)?",
    "What is the greatest common factor of 9x, 3y, and 12z?",
    "What value of x makes '-6x = -42' a true statement?",
    "What is the slope of y = -4x + 1?",
    "What value of x makes 4x - 2 = 2(x + 1) a true statement?",
    "What is the square root of 28 in simplified form?",
    "What is the solution of 4x - 7(x - 1) > 3(x + 1)?",
    "What value of x makes '2x + 3 = 15' a true statement?",
    "What kind of slope does the line 3x - 2y = 6 have?",
    "What kind of slope does the line '3x + 2y = 6' have?",
    "If x = 4, what is 3^x (3 to the power of x)?",
    "What kind of slope does y = 4 have?",
    "What is the y-intercept of 4x + 2y = -8?",
    "What is the midpoint of the line segment with endpoints at (-1, 1) and (7, -3)?",
    "What are the x- and y-intercepts for the equation '2x + 3y = 6'?",
    "What is (3x + 4) (2x + 3)?",
    "What is the sin of 225 degrees (to 4 decimal places)?",
    "What is the sine of 45 degrees?",
    "What is the slope of the line connecting (0, 0) and (3, 4)?",
]

answer_choice12 = [
    ["75%", "20.83%", "15%", "25%",],
    ["a + 3b", "3a + b", "3a + 3b", "3ab", ],
    ["3x", "3", "3y", "xyz", ],
    ["-7", "-6", "6", "7", ],
    ["1", "-4", "4", "-1", ],
    ["-2", "1", "2", "0", ],
    ["Square Root 14", "2 Times the Square Root of 7", "7 Times the Square Root of 2", "Square Root 9", ],
    ["X > -2/3", "X > 2/3", "X < -2/3", "X < 2/3", ],
    ["-9", "-6", "6", "9", ],
    ["Zero(0)", "Undefined", "Positive", "Negative", ],
    ["Negative", "Zero(0)", "Undefined", "Positive", ],
    ["81", "64", "27", "243", ],
    ["Undefined", "Negative", "Zero(0)", "Positive", ],
    ["(-2, 0)", "(2, 0)", "(0, -4)", "(0, 4)", ],
    ["(3, -1)", "(6,3)", " (5,1)", "(1, -3)", ],
    ["(0, 2) & (3, 0)", "(0,3) & (2,0)", "(0,3) & (0,2)", "(2,0) & (3,0)", ],
    ["6x^2 - 17x + 12", "6x^2 + x + 12", "6x^2 - x + 12", "6x^2 + 17x + 12", ],
    ["-0.7071", "0", "1", "0.7071", ],
    ["0.7071", "1", "-0.7071", "0", ],
    ["8", "-1.333333", "-0.75", "1.33333333", ],
]

answer_12 = [1, 2, 1, 3, 1, 2, 1, 3, 2, 2, 0, 0, 2, 2, 0, 0, 3, 0, 0, 3,]

user_answer_12 = []

indexe12 = []

def gen12():
    global indexe12
    while (len(indexe12) < 16):  # nr of questions12
        x12 = random.randint(0, 19) #form to
        if x12 in indexe12:
            continue
        else:
            indexe12.append(x12)

def showresult_12(score_12):
    lblQuestion_12.destroy()
    r1_12.destroy()
    r2_12.destroy()
    r3_12.destroy()
    r4_12.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score_12 >= 12:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice1)
        buttonclaim.pack(pady=5)
    elif (score_12 >= 6 and score_12 < 12):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice1)
        buttonclaim.pack(pady=5)
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a worst Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice1)
        buttonclaim.pack(pady=5)

def calc_12():
    global indexe12, user_answer_12, answer_12
    x12 = 0
    score_12 = 0
    for i in indexe12:
        if user_answer_12[x12] == answer_12[i]:
            score_12 = score_12 + 1
        x12 += 1
    print(score_12)
    showresult_12(score_12)

ques_12 = 1

def selected_12():
    global radiovar_12, user_answer_12
    global lblQuestion_12, r1_12, r2_12 ,r3_12, r4_12
    global ques_12
    x12 = radiovar_12.get()
    user_answer_12.append(x12)
    radiovar_12.set(-1)

    if ques_12 < 16:  # nr of questions12
        lblQuestion_12.config(text=questions12[indexe12[ques_12]])
        r1_12['text'] = answer_choice12[indexe12[ques_12]][0]
        r2_12['text'] = answer_choice12[indexe12[ques_12]][1]
        r3_12['text'] = answer_choice12[indexe12[ques_12]][2]
        r4_12['text'] = answer_choice12[indexe12[ques_12]][3]
        ques_12 += 1
    else:
        calc_12()

def startQuiz_12():
    global lblQuestion_12, r1_12, r2_12, r3_12, r4_12
    lblQuestion_12 = Label(
        root,
        text=questions12[indexe12[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion_12.pack(pady=(100, 30))

    global radiovar_12
    radiovar_12 = IntVar()
    radiovar_12.set(-1)

    r1_12 = Radiobutton(
        root,
        text=answer_choice12[indexe12[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar_12,
        command=selected_12,
        background="#ffffff",
    )
    r1_12.pack(pady=5)

    r2_12 = Radiobutton(
        root,
        text=answer_choice12[indexe12[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar_12,
        command=selected_12,
        background="#ffffff",
    )
    r2_12.pack(pady=5)

    r3_12 = Radiobutton(
        root,
        text=answer_choice12[indexe12[0]][2],
        font=("Times", 12),
        value=2,
        variable=radiovar_12,
        command=selected_12,
        background="#ffffff",
    )
    r3_12.pack(pady=5)

    r4_12 = Radiobutton(
        root,
        text=answer_choice12[indexe12[0]][3],
        font=("Times", 12),
        value=3,
        variable=radiovar_12,
        command=selected_12,
        background="#ffffff",
    )
    r4_12.pack(pady=5)

def lvl2math():
    lvl1buton.destroy()
    lvl2buton.destroy()
    lvl3buton.destroy()
    backbutton1.destroy()
    gen12()
    startQuiz_12()
#-----------------------------------------------------------------------------------------------------------------




#---------------------------------------------------------------------------------------------------------------


questions13 = [
    "If Logx (1 / 8) = - 3 / 2, then x is equal to",
    "20 % of 2 is equal to",
    "If Log 4 (x) = 12, then log 2",
    "f is a quadratic function whose graph is a parabola opening upward and has a vertex on the x-axis. "
    "The graph of the new function g defined by g(x) = 2 - f(x - 5) has a range defined by the interval",
    "f is a function such that f(x) < 0. The graph of the new function g defined by g(x) = | f(x) | "
    "is a reflection of the graph of ",
    "If the graph of y = f(x) is transformed into the graph of 2y - 6 = - 4 f(x - 3), point (a , b) on the graph "
    "of y = f(x) becomes point (A , B) on the graph of 2y - 6 = - 4 f(x - 3) where A and B are given by",
    "When a parabola represented by the equation y - 2x 2 = 8 x + 5 is translated 3 units to the left "
    "and 2 units up, the new parabola has its vertex at",
    "The graphs of the two linear equations a x + b y = c and b x - a y = c, "
    "where none of the coefficients a, b, c is equal to zero,",
    "The graphs of the two equations y = a x 2 + b x + c and y = A x 2 + B x + C, such that a and A have "
    "different signs and that the quantities b 2 - 4 a c and B 2 - 4 A C are both negative,",
    "-) For x greater than or equal to zero and less than or equal to 2 π, "
    "sin x and cos x are both decreasing on the intervals",
    "The three solutions of the equation f(x) = 0 are -2, 0, and 3. Therefore, "
    "the three solutions of the equation f(x - 2) = 0 are",
    "The three solutions of the equation f(x) = 0 are - 4, 8, and 11. "
    "Therefore, the three solutions of the equation f(2 x) = 0 are",
    "A school committee consists of 2 teachers and 4 students. The number of different committees that "
    "can be formed from 5 teachers and 10 students is",
    "Five different books (A, B, C, D and E) are to be arranged on a shelf."
    " Books C and D are to be arranged first and second starting from the right of the shelf. "
    "The number of different orders in which books A, B and E may be arranged is",
    "The mean of a data set is equal to 10 and its standard deviation is equal to 1. "
    "If we add 5 to each data value, then the mean and standard deviation become",
    "The exam scores of all 500 students were recorded and it was determined that scores were normally distributed. "
    "If Jane's score is 0.8 standard deviation above the mean, "
    "then how many, to the nearest unit, students scored above Jane?",
    "If f(x) is an odd function, then | f(x) | is",
    "The period of | sin (3x) | is",
    "When a metallic ball bearing is placed inside a cylindrical container, of radius 2 cm, the height of the water, "
    "inside the container, increases by 0.6 cm. The radius, to the nearest tenth of a centimeter, of the ball bearing:",

]

answer_choice13 = [
    ["-4", "4", "1/4", "10",],
    ["20", "4", "0.4", "0.04", ],
    ["11", "48", "12", "22", ],
    ["[ -5, + infinity)", "[ 2, + infinity)", "(- infinity, 2]", "(- infinity, 0]", ],
    ["on the y axis", " on the x axix", "on the line y = x", "on the line y = - x", ],
    ["A = a - 3, B = b", "A = a - 3, B = b", "A = a + 3, B = -2 b", "A = a + 3, B = -2 b +3", ],
    ["(-5, -1)", "(-5, -5)", "(-1, -3)", "(-2, -3)", ],
    ["are parallel", "intersect at the point (0,0)", "intersect at two points", "perpendicular", ],
    ["intersect at two points", "intersect at one point", "do not intersect", "none of the above", ],
    ["(0, π/2)", "(π/2, π)", "(π , 3 π / 2)", "(3 π / 2 , 2 π)", ],
    ["- 4, -2, and 1", "-2, 0 and 3", "4, 2, and 5", "0, 2 and 5", ],
    ["- 2, 4, and 11/2", "- 8, 16 and 22", "- 4, 8, and 11", "2, 19 / 2 and 7 / 2", ],
    ["10", "15", "2100", "8", ],
    ["5!", "3!", "2!", "3!*2!", ],
    ["mean = 15, standard deviation = 6", "mean = 10, standard deviation = 6", "mean = 15, standard deviation = 1",
     "mean = 10, standard deviation = 1", ],
    ["394", "250", "400", "106", ],
    ["an odd function", "an even function", "neither odd nor even", "even and odd", ],
    ["2 π", "2 π / 3", "π / 3", "3 π", ],
    ["1 cm", "1.2 cm", "2 cm", "0.6 cm", ],
]

answer_13 = [ 1, 2, 3, 2, 1, 3, 0, 3, 2, 1, 3, 0, 2, 1, 2, 3, 1, 2, 1, ]

user_answer_13 = []

indexe13 = []

def gen13():
    global indexe13
    while (len(indexe13) < 16):  # nr of questions13
        x13 = random.randint(0, 18) #form to
        if x13 in indexe13:
            continue
        else:
            indexe13.append(x13)

def showresult_13(score_13):
    lblQuestion_13.destroy()
    r1_13.destroy()
    r2_13.destroy()
    r3_13.destroy()
    r4_13.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score_13 >= 12:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice)
        buttonclaim.pack(pady=5)
    elif (score_13 >= 6 and score_13 < 12):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice)
        buttonclaim.pack(pady=5)
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a worst Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command=claimprice)
        buttonclaim.pack(pady=5)

def calc_13():
    global indexe13, user_answer_13, answer_13
    x13 = 0
    score_13 = 0
    for i in indexe13:
        if user_answer_13[x13] == answer_13[i]:
            score_13 = score_13 + 1
        x13 += 1
    print(score_13)
    showresult_13(score_13)

ques_13 = 1

def selected_13():
    global radiovar_13, user_answer_13
    global lblQuestion_13, r1_13, r2_13 ,r3_13, r4_13
    global ques_13
    x13 = radiovar_13.get()
    user_answer_13.append(x13)
    radiovar_13.set(-1)

    if ques_13 < 16:  # nr of questions13
        lblQuestion_13.config(text=questions13[indexe13[ques_13]])
        r1_13['text'] = answer_choice13[indexe13[ques_13]][0]
        r2_13['text'] = answer_choice13[indexe13[ques_13]][1]
        r3_13['text'] = answer_choice13[indexe13[ques_13]][2]
        r4_13['text'] = answer_choice13[indexe13[ques_13]][3]
        ques_13 += 1
    else:
        calc_13()

def startQuiz_13():
    global lblQuestion_13, r1_13, r2_13, r3_13, r4_13
    lblQuestion_13 = Label(
        root,
        text=questions13[indexe13[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion_13.pack(pady=(100, 30))

    global radiovar_13
    radiovar_13 = IntVar()
    radiovar_13.set(-1)

    r1_13 = Radiobutton(
        root,
        text=answer_choice13[indexe13[0]][0],
        font=("Times", 13),
        value=0,
        variable=radiovar_13,
        command=selected_13,
        background="#ffffff",
    )
    r1_13.pack(pady=5)

    r2_13 = Radiobutton(
        root,
        text=answer_choice13[indexe13[0]][1],
        font=("Times", 13),
        value=1,
        variable=radiovar_13,
        command=selected_13,
        background="#ffffff",
    )
    r2_13.pack(pady=5)

    r3_13 = Radiobutton(
        root,
        text=answer_choice13[indexe13[0]][2],
        font=("Times", 13),
        value=2,
        variable=radiovar_13,
        command=selected_13,
        background="#ffffff",
    )
    r3_13.pack(pady=5)

    r4_13 = Radiobutton(
        root,
        text=answer_choice13[indexe13[0]][3],
        font=("Times", 13),
        value=3,
        variable=radiovar_13,
        command=selected_13,
        background="#ffffff",
    )
    r4_13.pack(pady=5)

def lvl3math():
    lvl1buton.destroy()
    lvl2buton.destroy()
    lvl3buton.destroy()
    backbutton1.destroy()
    gen13()
    startQuiz_13()
#---------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------

questions31 = [
    "Consider the following statements: A light year is the distance covered by light in one year ; "
    "The velocity of light is about 300,000 km/s.",
    "Ojos del Salado (6,893 m), the world’s highest volcano is located on ……",
    "Photochemical smog is the result of ……………",
    "Find the name of the river based on the following statements:It originates from the talus fan of the "
    "Shiwalik nearby Ambala (Haryana).This river disappears in the plains; however, it again appears in Karnal District"
    ".Choose the correct answer from the given codes:",
    "An earthquake is the shaking feature of the earth’s surface, which is caused by the sudden movement of a part "
    "of the earth’s plate/crust. Thousands of earthquakes occur every year, but most of them are small enough "
    "to get noticed. Select the correct answer from the given codes:",
    "Which one of the following states has the maximum area under the saline and alkaline soil?",
    "Mycorrhizal fungi acts as chemical fertilizer.    Mycorrhizal fungi protect plants from the disease. "
    " Select the correct answer from the given codes:",
    "In reference to Koeppen’s climate classification:The capital letter ‘A’ means",
    "Which one of the following is not a ‘vulture safe zone?’",
    "Which one of the following conferences discussed the issue of ‘Ozone Depletion?’",
    "Which one of the following countries has the maximum number of time zones?",
    "In which of the following year, the National Thermal Power Corporation (NTPC) was established?",
    "Which one of the following is popular as ‘Floating Islands Lake?’",
    "The basic coral reef classification scheme first described by ……",
    "In reference to Hydro-electric power plants, which one of the following pairs is incorrectly matched?",
    "Which one of the following countries is a leading Bauxite producer?",
    "River Sabarmati empties itself into:",
    "Buckingham Palace is located in ……………",
    "Which one of the following countries is a leading Cocoa (bean)producer?",
]

answer_choice31 = [
    ["Only 1", "Only 2", "Both", "Neither 1 nor 2",],
    ["Argentina – Chile border", "Chile – Peru border", "Canada – USA border", "France – Germany border", ],
    ["NO2, 03, ", "CO, S02 ", "CO, CO2 and N02 ", "High concentration of N02, SO2, and CO2 in the evening", ],
    ["Ghaggar", "Kali", "Beas", "Gomati", ],
    ["Only 1", "Only 2", "Both", "Neither 1 nor 2",],
    ["Gujarat", "Uttar Pradesh", "Rajasthan", "West Bengal", ],
    ["Only 1", "Only 2", "Both", "Neither 1 nor 2",],
    ["Tropical climate", "Warm climate", "Dry climate", "Cold climate", ],
    ["Gujarat", " Assam", "Uttarakhand", "Tamil Nadu", ],
    ["Bretton Woods Conference", "Kyoto Protocol", "Montreal Protocol", "Nagoya Protocol", ],
    ["USA", "Russia", "France", "Canada", ],
    ["1960", "1955", "1975", "1967", ],
    ["Nako Lake", "Loktak Lake", "Pangong Tso", "Khajjiar Lake", ],
    ["Charles Darwin", "Newton", "Matilene S. Berryman", "John A. Church", ],
    ["Machkund Project Andhra Pradesh", "Ukai Project Gujarat", "Baglihar Project Uttarakhand", "Panchet Project ", ],
    ["Australia", "China", "Brazil", "Guinea", ],
    ["Rann of Kutch", "Gulf of Khambhat", "Bay of Bengal", "Gulf of Mannar", ],
    ["Paris", "London", "Brussels", "Scotland", ],
    ["Ivory Coast", "Ghana", "Indonesia", "Nigeria", ],

]

answer_31 = [ 2, 0, 0, 0, 2, 1, 1, 0, 3, 2, 2, 2, 1, 0, 2, 0, 1, 1, 0, ]

user_answer_31 = []

indexe31 = []

def gen31():
    global indexe31
    while (len(indexe31) < 16):  # nr of questions31
        x31 = random.randint(0, 18) #form to
        if x31 in indexe31:
            continue
        else:
            indexe31.append(x31)

def showresult_31(score_31):
    lblQuestion_31.destroy()
    r1_31.destroy()
    r2_31.destroy()
    r3_31.destroy()
    r4_31.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score_31 >= 12:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0,command = claimprice1 )
        buttonclaim.pack(pady=5)
    elif (score_31 >= 6 and score_31 < 12):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0,command = claimprice1 )
        buttonclaim.pack(pady=5)
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a worst Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command = claimprice1 )
        buttonclaim.pack(pady=5)

def calc_31():
    global indexe31, user_answer_31, answer_31
    x31 = 0
    score_31 = 0
    for i in indexe31:
        if user_answer_31[x31] == answer_31[i]:
            score_31 = score_31 + 1
        x31 += 1
    print(score_31)
    showresult_31(score_31)

ques_31 = 1

def selected_31():
    global radiovar_13, user_answer_31
    global lblQuestion_31, r1_31, r2_31 ,r3_31, r4_31
    global ques_31
    x31 = radiovar_13.get()
    user_answer_31.append(x31)
    radiovar_13.set(-1)

    if ques_31 < 16:  # nr of questions31
        lblQuestion_31.config(text=questions31[indexe31[ques_31]])
        r1_31['text'] = answer_choice31[indexe31[ques_31]][0]
        r2_31['text'] = answer_choice31[indexe31[ques_31]][1]
        r3_31['text'] = answer_choice31[indexe31[ques_31]][2]
        r4_31['text'] = answer_choice31[indexe31[ques_31]][3]
        ques_31 += 1
    else:
        calc_31()

def startQuiz_31():
    global lblQuestion_31, r1_31, r2_31, r3_31, r4_31
    lblQuestion_31 = Label(
        root,
        text=questions31[indexe31[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion_31.pack(pady=(100, 30))

    global radiovar_13
    radiovar_13 = IntVar()
    radiovar_13.set(-1)

    r1_31 = Radiobutton(
        root,
        text=answer_choice31[indexe31[0]][0],
        font=("Times", 13),
        value=0,
        variable=radiovar_13,
        command=selected_31,
        background="#ffffff",
    )
    r1_31.pack(pady=5)

    r2_31 = Radiobutton(
        root,
        text=answer_choice31[indexe31[0]][1],
        font=("Times", 13),
        value=1,
        variable=radiovar_13,
        command=selected_31,
        background="#ffffff",
    )
    r2_31.pack(pady=5)

    r3_31 = Radiobutton(
        root,
        text=answer_choice31[indexe31[0]][2],
        font=("Times", 13),
        value=2,
        variable=radiovar_13,
        command=selected_31,
        background="#ffffff",
    )
    r3_31.pack(pady=5)

    r4_31 = Radiobutton(
        root,
        text=answer_choice31[indexe31[0]][3],
        font=("Times", 13),
        value=3,
        variable=radiovar_13,
        command=selected_31,
        background="#ffffff",
    )
    r4_31.pack(pady=5)

def lvl1geogrphy():
    lvl1buton.destroy()
    lvl2buton.destroy()
    lvl3buton.destroy()
    backbutton1.destroy()
    gen31()
    startQuiz_31()


#-------------------------------------------------------------------------------------------------------------------




#--------------------------------------------------------------------------------------------------------------

questions32 = [
    "Which of the following rocks formed from the existing rocks by undergoing the process of recrystallization?",
    "Where is the headquarters of the Tobacco Board?",
    "Which of the following is the world's longest estuary?",
    "Any moving object on earth finally comes to rest due to which among the following?",
    "Zebrafish, which has been genetically modified in Glofish to be sold as a pet, is native "
    "to which of the following countries?",
    "On June 21, the Sun is vertically overhead the following..?",
    "In which of the following River Jordan drains?",
    "Raja Ramanna Centre for Advanced Technology (RRCAT), which is engaged in development of technology and "
    "applications of particle accelerators and lasers, besides carrying out substantial activities in "
    "cryogenics and materials research is located at",
    "The Straits Times belongs to which of the following countries?",
    "Which among the following is true regarding Sound Waves?",
    "In which of the following countries is the majority of the population is Sunni Muslims?",
    "Which among the following is the world's largest freshwater lake? ",
    "The International Space Station is located in which of the following orbits?",
    "Which of the following archipelago is designated as a Ramsar site?",
    "What is the term used for countries that consist of an archipelago?",
    "Which coral reef system comprises a big field of sand mounds?",
    "Most of the world’s oil comes from which of the following gulf?",
    "Rama Setu or Rama Bridge is located in which gulf?",
    "Which of the following is the smallest gulf in the world?",
    "Which is the largest glacier in the world?",

]

answer_choice32 = [
    ["Igneous rocks", "Metamorphic rocks", "Sedimentary rocks", "None of the above",],
    ["Secunderabad", "Guntur", "Belgaum", "Gadag", ],
    ["Orange River Estuary", "Great Bay", "Gulf of Ob", "San Francisco Bay", ],
    ["Gravity", "Friction", "Inertia", " Motion", ],
    ["India and Sri Lanka", "Australia & New Zealand", "India and Pakistan", "Japan", ],
    ["Tropic of Cancer", "Tropic of Capricorn", "Equator", "None of the above", ],
    ["Atlantic Ocean", "Dead sea", "Red sea", "Gulf of suez", ],
    ["Bangalore", "Bhopal", "Indore", "Chennai", ],
    ["Singapore", "China", "Malaysia", "India", ],
    ["They are longitudinal waves and material medium is not required for their propagation",
     "They are transverse waves and material medium is required for their propagation",
     "They are longitudinal waves and material medium is required for their propagation",
     "They are transverse waves and material medium is not required for their propagation", ],
    ["Iran", "Iraq", "Azerbaijan", "Indonesia", ],
    ["Caspian Sea", "Lake Baikal", "Lake Superior", "Lake Nero", ],
    ["Low Earth Orbit (LEO)", "Medium Earth orbit (MEO)", "Intermediate Circular Orbit (ICO)",
     "Geostationary Orbit (GEO).", ],
    ["Indonesian Archipelago", "British Isles", "Stockholm Archipelago", "Norwegian Archipelago", ],
    ["Islet", "Archipelagic State", "Island", " Cays", ],
    ["Filippo Reef", "Flinders Reef", "Darwin Mounds", "Lansdowne Bank", ],
    ["Persian Gulf", "Gulf of Bahrain", "Gulf of Oman", "Gulf Islands", ],
    ["Gulf of Khambhat", "Gulf of Kutch", "Gulf of Oman", "Gulf of Mannar", ],
    ["Gulf of Aqaba", "Gulf of California", "Gulf of Guinea", "Gulf of Oman", ],
    ["Aletsch Glacier", "Baltoro Glacier", "Lambert Glacier", "Columbia Icefield", ],

]

answer_32 = [1, 1, 2, 1, 0, 0, 1, 2, 0, 2, 3, 2, 0, 2, 1, 2, 0, 3, 3, 2]

user_answer_32 = []

indexe32 = []

def gen32():
    global indexe32
    while (len(indexe32) < 16):  # nr of questions32
        x32 = random.randint(0, 19) #form to
        if x32 in indexe32:
            continue
        else:
            indexe32.append(x32)

def showresult_32(score_32):
    lblQuestion_32.destroy()
    r1_32.destroy()
    r2_32.destroy()
    r3_32.destroy()
    r4_32.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score_32 >= 12:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0,command = claimprice1 )
        buttonclaim.pack(pady=5)
    elif (score_32 >= 6 and score_32 < 12):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0,command = claimprice )
        buttonclaim.pack(pady=5)
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a worst Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command = claimprice1 )
        buttonclaim.pack(pady=5)

def calc_32():
    global indexe32, user_answer_32, answer_32
    x32 = 0
    score_32 = 0
    for i in indexe32:
        if user_answer_32[x32] == answer_32[i]:
            score_32 = score_32 + 1
        x32 += 1
    print(score_32)
    showresult_32(score_32)

ques_32 = 1

def selected_32():
    global radiovar_13, user_answer_32
    global lblQuestion_32, r1_32, r2_32 ,r3_32, r4_32
    global ques_32
    x32 = radiovar_13.get()
    user_answer_32.append(x32)
    radiovar_13.set(-1)

    if ques_32 < 16:  # nr of questions32
        lblQuestion_32.config(text=questions32[indexe32[ques_32]])
        r1_32['text'] = answer_choice32[indexe32[ques_32]][0]
        r2_32['text'] = answer_choice32[indexe32[ques_32]][1]
        r3_32['text'] = answer_choice32[indexe32[ques_32]][2]
        r4_32['text'] = answer_choice32[indexe32[ques_32]][3]
        ques_32 += 1
    else:
        calc_32()

def startQuiz_32():
    global lblQuestion_32, r1_32, r2_32, r3_32, r4_32
    lblQuestion_32 = Label(
        root,
        text=questions32[indexe32[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion_32.pack(pady=(100, 30))

    global radiovar_13
    radiovar_13 = IntVar()
    radiovar_13.set(-1)

    r1_32 = Radiobutton(
        root,
        text=answer_choice32[indexe32[0]][0],
        font=("Times", 13),
        value=0,
        variable=radiovar_13,
        command=selected_32,
        background="#ffffff",
    )
    r1_32.pack(pady=5)

    r2_32 = Radiobutton(
        root,
        text=answer_choice32[indexe32[0]][1],
        font=("Times", 13),
        value=1,
        variable=radiovar_13,
        command=selected_32,
        background="#ffffff",
    )
    r2_32.pack(pady=5)

    r3_32 = Radiobutton(
        root,
        text=answer_choice32[indexe32[0]][2],
        font=("Times", 13),
        value=2,
        variable=radiovar_13,
        command=selected_32,
        background="#ffffff",
    )
    r3_32.pack(pady=5)

    r4_32 = Radiobutton(
        root,
        text=answer_choice32[indexe32[0]][3],
        font=("Times", 13),
        value=3,
        variable=radiovar_13,
        command=selected_32,
        background="#ffffff",
    )
    r4_32.pack(pady=5)

def lvl2geogrphy():
    lvl1buton.destroy()
    lvl2buton.destroy()
    lvl3buton.destroy()
    backbutton1.destroy()
    gen32()
    startQuiz_32()

#-------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------
questions33 = [
    "Which type of farming is also known as mechanical farming?",
    "What are cowboys of the grasslands of Argentina, Brazil, and Uruguay called?",
    "What are large units where sheep are reared in Australia called?",
    "Which among the following is correct about the term Estancias?",
    "Which among the following statements is/are correct about Livestock Ranching? Most of the areas of livestock"
    " ranching are relatively humid.  The number of animals has to be decided keeping in view the carrying capacity"
    " of the land. Select the correct code from the options given below:",
    "Which among the following country/countries account for more than 50 % of the total world production of tobacco?",
    "Which among the following factor/factors affect the cotton textile industry in India? "
    "Availability of raw material; Availability of coal ; Vast domestic market; Cheap supply of skilled manpower",
    "In which of the following regions of the UK, 90 % of the total cotton spindles and looms are located?",
    "Which among the following statements is/are correct about Woollen Industries? "
    "The woollen fabrics are in demand in only the temperate and cold zones of the world. ;;"
    "The production of woollen textiles amounts to about only 50 %to 60 % of that of cotton textiles.",
    "Which among the following industries and the regions of India is/are correctly matched?  "
    "Locomotives – Bangalore ;; Aircraft – Visakhapatnam  ;; Ship-building – Tiruchirapalli ",
    "What is the position where the earth is closest to the sun called?",
    "What theory states that there was a near-extinction event for early humans about 70,000 years ago?",
    "Which among the following is/are major sub – divisions of the woolly haired division of the human race?"
    "Negroes ;; Bantu ;; Bushmen ;; Sinic",
    "What kind of settlements are found around the points where several roads cross each other?",
    "What are cities accommodating population size between one to five million called?",
    "When was the Blue Revolution in India launched?",

]

answer_choice33 = [
    ["Extensive Farming ", " Intensive Farming", "Shifting Agriculture ", "Subsistence Farming",],
    [" Lahars", "Gauchos ", "  Caballeros", "Campos", ],
    ["Sheep Cattle ", "Prairies ", " Sheep Station", "Pastures", ],
    [" The term applied to large animal farms in South America",
     "The term applied to small animal farms in South America ", " The term applied to large animal farms in Africa",
     "The term applied to large animal farms in NorthAmerica", ],
    ["Only 1 ", " Only 2", " Both 1 & 2", "Neither 1 & 2", ],
    [" Indonesia", "India ", " China", "US", ],
    ["Only 1 ", "Only 1, 3 & 4 ", "Only 1, 2 & 4 ", "1, 2, 3 & 4", ],
    ["Lancashire ", "Manchester ", "Bolton ", "Nelson", ],
    ["Only 1 ", " Only 2", " Both 1 & 2", "Neither 1 & 2", ],
    ["Only 1 & 3 ", " Only 2 & 3", " 1, 2 & 3", "None of the above", ],
    ["Apogee ", "Perigee ", "Aphelion ", "Perihelion", ],
    [" Toba catastrophe theory", "Turnover pulse hypothesis ", " Red Queen hypothesis", "Aridity hypothesis", ],
    ["Only 1 & 4 ", " 1, 2 & 4", "1, 2 & 3 ", "1, 2, 3 & 4", ],
    [" Linear", " Rectangular", " Circular ", "Star Like", ],
    ["Urban Agglomeration ", " Census Town", "Class I Town ", "Metropolitan City", ],
    [" During the 5th Five Year Plan", "During the 10th Five Year Plan ", " During the 7th Five Year Plan",
     "During the 9th Five Year Plan", ],


]

answer_33 = [0, 1, 2, 0, 1, 2, 1, 0, 0, 3, 3, 0, 2, 3, 3, 2,]

user_answer_33 = []

indexe33 = []

def gen33():
    global indexe33
    while (len(indexe33) < 16):  # nr of questions33
        x33 = random.randint(0, 15) #form to
        if x33 in indexe33:
            continue
        else:
            indexe33.append(x33)

def showresult_33(score_33):
    lblQuestion_33.destroy()
    r1_33.destroy()
    r2_33.destroy()
    r3_33.destroy()
    r4_33.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score_33 >= 12:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0,command = claimprice2 )
        buttonclaim.pack(pady=5)
    elif (score_33 >= 6 and score_33 < 12):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0,command = claimprice2 )
        buttonclaim.pack(pady=5)
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a worst Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command = claimprice2 )
        buttonclaim.pack(pady=5)

def calc_33():
    global indexe33, user_answer_33, answer_33
    x33 = 0
    score_33 = 0
    for i in indexe33:
        if user_answer_33[x33] == answer_33[i]:
            score_33 = score_33 + 1
        x33 += 1
    print(score_33)
    showresult_33(score_33)

ques_33 = 1

def selected_33():
    global radiovar_33, user_answer_33
    global lblQuestion_33, r1_33, r2_33 ,r3_33, r4_33
    global ques_33
    x33 = radiovar_33.get()
    user_answer_33.append(x33)
    radiovar_33.set(-1)

    if ques_33 < 16:  # nr of questions33
        lblQuestion_33.config(text=questions33[indexe33[ques_33]])
        r1_33['text'] = answer_choice33[indexe33[ques_33]][0]
        r2_33['text'] = answer_choice33[indexe33[ques_33]][1]
        r3_33['text'] = answer_choice33[indexe33[ques_33]][2]
        r4_33['text'] = answer_choice33[indexe33[ques_33]][3]
        ques_33 += 1
    else:
        calc_33()

def startQuiz_33():
    global lblQuestion_33, r1_33, r2_33, r3_33, r4_33
    lblQuestion_33 = Label(
        root,
        text=questions33[indexe33[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion_33.pack(pady=(100, 30))

    global radiovar_33
    radiovar_33 = IntVar()
    radiovar_33.set(-1)

    r1_33 = Radiobutton(
        root,
        text=answer_choice33[indexe33[0]][0],
        font=("Times", 13),
        value=0,
        variable=radiovar_33,
        command=selected_33,
        background="#ffffff",
    )
    r1_33.pack(pady=5)

    r2_33 = Radiobutton(
        root,
        text=answer_choice33[indexe33[0]][1],
        font=("Times", 13),
        value=1,
        variable=radiovar_33,
        command=selected_33,
        background="#ffffff",
    )
    r2_33.pack(pady=5)

    r3_33 = Radiobutton(
        root,
        text=answer_choice33[indexe33[0]][2],
        font=("Times", 13),
        value=2,
        variable=radiovar_33,
        command=selected_33,
        background="#ffffff",
    )
    r3_33.pack(pady=5)

    r4_33 = Radiobutton(
        root,
        text=answer_choice33[indexe33[0]][3],
        font=("Times", 13),
        value=3,
        variable=radiovar_33,
        command=selected_33,
        background="#ffffff",
    )
    r4_33.pack(pady=5)

def lvl3geogrphy():
    lvl1buton.destroy()
    lvl2buton.destroy()
    lvl3buton.destroy()
    backbutton1.destroy()
    gen33()
    startQuiz_33()
#-------------------------------------------------------------------------------------------------------------






#--------------------------------------------------------------------------------------------------------------
questions41 = [
    "  How fast does sound travel in meters per second?    ",
    "  Who discovered the neutron and in what year?   ",
    "  What is the second derivative of displacement?  ",
    "  What device would you use to open and close a circuit?   ",
    "  What is a space which is entirely devoid of matter called in science terms?   ",
    "  What tool do people at sea use to measure distance with echoes?   ",
    "  What physical constant did Henry Cavendish first determine using two weights and a cantilever?    ",
    "  The Bernoulli Effect concerns what physical system?    ",
    "   What does the word 'lodestone' mean?   ",
    "  What is the distance between two peaks of a wave called?    ",
    " What unit is resistance measured in?     ",
    "  What is the scientific word for push or pull?    ",
    "   If you throw a ball in the air, what curve does it trace out?   ",
    "   What is the antimatter equivalent of an electron?   ",
    "  What is the irregular and instantaneous motion of air called?    ",
    "   According to Ohm's Law, what would the resistance be in a circuit with 40 volts and 8 amps?   ",
    "   What is the wire that gives off light in a light bulb?   ",
    "   What sort of electricity do you get when you rub two balloons and they stick together?   ",
    "  One kilogram is equal to how many pounds?     ",
    "  A unit of electromotive force is called what?    ",

]

answer_choice41 = [
    ["260 ", "340  ", ],
    [" James Chadwick In 1932 ", " Isaac Newton ", ],
    ["Speed ", " Instantaneous Acceleration  ", ],
    [" Phone", " Switch ", ],
    [" Vacuum", " Meter ", ],
    ["  Cm", " Sonar ", ],
    ["Gravitational Constant  ", " Acceleration ", ],
    ["A Moving Fluid  ", "Leading stone  ", ],
    ["Leading Stone  ", " Wave ", ],
    [" Meter", " Wavelength ", ],
    ["Pressure ", " Ohm  ", ],
    ["Force  ", "  Newton", ],
    [" U - shape", "Parabola   ", ],
    ["Positron  ", "Antielectron   ", ],
    [" Instantaneous motion ", " Turbulence  ", ],
    [" 5 Ohms ", " 1 Ohms  ", ],
    ["Thin Wire ", " Filament  ", ],
    [" Static ", " Rubbing ", ],
    ["2.2 ", " 3.4 ", ],
    [" Volt", " Ohm ", ],

]

answer_41 = [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0,]

user_answer_41 = []

indexe41 = []

def gen41():
    global indexe41
    while (len(indexe41) < 16):  # nr of questions41
        x41 = random.randint(0, 19) #form to
        if x41 in indexe41:
            continue
        else:
            indexe41.append(x41)

def showresult_41(score_41):
    lblQuestion_41.destroy()
    r1_41.destroy()
    r2_41.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score_41 >= 12:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0,command = claimprice )
        buttonclaim.pack(pady=5)
    elif (score_41 >= 6 and score_41 < 12):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0,command = claimprice2 )
        buttonclaim.pack(pady=5)
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a worst Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command = claimprice1 )
        buttonclaim.pack(pady=5)

def calc_41():
    global indexe41, user_answer_41, answer_41
    x41 = 0
    score_41 = 0
    for i in indexe41:
        if user_answer_41[x41] == answer_41[i]:
            score_41 = score_41 + 1
        x41 += 1
    print(score_41)
    showresult_41(score_41)

ques_41 = 1

def selected_41():
    global radiovar_41, user_answer_41
    global lblQuestion_41, r1_41, r2_41
    global ques_41
    x41 = radiovar_41.get()
    user_answer_41.append(x41)
    radiovar_41.set(-1)

    if ques_41 < 16:  # nr of questions41
        lblQuestion_41.config(text=questions41[indexe41[ques_41]])
        r1_41['text'] = answer_choice41[indexe41[ques_41]][0]
        r2_41['text'] = answer_choice41[indexe41[ques_41]][1]

        ques_41 += 1
    else:
        calc_41()

def startQuiz_41():
    global lblQuestion_41, r1_41, r2_41
    lblQuestion_41 = Label(
        root,
        text=questions41[indexe41[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion_41.pack(pady=(100, 30))

    global radiovar_41
    radiovar_41 = IntVar()
    radiovar_41.set(-1)

    r1_41 = Radiobutton(
        root,
        text=answer_choice41[indexe41[0]][0],
        font=("Times", 13),
        value=0,
        variable=radiovar_41,
        command=selected_41,
        background="#ffffff",
    )
    r1_41.pack(pady=5)

    r2_41 = Radiobutton(
        root,
        text=answer_choice41[indexe41[0]][1],
        font=("Times", 13),
        value=1,
        variable=radiovar_41,
        command=selected_41,
        background="#ffffff",
    )
    r2_41.pack(pady=5)

def lvl1physics():
    lvl1buton.destroy()
    lvl2buton.destroy()
    lvl3buton.destroy()
    backbutton1.destroy()
    gen41()
    startQuiz_41()

#--------------------------------------------------------------------------------------------------------------








#----------------------------------------------------------------------------------------------------------------
questions42 = [
    " As light from a star spreads out and weakens, do gaps form between the photons? ",
    " Can a fire have a shadow? ",
    " Can air make shadows? ",
    " Can gold be created from other elements? ",
    " Can light bend around corners? ",
    " Can momentum be hidden to human eyes like how kinetic energy can be hidden as heat? ",
    " Can one bit of light bounce off another bit of light? ",
    " Can radio antennas emit visible light? ",
    " Can sound waves generate heat? ",
    " Can the decay half-life of a radioactive material be changed? ",
    " Can you go fast enough to get enough mass to become a black hole? ",
    " Can you make a shock wave of light by breaking the light barrier just like "
    "supersonic airplanes break the sound barrier? ",
    " Can you make a sunset in a cup of milk? ",
    " Could electronic devices charge themselves without being plugged into an electricity source? ",
    " Could scientists perfectly simulate the entire universe in a computer, down to the last atom? ",
    " Do atoms ever actually touch each other? ",
    " Do flames contain plasma? ",
    " Does a source of electricity ever run out of electrons? ",
    " Does an atom have a color? ",
    " Does an electron in an atom move at all? ",
]

answer_choice42 = [
    [" Depends ", " YES ", " NO ",],
    [" Depends ", " YES ", " NO ",],
    [" Depends ", " YES ", " NO ",],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],
    [" Depends ", " YES ", " NO ", ],

]

answer_42 = [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 2, 2, 1, 1, 2, 0, 0, 0, 0, 0, ]

user_answer_42 = []

indexe42 = []

def gen42():
    global indexe42
    while (len(indexe42) < 16):  # nr of questions42
        x42 = random.randint(0, 19) #form to
        if x42 in indexe42:
            continue
        else:
            indexe42.append(x42)

def showresult_42(score_42):
    lblQuestion_42.destroy()
    r1_42.destroy()
    r2_42.destroy()
    r3_42.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score_42 >= 12:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0,command = claimprice)
        buttonclaim.pack(pady=5)
    elif (score_42 >= 6 and score_42 < 12):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0,command = claimprice1)
        buttonclaim.pack(pady=5)
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a worst Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command = claimprice2 )
        buttonclaim.pack(pady=5)

def calc_42():
    global indexe42, user_answer_42, answer_42
    x42 = 0
    score_42 = 0
    for i in indexe42:
        if user_answer_42[x42] == answer_42[i]:
            score_42 = score_42 + 1
        x42 += 1
    print(score_42)
    showresult_42(score_42)

ques_42 = 1

def selected_42():
    global radiovar_42, user_answer_42
    global lblQuestion_42, r1_42, r2_42 ,r3_42
    global ques_42
    x42 = radiovar_42.get()
    user_answer_42.append(x42)
    radiovar_42.set(-1)

    if ques_42 < 16:  # nr of questions42
        lblQuestion_42.config(text=questions42[indexe42[ques_42]])
        r1_42['text'] = answer_choice42[indexe42[ques_42]][0]
        r2_42['text'] = answer_choice42[indexe42[ques_42]][1]
        r3_42['text'] = answer_choice42[indexe42[ques_42]][2]

        ques_42 += 1
    else:
        calc_42()

def startQuiz_42():
    global lblQuestion_42, r1_42, r2_42, r3_42
    lblQuestion_42 = Label(
        root,
        text=questions42[indexe42[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion_42.pack(pady=(100, 30))

    global radiovar_42
    radiovar_42 = IntVar()
    radiovar_42.set(-1)

    r1_42 = Radiobutton(
        root,
        text=answer_choice42[indexe42[0]][0],
        font=("Times", 13),
        value=0,
        variable=radiovar_42,
        command=selected_42,
        background="#ffffff",
    )
    r1_42.pack(pady=5)

    r2_42 = Radiobutton(
        root,
        text=answer_choice42[indexe42[0]][1],
        font=("Times", 13),
        value=1,
        variable=radiovar_42,
        command=selected_42,
        background="#ffffff",
    )
    r2_42.pack(pady=5)

    r3_42 = Radiobutton(
        root,
        text=answer_choice42[indexe42[0]][2],
        font=("Times", 13),
        value=2,
        variable=radiovar_42,
        command=selected_42,
        background="#ffffff",
    )
    r3_42.pack(pady=5)

def lvl2physics():
    lvl1buton.destroy()
    lvl2buton.destroy()
    lvl3buton.destroy()
    backbutton1.destroy()
    gen42()
    startQuiz_42()

#-----------------------------------------------------------------------------------------------------------------






#---------------------------------------------------------------------------------------------------------------
questions43 = [
    "Do heavier objects fall more slowly than lighter objects? ",
    "Which of these situations can increase the reaction time of a driver? ",
    "A car driver sees a rabbit on the road. The driver makes an emergency stop after he sees the rabbit. "
    " The graph shows the speed of the car from the time the driver sees the rabbit until the car stops.  "
    "The distance travelled by the car from the time the driver first sees the rabbit to "
    "when car starts to slow down is the:  ",
    " Before the fuse is lit, the total weight of a model rocket including fuel is 0.7 N. "
    "The gravitational field strength is 10 N/kg.The total mass of the model rocket including fuel is:",
    "  A ball rolls off the edge of the table. The horizontal component of the ball’s velocity "
    "remains constant during its entire trajectory because",
    " A force produces power P by doing work W in a time T. What power will be produced by a force that does "
    "six times as much work in half as much time?",
    " Two identical cars collide head on. Each car is traveling at 100 km/h."
    " The impact force on each car is the same as hitting a solid wall at:",
    " A man presses more weight on earth at :",
    "A piece of ice is dropped in a vesel containing kerosene. When ice melts, the level of kerosene will ",
    "Young's modulus is the property of ",
    "Which one of the following has the highest value of specific heat ? ",
    "With the increase of pressure, the boiling point of any substance ",
    "Elecronegativity is the measure of ",
    "The rotational effect of a force on a body about an axis of rotation is described in terms of the ",
    " If no external force acts on a system of bodies, the total linear momentum of the system of bodies"
    " remains constant. Which law states that ?",


]

answer_choice43 = [
    ["Depends ", " Yes", " No ", "-- ",],
    [" An icy road", "Worn tyres on his car ", "Stopping for a cup of coffee ",
     " Driving for a long time without taking a break", ],
    [" Average distance", " Braking distance", " Stopping distance", "Thinking distance ", ],
    ["0.007 kg ", " 0.07 kg", "0.7 kg ", "7 kg ", ],
    ["the ball is not acted upon by a force in the horizontal direction.",
     "the ball is not acted upon by any force.  ",
     " the ball is not acted upon by any force in the vertical direction. ",
     " None of the other choices are correct.", ],
    ["12P ", "6P ", "1/12 P ", "3/8 P ", ],
    ["100 km/h ", "200 km/h ", "150 km/h ", "50 km/h ", ],
    ["Sitting position ", " Standing Position", "Lying Position ", "None of these ", ],
    [" Rise", "Fall ", "Remain Same ", "None of these ", ],
    [" Gas only", " Both Solid and Liquid", "Liquid only ", " Solid only", ],
    ["Alcohol ", " Methane", " Kerosene", "Water ", ],
    ["Increases ", "Decreases ", " Remains Same", "Becomes zero ", ],
    ["Metallic character ", "Non-metallic character ", " Basic Character", "None of these ", ],
    ["Centre of gravity ", " Centripetal force", "Centrifugal force ", "Moment of force ", ],
    [" Newton's first law", "Newton's Second Law ", "Newton's Third Law ",
     "Principle of conservation of linear momentum ", ],


]

answer_43 = [1, 3, 3, 1, 0, 0, 0, 1, 1, 3, 3, 0, 1, 3, 3,]

user_answer_43 = []

indexe43 = []

def gen43():
    global indexe43
    while (len(indexe43) < 14):  # nr of questions43
        x43 = random.randint(0, 14) #form to
        if x43 in indexe43:
            continue
        else:
            indexe43.append(x43)

def showresult_43(score_43):
    lblQuestion_43.destroy()
    r1_43.destroy()
    r2_43.destroy()
    r3_43.destroy()
    r4_43.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score_43 >= 12:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0,command = claimprice2 )
        buttonclaim.pack(pady=5)
    elif (score_43 >= 6 and score_43 < 12):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You Can Be Better!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0,command = claimprice1 )
        buttonclaim.pack(pady=5)
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You are a worst Genius!!")
        buttonclaim = Button(root, image=claimbutton, bg="#ffffff", relief=FLAT, border=0, command = claimprice )
        buttonclaim.pack(pady=5)

def calc_43():
    global indexe43, user_answer_43, answer_43
    x43 = 0
    score_43 = 0
    for i in indexe43:
        if user_answer_43[x43] == answer_43[i]:
            score_43 = score_43 + 1
        x43 += 1
    print(score_43)
    showresult_43(score_43)

ques_43 = 1

def selected_43():
    global radiovar_43, user_answer_43
    global lblQuestion_43, r1_43, r2_43 ,r3_43, r4_43
    global ques_43
    x43 = radiovar_43.get()
    user_answer_43.append(x43)
    radiovar_43.set(-1)

    if ques_43 < 14:  # nr of questions43
        lblQuestion_43.config(text=questions43[indexe43[ques_43]])
        r1_43['text'] = answer_choice43[indexe43[ques_43]][0]
        r2_43['text'] = answer_choice43[indexe43[ques_43]][1]
        r3_43['text'] = answer_choice43[indexe43[ques_43]][2]
        r4_43['text'] = answer_choice43[indexe43[ques_43]][3]
        ques_43 += 1
    else:
        calc_43()

def startQuiz_43():
    global lblQuestion_43, r1_43, r2_43, r3_43, r4_43
    lblQuestion_43 = Label(
        root,
        text=questions43[indexe43[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion_43.pack(pady=(100, 30))

    global radiovar_43
    radiovar_43 = IntVar()
    radiovar_43.set(-1)

    r1_43 = Radiobutton(
        root,
        text=answer_choice43[indexe43[0]][0],
        font=("Times", 13),
        value=0,
        variable=radiovar_43,
        command=selected_43,
        background="#ffffff",
    )
    r1_43.pack(pady=5)

    r2_43 = Radiobutton(
        root,
        text=answer_choice43[indexe43[0]][1],
        font=("Times", 13),
        value=1,
        variable=radiovar_43,
        command=selected_43,
        background="#ffffff",
    )
    r2_43.pack(pady=5)

    r3_43 = Radiobutton(
        root,
        text=answer_choice43[indexe43[0]][2],
        font=("Times", 13),
        value=2,
        variable=radiovar_43,
        command=selected_43,
        background="#ffffff",
    )
    r3_43.pack(pady=5)

    r4_43 = Radiobutton(
        root,
        text=answer_choice43[indexe43[0]][3],
        font=("Times", 13),
        value=3,
        variable=radiovar_43,
        command=selected_43,
        background="#ffffff",
    )
    r4_43.pack(pady=5)

def lvl3physics():
    lvl1buton.destroy()
    lvl2buton.destroy()
    lvl3buton.destroy()
    backbutton1.destroy()
    gen43()
    startQuiz_43()

#---------------------------------------------------------------------------------------------------------------



def histroypressd():
    global lvl1buton
    global lvl2buton
    global lvl3buton
    global backbutton1
    buttonmath.destroy()
    buttongeography.destroy()
    buttonphysics.destroy()
    buttonhistory.destroy()
    buttonback.destroy()
    root.config(background = "#ffffff")
    lvl1buton= Button(root, image=level_button, relief=FLAT, border=0, bg="#ffffff",)
    lvl1buton.pack(pady=15)
    lvl2buton= Button(root, image=leve2_button, relief=FLAT, border=0, bg="#ffffff", command = lvl2history)
    lvl2buton.pack(pady=15)
    lvl3buton= Button(root, image=leve3_button, relief=FLAT, border=0, bg="#ffffff", command = lvl3history)
    lvl3buton.pack(pady=15)
    backbutton1 = Button(root, image=backbutton, relief=FLAT, border=0, bg="#ffffff", command = back_button )
    backbutton1.pack(pady=15)

def mathpressd():
    global lvl1buton
    global lvl2buton
    global lvl3buton
    global backbutton1
    buttonmath.destroy()
    buttongeography.destroy()
    buttonphysics.destroy()
    buttonhistory.destroy()
    buttonback.destroy()
    root.config(background="#ffffff")
    lvl1buton = Button(root, image=level_button, relief=FLAT, border=0, bg="#ffffff", command = lvl1math )
    lvl1buton.pack(pady=15)
    lvl2buton = Button(root, image=leve2_button, relief=FLAT, border=0, bg="#ffffff", command = lvl2math )
    lvl2buton.pack(pady=15)
    lvl3buton = Button(root, image=leve3_button, relief=FLAT, border=0, bg="#ffffff", command = lvl3math )
    lvl3buton.pack(pady=15)
    backbutton1 = Button(root, image = backbutton, relief=FLAT, border=0, bg="#ffffff", command = back_button )
    backbutton1.pack(pady=15)

def geographypressd():
    global lvl1buton
    global lvl2buton
    global lvl3buton
    global backbutton1
    buttonmath.destroy()
    buttongeography.destroy()
    buttonphysics.destroy()
    buttonhistory.destroy()
    buttonback.destroy()
    root.config(background="#ffffff")
    lvl1buton = Button(root, image=level_button, relief=FLAT, border=0, bg="#ffffff", command = lvl1geogrphy)
    lvl1buton.pack(pady=15)
    lvl2buton = Button(root, image=leve2_button, relief=FLAT, border=0, bg="#ffffff", command = lvl2geogrphy)
    lvl2buton.pack(pady=15)
    lvl3buton = Button(root, image=leve3_button, relief=FLAT, border=0, bg="#ffffff", command = lvl3geogrphy)
    lvl3buton.pack(pady=15)
    backbutton1 = Button(root, image=backbutton, relief=FLAT, border=0, bg="#ffffff", command=back_button)
    backbutton1.pack(pady=15)

def physicspressd():
    global lvl1buton
    global lvl2buton
    global lvl3buton
    global backbutton1
    buttonmath.destroy()
    buttongeography.destroy()
    buttonphysics.destroy()
    buttonhistory.destroy()
    buttonback.destroy()
    root.config(background="#ffffff")
    lvl1buton = Button(root, image=level_button, relief=FLAT, border=0, bg="#ffffff", command = lvl1physics)
    lvl1buton.pack(pady=15)
    lvl2buton = Button(root, image=leve2_button, relief=FLAT, border=0, bg="#ffffff", command = lvl2physics)
    lvl2buton.pack(pady=15)
    lvl3buton = Button(root, image=leve3_button, relief=FLAT, border=0, bg="#ffffff", command = lvl3physics)
    lvl3buton.pack(pady=15)
    backbutton1 = Button(root, image=backbutton, relief=FLAT, border=0, bg="#ffffff", command=back_button)
    backbutton1.pack(pady=15)

def pick_test_lvl():
    my_canvas.destroy()
    global buttonmath
    global buttonhistory
    global buttongeography
    global buttonphysics
    global buttonback
    root.config(background= "#0063B2")
    buttonmath = Button(root, image=mathbutton, relief=FLAT, border=0, bg="#0063B2", command = mathpressd )
    buttonmath.pack(pady=15)
    buttonhistory = Button(root, image=historybutton, relief=FLAT, border=0, bg="#0063B2", command = histroypressd )
    buttonhistory.pack(pady=15)
    buttongeography = Button(root, image=geographybutton, relief=FLAT, border=0, bg="#0063B2", command = geographypressd)
    buttongeography.pack(pady=15)
    buttonphysics = Button(root, image=physicbutton, relief=FLAT, border=0, bg="#0063B2", command = physicspressd)
    buttonphysics.pack(pady=15)
    buttonback = Button(root, image=backbutton, relief=FLAT, border=0, bg="#0063B2",command=turn_back)
    buttonback.pack(pady=15)

def help():
    screen20 = Toplevel(root)
    screen20.title = ("Instructions")
    screen20.geometry("500x450")
    Label(screen20, font=("Times", 14), background="#000000", foreground="#ffcc33" ,
          text=" WELCOME!!!!\n\n This application was developed by T.E.D Inc. \n In the homepage, first you need to "
               "register if you are not. \nThen you need to log in.\n If you want to suggest your own question"
               "\n then you need to press 'proceed' after you log in.\nPress add question to add a question, view: to view"
               "\nyour question, delete:to delete it. \nIn the homepage you have music buttons if you want a nice "
               "\nmelody running in the background. \nYou press start. \nChoose a field or go back. \nChoose a level. "
               " \nYou will get 20 seconds for each question. \nOnce you select you can not go back. "
               "\nThink CAREFULY! \nIn the end, based on your score, you can win coupons.\n\n"
               " DO NOT FORGET TO LEAVE A LIKE \n😁 +_+ 😁").pack()

def back_button():
    lvl1buton.destroy()
    lvl2buton.destroy()
    lvl3buton.destroy()
    backbutton1.destroy()
    pick_test_lvl()

def turn_back():
    buttonmath.destroy()
    buttonhistory.destroy()
    buttongeography.destroy()
    buttonphysics.destroy()
    buttonback.destroy()
    global my_canvas

    my_canvas = Canvas(root, width=700, height=560)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0, 0, image=img, anchor="nw")
    my_canvas.create_text(50, 490, text="T.E.D.Inc", font=("Times New Roman", 10), fil="#a4a4a4")

    button1 = Button(root, image=img_button2, command=pick_test_lvl, relief=FLAT, border=0, bg="#000966")
    button2 = Button(root, image=helpbutton, command=help, bg="#013287")
    button3 = Button(root, image=login_button, command=login, bg="#000562")
    button4 = Button(root, image=register_button, command=register, bg="#000c68")
    button5 = Button(root, image=musbut, font=("Helvetica", 32), command=play, bg="#000764", relief=FLAT, border=0, )
    button6 = Button(root, image=msnotbut, command=stop, bg="#000966", relief=FLAT, border=0, )

    button1_window = my_canvas.create_window(15, 15, anchor="nw", window=button1)
    button2_window = my_canvas.create_window(155, 15, anchor="nw", window=button2)
    button3_window = my_canvas.create_window(550, 15, anchor="nw", window=button3)
    button4_window = my_canvas.create_window(550, 65, anchor="nw", window=button4)
    button5_window = my_canvas.create_window(630, 145, anchor="nw", window=button5)
    button6_window = my_canvas.create_window(630, 180, anchor="nw", window=button6)



def claimprice():
    global root777
    root777 = Toplevel(root)
    root777.title("Claim PRICE")
    root777.geometry("500x500")
    root777.config(background = "#ffffff")
    Label(root777, text="Congratulations! \n You are rewarded with a coupon! \n Do not forget to check our sponsor: "
                      "\nhttps://www.joinhoney.com/ ", font= ("Times New Roman",15),background="#000000",
          foreground="#ffcc33" ).pack()
    Label(root777, text="", background = "#ffffff").pack()
    couponbutton = Button(root777, image = couponbutt, border = 0, bg="#ffffff", command = click)
    couponbutton.pack(pady=5)

def click():
    webbrowser.open("https://www.joinhoney.com/stores/trending")


def claimprice1():
    global root777
    root777 = Toplevel(root)
    root777.title("Claim PRICE")
    root777.geometry("500x500")
    root777.config(background = "#ffffff")
    Label(root777, text="Congratulations! \n You are rewarded with a coupon! \n Do not forget to check our sponsor: "
                      "\nhttps://www.joinhoney.com/ ", font= ("Times New Roman",15),background="#000000",
          foreground="#ffcc33" ).pack()
    Label(root777, text="", background = "#ffffff").pack()
    couponbutton = Button(root777, image = couponbutt2, border = 0, bg="#ffffff", command = click1)
    couponbutton.pack(pady=5)

def click1():
    webbrowser.open("https://www.nike.com/w/new-3n82y")


def claimprice2():
    global root777
    root777 = Toplevel(root)
    root777.title("Claim PRICE")
    root777.geometry("500x500")
    root777.config(background = "#ffffff")
    Label(root777, text="Congratulations! \n You are rewarded with a coupon! \n Do not forget to check our sponsor: "
                      "\nhttps://www.joinhoney.com/ ", font= ("Times New Roman",15),background="#000000",
          foreground="#ffcc33" ).pack()
    Label(root777, text="", background = "#ffffff").pack()
    couponbutton = Button(root777, image = cuponbutt3, border = 0, bg="#ffffff", command = click2)
    couponbutton.pack(pady=5)

def click2():
    webbrowser.open("https://www.amazon.com/")




















# the workplace is created


root = tkinter.Tk()
root.title("QuizApp")
root.geometry("700x560")
root.config(background="#ffffff")
root.resizable(0, 0)  # if we want to adjust however we remove code

image = Image.open("try1.png")
# Reszie the image using resize() method
resize_image = image.resize((700, 560))
img = ImageTk.PhotoImage(resize_image)

mathbutton = PhotoImage(file = "Math_Buttons.png")
historybutton = PhotoImage(file = "History_Button.png")
geographybutton = PhotoImage(file = "Geography_Button.png")
physicbutton = PhotoImage(file = "Physics_Button.png")


pygame.mixer.init()

def play():
    pygame.mixer.music.load("melody.mp3")
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()


img_button2 = PhotoImage(file="startButton11.png")
helpbutton = PhotoImage(file = "Help_Button1.png")
login_button = PhotoImage(file = "LogIn_button.png")
register_button = PhotoImage(file = "Register_button.png")
level_button = PhotoImage(file = "Level1_button.png")
leve2_button = PhotoImage(file = "Level2_button.png")
leve3_button = PhotoImage(file = "Level3_Buttons.png")
backbutton = PhotoImage(file = "Backbutton.png")
musbut = PhotoImage(file = "music_button.png")
msnotbut = PhotoImage(file = "music_not_button.png")
claimbutton = PhotoImage(file = "shop_Button.png")
couponbutt = PhotoImage(file= "cupon.png")
load = Image.open("cupon3.jpg")
couponbutt2 = ImageTk.PhotoImage(load)
load2 = Image.open("cupon4.jpg")
cuponbutt3 = ImageTk.PhotoImage(load2)



my_canvas = Canvas(root, width=700, height=560)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0,0, image=img,anchor="nw")
my_canvas.create_text(50,490, text="T.E.D.Inc",font=("Times New Roman",10), fil="#a4a4a4")


button1= Button(root, image=img_button2,  command=pick_test_lvl, relief=FLAT, border=0, bg = "#000966")
button2= Button(root, image = helpbutton, command=help, bg = "#013287")
button3= Button(root, image = login_button, command = login, bg ="#000562")
button4= Button(root, image = register_button, command = register, bg="#000c68")
button5 = Button(root, image = musbut, font = ("Helvetica" ,32 ), command = play, bg="#000764", relief=FLAT, border=0,)
button6 = Button(root, image= msnotbut, command = stop, bg="#000966", relief=FLAT, border=0,)

button1_window = my_canvas.create_window(15,15, anchor="nw",window=button1)
button2_window = my_canvas.create_window(155,15, anchor="nw",window=button2)
button3_window = my_canvas.create_window(550,15, anchor="nw",window=button3)
button4_window = my_canvas.create_window(550,65, anchor="nw",window=button4)
button5_window = my_canvas.create_window(630,145, anchor="nw",window=button5)
button6_window = my_canvas.create_window(630,180, anchor="nw",window=button6)


root.mainloop()