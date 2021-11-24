import tkinter
def startWindow(toRender, isOnline, fileName):
    root = tkinter.Tk()
    root.configure(bg='white', padx=8, pady=8)
    isCentered = "nw"
    textTags = ["<h1", "<h2", "<h3", "<h4", "<h5", "<h6", "<p"]
    u = 0
    #print(toRender)
    while(u < len(toRender)):
        if toRender[u] in textTags:
            renderText(toRender, u, root, isCentered)
        if "<img" in toRender[u]:
            import renderImage
            renderImage.startImage(root, toRender[u], isOnline, fileName, isCentered, tkinter)
        if "<button" in toRender[u] and not "/" in toRender[u]:
            tkinter.Button(root, text=toRender[u+1]).pack(side=tkinter.TOP, anchor=isCentered)
        if "<br" in toRender[u]:
            tkinter.Label(root, bg=root.cget('bg')).pack(side=tkinter.TOP, anchor=isCentered)
        if "<center" in toRender[u]:
            isCentered = "center"
        if "</center" in toRender[u]:
            isCentered = "nw"
        if "<title" in toRender[u]:
            root.title(toRender[u+1])
            u+=1
        if "<hr" in toRender[u]:
            renderHRule(root)
        if "<style>" in toRender[u]:
            import handleCSS
            handleCSS.doCSS(root, toRender, u)
            u = toRender.index("</style>")+1

        u+=1
    #root.destroy()
    root.mainloop()


def renderText(TRtext, ITR, TTR, C):
    from tkinter.font import Font
    textSizes = ["<katanaclassbig>", 15, "<katanaclassbig2>",20,"<katanaclassbig3>",30, "<h1",23.9, "<h2", 17.9, "<h3", 15.9, "<h4", 14, "<h5", 9.9, "<h6", 8, "<p", 12]
    textSize = textSizes[textSizes.index(TRtext[ITR])+1]
    myFont = Font(family="SF Pro bold", size=int(textSize))

def renderHRule(root):
    canvas=tkinter.Canvas(root, width=1500, height=1, background="white")
    canvas.pack()
    canvas.create_line(1000,0,10,0, fill="black", width=5)
