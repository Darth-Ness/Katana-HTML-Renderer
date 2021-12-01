from tkinter import Button, Tk, TOP, Label, Canvas
def startWindow(toRender, isOnline, fileName):
    root = Tk()
    root.configure(bg='white', padx=8, pady=8)
    isCentered = "nw"
    textTags = ["<h1", "<h2", "<h3", "<h4", "<h5", "<h6", "<p", "<katanaclassbig", "<katanaclassbig2","<katanaclassbig3"]
    tags = ["<img", "<button", "<br>", "<center>", "</center>", "<title", "<hr>", "<style>"]
    u = 0
    print(toRender)
    length = len(toRender)
    while(u < length):
        if toRender[u] in textTags or toRender[u] in tags:
            if toRender[u] in textTags:renderText(toRender, u, root, isCentered)
            elif "<img" in toRender[u]:
                import renderImage
                renderImage.startImage(root, toRender[u], isOnline, fileName, isCentered)
            elif "<button" in toRender[u]:Button(root, text=toRender[u+1]).pack(side=TOP, anchor=isCentered)
            elif "<br" in toRender[u]:Label(root, bg=root.cget('bg')).pack(side=TOP, anchor=isCentered)
            elif "<center" in toRender[u]:isCentered = "center"
            elif "</center" in toRender[u]:isCentered = "nw"
            elif "<title" in toRender[u]:root.title(toRender[u+1])
            elif "<hr>" in toRender[u]:renderHRule(root)
            elif "<style>" in toRender[u]:
                import handleCSS
                handleCSS.doCSS(root, toRender, u)
                u = toRender.index("</style>")+1

        u+=1
    #root.destroy()
    root.mainloop()


def renderText(TRtext, ITR, TTR, C):
    textSizes = ["<katanaclassbig", 15, "<katanaclassbig2",20,"<katanaclassbig3",30, "<h1",24, "<h2", 18, "<h3", 16, "<h4", 14, "<h5", 10, "<h6", 8, "<p", 12]
    textSize = textSizes[textSizes.index(TRtext[ITR])+1]
    Label(TTR, text=TRtext[ITR+1], fg="black", height= 1, borderwidth=0, bg=TTR.cget('bg'), font= ("SF Pro", textSize)).pack(side=TOP, anchor=C)

def renderHRule(root):
    canvas=Canvas(root, width=1500, height=1, background="white")
    canvas.pack()
    canvas.create_line(5000,0,10,0, fill="black", width=5)