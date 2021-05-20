import time
def clearscreen():
    print('\n'*50)
height = 10
while True:
    try:
        clearscreen()
        print('_'*100), print('\n'*(16 - round(height))), print('(0)>'), print('_|_ '), print('\n'*round(height)), print('_'*100)
        time.sleep(0.1)
        height -= 0.5
        if height <= -1:
            print('you have hit the ground')
            break
        if height >= 16:
            print('you have hit the ceiling')
            break
    except:
        height += 2
        time.sleep(0.1)
    