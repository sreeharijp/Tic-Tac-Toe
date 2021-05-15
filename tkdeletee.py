from tkinter import *
import tksnack
root=Tk()
tksnack.initializeSnack(root)
snd=tkSnack.Sound()
snd.read('bgm.wav')
snd.play(blocking=1)
