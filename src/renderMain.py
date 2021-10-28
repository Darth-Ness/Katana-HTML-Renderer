import tkinter
def startWindow(toRender):

    root = tkinter.Tk()
    textTags = ["h1", "h2", "h3", "h4", "h5", "h6", "p"]
    root.configure(bg='white', padx=8, pady=8)
    root.title("Katana 0.03")
    u = 0
    while(u < len(toRender)):
        if toRender[u] in textTags:
            renderText(toRender, u, root)
        if "img" in toRender[u]:
            renderImage(root, toRender[u])
        if "button" in toRender[u] and not "/" in toRender[u]:
            renderButton(root, toRender[u+1])
        u+=1
    
    #root.destroy()
    root.mainloop()


def renderText(TRtext, ITR, TTR):
    from tkinter.font import Font
    textSize = 12

    if "h1" in TRtext[ITR]:
        textSize = 23.9
    if "h2" in TRtext[ITR]:
        textSize = 17.9
    if "h3" in TRtext[ITR]:
        textSize = 14
    if "h4" in TRtext[ITR]:
        textSize = 15.9
    if "h5" in TRtext[ITR]:
        textSize = 9.9
    if "h6" in TRtext[ITR]:
        textSize = 8
    myFont = Font(family="SF Pro bold", size=int(textSize))
    text = tkinter.Label(TTR, text=TRtext[ITR+1], fg="black", height= 1, borderwidth=0, bg='white', font=myFont)
    text.pack(side=tkinter.TOP, anchor=tkinter.NW)
#Render image after finding the file
def renderImage(root, tags):
    from PIL import ImageTk, Image
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

def renderButton(window, text):
    button = tkinter.Button(window, text=text)
    button.pack(anchor=tkinter.NW)
