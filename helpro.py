import time
from pygame import mixer
wat = 5
ey = 20
ex = 35

def music(file , stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while(True):
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def msg(msg):
    with open("sc.txt", "a") as f:
        f.write(f"{msg} {time.asctime(time.localtime())}\n")
if  __name__ == '__main__':
    iniwat = time.time()
    iniey = time.time()
    iniex = time.time()
    while True:
        if time.time() - iniwat > wat:
            print("Water drinking time. Type drank to stop")
            music("water.mp3", "drank")
            msg("Water drank at")
            iniwat = time.time()
            continue
        elif time.time() - iniey > ey:
            print("Eyes relaxing time. Type eydone to stop")
            music("eyes.mp3", "eydone")
            msg("eyes exercise done at")
            iniey = time.time()
            continue
        elif time.time() - iniex > ex:
            print("Please do some exercise. Type exdone to stop")
            music("exer.mp3", "exdone")
            msg("physical exercise done at")
            iniex = time.time()
            continue







