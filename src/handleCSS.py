#Parse out everything but the CSS code
def parseOutCss(toRender,u):
    end = toRender.index("</style>")
    i = u+1
    result = []
    while (i < end):
        result.append(toRender[i])
        i+=1
    return result

def doCSS(root, toRender, u):
    CSS = parseOutCss(toRender, u)
    i = 0
    while (i < len(CSS)):
        if ("background-color:" in CSS[i]):
            #Slice everything between ":" ";" in the line of CSS
            root.configure(bg= CSS[u][CSS[u].index(":")+2:CSS[u].index(";")])
        i+=1