# CV Maker is a Tommi Bimbato's program to create a ".tex" CV based on the information given by the inputs below

# variables:

# name
# surname
# e_mail
# pnumber
# title
# summary

# EDU:
edu_title = []
edu_start_date = []
edu_end_date = []
e_count = -1
edu_complete = []

# EXP LOOP:
exp_title = []
exp_start_date = []
exp_end_date = []
ex_count = -1
exp_complete = []

print("in this program you will be guided to write down and save your own LaTex format resume")

user_input = input("Are yoy ready? (Y/N): ")

if user_input == "Y":
    print("Cool, let's start.")
else:
    print("Input given differ form \"YES\", see you soon!")
    exit()

print("BASIC INFO. . . . ")
name = input("TYPE YOUR FIRST NAME: . . .\n")
surname = input("TYPE YOUR SURNAME: . . .\n")
e_mail = input("TYPE YOUR WORK E-MAIL ADDRESS: . . .\n")
pnumber = input("TYPE YOUR PHONE NUMBER WITH PREFIX: . . . \n eg.: \"+000 0000000000\" \n")
title = input("TYPE YOUR TITLE: . . . \n eg.: \"architect\" or \"doctor\" write it down here:..\n")
print("now it's time to have a little summary of yout experiences and goals.. ")
summary = input("may you write down something 'bout you?")

print("perfect, now lets talk about your education")

# EDU LOOP:
while True:

    e_add = input("do you want to add an educational title? (Y/N)")
    if e_add == "Y":
        e_title = input("whats your educational title (eg. Bachelor in Psichology or Surveyor diploma)")
        edu_title.append(e_title)
        e_start_date = input("when you started? (format should be = MONTH - YYYY eg: Agoust - 2004")
        edu_start_date.append(e_start_date)
        e_end_date = input("when you finished? (format should be = MONTH - YYYY eg: Agoust - 2004")
        edu_end_date.append(e_end_date)
        e_count = e_count + 1
        edu_complete.append([edu_title[e_count], edu_start_date[e_count], edu_end_date[e_count]])
        continue

    else:
        print("the answer differ from Y or N or you simply want to go in the next step.")
    break

print_count = -1

while True:
    if print_count < e_count:
        print_count = print_count + 1
    else:
        break

# EXP LOOP:
while True:

    ex_add = input("do you want to add a work experience title? (Y/N)")
    if ex_add == "Y":
        ex_title = input("whats your work experience title (eg. Bachelor in Psichology or Surveyor diploma)")
        exp_title.append(ex_title)
        ex_start_date = input("when you started? (format should be = MONTH - YYYY eg: Agoust - 2004")
        exp_start_date.append(ex_start_date)
        ex_end_date = input(
            "when you finished?\n(format should be = MONTH - YYYY eg: Agoust - 2004\nIf you are currently working "
            "here typr \"Currently\"")
        exp_end_date.append(ex_end_date)
        ex_count = ex_count + 1
        exp_complete.append([exp_title[ex_count], exp_start_date[ex_count], exp_end_date[ex_count]])
        continue

    else:
        print("the answer differ from Y or N or you simply want to go in the next step.")
    break

# FIELD OF INTEREST

field_of_interest = input("Describe your field of interest")

# SKILLS LOOP

# HARDSKILLS
h_skill = []
h_skill_count = -1
h_skill_list = []

while True:

    h_skill_q = input("do you want to add a Hard Skill? (Y/N)")
    if h_skill_q == "Y":
        h_skill_count = h_skill_count + 1
        h_skill = input("type your Hard Skill")
        h_skill_list.append(h_skill)
        continue

    else:
        print("the answer differ from Y or N or you simply want to go in the next step.")
    break

# SOFTSKILLS

s_skill = []
s_skill_count = -1
s_skill_list = []

while True:

    s_skill_q = input("do you want to add a Soft Skill? (Y/N)")
    if s_skill_q == "Y":
        s_skill_count = s_skill_count + 1
        s_skill = input("type your Soft Skill")
        s_skill_list.append(s_skill)
        continue

    else:
        print("the answer differ from Y or N or you simply want to go in the next step.")
    break

# --------- TEX BUILDER ---------

with open("test_OUTPUT.tex", "w") as fhand:
    fhand.write("\documentclass[a4paper, 9pt]{article}")
    fhand.write("\usepackage[utf8]{inputenc}")
    fhand.write("\usepackage[left=1.75cm, right=2.5cm, top=1.25cm, bottom=2.5cm]{geometry}")
    fhand.write("\usepackage{enumitem}")
    fhand.write("")
    fhand.write("\usepackage{tgheros}")
    fhand.write("\renewcommand*\familydefault{\sfdefault} %% Only if the base font of the document is to be sans serif")
    fhand.write("\usepackage[T1]{fontenc}")
    fhand.write("")
    fhand.write("")
    fhand.write("\usepackage{titlesec}")
    fhand.write("\titlespacing*{\section}{0pt}{0.3\baselineskip}{0.3\baselineskip}")
    fhand.write("\titlespacing*{\subsection}{0pt}{0.3\baselineskip}{0.2\baselineskip}")
    fhand.write("\titlespacing*{\subsubsection}{0pt}{0.3\baselineskip}{0.1\baselineskip}")
    fhand.write("")
    fhand.write("\usepackage{fancyhdr}")
    fhand.write("\fancyhf{}")
    fhand.write(
        "\fancyfoot[L]{\scriptsize According to law 679/2016 of the Regulation of the European Parliament of 27th April 2016, I hereby express my consent to process and use my data provided in this CV and application for recruiting purposes}")
    fhand.write("\renewcommand\headrulewidth{0pt}")
    fhand.write("\pagestyle{fancy}")
    fhand.write("")
    fhand.write("")
    fhand.write("\title{Curriculum Vitae}")
    fhand.write("\author{NAME AND SURNAME!!!!!!!!}")
    fhand.write("\date{\today}")
    fhand.write("")
    fhand.write("")
    fhand.write("\begin{document}")
    fhand.write("\section*{NAME SURNAME AND TITLE!!!!!!}")
    fhand.write("")
    fhand.write("\small LOCATION!!!! -- Contacts: \textbf{MAIL!!!!!} -- CELL NUMBER!!!! --")
    fhand.write("")
    fhand.write("")
    fhand.write("\section*{Summary}")
    fhand.write("SUMMARY!!!!!.")
    fhand.write("")
    fhand.write("")
    fhand.write("\section*{Education}")
    fhand.write("\begin{itemize}[noitemsep]")
    fhand.write("\item EDU 1!!!!.")
    fhand.write("\item EDU 2!!!!.")
    fhand.write("\end{itemize}")
    fhand.write("")
    fhand.write("")
    fhand.write("\section*{Experience}")
    fhand.write("")
    fhand.write("\subsection*{EXP1 TITLE!!!!!}")
    fhand.write("\subsubsection*{EXP1 DATES!!!!!}")
    fhand.write("")
    fhand.write("\begin{itemize}[noitemsep]")
    fhand.write("")
    fhand.write("\item EXP1 BULLET 01!!!!.")
    fhand.write("\item EXP1 BULLET 02!!!!.")
    fhand.write("\end{itemize}")
    fhand.write("")
    fhand.write("\subsection*{EXP2 TITLE!!!!!}")
    fhand.write("\subsubsection*{EXP2 DATES!!!!!}")
    fhand.write("\begin{itemize}[noitemsep]")
    fhand.write("\item EXP2 BULLET 01!!!!.")
    fhand.write("\item EXP2 BULLET 02!!!!.")
    fhand.write("\end{itemize}")
    fhand.write("")
    fhand.write("\subsection*{}")
    fhand.write("\subsection*{Skills}")
    fhand.write("")
    fhand.write("\textbf {Languages}:\small LENGUAGES!!!.")
    fhand.write("")
    fhand.write("\noindent \textbf{Software}:\small SOFTWARE!!!.")
    fhand.write("")
    fhand.write("\noindent \textbf{Hard Skills}:\small HARD SKILLS!!!!.")
    fhand.write("")
    fhand.write("\noindent \textbf{Soft skills}:\small SOFT SKILLS!!!.")
    fhand.write("")
    fhand.write("\noindent \textbf{Field of Interest}:\small FIELD OF INTEREST!!!!.")
    fhand.write("")
    fhand.write("\end{document}")
