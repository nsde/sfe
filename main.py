import tkinter as tk
import webbrowser, tkinter.scrolledtext, tkinter.messagebox, tkinter.filedialog, tkinter.colorchooser, sys, os

print('\n')

#TK-Window Stuff
win = tk.Tk()
win.title('New File | SFE Alpha 1.0')
win.geometry('1400x620')
win.minsize(200,200)
win.maxsize(1920,1080)
win.configure(bg='black')
win.iconphoto(False,tk.PhotoImage(file='C:/Styx/SFE/assets/pictures/icon.png'))

menubar = tk.Menu(win)

filemenu = tk.Menu(win,tearoff=0)
editmenu = tk.Menu(win,tearoff=0)
thememenu = tk.Menu(win,tearoff=0)
settingsmenu = tk.Menu(win,tearoff=0)
helpmenu = tk.Menu(win,tearoff=0)

l = ['empty','text']
l.clear()

# Error popup
def errormsg():
    errpopup = tkinter.messagebox.Message(win,type=tkinter.messagebox.ABORTRETRYIGNORE,icon=tkinter.messagebox.ERROR,title='ERROR',message='We are sorry about that. Please visit \ngithub.com/nsde/sfe/issues\nand report the problem. Thanks!\n\n(We recommend clicking on retry. Warning: "retry" could corrupt files!)')
    errorasw = errpopup.show()    

    if errorasw == 'abort':
        sys.exit(0)
    elif errorasw == 'retry':
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
    else:
        return
        
# Save the i
def savefile():
    flpath = tk.filedialog.asksaveasfilename(title='Save file | SFE',filetypes=(('Text files','*.txt'),('All files','*.*')))
    winttl = flpath + ' | SFE'
    win.title(winttl)
    
    try:
        f1 = open(flpath + 'w+')
    except:
        if flpath == '':
            refresh()
            t["font"] = 'Arial','30'
            t["fg"] = 'black'
            t["bg"] = 'orange'
            t.insert("end",'\n***SFE-INFO***\nERROR: Please select a valid file path and try again.')
            savefile()
        else:
            t["font"] = 'Arial','30'
            t["fg"] = 'black'
            t["bg"] = 'red'
            t.insert("end",'\n***SFE-INFO***\nERROR: Couldn\'t save file')
            errormsg()

    f1.write(str(t.get()))
    f1.close()
    return f1

def openfile():
    flpath = tk.filedialog.askopenfilename(title='Open file | SFE',filetypes=(('Text files','*.txt'),('All files','*.*')))

    winttl = flpath + ' | SFE'
    win.title(winttl)

    flpath = str(flpath)

    try:
        f1 = open(flpath,'r')
    except:
        t["font"] = 'Arial','30'
        t["fg"] = 'black'
        t["bg"] = 'red'
        t.insert("end",'')
        errormsg()

    q = f1.read()
    opaw = tkinter.messagebox
    if opaw:
        pass
    else:
        pass
    t.insert("end",q)
    f1.close()
    return f1

def quit():
    aw_quit = tk.messagebox.askyesno(title='Quit?', message='All not saved data will be lost! Do you want to continue?')
    # Yee, this is so dumb: if your code is open source, you can't really make eastereggs :(
    # (Because they will be able to read the easteregg)
    # nvm

    global easteregg_quit
    try:
        pass
        # easteregg_quit +=1
    except:
        easteregg_quit = 1

    if aw_quit == 1:
        win.destroy()
    else:
        if easteregg_quit == 3:
            t["font"] = 'Arial','30'
            t["fg"] = 'white'
            t["bg"] = 'green'
            t.insert("end",'\n\n\nThis is a little easteregg :)\nThanks for using SFE <3')
        
        return

def undo():
    try:
        refresh()
    except:
        pass

def redo():
    betainfo()

def fontinfo():
    tkinter.messagebox.showinfo('Information about Fonts','If a font doesn\'t work, you maybe haven\'t installed it yet.\
        On Windows ten, open your the following: settings > Personalisation > Fonts. There, you can manage your fonts.\
        \n\nIf you can\'t write specifitc symbols, try another font: some fonts don\'t support\
        every language and symbol!')

def betainfo():
    tkinter.messagebox.showinfo('Not avaiable yet','Sorry, but this feature is planned.\
        Please help us on "github.com/nsde/sfe/issues" by making suggestions!')

def deleteall():
    aw_delall = tk.messagebox.askyesno(title='Delete all?', message='All not saved data will be lost! Do you want to continue?')
    if aw_delall == 1:
        t.set()
    else:
        return

def refresh():
    pass

#----------------- Help

def webbugs():
    webbrowser.open('https://github.com/nsde/sfe/issues')

def webemail():
    webbrowser.open('mailto:neostyx@pm.me')

def webdoc():
    webbrowser.open('https://github.com/nsde/sfe/wiki')

#----------------- Search

def search():
    pass

def themeidea():
    #----------------- Custom Theme

    # def customtheme():
    #     global ctw
    #     ctw = tk.Tk()
    #     ctw.title('Custom Theme')
    #     ctw.geometry('600x350')
    #     # ctw.iconphoto(False,tk.PhotoImage(file='C:/Styx/SFE/assets/pictures/icon.png'))

    #     global fgc
    #     global bgc
    #     fgc = None
    #     bgc = None

    #     def pickfg():
    #         global ctw
    #         global fgc
    #         ctw.destroy()
    #         fgc = tkinter.colorchooser.askcolor()
    #         customtheme()
    #         fgc = fgc[1]
            
    #         # sfecachefg = open('C:/Styx/SFE/cache/preview_colorfg_customtheme.txt', 'w+')
    #         sfecachefg.write('fgc\n')
    #         sfecachefg.close()

    #     def pickbg():
    #         global ctw
    #         global bgc
    #         ctw.destroy()
    #         bgc = tkinter.colorchooser.askcolor()
    #         customtheme()
    #         bgc = bgc[1]
    #         # sfecachebg = open('C:/Styx/SFE/cache/preview_colorbg_customtheme.txt', 'w+')
    #         sfecachebg.write('bgc\n')
    #         sfecachefg.close()

    #     fgbtn = tk.Button(ctw,text='Choose foregroud color',command=pickfg)
    #     bgbtn = tk.Button(ctw,text='Choose background color',command=pickbg)

    #     fgbtn.pack()
    #     bgbtn.pack()
    
    #     pvtxt = tk.Label(ctw,text='PreviewText Abc123!?.')
    #     pvtxt.pack()
        
    #     sfecachefg = open()
    #     sfecachebg = open()

    #     fgc = sfecachefg.readline(0)
    #     bgc = sfecachebg.readline(0)

    #     pvtxt["fg"] = fgc
    #     pvtxt["bg"] = bgc

    #     ctw.mainloop()
    pass

#-------------------------------------------------------

def styxtheme():
    t["font"] = 'Yu Gothic UI Semilight', 20
    t["fg"] = 'white'
    t["bg"] = '#141414'

def styxblue():
    t["font"] = 'Yu Gothic UI Semilight', 20
    t["fg"] = '#006DCC'
    t["bg"] = '#141414'    

def styxpurple():
    t["font"] = 'Yu Gothic UI Semilight', 20
    t["fg"] = '#7800CC'
    t["bg"] = '#141414'

def styxmidnight():
    t["font"] = 'Yu Gothic UI Semilight', 20
    t["fg"] = 'white'
    t["bg"] = 'black'

def classic():
    t["font"] = 'Times', 18
    t["fg"] = 'black'
    t["bg"] = 'white'

def kid():
    t["font"] = 'Kristen ITC', 25
    t["fg"] = '#290038'
    t["bg"] = '#C9BACC'

def notepad():
    t["font"] = 'Ink Free', 25
    t["fg"] = '#000026'
    t["bg"] = '#CCC995'

def modern():
    t["font"] = 'Arial', 20
    t["fg"] = 'black'
    t["bg"] = 'white'

def moderndark():
    t["font"] = 'Arial', 20
    t["fg"] = 'white'
    t["bg"] = '#141414'

def console():
    t["font"] = 'Consolas', 18
    t["fg"] = 'green'
    t["bg"] = 'black'

def devil():
    t["font"] = 'Chiller', 24
    t["fg"] = 'red'
    t["bg"] = 'black'

def steel():
    t["font"] = 'Bahnschrift', 20
    t["fg"] = '#B0B0B0'
    t["bg"] = '#1A1A1A'

filemenu.add_command(label='Save',command=savefile)
filemenu.add_command(label='Open',command=openfile)
filemenu.add_separator()
filemenu.add_command(label='Quit',command=quit)

menubar.add_cascade(label='File',menu=filemenu)

editmenu.add_command(label='Undo',command=undo)
# editmenu.add_command(label='Redo',command=redo)
editmenu.add_command(label='Search',command=search)
editmenu.add_separator()
editmenu.add_command(label='Delete whole text',command=deleteall)

menubar.add_cascade(label='Edit',menu=editmenu)

thememenu.add_separator()
thememenu.add_command(label='STYX THEMES')
thememenu.add_separator()
thememenu.add_command(label='Styx',command=styxtheme)
thememenu.add_command(label='Styx Blue',command=styxblue)
thememenu.add_command(label='Styx Purple',command=styxpurple)
thememenu.add_command(label='Styx Midnight',command=styxmidnight)
thememenu.add_separator()
thememenu.add_command(label='BASIC THEMES')
thememenu.add_separator()
thememenu.add_command(label='Basic (Standard)',command=modern)
thememenu.add_command(label='Classic',command=classic)
thememenu.add_command(label='Dark',command=moderndark)
thememenu.add_command(label='Console',command=console)
thememenu.add_command(label='Steel',command=steel)
thememenu.add_separator()
thememenu.add_command(label='UNUSUAL THEMES')
thememenu.add_separator()
thememenu.add_command(label='Little kid',command=kid)
thememenu.add_command(label='Notepad',command=notepad)
thememenu.add_command(label='Devil',command=devil)

menubar.add_cascade(label='Theme',menu=thememenu)

# settingsmenu.add_command(label='Custom Theme',command=customtheme)

menubar.add_cascade(label='Settings',menu=settingsmenu)

helpmenu.add_command(label='Report Bugs and Errors',command=webbugs)
helpmenu.add_command(label='Open Documentation',command=webdoc)
helpmenu.add_command(label='Font tips',command=fontinfo)
helpmenu.add_separator()
helpmenu.add_command(label='E-Mail us',command=webemail)
menubar.add_cascade(label='?',menu=helpmenu)

win.config(menu=menubar)

t = tk.scrolledtext.ScrolledText(win, width = 1300, height = 800,bd=2)
t.pack()

modern()

win.mainloop()
