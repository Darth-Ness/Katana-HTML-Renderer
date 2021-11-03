import tkinter
def startWindow(toRender, isOnline, fileName):

    root = tkinter.Tk()
    textTags = ["h1", "h2", "h3", "h4", "h5", "h6", "p"]
    root.configure(bg='white', padx=8, pady=8)
    isCentered = False
    u = 0
    while(u < len(toRender)):
        if toRender[u] in textTags:
            renderText(toRender, u, root, isCentered)
        if "img" in toRender[u]:
            renderImage(root, toRender[u], isOnline, fileName, isCentered)
        if "button" in toRender[u] and not "/" in toRender[u]:
            renderButton(root, toRender[u+1], isCentered)
        if "br" in toRender[u]:
            renderBreak(root,isCentered)
        if "center" in toRender[u]:
            isCentered = True
        if "/center" in toRender[u]:
            isCentered = False
        if "title" in toRender[u]:
            setTitle(root, toRender[u+1])
        if "hr" in toRender[u]:
            renderHRule(root)
        u+=1
    #root.destroy()
    root.mainloop()


def renderText(TRtext, ITR, TTR, C):
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
    if (C):
        text.pack(side=tkinter.TOP, anchor=tkinter.CENTER)
    else:
        text.pack(side=tkinter.TOP, anchor=tkinter.NW)
#Render image after finding the file
def renderImage(root, tags, isOnline, url, isCentered):
    from PIL import ImageTk, Image
    global img
    img = ImageTk.PhotoImage(Image.open(findTarget(tags, isOnline, url)))
    panel = tkinter.Label(root, width=img.width(), height=img.height(), bg='white', highlightthickness=0, image=img, anchor=tkinter.NW)
    panel.image = img
    if (isCentered):
        panel.pack(side=tkinter.TOP, anchor=tkinter.CENTER)
    else:
        panel.pack(side=tkinter.TOP, anchor=tkinter.NW)

def findTarget(item, parseType, url):
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

    if (parseType):
        import requests
        img_data = requests.get(str(url) + "/" + fileName).content
        with open(fileName, 'wb') as handler:
            handler.write(img_data)
    return fileName

def renderButton(window, text, isCentered):
    button = tkinter.Button(window, text=text)
    if (isCentered):
        button.pack(side=tkinter.TOP, anchor=tkinter.CENTER)
    else:
        button.pack(side=tkinter.TOP, anchor=tkinter.NW)

def renderBreak(window, centered):
    br = tkinter.Label(window, bg="white")
    if (centered):
        br.pack(side=tkinter.TOP, anchor=tkinter.CENTER)
    else:
        br.pack(side=tkinter.TOP, anchor=tkinter.NW)

#Set window title

def setTitle(root, title):
    root.title(title)

#Render a horizontal line

def renderHRule(root):
    from tkinter import ttk
    sep = ttk.Separator(root,orient='horizontal')
    sep.pack(fill="x")