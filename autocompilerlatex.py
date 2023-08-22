# Wrote this loope for complete the latex template easily


with open('CVTEX_EMPTY.tex') as texhand:
    texlist = texhand.readlines()
li = [x.strip() for x in texlist]


for lines in li:
    print(lines)
with open("texcompiler2.py", "w") as ttemplate:
    for lines in li:
        ttemplate.write("f.write(" + "\"" + lines + ")\"" + ")\n")
        ttemplate.write("f.write(" +  lines + ")\"" + ")\n")
