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
h_skill = -1
h_skill_list = []

while True:

    h_skill_q = input("do you want to add a Hard Skill? (Y/N)")
    if h_skill_q == "Y" :
        h_skill = input("type your Hard Skill")
        h_skill_list.append(h_skill)
        continue

    else: print("the answer differ from Y or N or you simply want to go in the next step.")
    break

#SOFTSKILLS

s_skill = []
s_skill = -1
s_skill_list = []

while True:

    s_skill_q = input("do you want to add a Soft Skill? (Y/N)")
    if s_skill_q == "Y" :
        s_skill = input("type your Soft Skill")
        s_skill_list.append(s_skill)
        continue

    else: print("the answer differ from Y or N or you simply want to go in the next step.")
    break


