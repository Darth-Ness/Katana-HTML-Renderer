def startWindow(toRender):
    isCentered = False
    textTags = ["<h1", "<h2", "<h3", "<h4", "<h5", "<h6", "<p"]
    u = 0
    #print(toRender)
    while(u < len(toRender)):
        if toRender[u] in textTags:
            renderText(toRender[u+1], isCentered)
        if "<br" in toRender[u]:
            print("/n")
        if "<center" in toRender[u]:
            isCentered = True
        if "</center" in toRender[u]:
            isCentered = False
        if "<hr" in toRender[u]:
            print("-------------------------------------------------------------------------------------------------")

        u+=1
def renderText(TRtext, C):
    if (C):
        print(TRtext.center(100))
    else:
        print(TRtext)