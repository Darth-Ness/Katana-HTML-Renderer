import renderMain
#Import the HTML file to parse
#Check if target is a URL or a local file
def read():

    #fileName = "test.htm"
    fileName = input("Enter HTML file: ")

    if (fileName == "test.htm"):
        fileName = "core/test.htm"
        
    if (":"  not in fileName):
        #Parse HTML for local file
        try:
            with open(fileName, "r") as file:
                HTML=file.read().split("\n")

                HTML2 = "".join(map(str,HTML))
                HTML3 = (HTML2.split("<"))

                HTML4 = ">".join(map(str,HTML3))
                HTML5 = (HTML4.split(">"))
 
                renderMain.startWindow(HTML5, False, fileName)
        except:
            with open("core/404.htm", "r") as file:
                HTML=file.read().split("\n")

                HTML2 = "".join(map(str,HTML))
                HTML3 = (HTML2.split("<"))

                HTML4 = ">".join(map(str,HTML3))
                HTML5 = (HTML4.split(">"))
 
                renderMain.startWindow(HTML5, True, fileName)
    else:
        #Parse HTML for websites on the internet
        import requests
        x = requests.get(fileName)
        HTML = x.text

        HTML2 = (HTML.split("<"))

        HTML3 = ">".join(map(str,HTML2))
        HTML4 = (HTML3.split(">"))

        renderMain.startWindow(HTML4, True, fileName)

read()
