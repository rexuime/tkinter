
import re

hold_bg = "#000000"
replace_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

print(hold_bg)

for i in range(16):

    if i == 15:
        print(i)
        hold_bg = "#000000"
        print(hold_bg)
    else:
        print("Iteration: " + str(i))
        print("Replace: " + str(replace_list[i]))
        print("With: " + str(replace_list[i+1]))
        hold_bg = re.sub(replace_list[i], replace_list[i+1], hold_bg)
        print(hold_bg)
        
