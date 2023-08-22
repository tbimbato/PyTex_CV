
import json

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
