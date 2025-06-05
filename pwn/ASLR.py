main_address = int(input(), 16)

main_win = 0x96

win_address = main_address - main_win

print(hex(win_address))