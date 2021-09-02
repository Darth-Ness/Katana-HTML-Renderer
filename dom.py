#Assign a indefencation code for all lines of the website
#The format is IC#(Line number)
#Example: IC#12 would be the twelth line
import globalvar
def assign():

    i = 0  
    #Assign the codes

    while(i < len(globalvar.input)):
        globalvar.domCodes.append("IC#" + str(i+1))
        i+=1