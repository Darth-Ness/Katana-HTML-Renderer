from tkinter import Label,TOP,NW
def renderImage(root, isCentered):
    panel = Label(root, width=img.width(), height=img.height(), bg='white', highlightthickness=0, image=img, anchor=NW)
    panel.image = img
    panel.pack(side=TOP, anchor=isCentered)
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
            from requests import get
            img_data = get(str(url) + "/" + fileName).content
            try:
                with open(fileName, 'wb') as handler:
                    handler.write(img_data)
            except:
                fileName = "core/ui/noimage.png"
        return fileName
    except:
        print("FATAL ERROR: No src found")
        return "Error"
