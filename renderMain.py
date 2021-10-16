import tkinter
from tkinter.font import Font
from PIL import ImageTk, Image

def identifyModule(toRender):
    i = 0
    print(toRender)
    textTags = ["<h1>", "<h2>", "<h3>", "<h4>", "<h5>", "<h6>", "<p>"]
    tagsFound = []
    while(i < len(toRender)):
        
        if toRender[i] in textTags and "/" not in toRender[i]:
            tagsFound.append(toRender[i])
            tagsFound.append(toRender[i+1])
        if "img" in toRender[i]:
            tagsFound.append(toRender[i])
       
        i+=1
    startWindow(tagsFound, textTags)

def startWindow(toRender, TT):
    root = tkinter.Tk()
    root.configure(bg='white', padx=8, pady=8)
    root.geometry("1900x1200")
    root.title("Katana 0.02")
    u = 0
    print(toRender)
    while(u < len(toRender)):
        if toRender[u-1] in TT:
            renderText(toRender, u, root)
        if "<img" in toRender[u]:
            renderImage(root, toRender[u])
        u+=1
    #root.destroy()
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
    myFont = Font(family="SF Pro bold", size=int(textSize))
    if "<p>" in TRtext[ITR-1]:
        myFont.configure(family="SF Pro")
    text = tkinter.Label(TTR, text=TRtext[ITR], fg="black", height= 1, borderwidth=0, bg='white', font=myFont)
    text.pack(side=tkinter.TOP, anchor=tkinter.NW)
#Render image after finding the file
def renderImage(root, tags):
    global img
    img = ImageTk.PhotoImage(Image.open(findTarget(tags)))
    panel = tkinter.Label(root, width=img.width(), height=img.height(), bg='white', highlightthickness=0, image=img, anchor=tkinter.NW)
    panel.image = img
    panel.pack(anchor=tkinter.NW)

def findTarget(item):
    #Loop through the item to find a quotation mark 

    i = 0
    fileName = ""
    while (item[i] != "\""):
        i+=1
    #then find the name of the file by moving to the next mark
    i+=1

    while (item[i] != "\""):
        fileName += item[i]
        i+=1
    return fileName
