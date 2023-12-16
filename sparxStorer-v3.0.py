import tkinter as tk
from tkinter import colorchooser

storedAnswers = {
    
}

window = tk.Tk()
window.geometry('750x500')
window.configure(bg = '#303030')
window.title('Sparx Storer')
window.resizable(False,False)

currentEntry = tk.StringVar()
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabetNum = tk.IntVar()
alphabetNum.set(0)
questionNum = tk.IntVar()
questionNum.set(1)
currentCode = tk.StringVar(value = '1A')
viewingBookwork = tk.StringVar()
currentViewCode = tk.StringVar()
viewingBookwork.set('Not currently viewing a code.')

def getCurrentCode():
    currentCode = str(questionNum.get()) + str(alphabet[alphabetNum.get()])
    return currentCode

def nextLetter():
    alphabetNum.set(alphabetNum.get()+1)
    if alphabetNum.get() > 25:
        alphabetNum.set(0)
    currentCode.set(getCurrentCode())
    
def nextNumber():
    questionNum.set(questionNum.get()+1)
    alphabetNum.set(0)
    currentCode.set(getCurrentCode())
    
def prevNumber():
    questionNum.set(questionNum.get()-1)
    currentCode.set(getCurrentCode())
    
def prevLetter():
    alphabetNum.set(alphabetNum.get()-1)
    if alphabetNum.get() < 0:
        alphabetNum.set(25)
    currentCode.set(getCurrentCode())

def submitEntry():
    storedAnswers[currentCode.get()] = currentEntry.get()
    alphabetNum.set(alphabetNum.get()+1)
    currentCode.set(getCurrentCode())
    currentEntry.set('')
    
def clearBWVEntry():
    viewingBookwork.set('Not currently viewing a code.')

def viewBookwork():
    try: viewingBookwork.set(storedAnswers[bookworkViewEntry.get().upper()])
    except:
        viewingBookwork.set('Code not found...')
        window.after(1000, clearBWVEntry)
    currentViewCode.set('')

def saveAllCodes():
    storedAnswersFormatted = "Codes:\n\n"
    with open("SAVEDCODES.txt", "w") as file:
        for key in storedAnswers.keys():
            storedAnswersFormatted += key + ": " + storedAnswers[key] + "\n"
        file.write(storedAnswersFormatted)
        
def chooseColour():
    colour = colorchooser.askcolor(title ="Change Theme")[1]
    colourChooseBtn.configure(bg = colour)
    currentCodeLabel.configure(bg = colour)
    infoLabel2.configure(bg = colour)
    entry.configure(bg = colour)
    submitBtn.configure(bg = colour)
    infoLabel4.configure(bg = colour)
    infoLabel3.configure(bg = colour)
    nextLetterBtn.configure(bg = colour)
    nextNumberBtn.configure(bg = colour)
    prevLetterBtn.configure(bg = colour)
    prevNumberBtn.configure(bg = colour)
    infoLabel1.configure(bg = colour)
    bookworkViewEntry.configure(bg = colour)
    bookworkViewConfirm.configure(bg = colour)
    bookworkViewLabel.configure(bg = colour)
    saveCodesBtn.configure(bg = colour)
    infoLabel5.configure(bg = colour)
    colourChooseBtn.configure(bg = colour)
    titleLabel.configure(bg = colour)
    versionLabel.configure(bg = colour)

currentCodeLabel = tk.Label(
    window,
    textvariable = currentCode,
    font = ("Arial", 25),
    bg = '#2020A0',
    fg = "White"
)

entry = tk.Entry(
    window,
    textvariable = currentEntry,
    font = ("Arial", 25),
    bg = '#2020A0',
    fg = "White"
)

submitBtn = tk.Button(
    window,
    text = "Store",
    command = submitEntry,
    font = ("Arial", 16),
    bg = '#2020A0',
    fg = "White"
)

nextLetterBtn = tk.Button(
    window,
    text = "+",
    command = nextLetter,
    font = ("Arial", 17),
    bg = '#2020A0',
    fg = "White"
)

nextNumberBtn = tk.Button(
    window,
    text = "+",
    command = nextNumber,
    font = ("Arial", 17),
    bg = '#2020A0',
    fg = "White"
)

prevNumberBtn = tk.Button(
    window,
    text = "-",
    command = prevNumber,
    font = ("Arial", 17),
    bg = '#2020A0',
    fg = "White"
)

prevLetterBtn = tk.Button(
    window,
    text = "-",
    command = prevLetter,
    font = ("Arial", 17),
    bg = '#2020A0',
    fg = "White"
)

bookworkViewLabel = tk.Label(
    window,
    textvariable = viewingBookwork,
    font = ("Arial", 25),
    bg = '#2020A0',
    fg = "White"
)

bookworkViewEntry = tk.Entry(
    window,
    textvariable = currentViewCode,
    font = ("Arial", 25),
    bg = '#2020A0',
    fg = "White",
    width=3
)

bookworkViewConfirm = tk.Button(
    window,
    text = 'Enter',
    command = viewBookwork,
    font = ("Arial Bold", 16),
    bg = '#2020A0',
    fg = "White"
)

infoLabel1 = tk.Label(
    window,
    text = 'Enter a bookwork code',
    font = ("Arial", 25),
    bg = '#2020A0',
    fg = "White"
)

infoLabel2 = tk.Label(
    window,
    text = 'Current Code:',
    font = ("Arial", 25),
    bg = '#2020A0',
    fg = "White"
)

infoLabel3 = tk.Label(
    window,
    text = 'Number',
    font = ("Arial", 25),
    bg = '#2020A0',
    fg = "White"
)

infoLabel4 = tk.Label(
    window,
    text = 'Letter    ',
    font = ("Arial", 25),
    bg = '#2020A0',
    fg = "White"
)

infoLabel5 = tk.Label(
    window,
    text = 'Save all your bookwork\ncodes into a text file.',
    font = ("Arial", 17),
    bg = '#2020A0',
    fg = "White"
)

saveCodesBtn = tk.Button(
    window,
    text = 'Save',
    command = saveAllCodes,
    font = ("Arial Bold", 21),
    bg = '#2020A0',
    fg = "White"
)

colourChooseBtn = tk.Button(
    window,
    text = 'Change\nTheme',
    command = chooseColour,
    font = ("Arial Bold", 15),
    bg = '#2020A0',
    fg = "White"
)

titleLabel = tk.Label(
    window,
    text = 'Sparx Storer',
    font = ("Arial", 27),
    bg = '#2020A0',
    fg = "White"
)

versionLabel = tk.Label(
    window,
    text = 'v3.0',
    font = ("Arial", 14),
    bg = '#2020A0',
    fg = "White"
)

currentCodeLabel.place(anchor = 'nw', relx = 0.31)
infoLabel2.place(anchor='nw', relx = 0.02)
entry.place(anchor='nw', relx = 0.02, rely = 0.1)
submitBtn.place(anchor='nw', relx = 0.51, rely = 0.1)
infoLabel4.place(anchor='nw', relx = 0.07, rely  = 0.2)
infoLabel3.place(anchor='nw', relx = 0.07, rely = 0.3)
nextLetterBtn.place(anchor = 'nw', relx = 0.25, rely = 0.2)
nextNumberBtn.place(anchor = 'nw', relx = 0.25, rely = 0.3)
prevLetterBtn.place(anchor = 'nw', relx = 0.02, rely = 0.2)
prevNumberBtn.place(anchor = 'nw', relx = 0.02, rely = 0.3)

infoLabel1.place(anchor = 'nw', relx = 0.02, rely = 0.5)
bookworkViewEntry.place(anchor = 'nw', relx = 0.02, rely = 0.6)
bookworkViewConfirm.place(anchor = 'nw', relx = 0.11, rely = 0.6)
bookworkViewLabel.place(anchor = 'nw', relx = 0.02, rely = 0.7)
saveCodesBtn.place(anchor = 'nw', relx = 0.86, rely = 0.85)
infoLabel5.place(anchor = 'nw', relx = 0.53, rely = 0.85)
colourChooseBtn.place(anchor = 'nw', relx = 0.86, rely = 0.7)

titleLabel.place(anchor = 'nw', relx = 0.7)
versionLabel.place(anchor = 'nw', relx = 0.02, rely = 0.93)

window.mainloop()

print('Quitting..')