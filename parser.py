import renderMain
import newLine

 #Completes spliting lines with a open (<example>) and a close (</example>)
 #It also removes spaces from non outputed text

def parse(toParse) :
    i = 0
    u = 0
    if ">" in toParse[i]:

        #Scan for a ">"

        while (i < len(toParse)):
        
            while(u < len(toParse[i])):

                if toParse[i][u] == ">":
                    newLine.pushEnter(u, len(toParse[i]), i, toParse)
                u+=1
            i+=1
            u = 0

    #Invoke the renderer
    renderMain.startWindow(toParse)