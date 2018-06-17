#Ennis M 6/17/18

from pathlib import Path

#Enter path to file.
main = Path("/Users/ennismachta/desktop/whole")

#Counts how many files parsed.
counter = 0

for file in main.glob("**/*"):
    if not file.is_dir():
        counter += 1
        #change list elements to file extensions you would like to parse
        if file.suffix in [".html", ".php",".css",".txt",".shtml"]:
            x = file.open(encoding="ascii")
            try:
                for h in x:
                    #Change string to the string you would like to search for
                    if 'be-section-pad clearfix' in h:
                        #if found your file path will print
                        print(file)
            except:
                #if not found nothing will happen
               continue

#print the amount of files parsed
print(counter)
            

            
