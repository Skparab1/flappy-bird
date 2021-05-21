import time
def clearscreen():
    print('\n'*50)
def addbird(line):
    line = '(0)>' + line
    return line
def removebird(line):
    line.replace('(','')
    line.replace('0','')
    line.replace(')','')
    line.replace('>','')
    return line
def removebirdfromall(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18):
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removebird(line1),removebird(line2),removebird(line3),removebird(line4),removebird(line5),removebird(line6),removebird(line7),removebird(line8),removebird(line9),removebird(line10),removebird(line11),removebird(line12),removebird(line13),removebird(line14),removebird(line15),removebird(line16),removebird(line17),removebird(line18)
    return line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
height = 10
adder = 0
line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = '          ','          ','          ','          ','          ','          ','          |','          ','          ',' (0)>     ','          ','          ','          ','          ','          ','          ','          ','          '
while True:
    try:
        clearscreen()
        obstacleabove = ''
        top = '\n' + obstacleabove
        print(line18),print(line17),print(line16),print(line15),print(line14),print(line13),print(line12),print(line11),print(line10),print(line9),print(line8),print(line7),print(line6),print(line5),print(line4),print(line3),print(line2),print(line1)
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removebirdfromall(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        line10 = removebird(line10)
        input(line10)
        time.sleep(0.1)
        height -= 0.5
        print(height)
        #line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addbird(line1) if round(height,0) == 1 else line1),(addbird(line2) if round(height,0) == 1 else line2),(addbird(line3) if round(height,0) == 1 else line3),(addbird(line4) if round(height,0) == 1 else line4),(addbird(line5) if round(height,0) == 1 else line5),(addbird(line6) if round(height,0) == 1 else line6),(addbird(line7) if round(height,0) == 1 else line7),(addbird(line8) if round(height,0) == 1 else line8),(addbird(line9) if round(height,0) == 1 else line9),(addbird(line10) if round(height,0) == 1 else line10),(addbird(line11) if round(height,0) == 1 else line11),(addbird(line12) if round(height,0) == 1 else line12),(addbird(line13) if round(height,0) == 1 else line13),(addbird(line14) if round(height,0) == 1 else line14),(addbird(line15) if round(height,0) == 1 else line15),(addbird(line16) if round(height,0) == 1 else line16),(addbird(line17) if round(height,0) == 1 else line17),(addbird(line18) if round(height,0) == 1 else line18)
        if height <= -1:
            print('you have hit the ground')
            break
        if height >= 16:
            print('you have hit the ceiling')
            break
    except:
        height += 2
        time.sleep(0.1)
    