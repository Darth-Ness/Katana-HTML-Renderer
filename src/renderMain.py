from tkinter import Button, Tk, TOP, Label, Canvas
def startWindow(toRender, isOnline, fileName):
    root = Tk()
    root.configure(bg='white', padx=8, pady=8)
    isCentered = "nw"
    textSizes = ["<katanaclassbig", 15, "<katanaclassbig2",20,"<katanaclassbig3",30, "<h1",24, "<h2", 18, "<h3", 16, "<h4", 14, "<h5", 10, "<h6", 8, "<p", 12]
    tags = ["<img", "<button", "<br>", "<center>", "</center>", "<title", "<hr>", "<style>", "<script>"]
    u = 0
    #Load dependencies (if needed)
    if ("<img" in toRender):
        from renderImage import startImage
    if ("<style>" in toRender):
        from handleCSS import doCSS

    #print(toRender)
    length = len(toRender)
    while(u < length):
        if toRender[u] in textSizes or toRender[u] in tags:
            if toRender[u] in textSizes:renderText(toRender, u, root, isCentered, True, textSizes);u+=1
            if "<img" in toRender[u]:startImage(root, toRender[u], isOnline, fileName, isCentered)
            if "<button" in toRender[u]:Button(root, text=toRender[u+1]).pack(side=TOP, anchor=isCentered)
            if "<br" in toRender[u]:Label(root, bg=root.cget('bg')).pack(side=TOP, anchor=isCentered)
            if "<center" in toRender[u]:isCentered = "center"
            if "</center" in toRender[u]:isCentered = "nw"
            if "<title" in toRender[u]:root.title(toRender[u+1]);u+=1
            if "<hr>" in toRender[u]:renderHRule(root)
            if "<style>" in toRender[u]:
                doCSS(root, toRender, u)
                u = toRender.index("</style>")+1
            if "<script>" in toRender[u]:
                try:
                    from handleJS import executeJS
                    executeJS(root, toRender, isCentered)
                    u = toRender.index("</script>")+1
                except:
                    print("Either Shurkien is not included, or there was a error during excution.")
        else:renderText(toRender, u, root, isCentered, False, textSizes)

        u+=1
    #root.destroy()
    root.mainloop()


def renderText(TRtext, ITR, TTR, C, isTag, textSizes):
    if(isTag):
        textSize = textSizes[textSizes.index(TRtext[ITR])+1]
        Label(TTR, text=TRtext[ITR+1], fg="black", height= 1, borderwidth=0, bg=TTR.cget('bg'), font= ("Helvetica", textSize)).pack(side=TOP, anchor=C)
    else:Label(TTR, text=TRtext[ITR], fg="black", height= 1, borderwidth=0, bg=TTR.cget('bg'), font= ("Helvetica", 16)).pack(side=TOP, anchor=C)

def renderHRule(root):
    canvas=Canvas(root, width=1500, height=1, background="white")
    canvas.pack()
    canvas.create_line(5000,0,10,0, fill="black", width=5)