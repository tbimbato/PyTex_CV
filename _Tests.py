
name = "gigi"
title = "prova"

explist = ["bachelor", "master", "stage"]

with open("test.tex", "w") as f:
    f.write("\\documentclass[a4paper, 9")
    pt]{article}
    \usepackage[utf8]
    {inputenc}
    \usepackage[left = 1.75
    cm, right = 2.5
    cm, top = 1.25
    cm, bottom = 2.5
    cm]{geometry}
    \usepackage
    {enumitem}
    

    f.write("\\documentclass{article}\n")
    f.write("\\begin{document}\n")
    f.write("\\section*{testttt}\n")
    f.write("\\textbf{Nome}: " + name + " \\\\\n")
    f.write("\\textbf{Titolo}: " + title + " \\\\\n")
    f.write("\\textbf{Esperienza}:\n")
    f.write("\\begin{itemize}\n")
    for exp in explist:
        f.write("    \\item " + exp + "\n")
    f.write("\\end{itemize}\n")
    f.write("\\end{document}\n")
