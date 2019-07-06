# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:08:19 2019

@author: leon
"""

import cv2
import numpy as np
import tkinter
#import os

def save_movie(mov1, mov2, direct, result):

    # 動画の読み込み
    cap1 = cv2.VideoCapture(mov1)
    cap2 = cv2.VideoCapture(mov2)
    
    len1 = int(cap1.get(7))
    len2 = int(cap2.get(7))
    length = min(len1, len2)
    
    # 動画像を結合する向き 0: 上下，1：左右
    # 縦には対応していない
    DIRECTION = direct
    
    # 前準備
    wid = int(cap1.get(3))
    hei = int(cap1.get(4))
    pre_img1 = np.zeros((wid, hei, 3)).astype(np.uint8)
    
    wid = int(cap2.get(3))
    hei = int(cap2.get(4))
    pre_img2 = np.zeros((wid, hei, 3)).astype(np.uint8)
    
    # 動画の保存用
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    output_filename = result
    
    if DIRECTION == 0:
        hei = 2 * hei
        wid = wid
    else:
        hei = hei
        wid = 2 * wid
    output_video = cv2.VideoWriter(output_filename, fourcc, 30, (wid, hei), isColor=True)
    
    for f in range(length):
        print("----")
        print(f+1)
        
        _, img1 = cap1.read()
        if _ == False:
            print("1")
            img1 = pre_img1
        _, img2 = cap2.read()
        if _ == False:
            print("2")
            img2 = pre_img2
        
        pre_img1, pre_img2 = img1, img2
        
        concat_img = np.concatenate((img2, img1), axis=DIRECTION)
        
        output_video.write(concat_img)
        
    output_video.release()

#
# ボタンが押されるとここが呼び出される
#
def Button_Concat(event):
  #エントリーの中身を削除
#  EditBox.delete(0, tkinter.END)
  print("hello")
  print(val.get())
  save_movie("./sample1.MOV", "./sample2.MOV", val.get(), "result.avi")

def img():
    pass
    if val.get() == 0:
        label.configure(image=img1)
    else:
        label.configure(image=img2)

root = tkinter.Tk()
root.title(u"動画結合ツール")
root.geometry("400x300")

Static1 = tkinter.Label(text=u'Path of video1')
Static1.place(x=10, y=10)
Static2 = tkinter.Label(text=u'Path of video2')
Static2.place(x=200, y=10)

EditBox = tkinter.Entry(width=30)
EditBox.place(x=10, y=30)
EditBox = tkinter.Entry(width=30)
EditBox.place(x=200, y=30)

Button = tkinter.Button(text=u'結合')
Button.place(x=350, y=250)

# チェック有無変数
val = tkinter.IntVar()
Button.bind("<Button-1>",Button_Concat) 
# value=0のラジオボタンにチェックを入れる
val.set(0)

rdo1 = tkinter.Radiobutton(root, text='上下', variable = val, value = 0, command=img)
rdo1.place(x=10, y=70)
rdo2 = tkinter.Radiobutton(root, text='左右', variable = val, value = 1, command=img)
rdo2.place(x=80, y=70)

# 画像の取得
img1 = tkinter.PhotoImage(file='1.gif')
img2 = tkinter.PhotoImage(file='2.gif')
label = tkinter.Label(root, image=img1)
label.place(x=97, y=120)

root.mainloop()
