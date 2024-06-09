from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
import tkinter.ttk as ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from screeninfo import get_monitors
import mysql.connector as conn

con = conn.connect(host='localhost', user='yogesh', password='Lvju2aml15d##')
cursor = con.cursor()
cursor.execute('use proj')

if con.is_connected():
    pass
else:
    pass

for m in get_monitors():
    w, h = m.width, m.height
    w, h = w - 20, h - 70
    kn = 1
    qsct = 1
    qrst = 1
    sl = False
    tll = False
    lbb = {}
    fmarks = 0
    root = Tk()
    attendlist, unattendlist = [], []
    btndict = {}
    onum = 0
    cc1, cc2, cc3, cc4 = IntVar(), IntVar(), IntVar(), IntVar()
    root.geometry('600x600')
    bkg = Image.open(r'bg1.jpg')
    bkg = bkg.resize((600, 600))
    bkg2 = ImageTk.PhotoImage(bkg)
    bkg = Label(image=bkg2)
    bkg.place(x=0, y=0)


def insid():
    global logn, logn2, sl, tll
    if logn.get() == 'student' and logn2.get() == 'study':
        sl = True
    if logn.get() == 'teacher' and logn2.get() == 'teach':
        tll = True
    root.destroy()
    return sl, tll


win2 = Frame(root, height=300, width=300, relief=RAISED)
win2.configure(bg='#FFDAB9', highlightbackground='black', highlightthickness=1.5)
win2.place(x=150, y=150)

win = Frame(win2, bg='#FFDAB9')
win.place(relx=0, rely=0.3)

win3 = Frame(win2, width=290, height=90, bg='#FFDAB9')
win3.place(x=0, y=0)

win4 = Frame(win2, width=290, height=40, bg='#FFDAB9')
win4.place(relx=0, rely=0.6)

fs = tkFont.Font(family="Lucida Grande", size=30)
fs2 = tkFont.Font(family="Lucida Grande", size=15)

Label(win3, text='LOGIN', font=fs, bg='#FFDAB9').place(relx=0.314159, rely=0)
Label(win, text='User Id     : ', font=fs2, bg='#FFDAB9').grid(column=0, row=1)
Label(win, text='Password : ', font=fs2, bg='#FFDAB9').grid(column=0, row=2)

logn = Entry(win, width=25)
logn2 = Entry(win, width=25)
logn.grid(column=1, row=1)
logn2.grid(column=1, row=2)
Button(win4, text='Login', font=fs2, bd=1.5, command=insid, relief=RIDGE).place(relx=0.314159, rely=0)

root.mainloop()

if sl == True:
    j = {}
    button_dict1 = {}
    button_dict2 = {}

    aroot = Tk()
    fs = tkFont.Font(family="Lucida Grande", size=30)
    fs2 = tkFont.Font(family="Lucida Grande", size=20)
    fs4 = tkFont.Font(family="Lucida Grande", size=10)
    fs3 = tkFont.Font(family="Lucida Grande", size=40)
    cursor.execute('show tables')
    tabel = cursor.fetchall()


def opn(x):
    global qdb, kq, fs, fs2, fs3
    cursor.execute(str('select * from ' + str(x)))
    qdb = cursor.fetchall()

    kq = Tk()
    kq.geometry('%dx%d+%d+%d' % (w, h, 0, 0))
    fs = tkFont.Font(family="Lucida Grande", size=30)
    fs2 = tkFont.Font(family="Lucida Grande", size=20)
    fs3 = tkFont.Font(family="Lucida Grande", size=40)


def addinopn(num, dta):
    global frm1, labe, qno, que, op1, op2, op3, op4, oc
    try:
        qno, que, op1, op2, op3, op4, oc = dta[num]
    except:
        pass
    try:
        frm1.place_forget()
    except:
        pass

    namevar = str(que)
    frm1 = Frame(fm1, width=w * 0.597, height=h * 0.2, highlightbackground='black', highlightthickness=0, bg='white')
    frm1.place(relx=0, rely=0, in_=fm1)
    frm2 = Frame(fm1, width=w * 0.597, height=h * 0.6, highlightbackground='black', highlightthickness=0, bg='white')
    frm2.place(relx=0, rely=0.4, in_=fm1)

    if len(que) <= 40:
        namevar = str(que)
        Label(frm1, text='   ' + str(qno) + ')  ' + namevar, font=("Lucida Grande", 30), bg='white').grid(column=0,
                                                                                                                row=0)
    else:
        Label(frm1, text='   ' + str(qno) + ')  ', font=("Lucida Grande", 30), bg='white').grid(column=0, row=0)
    ste2 = []
    stee = que.split()
    ster = ''
    for i in stee:
        if len(str(ster + i)) <= 42:
            ster += str(i + ' ')
        else:
            ste2.append(ster)
            ster = ''
            ster += str(i + ' ')
    else:
        ster = ster + ' ' * int(42 - len(ster)) + '         '
        ste2.append(ster)
    for i in range(0, len(ste2)):
        Label(frm1, text=str(ste2[i]), font=("Lucida Grande", 30), bg='white').grid(column=1, row=i)

    Label(frm2, text=' ', bg='white').grid(column=0, row=0)
    Label(frm2, text=' ', bg='white').grid(column=0, row=1)
    Label(frm2, text=' ', bg='white').grid(column=0, row=2)
    Label(frm2, text=' ', bg='white').grid(column=0, row=3)

    i1
if len(que) <= 40:
    namevar = str(que)
    Label(frm1, text='   ' + str(qno) + ')  ' + namevar, font=("Lucida Grande", 30), bg='white').grid(column=0, row=0)
else:
    Label(frm1, text='   ' + str(qno) + ')  ', font=("Lucida Grande", 30), bg='white').grid(column=0, row=0)
    
    ste2 = []
    stee = que.split()
    ster = ''
    for i in stee:
        if len(str(ster + i)) <= 42:
            ster += str(i + ' ')
        else:
            ste2.append(ster)
            ster = ''
            ster += str(i + ' ')
    
    ster = ster + ' ' * int(42 - len(ster)) + '         '
    ste2.append(ster)
    
    for i in range(len(ste2)):
        Label(frm1, text=str(ste2[i]), font=("Lucida Grande", 30), bg='white').grid(column=1, row=i)

Label(frm2, text=' ', bg='white').grid(column=0, row=0)
Label(frm2, text=' ', bg='white').grid(column=0, row=1)
Label(frm2, text=' ', bg='white').grid(column=0, row=2)
Label(frm2, text=' ', bg='white').grid(column=0, row=3)

i1 = Label(frm2, text='      A)' + str(op1), font=("Lucida Grande", 25), bg='white', width=41)
i1.grid(column=1, row=0)
i2 = Label(frm2, text='      B)' + str(op2), font=("Lucida Grande", 25), bg='white', width=41)
i2.grid(column=1, row=1)
i3 = Label(frm2, text='      C)' + str(op3), font=("Lucida Grande", 25), bg='white', width=41)
i3.grid(column=1, row=2)
i4 = Label(frm2, text='      D)' + str(op4), font=("Lucida Grande", 25), bg='white', width=41)
i4.grid(column=1, row=3)

if oc == op1:
    i1.config(bg='light green')
elif oc == op2:
    i2.config(bg='light green')
elif oc == op3:
    i3.config(bg='light green')
elif oc == op4:
    i4.config(bg='light green')

fm1 = Frame(kq, width=w*0.6, height=h*0.8, bg='white', highlightthickness=2, highlightbackground='black', relief=RAISED)
fm1.place(x=w*0.04, y=h*0.1)
fm21 = Frame(kq, width=w*0.3, height=h*0.4, bg='cyan', highlightthickness=2, highlightbackground='black', relief=RAISED)
fm21.place(x=w*0.675, y=h*0.2)
fm2 = Frame(fm21, width=w*0.3, height=h*0.4, bg='cyan', relief=RIDGE)
fm2.place(relx=0.2, rely=0.2, in_=fm21)

ne = len(qdb)
for i in range(1, ne + 1):
    n = i - 1
    button_dict1[i] = Button(fm2, text='   ' + str(i) + '   ', font=fs3, bg='white', fg='Black', anchor='center', highlightthickness=0.5, highlightbackground='black', command=lambda te=i-1: addinopn(int(te), qdb), relief=RAISED)
    button_dict1[i].grid(row=(n // 5), column=(n - ((n // 5) * 5)))

kq.mainloop()

def ent(i, lst):
    if tabel[i][0] in ('main', 'marks'):
        pass
    else:
        Label(fr3, text=str(tabel[i][0]).capitalize(), font=fs2, width=int(50), anchor='center', bg='#FF7F24', highlightthickness=1.5, highlightbackground='black', relief=FLAT).grid(column=1, row=int(i) + 1)
        button_dict2[i] = Button(fr3, text='Load', font=fs2, width=15, bg='#FAEBD7', anchor='center', highlightthickness=1.5, highlightbackground='black', command=lambda ht=i: opn(str(tabel[ht][0])), relief=RIDGE)
        button_dict2[i].grid(column=2, row=int(i) + 1)

def qbank(x, y):
    for i in entrq:
        if str(x) == str(i[0]) and str(y) == str(i[1]):
            genpaper(i[2])

def genpaper(name):
    def savecheck(l):
        global fmarks, attendlist, unattendlist, onum, dpa
        if l in unattendlist:
            c = int(onum)
            dpa = dta2[l - 1]
            anscor = dpa[6].lower()
            if (anscor == 'a' or anscor == 'aa'):
                if c == 1:
                    fmarks = fmarks + 4
                else:
                    fmarks = fmarks - 1
            elif (anscor == 'b' or anscor == 'bb'):
                if c == 2:
                    fmarks = fmarks + 4
                else:
                    fmarks = fmarks - 1
            elif (anscor == 'c' or anscor == 'cc'):
                if c == 3:
                    fmarks = fmarks + 4
                else:
                    fmarks = fmarks - 1
            elif (anscor == 'd' or anscor == 'dd'):
                if c == 4:
                    fmarks = fmarks + 4
                else:
                    fmarks = fmarks - 1
            attendlist.append(l)
            unattendlist.remove(l)
        addinque(l + 1)

    def clearcheck(l):
        global fmarks, attendlist, unattendlist, onum, dpa
        if l in attendlist:
            c = int(onum)
            dpa = dta2[l - 1]
            anscor = dpa[6].lower()
            if (anscor == 'a' or anscor == 'aa'):
                if c == 1:
                    fmarks = fmarks - 4
                else:
                    fmarks = fmarks + 1
            elif (anscor == 'b' or anscor == 'bb'):
                if c == 2:
                    fmarks = fmarks - 4
                else:
                    fmarks = fmarks + 1
            elif (anscor == 'c' or anscor == 'cc'):
                if c == 3:
                    fmarks = fmarks - 4
                else:
                    fmarks = fmarks + 1
            elif (anscor == 'd' or anscor == 'dd'):
                if c == 4:
                    fmarks = fmarks - 4
                else:
                    fmarks = fmarks + 1
            unattendlist.append(l)
            attendlist.remove(l)
        else:
            onum = 0
            cbtn1.deselect()
            cbtn2.deselect()
            cbtn3.deselect()
            cbtn4.deselect()
    
    def submbtn():
        global fmarks
        name = askstring('Name', 'Enter your Name : ')
        response = messagebox.askquestion('Submit', 'Submit ??')
        if response == 'yes':
            res.destroy()
            cursor.execute('insert into MARKS values(%s,%s)', (str(name), str(fmarks)))
            con.commit()
            text = 'Marks scored = ' + str(fmarks)
            messagebox.showinfo('Marks', text)
            fmarks = 0
        else:
            pass
    def addinque(nu):
        global qds, quefrs, ofrs, ofr, cc1, cc2, cc3, cc4, cbtn1, cbtn2, cbtn3, cbtn4, qds2, fsm1, onum, dpa, qrst, dpa
    
        try:
            quefrs.place_forget()
        except:
            pass
    
        num = nu
        quefrs = Frame(qds, width=(w*0.7)-4, height=(h*0.25)-2, highlightbackground='black', highlightthickness=0, bg='white')
        quefrs.place(relx=0, rely=0, in_=qds)
        quefr = Frame(qds, width=(w*0.7)-4, height=(h*0.25)-2, highlightbackground='black', highlightthickness=0, bg='white')
        quefr.place(relx=0, rely=0, in_=quefrs)
    
        dpa = dta2[nu-1]
        qrst = nu
    
        Label(quefr, text=str(str(num) + ')  ' + dpa[1]), fg='black', font=("Lucida Grande", 25), bg='white', width=41, highlightthickness=0).pack()
    
        try:
            cbtn1.config(text=dpa[2])
            cbtn2.config(text=dpa[3])
            cbtn3.config(text=dpa[4])
            cbtn4.config(text=dpa[5])
            onum = 0
        except:
            pass
    
        try:
            onum = 0
            cbtn1.deselect()
            cbtn2.deselect()
            cbtn3.deselect()
            cbtn4.deselect()
        except:
            pass

    def ckbtn(y):
        global onum
        print(onum)
        if onum == int(y):
            onum = 0
            cbtn1.deselect()
            cbtn2.deselect()
            cbtn3.deselect()
            cbtn4.deselect()
        else:
            cbtn1.deselect()
            cbtn2.deselect()
            cbtn3.deselect()
            cbtn4.deselect()
            onum = int(y)
            if onum == 1:
                cbtn1.select()
            elif onum == 2:
                cbtn2.select()
            elif onum == 3:
                cbtn3.select()
            elif onum == 4:
                cbtn4.select()
            else:
                pass
        print(onum)
        print()
    
    global fsm1, rfsm1, fs, fs2, fs3, onum, cbtn1, cbtn2, cbtn3, cbtn4, qds, rqds
    res = Tk()
    fs = tkFont.Font(family="Lucida Grande", size=30)
    fs2 = tkFont.Font(family="Lucida Grande", size=20)
    fs3 = tkFont.Font(family="Lucida Grande", size=40)
    res.geometry('%dx%d+0+0' % (w, h))
    
    rfsm1 = Frame(res, width=w, height=h, highlightbackground='black', highlightthickness=1.5, bg='#FFD39B')
    rfsm1.place(relx=0, rely=0, in_=res)
    fsm1 = Frame(rfsm1, width=w, height=h, highlightbackground='black', highlightthickness=1.5, bg='#FFD39B')
    fsm1.place(relx=0, rely=0, in_=rfsm1)
    
    cursor.execute('select * from ' + name)
    dta2 = cursor.fetchall()
    for i in range(1, len(dta2)+1):
        unattendlist.append(i)
    
    rqds = Frame(fsm1, width=w*0.7, height=h*0.65, highlightbackground='black', highlightthickness=1, bg='white')
    rqds.place(x=w*0.05, y=h*0.15, in_=fsm1)
    qds = Frame(rqds, width=(w*0.7-4), height=(h*0.65-3), highlightbackground='black', highlightthickness=1, bg='white')
    qds.place(relx=0, rely=0, in_=rqds)
    
    rqds2 = Frame(fsm1, width=w*0.9, height=h*0.08, highlightbackground='black', highlightthickness=1, bg='white')
    rqds2.place(x=w*0.05, y=h*0.85, in_=fsm1)
    qds2 = Frame(rqds2, width=(w*0.9)-2, height=(h*0.08)-2, highlightbackground='black', highlightthickness=1, bg='white')
    qds2.place(relx=0, rely=0, in_=rqds2)
    
    rqds3 = Frame(fsm1, width=w*0.15, height=h*0.65, highlightbackground='black', highlightthickness=1, bg='white')
    rqds3.place(x=w*0.8, y=h*0.15, in_=fsm1)
    qds3 = Frame(rqds3, width=(w*0.15)-2, height=(h*0.65)-2, highlightbackground='black', highlightthickness=1, bg='white')
    qds3.place(relx=0, rely=0, in_=rqds3)
    
    quefrs = Frame(qds, width=(w*0.7)-4, height=(h*0.25)-2, highlightbackground='black', highlightthickness=0, bg='white')
    quefrs.place(relx=0, rely=0, in_=qds)
    quefr = Frame(qds, width=(w*0.7)-4, height=(h*0.25)-2, highlightbackground='black', highlightthickness=0, bg='white')
    quefr.place(relx=0, rely=0, in_=quefrs)
    
    ofrs = Frame(qds, width=(w*0.7)-4, height=(h*0.4)-2, highlightbackground='black', highlightthickness=0, bg='white')
    ofrs.place(relx=0, y=(h*0.25), in_=qds)
    ofr = Frame(qds, width=(w*0.7)-4, height=(h*0.4)-2, highlightbackground='black', highlightthickness=0, bg='white')
    ofr.place(relx=0.2, rely=0, in_=ofrs)
    
    for i in range(1, len(dta2)+1):
        n = i - 1
        btndict[i] = Button(qds3, text='   ' + str(i) + '   ', font=fs3, bg='white', fg='Black', anchor='center', highlightthickness=0.5, highlightbackground='black', command=lambda te=i: addinque(te), relief=RAISED)
        btndict[i].grid(row=(n//3), column=(n-((n//3)*3)))
    
    addinque(1)
    cbtn1 = Radiobutton(ofr, text=dpa[2], font=("Lucida Grande", 20), bg='white', width=20, variable=cc1, value=1, tristatevalue=0, command=lambda: ckbtn(1))
    cbtn2 = Radiobutton(ofr, text=dpa[3], font=("Lucida Grande", 20), bg='white', width=20, variable=cc2, value=2, tristatevalue=0, command=lambda: ckbtn(2))
    cbtn3 = Radiobutton(ofr, text=dpa[4], font=("Lucida Grande", 20), bg='white', width=20, variable=cc3, value=3, tristatevalue=0, command=lambda: ckbtn(3))
    cbtn4 = Radiobutton(ofr, text=dpa[5], font=("Lucida Grande", 20), bg='white', width=20, variable=cc4, value=4, tristatevalue=0, command=lambda: ckbtn(4))
    
    cbtn1.grid(column=1, row=0)
    cbtn2.grid(column=1, row=1)
    cbtn3.grid(column=1, row=2)
    cbtn4.grid(column=1, row=3)
    
    savebutton = Button(qds2, text='  Save and Next  ', font=fs2, width=15, bg='white', highlightthickness=1.5, highlightbackground='black', command=lambda: savecheck(qrst), relief=RIDGE)
    clearbutton = Button(qds2, text='   Clear   ', font=fs2, width=15, bg='white', highlightthickness=1.5, highlightbackground='black', command=lambda: clearcheck(qrst), relief=RIDGE)
    submitbutton = Button(qds2, text='   Submit   ', font=fs2, width=15, bg='white', highlightthickness=1.5, highlightbackground='black', command=submbtn, relief=RIDGE)
    
    savebutton.grid(column=0, row=0)
    clearbutton.grid(column=1, row=0)
    submitbutton.grid(column=2, row=0)
    
    print(onum)
    res.mainloop()

def lgp():
    global btn1, fr1c, fr4, fr5c, useent, pcent, entrq

    try:
        btn1.place_forget()
        fr3.place_forget()
    except:
        pass

    fr4c = Frame(fr1, width=w * 0.8, height=h, bg='white', highlightthickness=0, highlightbackground='black', relief=RAISED)
    fr4c.place(relx=0.2, rely=0)
    fr4 = Frame(fr4c, width=w * 0.8, height=h, bg='white', highlightthickness=0, highlightbackground='black', relief=RAISED)
    fr4.place(relx=0, rely=0, in_=fr4c)
    btn1 = Button(fr2, text='     ARCHIVES      ', font=fs2, fg='white', bg='#8B4726', relief=FLAT, command=arvp)
    btn1.place(x=5, y=10, in_=fr2)
    fr1c = Frame(fr1, width=w * 0.8, height=h * 0.1, bg='#FFD39B', highlightthickness=0, highlightbackground='black')
    fr1c.place(relx=0.2, rely=0)
    Label(fr1c, text='                         LOGIN PAGE', font=fs, fg='black', bg='#FFD39B').place(relx=0, rely=0, in_=fr1c)

    cursor.execute('select * from main')
    entrq = cursor.fetchall()

    fr5c = Frame(fr4, width=w * 0.35, height=h * 0.4, bg='#FF7F24', highlightthickness=1, highlightbackground='black', relief=RAISED)
    fr5c.place(relx=0.3, rely=0.314, in_=fr4)
    fr5 = Frame(fr5c, width=w * 0.3488, height=h * 0.397, bg='#FF7F24', highlightthickness=0, highlightbackground='white', relief=RAISED)
    fr5.place(relx=0, rely=0.3, in_=fr5c)
    Label(fr5, text='    User ID :   ', font=fs2, fg='black', bg='#FF7F24').grid(row=0, column=0)
    Label(fr5, text='    Password : ', font=fs2, fg='black', bg='#FF7F24').grid(row=1, column=0)
    useent = Entry(fr5, width=25, highlightbackground='black', highlightthickness=1, relief=RIDGE, font=tkFont.Font(family="Lucida Grande", size=15))
    useent.grid(column=1, row=0)
    pcent = Entry(fr5, width=25, highlightbackground='black', highlightthickness=1, relief=RIDGE, font=tkFont.Font(family="Lucida Grande", size=15))
    pcent.grid(column=1, row=1)
    Button(fr5, text='  Proceed  ', highlightbackground='black', highlightthickness=1, relief=RIDGE, font=fs4, command=lambda: qbank(str(useent.get()), str(pcent.get()))).grid(column=1, row=2)

    aroot.geometry('%dx%d+0+0' % (w, h))


def arvp():
    global btn1, fr3c, fr3

    try:
        btn1.place_forget()
        fr4.place_forget()
    except:
        pass

    btn1 = Button(fr2, text='         LOGIN         ', font=fs2, fg='white', bg='#8B4726', relief=FLAT, command=lgp)
    btn1.place(x=5, y=10, in_=fr2)
    fr3c = Frame(fr1, width=w * 0.8, height=h * 0.9, bg='white', highlightthickness=0, highlightbackground='black', relief=RAISED)
    fr3c.place(relx=0.2, rely=0.1)
    fr3 = Frame(fr3c, width=w * 0.8, height=h * 0.9, bg='#FF7F24', highlightthickness=1, highlightbackground='black', relief=RAISED)
    fr3.place(relx=0, rely=0, in_=fr3c)
    Label(fr1c, text='                       ARCHIVE PAGE', font=fs, fg='black', bg='#FFD39B').place(relx=0, rely=0, in_=fr1c)
    for i in range(0, len(tabel)):
        ent(i, tabel)


def arwin():
    global fr1, fr2, fr3, btn1

    fr1 = Frame(aroot, width=w, height=h, bg='white', highlightthickness=0, highlightbackground='black')
    fr1.place(x=0, y=0)
    fr1c = Frame(fr1, width=w * 0.8, height=h * 0.1, bg='white', highlightthickness=0, highlightbackground='black')
    fr1c.place(relx=0.2, rely=0)
    fr2 = Frame(fr1, width=w * 0.2, height=h, bg='#FFD39B', highlightthickness=0, highlightbackground='black', relief=RAISED)
    fr2.place(x=0, y=0)
    lgp()
    arwin()
    aroot.mainloop()


if tll == True:
    root = Tk()
    style = ttk.Style()
    style.configure("Treeview.Heading", font=("Lucida Grande", 25))
    style.configure("Treeview.Insert", font=("Lucida Grande", 25))

    root.geometry('%dx%d+0+0' % (w, h))
    fs2k = tkFont.Font(family="Lucida Grande", size=5)
    cfr = Frame(root, width=w, height=h, bg='light pink')
    fr = Frame(cfr, width=w, height=h, bg='light pink')
    cfr.place(x=0, y=0)
    fr.place(relx=0, rely=0, in_=cfr)
    fr1 = Frame(fr, width=w * 0.6, height=h * 0.8, bg='white', highlightbackground='black', highlightthickness=2)
    fr1.place(relx=0.2, rely=0.1, in_=fr)
    Label(fr1, text='                             SCORE CARD ', font=tkFont.Font(family="Lucida Grande", size=25), fg='black', bg='white').place(relx=0, rely=0, in_=fr1)
    fr1a = Frame(fr, width=w * 0.5, height=h * 0.7, bg='white', highlightbackground='black', highlightthickness=2)
    fr1a.place(x=w * 0.05, y=h * 0.05, in_=fr1)
    fr1b = Frame(fr1a, width=w * 0.49, height=h * 0.69, bg='white', highlightbackground='black', highlightthickness=0)
    fr1b.place(relx=0, rely=0, in_=fr1a)
    tree = ttk.Treeview(fr1b, columns=("name", "marks"), show='headings', height=22)
    tree.heading('name', text='Name')
    tree.heading('marks', text='Marks')
    tree.column('name', width=int((w * 0.49) // 2) + 4, anchor=CENTER)
    tree.column('marks', width=int((w * 0.49) // 2) + 4, anchor=CENTER)
    cursor.execute('select * from marks')
    dar = cursor.fetchall()
    print(dar, dar[0])
    dar = list(dar)
    for i in dar:
        i = list(i)
        num = 30 - len(str(i[0]))
        num2 = 30 - len(str(i[1]))
        i[0] = ' ' * (num // 2) + str(i[0]) + ' ' * (num - num // 2)
        i[1] = ' ' * (num2 // 2) + str(i[1]) + ' ' * (num2 - num2 // 2)

        tree.insert('', END, values=i)

  tree.grid(row=0, column=0, sticky='nsew')
  root.mainloop()
