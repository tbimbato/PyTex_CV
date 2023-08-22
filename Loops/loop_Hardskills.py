


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