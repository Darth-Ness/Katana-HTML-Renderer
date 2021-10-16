import tkinter
from tkinter.font import Font

def identifyModule(toRender):
    print(toRender)
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
    root.title("Katana")
    u = 0
    while(u < len(TTF)):
        if not TTF[u] in TT:
            renderText(TTF, u, root)
        u+=1
    root.mainloop()


def renderText(TRtext, ITR, TTR):

    textSize = 12
    
    if "<h1>" in TRtext[ITR-1]:
        textSize = 23.9
    if "<h2>" in TRtext[ITR-1]:
        textSize = 17.9
    if "<h3>" in TRtext[ITR-1]:
        textSize = 14
    if "<h4>" in TRtext[ITR-1]:
        textSize = 15.9
    if "<h5>" in TRtext[ITR-1]:
        textSize = 9.9
    if "<h6>" in TRtext[ITR-1]:
        textSize = 8

    text = tkinter.Label(TTR, text=TRtext[ITR], fg="black", height= 1, borderwidth=0, bg='white')
    text.pack(side=tkinter.TOP, anchor=tkinter.NW)

    myFont = Font(family="SF Pro", size=int(textSize)-3)
    text.configure(font=myFont)
