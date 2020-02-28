
f = open("c:\\stf\\2018\\STF2018Clean.htm", "r", encoding="utf8")
outfile = open("c:\\stf\\STF20192018.htm", "a", encoding="utf8")
output = f.read()
outfile.write(output)
