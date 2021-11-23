#Import the HTML file to parse
def read():

    fileName = "test.htm"
    #fileName = input("Enter HTML file: ")
    import parser

    
    if (fileName == "test.htm"):
        fileName = "core/test.htm"    
        #Parse HTML for local file

        with open(fileName, "r") as file:
            HTML=file.read().split("\n")
            parser.parse(HTML)
        
read()