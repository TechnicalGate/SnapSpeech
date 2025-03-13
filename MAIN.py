from image_recognition import get_text, get_fancy_text
from text_to_speech import sound_setup,tts

from tkinter import filedialog
import tkinter as tk#importing tkinter doesnt also import filedialog for some reason

#fancy is showing more data
#gottentext = [text, language]

def select_image():#by fern
    #get user file input
    path = filedialog.askopenfilename(
        filetypes = [('Image Files', '*.png *.jpg *.jpeg')],
        title = 'Select An Image')
    
    if path:
        updateUI(path)

#=====================UPDATING UI=================================
def updateUI(path):#by fern
    #scrollbar
    scroll = tk.Scrollbar(frame)
    scroll.pack(side = tk.RIGHT, anchor = 'ne')
    
    #show text
    if fancy == 0:
        text = get_fancy_text(path)
        update_text_fancy(text)
    else:
        text = get_text(path)
        update_text(text)

def update_text_fancy(gottentext):#by fern
    #code is different for displaying normal text vs displaying the data due to formatting stuff
    #remove previous labels
    for w in frame.winfo_children():
        w.destroy()
    #write the text
    if gottentext:
        for i in gottentext[0]:#[0] is the text and confidence, [1] is just the text, [2] is the language
            #write text and confidence amount
            textlabel = tk.Label(frame,
                                 text = f'Text: {i[0]}  Confidence: {i[1]}',
                                 font = ('Arial',18))
            textlabel.pack()
        #write whole text
        text = tk.Text(frame, font = ('Arial',20), width=30)
        text.insert('1.0',gottentext[1])
        text.config(state='disabled')
        text.pack()
        
        #display language
        langlabel = tk.Label(frame,
                             text = f' Language: {gottentext[2]}',
                             font = ('Arial',20))
        langlabel.pack()

        #show sound
        #if there is langauge (if text is actually detected)
        soundbutton = tk.Button(frame,
                            text = 'Play Sound',
                            font = ('Arial',20),
                            cursor = 'hand2',
                            command = lambda: tts([gottentext[1],gottentext[2]]))#use lambda so i can pass an argument in, slice gottentext so the big confidence list is not thete
        soundbutton.pack()

    else:
        #error message thing
        textlabel = tk.Label(frame,
                             text = 'Unable to extract text from image',
                             font = ('Arial',18))
        textlabel.pack()

def update_text(gottentext):#by fern
    #remove previous labels
    for w in frame.winfo_children():
        w.destroy()
    #show text
    if gottentext:
        #write whole text
        text = tk.Text(frame, font = ('Arial',20), width=30)
        text.insert('1.0',gottentext[0])
        text.config(state='disabled')
        text.pack()
        
        #display language
        langlabel = tk.Label(frame,
                             text = f' Language: {gottentext[1]}',
                             font = ('Arial',20))
        langlabel.pack()

        #show sound
        #if there is langauge (if text is actually detected)
        soundbutton = tk.Button(frame,
                            text = 'Play Sound',
                            font = ('Arial',20),
                            cursor = 'hand2',
                            command = lambda: tts(gottentext))#use lambda so i can pass an argument in, slice gottentext so the big confidence list is not thete
        soundbutton.pack()
        
    else:
        textlabel = tk.Label(frame,
                             text = 'Unable to extract text from image',
                             font = ('Arial',18))
        textlabel.pack()

def fancy_toggle():#by fern
    #for extra data toggle thing
    global fancy
    fancy = 1 if fancy == 0 else 0#change fancy every time its clicked

def update_scrollregion(event):#for scrollbar
    canvas.configure(scrollregion=canvas.bbox('all'))
    
#=======================================================================
    
#==============UI BUTTONS AND STUFF================================
#still by fern
#the window itself
root = tk.Tk()
root.title('Image to Text to Speech Converter')
root.geometry('600x400')

#set up sound
sound_setup()

#button to choose image
imagebutton = tk.Button(root,
                        #make it pretty
                        text = 'Select An Image',
                        font = ('Arial',20),
                        cursor = 'hand2',
                        #assign function to button
                        command = select_image
                        )
imagebutton.pack()

#canvas that holds text (makes it easier to delete old labels) (also can scroll)
#canvas is packed after imagebutton so imagebutton can stay at the top of the screen
canvas = tk.Canvas(root)
canvas.pack(fill = 'both',expand=True)

scrollbar = tk.Scrollbar(canvas, orient='vertical', command=canvas.yview)
#canvas holds frame, frame is what scrolls

frame = tk.Frame(canvas)
#let scrollbar scroll on frame
frame.bind('<Configure>', update_scrollregion)
canvas.create_window((0,0), window=frame, anchor='nw')
canvas.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side='right', fill='y')

#extra data toggle
fancy = tk.IntVar
checkbutton = tk.Checkbutton(root, text='More Data', variable=fancy, 
                             onvalue=1, offvalue=0, command=fancy_toggle)
checkbutton.pack()

root.mainloop()
