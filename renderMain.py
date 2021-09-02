import tkinter
from tkinter.font import Font

def identifyModule(toRender):

    i = 0
    d = 0
    textTags = ["<h1>", "<h2>", "<h3>", "<h4>", "<h5>", "<h6>", "<p>"]
    textTagsFound = []
    while(i < len(toRender)):
        
        if toRender[i] in textTags and "/" not in toRender[i]:
            textTagsFound.append(toRender[i])
            textTagsFound.append(toRender[i+1])
            d+=1
        i+=1
    startWindow(textTagsFound, textTags)

def startWindow(TTF, TT):
    root = tkinter.Tk()
    root.configure(bg='white', padx=8, pady=8)
    root.geometry("1900x1200")
    root.title("ZeroBlade")
    u = 0
    while(u < len(TTF)):
        if not TTF[u] in TT:
            renderText(TTF, u, root)
        u+=1
    root.mainloop()


def renderText(TRtext, ITR, TTR):

    textSize = 16
    
    if "<h1>" in TRtext[ITR-1]:
        textSize = 32
    if "<h2>" in TRtext[ITR-1]:
        textSize = 24
    if "<h3>" in TRtext[ITR-1]:
        textSize = 20.8
    if "<h4>" in TRtext[ITR-1]:
        textSize = 16
    if "<h5>" in TRtext[ITR-1]:
        textSize = 12.8
    if "<h6>" in TRtext[ITR-1]:
        textSize = 11.2
    if "<p>" in TRtext[ITR-1]:
        textSize = 16

    text = tkinter.Label(TTR, text=TRtext[ITR], fg="black", height= 1, borderwidth=0, bg='white')
    text.pack(side=tkinter.TOP, anchor=tkinter.NW)

    myFont = Font(family="SF Pro", size=int(textSize))
    text.configure(font=myFont)
