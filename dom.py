#Assign a indefencation code for all lines of the website
#The format is IC#(Line number)
#Example: IC#12 would be the twelth line
import parser

domCodes = []
def assign():

    i = 0  
    #Assign the codes

    while(i < len(parser.input)):
        domCodes.append("IC#" + str(i+1))
        i+=1