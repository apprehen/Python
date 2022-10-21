dice_tpl= '''\
┌───┐,┌───┐,┌───┐,┌───┐,┌───┐,┌───┐
│   │,│ ● │,│●  │,│● ●│,│● ●│,│● ●│
│ ● │,│   │,│ ● │,│   │,│ ● │,│● ●│
│   │,│ ● │,│  ●│,│● ●│,│● ●│,│● ●│
└───┘,└───┘,└───┘,└───┘,└───┘,└───┘'''
# print(dice_tpl)
dice_lines = dice_tpl.split('\n')
# print(dice_lines)
for i in range(5):
    dice_lines[i] = dice_lines[i].split(',')
    # print(dice_lines[i])
dice = list(range(6))
dice[0] =  dice_lines[0][0]+'\n'+dice_lines[1][0]+'\n'+dice_lines[2][0]+'\n' + dice_lines[3][0] + '\n' + dice_lines[4][0]
dice[1] =  dice_lines[0][1]+'\n'+dice_lines[1][1]+'\n'+dice_lines[2][1]+'\n' + dice_lines[3][1] + '\n' + dice_lines[4][1]
dice[2] =  dice_lines[0][2]+'\n'+dice_lines[1][2]+'\n'+dice_lines[2][2]+'\n' + dice_lines[3][2] + '\n' + dice_lines[4][2]
dice[3] =  dice_lines[0][3]+'\n'+dice_lines[1][3]+'\n'+dice_lines[2][3]+'\n' + dice_lines[3][3] + '\n' + dice_lines[4][3]
dice[4] =  dice_lines[0][4]+'\n'+dice_lines[1][4]+'\n'+dice_lines[2][4]+'\n' + dice_lines[3][4] + '\n' + dice_lines[4][4]
dice[5] =  dice_lines[0][5]+'\n'+dice_lines[1][5]+'\n'+dice_lines[2][5]+'\n' + dice_lines[3][5] + '\n' + dice_lines[4][5]
for i in range(6):
    print(dice[i])
