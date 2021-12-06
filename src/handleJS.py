def parseOutJS(toRender):
    start,end,result,i = toRender.index("<script>")+1, toRender.index("</script>")-1, [],0
    if start != end: 
        while(i < end):result.append(toRender[i])
    else:result.append(toRender[start])
    return result
def executeJS(root, toRender,C):
    i,JS = 0,parseOutJS(toRender)
    from tkinter import Label,TOP
    while(i < len(JS)):
        if ("document.write" in JS[i]):Label(root, text=(JS[i][JS[i].index("\"")+1:len(JS[i])-3]), fg="black", height= 1, borderwidth=0, bg=root.cget('bg'), font= ("Helvetica", 16)).pack(side=TOP, anchor=C)
        i+=1