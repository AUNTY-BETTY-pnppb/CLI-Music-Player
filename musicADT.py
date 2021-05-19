import pygame # the music stuff
import glob # gives filepaths/names
import time
import keyboard 

class musicADT:
    def __init__(self):
        types = ('./**/*.wav', './**/*.mp3')
        self._files = []
        self._current = 0
        self.checkpause = False
        self.start = False
        self.re = 0

        for files in types:
            self._files.extend(glob.glob(files, recursive=True))

        pygame.init()
        # edit quality
        pygame.mixer.pre_init(frequency=48000, size=32, buffer=1024)
        pygame.mixer.init()
    
    def play(self):
        if self.check():
            pygame.mixer.music.stop()
        pygame.mixer.music.load(self._files[self._current])
        pygame.mixer.music.play()
        time.sleep(1)
        s = self._files[self._current][:-4]
        s = s[2:]
        print("Playing - " + s)

    def pause(self):
        if not self.checkpause:
            pygame.mixer.music.pause()
            self.checkpause = True
        else:
            pygame.mixer.music.unpause()
            self.checkpause = False
    
    def stop(self):
        if self.check():
            pygame.mixer.music.stop()

    def check(self):
        if pygame.mixer.music.get_busy():
            return True
        else:
            return False

    def next_track(self):
        if self._current == len(self._files)-1:
            self._current = 0
        else:
            self._current += 1
        self.play()

    def prev_track(self):
        if self._current == 0:
            self._current = len(self._files)-1
        else:
            self._current -=1
        self.play()

    def rewind(self):
        pygame.mixer.music.rewind()

    def printList(self):
        for file in self._files:
            s = file[:-4]
            s = s[2:]
            print(s)

def Main():
    p_list = musicADT()
    p_list.printList()
    while True:
        if keyboard.is_pressed('l + space'): 
            if not p_list.check() and p_list.start == False:
                p_list.play()
                p_list.start = True
                time.sleep(0.5)
            else:
                p_list.pause()    
                time.sleep(0.5)  
        if keyboard.is_pressed('l + right'):
            p_list.next_track()
            time.sleep(0.5)
        if keyboard.is_pressed('l + left'):
            if p_list.re == 0 and p_list.check():
                p_list.rewind()
                p_list.re = 1
            else:
                p_list.prev_track()
                p_list.re = 0
            time.sleep(0.5)
        if keyboard.is_pressed('l + esc'):
            p_list.stop()
            print("Playlist Off")
            time.sleep(0.5)
            break

Main()
