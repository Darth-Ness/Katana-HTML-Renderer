#Load core/ui/chrome.html
def renderChrome(root, tkinter):
    with open("core/ui/chrome.html", "r") as file:
            HTML=file.read().split("\n")
            u = 0
            textSizes = ["<katanaclassbig", 15, "<katanaclassbig2",20,"<katanaclassbig3",30, "<h1",24, "<h2", 18, "<h3", 16, "<h4", 14, "<h5", 10, "<h6", 8, "<p", 12]
            tags = ["<img", "<button", "<br>", "<center>", "</center>", "<title", "<hr>", "<style>", "<script>", "<input>"]
            isCentered = "nw"
            while(u < len(HTML)):
                if HTML[u] in textSizes or HTML[u] in tags:
                    if HTML[u] in textSizes:renderText(HTML, u, root, isCentered, True, textSizes);u+=1
                    if "<button" in HTML[u]:tkinter.Button(root, text=HTML[u+1]).pack(side=tkinter.TOP, anchor=isCentered)
                    if "<br>" in HTML[u]:tkinter.Label(root, bg=root.cget('bg')).pack(side=tkinter.TOP, anchor=isCentered)
                    if "<center" in HTML[u]:isCentered = "center"
                    if "</center" in HTML[u]:isCentered = "nw"
                    if "<hr>" in HTML[u]:renderHRule(root)
                    if "<input>" in HTML[u]:tkinter.Entry(root).pack()
                else:renderText(HTML, u, root, isCentered, False, textSizes, tkinter)
                u+=1
#Render parsed HTML
def renderPage(toRender, isOnline, fileName, root, tkinter):
    isCentered = "nw"
    textSizes = ["<katanaclassbig", 15, "<katanaclassbig2",20,"<katanaclassbig3",30, "<h1",24, "<h2", 18, "<h3", 16, "<h4", 14, "<h5", 10, "<h6", 8, "<p", 12]
    tags = ["<img", "<button", "<br>", "<center>", "</center>", "<title", "<hr>", "<style>", "<script>", "<input>"]
    u = 0
    #Load dependencies (if needed)
    if ("<img" in toRender):
        from renderImage import startImage
    if ("<style>" in toRender):
        from handleCSS import doCSS
    if ("<script>" in toRender):
        try:from handleJS import executeJS
        except:print("Error: Shurkien is not included.")
    #print(toRender)
    length = len(toRender)
    while(u < length):
        if toRender[u] in textSizes or toRender[u] in tags:
            if toRender[u] in textSizes:renderText(toRender, u, root, isCentered, True, textSizes, tkinter);u+=1
            if "<img" in toRender[u]:startImage(root, toRender[u], isOnline, fileName, isCentered)
            if "<button" in toRender[u]:tkinter.Button(root, text=toRender[u+1]).pack(side=tkinter.TOP, anchor=isCentered)
            if "<br>" in toRender[u]:tkinter.Label(root, bg=root.cget('bg')).pack(side=tkinter.TOP, anchor=isCentered)
            if "<center" in toRender[u]:isCentered = "center"
            if "</center" in toRender[u]:isCentered = "nw"
            if "<title" in toRender[u]:root.title(toRender[u+1]);u+=1
            if "<hr>" in toRender[u]:renderHRule(root)
            if "<style>" in toRender[u]:
                doCSS(root, toRender, u)
                u = toRender.index("</style>")+1
            if "<script>" in toRender[u]:
                executeJS(root, toRender, isCentered)
                u = toRender.index("</script>")+1
            if "<input>" in toRender[u]:Entry(root).pack()
        else:renderText(toRender, u, root, isCentered, False, textSizes, tkinter)

        u+=1
    #root.destroy()
    root.mainloop()


def renderText(TRtext, ITR, TTR, C, isTag, textSizes , tkinter):
    if(isTag):
        textSize = textSizes[textSizes.index(TRtext[ITR])+1]
        tkinter.Label(TTR, text=TRtext[ITR+1], fg="black", height= 1, borderwidth=0, bg=TTR.cget('bg'), font= ("Helvetica", textSize)).pack(side=tkinter.TOP, anchor=C)
    else:tkinter.Label(TTR, text=TRtext[ITR], fg="black", height= 1, borderwidth=0, bg=TTR.cget('bg'), font= ("Helvetica", 16)).pack(side=tkinter.TOP, anchor=C)

def renderHRule(root,tkinter):
    canvas=tkinter.Canvas(root, width=1500, height=1, background="white")
    canvas.pack()
    canvas.create_line(5000,0,10,0, fill="black", width=5)






 #Completes spliting lines with a open (<example>) and a close (</example>)
 #It also removes spaces from non outputed text

def parse(toParse) :
    i,x = 0,0
    while (i < len(toParse)):
        x=0
        for u in toParse[i]:
            if u == ">": pushEnter(len(toParse[i]), i, toParse,x);x-=1
            x+=1
        i+=1
    return toParse
#When a ">" is detected move the rest of the line to a new element

def pushEnter(Llen, i, list,x) :
    if x+1 != Llen:
        #Idenitfy the opening tag
        openingTag = list[i][0: list[i].find(">")]

        parseValue = list[i][x+1: Llen]
        list.insert(i+1, openingTag)
        list.insert(i+2, parseValue)
        del list[i]





#Import the HTML file to parse

def read(fileName):
    
    if (fileName == "test.htm"):fileName = "core/html/test.htm"    
    if (":"  not in fileName):
        #Parse HTML for local file
        with open(fileName, "r") as file:
            HTML=file.read().split("\n")
            return HTML
    else:
        #Parse HTML for websites on the internet
        from requests import get
        HTML = get(fileName, verify=True)
        return HTML