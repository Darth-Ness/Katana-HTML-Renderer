import tkinter
def startWindow(toRender, isOnline, fileName):
    root = tkinter.Tk()
    root.configure(bg='white', padx=8, pady=8)
    isCentered = "nw"
    textTags = ["<h1", "<h2", "<h3", "<h4", "<h5", "<h6", "<p"]
    u = 0
    print(toRender)
    while(u < len(toRender)):
        if toRender[u] in textTags:
            renderText(toRender, u, root, isCentered)
        if "<img" in toRender[u]:
            startImage(root, toRender[u], isOnline, fileName, isCentered)
        if "<button" in toRender[u] and not "/" in toRender[u]:
            renderButton(root, toRender[u+1], isCentered)
        if "<br" in toRender[u]:
            renderBreak(root,isCentered)
        if "<center" in toRender[u]:
            isCentered = "center"
        if "</center" in toRender[u]:
            isCentered = "nw"
        if "<title" in toRender[u]:
            root.title(toRender[u+1])
            u+=1
        if "<hr" in toRender[u]:
            renderHRule(root)
        u+=1
    #root.destroy()
    root.mainloop()


def renderText(TRtext, ITR, TTR, C):
    from tkinter.font import Font
    textSizes = ["<katanaclassbig>", 15, "<katanaclassbig2>",20,"<katanaclassbig3>",30, "<h1",23.9, "<h2", 17.9, "<h3", 15.9, "<h4", 14, "<h5", 9.9, "<h6", 8, "<p", 12]
    textSize = textSizes[textSizes.index(TRtext[ITR])+1]
    myFont = Font(family="SF Pro bold", size=int(textSize))
    text = tkinter.Label(TTR, text=TRtext[ITR+1], fg="black", height= 1, borderwidth=0, bg='white', font=myFont)
    text.pack(side=tkinter.TOP, anchor=C)

def renderImage(root, isCentered):
    panel = tkinter.Label(root, width=img.width(), height=img.height(), bg='white', highlightthickness=0, image=img, anchor=tkinter.NW)
    panel.image = img
    panel.pack(side=tkinter.TOP, anchor=isCentered)
#Render image after finding the file
def startImage(root, tags, isOnline, url, isCentered):
    from PIL import ImageTk, Image
    global img
    toTry = findTarget(tags, isOnline, url)
    if (toTry != "Error"):
        try:
            img = ImageTk.PhotoImage(Image.open(toTry))
            renderImage(root, isCentered)
        except:
            img = ImageTk.PhotoImage(Image.open("core/ui/noimage.png"))
            renderImage(root, isCentered)

def findTarget(item, parseType, url):
    #Loop through the item to find a quotation mark
    try:
        i = item.find("src=")
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
            try:
                with open(fileName, 'wb') as handler:
                    handler.write(img_data)
            except:
                fileName = "core/ui/noimage.png"
        return fileName
    except:
        print("FATAL ERROR: No src found")
        return "Error"
def renderButton(window, text, isCentered):
    button = tkinter.Button(window, text=text)
    button.pack(side=tkinter.TOP, anchor=isCentered)

def renderBreak(window, centered):
    br = tkinter.Label(window, bg="white")
    br.pack(side=tkinter.TOP, anchor=centered)
#Render a horizontal line

def renderHRule(root):
    canvas=tkinter.Canvas(root, width=1000, height=1, background="white")
    canvas.pack()
    canvas.create_line(1000,0,10,0, fill="black", width=5)
