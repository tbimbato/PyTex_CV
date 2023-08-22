


exp_title = []
exp_start_date = []
exp_end_date = []
ex_count = -1
exp_complete = []

while True:

    ex_add = input("do you want to add a work experience title? (Y/N)")
    if ex_add == "Y" :
        ex_title = input("whats your work experience title (eg. Bachelor in Psichology or Surveyor diploma)")
        exp_title.append(ex_title)
        ex_start_date = input("when you started? (format should be = MONTH - YYYY eg: Agoust - 2004")
        exp_start_date.append(ex_start_date)
        ex_end_date = input("when you finished?\n(format should be = MONTH - YYYY eg: Agoust - 2004\nIf you are currently working here typr \"Currently\"")
        exp_end_date.append(ex_end_date)
        ex_count = ex_count + 1
        exp_complete.append([exp_title[ex_count], exp_start_date[ex_count], exp_end_date[ex_count]])
        continue

    else: print("the answer differ from Y or N or you simply want to go in the next step.")
    break

print_count = -1

while True:
    if print_count < ex_count:
        print_count = print_count + 1
        print(exp_complete[print_count])
    else:
        break