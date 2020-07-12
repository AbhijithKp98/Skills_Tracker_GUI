'''
This Module is a basic version of an SkillSet Tracker
Inputs : Name, Email, Stream, Experience, Skills
Data loaded into DB Browser for SQLite
To check the records, search for "Skill_Tracker.db" on your system
'''

# import only required func from the tkinter library
from tkinter import Label, StringVar, IntVar, Tk, Entry
from tkinter import Radiobutton, OptionMenu, Checkbutton, Button
import sqlite3

root = Tk()
root.geometry('480x460')  # Window size
root.configure(bg='white')  # Background color set to white
root.title("Basic Skill Tracker")

Fullname = StringVar()
Email = StringVar()
streamm = IntVar()
year = StringVar()
SQL = StringVar()
Python = StringVar()
spark = StringVar()
EDA = StringVar()


# Main Function for taking inputs and writing it to SQL db
def database():

    create_table = '''CREATE TABLE IF NOT EXISTS Skills_Tracker
                    (
                        Fullname TEXT,
                        Email TEXT,
                        stream TEXT,
                        experience TEXT,
                        skills TEXT
                    )'''

    add_col = '''INSERT INTO Skills_Tracker
               (
                   FullName,
                   Email,
                   stream,
                   experience,
                   skills
                )
               VALUES(?,?,?,?,?)'''

    name1 = Fullname.get()
    email = Email.get()
    stream = streamm.get()
    experience = year.get()
    skill = SQL.get()
    conn = sqlite3.connect('Skill_Tracker.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute(f'{create_table}')
    cursor.execute(f'{add_col}', (name1, email, stream, experience, skill,))
    conn.commit()


# Labels & entries which will appear on the GUI
label_0 = Label(root, text="Skill Tracker Tool", width=30, font=("bold", 14))
label_0.place(x=80, y=53)

label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
label_1.place(x=90, y=130)

entry_1 = Entry(root, textvar=Fullname)
entry_1.place(x=270, y=130)

label_2 = Label(root, text="Email", width=20, font=("bold", 10))
label_2.place(x=90, y=180)

entry_2 = Entry(root, textvar=Email)
entry_2.place(x=270, y=180)

label_3 = Label(root, text="Stream", width=20, font=("bold", 10))
label_3.place(x=90, y=230)

Radiobutton(root, text="DS", padx=4, variable=streamm, value=1)\
    .place(x=270, y=230)
Radiobutton(root, text="Engineering", padx=5, variable=streamm, value=2)\
    .place(x=321, y=230)

label_4 = Label(root, text="Experience", width=20, font=("bold", 10))
label_4.place(x=90, y=280)

range = ['<1', '1-2', '2-4', '4-6', '6-10', '10+']

droplist = OptionMenu(root, year, *range)
droplist.config(width=15)
year.set('Years of Experience')
droplist.place(x=270, y=280)

label_4 = Label(root, text="Skills", width=20, font=("bold", 10))
label_4.place(x=90, y=330)

Checkbutton(root, text="SQL", variable=SQL).place(x=270, y=330)
Checkbutton(root, text="Python", variable=Python).place(x=320, y=330)
Checkbutton(root, text="Spark", variable=spark).place(x=270, y=350)
Checkbutton(root, text="EDA", variable=EDA).place(x=332, y=350)

Button(root, text='Submit',
       width=20, bg='black',
       fg='white',
       command=database)\
           .place(x=180, y=380)

root.mainloop()
