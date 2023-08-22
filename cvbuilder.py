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

with open("test_OUTPUT.tex", "w") as f:
    f.write("\documentclass[a4paper, 9pt]{article})")
    f.write("\usepackage[utf8]{inputenc})")
    f.write("\usepackage[left=1.75cm, right=2.5cm, top=1.25cm, bottom=2.5cm]{geometry})")
    f.write("\usepackage{enumitem})")
    f.write(")")
    f.write("\usepackage{tgheros})")
    f.write("\renewcommand*\familydefault{\sfdefault} %% Only if the base font of the document is to be sans serif)")
    f.write("\usepackage[T1]{fontenc})")
    f.write(")")
    f.write(")")
    f.write("\usepackage{titlesec})")
    f.write("\titlespacing*{\section}{0pt}{0.3\baselineskip}{0.3\baselineskip})")
    f.write("\titlespacing*{\subsection}{0pt}{0.3\baselineskip}{0.2\baselineskip})")
    f.write("\titlespacing*{\subsubsection}{0pt}{0.3\baselineskip}{0.1\baselineskip})")
    f.write(")")
    f.write("\usepackage{fancyhdr})")
    f.write("\fancyhf{})")
    f.write(
        "\fancyfoot[L]{\scriptsize According to law 679/2016 of the Regulation of the European Parliament of 27th April 2016, I hereby express my consent to process and use my data provided in this CV and application for recruiting purposes})")
    f.write("\renewcommand\headrulewidth{0pt})")
    f.write("\pagestyle{fancy})")
    f.write(")")
    f.write(")")
    f.write("\title{Curriculum Vitae})")
    f.write("\author{NAME AND SURNAME!!!!!!!!})")
    f.write("\date{\today})")
    f.write(")")
    f.write(")")
    f.write("\begin{document})")
    f.write("\section*{NAME SURNAME AND TITLE!!!!!!})")
    f.write(")")
    f.write("\small LOCATION!!!! -- Contacts: \textbf{MAIL!!!!!} -- CELL NUMBER!!!! --)")
    f.write(")")
    f.write(")")
    f.write("\section*{Summary})")
    f.write("SUMMARY!!!!!.)")
    f.write(")")
    f.write(")")
    f.write("\section*{Education})")
    f.write("\begin{itemize}[noitemsep])")
    f.write("\item EDU 1!!!!.)")
    f.write("\item EDU 2!!!!.)")
    f.write("\end{itemize})")
    f.write(")")
    f.write(")")
    f.write("\section*{Experience})")
    f.write(")")
    f.write("\subsection*{EXP1 TITLE!!!!!})")
    f.write("\subsubsection*{EXP1 DATES!!!!!})")
    f.write(")")
    f.write("\begin{itemize}[noitemsep])")
    f.write(")")
    f.write("\item EXP1 BULLET 01!!!!.)")
    f.write("\item EXP1 BULLET 02!!!!.)")
    f.write("\end{itemize})")
    f.write(")")
    f.write("\subsection*{EXP2 TITLE!!!!!})")
    f.write("\subsubsection*{EXP2 DATES!!!!!})")
    f.write("\begin{itemize}[noitemsep])")
    f.write("\item EXP2 BULLET 01!!!!.)")
    f.write("\item EXP2 BULLET 02!!!!.)")
    f.write("\end{itemize})")
    f.write(")")
    f.write("\subsection*{})")
    f.write("\subsection*{Skills})")
    f.write(")")
    f.write("\textbf {Languages}:\small LENGUAGES!!!.)")
    f.write(")")
    f.write("\noindent \textbf{Software}:\small SOFTWARE!!!.)")
    f.write(")")
    f.write("\noindent \textbf{Hard Skills}:\small HARD SKILLS!!!!.)")
    f.write(")")
    f.write("\noindent \textbf{Soft skills}:\small SOFT SKILLS!!!.)")
    f.write(")")
    f.write("\noindent \textbf{Field of Interest}:\small FIELD OF INTEREST!!!!.)")
    f.write(")")
    f.write("\end{document})")
