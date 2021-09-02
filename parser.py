import globalvar
import newLine
import renderMain

 #Completes spliting lines with a open (<example>) and a close (</example>)
 #It also removes spaces from non outputed text

def parse() :
    i = 0
    u = 0
    if ">" in globalvar.input[i]:


        #Scan for a ">"

        while (i < len(globalvar.input)):
        
            while(u < len(globalvar.input[i])):

                if globalvar.input[i][u] == ">":
                    newLine.pushEnter(u, len(globalvar.input[i]), i)
                u+=1
            i+=1
            u = 0

    #Invoke the renderer
    renderMain.identifyModule(globalvar.input)


#This runs "parse" and "pushEnter"
parse()