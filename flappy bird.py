import time
def clearscreen():
    print('\n'*50)
height = 10
adder = 0
obstacleabove = '                                         |   '
while True:
    try:
        clearscreen()
        top = '\n' + obstacleabove
        print('_'*100), print(top*(16 - round(height))), print('(0)>'), print('_|_ '), print(('\n'+ obstacleabove)*round(height)), print('_'*100)
        time.sleep(0.1)
        height -= 0.5
        if height <= -1:
            print('you have hit the ground')
            break
        if height >= 16:
            print('you have hit the ceiling')
            break
        obstacleabove = obstacleabove[1:100]
        adder += 1
        if adder >= 10:
            adder = 0
            obstacleabove = obstacleabove[1:90] + '              |'
    except:
        height += 2
        time.sleep(0.1)
    