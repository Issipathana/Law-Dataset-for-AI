for r in range(1,668):
    f = open("c:\\stf\\2018\\"+str(r)+".htm", "r")
    outfile = open("c:\\stf\\2018\\merge2018.htm", "a")
    text = ""
    while True:
        # read a single line
        line = f.readline()
        if not line:
            break
        if line.find("<strong>Ementa</strong>") != -1:
            while line.find("<b>Outras informações&nbsp</b>") == -1:
                text += line
                line = f.readline()
    outfile.write(text)
    # close the pointer to that file
    f.close()
