#Parse out everything but the CSS code
def doCSS(root, toRender, u):
    CSS = toRender[toRender.index("<style>")+1:toRender.index("</style>")-1]
    i = 0
    while (i < len(CSS)):
        if ("background-color:" in CSS[i]):
            #Slice everything between ":" ";" in the line of CSS
            root.configure(bg= CSS[u][CSS[u].index(":")+2:CSS[u].index(";")])
        i+=1