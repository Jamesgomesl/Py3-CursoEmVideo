from pygame import mixer
from time import sleep


def play_fantastic_baby():
    mixer.init()
    mixer.music.load('Wow fantastic baby.mp3')
    mixer.music.play()


print('\n=== CONTAGEM REGRESSIVA ===')
for count in range(10, 0, -1):
    print('\n', count)
    if count == 3:
        play_fantastic_baby()
    sleep(1)

print('\nWow,', end=''), sleep(1)
print(' fantastic baby!'), sleep(1)
print('\n    DANCE!  :P')

# Espero que tenha compensado seu ano novo :)
# DO KWY - JuhLyanna <3

sleep(3)
input('\nENTER para sair')
