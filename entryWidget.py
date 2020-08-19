from Tkinter import *
import sys  
import os                      # make directory and paths for new utterence folders
from pydub import AudioSegment # Open Source Python Library to process Audio as array

#------------------------------------ DEFINE GLOBAL ------------------------------------#
# INCLUDE ENDING / on mac or \\ on windows

PARENT_DIR = '/Users/alex/Documents/GitHub/SubMusic/'
#where newly exported audio will initially go

OLD_MUSIC_DIR = '/Users/alex/Documents/GitHub/SubMusic/MusicFiles/'
NEW_MUSIC_DIR = '/Users/alex/Documents/GitHub/SubMusic/changedAudio/'


#---------------------------------------------------------------------------------------#

def close_window():
    my_window.destroy()
    exit()

def convertMinToMS(entryString):
    try:
        minVal = int(entryString[:entryString.index(':')])
        secVal = int(entryString[entryString.index(':') + 1:entryString.index('.')])
        msVal  = int(entryString[entryString.index('.') + 1:])
        
        return ((minVal * 60 + secVal) * 1000) + msVal
        #convert string time index to ms

    except ValueError:
        return -1


def cut_wav_file():
    name_of_song = entry_1.get()
    
    mp3_directory = OLD_MUSIC_DIR + name_of_song + '.mp3'
    string_to_display = ''
    
    try: 
        sound_file = AudioSegment.from_mp3(mp3_directory)
    except IOError:
        string_to_display = "_______No Such Song File________"
    
    if(string_to_display != "_______No Such Song File________"):
        
        startMinToMS = convertMinToMS(entry_2.get())
        endMinToMS = convertMinToMS(entry_3.get())
        
        if(startMinToMS == -1 or endMinToMS == -1):
            string_to_display = "Time Stamp Format is Incorrect"

        elif(endMinToMS < startMinToMS):

            string_to_display = "_______End is before Start______"
        
        else:
            if(startMinToMS >= len(sound_file)):
                new_audio = sound_file

            elif(endMinToMS >= len(sound_file)):
                new_audio = sound_file[:startMinToMS]

            else:
                new_audio = sound_file[:startMinToMS] + sound_file[endMinToMS:]

                        
            changed_file = name_of_song + '_Improved.mp3'
            new_audio.export(changed_file, format="mp3")
            os.rename(PARENT_DIR + changed_file, NEW_MUSIC_DIR + name_of_song + '.mp3')
            os.rename(OLD_MUSIC_DIR + name_of_song + '.mp3', OLD_MUSIC_DIR + name_of_song + '_outdated.mp3')
            string_to_display = "____Song has been Modified!_____"
    
    label_4 = Label(my_window, font = 'Helvetica 40')
    label_4['text'] = string_to_display
    return label_4.grid(row = 5, column = 1)
    

my_window = Tk()
my_window.title("Wav File Cutter")
my_window.configure(background = "black")


MyTitle = Label(my_window, text='Wav File Cutter', bg = "black", fg ="white", font='Helvetica 32 bold')

label_1 = Label(my_window, text = "Enter the song file name:", bg = "black", fg ="white", font='Helvetica 32')
entry_1 = Entry(my_window, font = 'Helvetica 32 bold')
label_2 = Label(my_window, text = "Format- MIN:SEC.MS", bg = "black", fg = "white", font ='Helvetica 32')
label_3 = Label(my_window, text = "Where should the cut start:",  bg = "black", fg ="white",font='Helvetica 32')
entry_2 = Entry(my_window, font = 'Helvetica 32 bold')
label_4 = Label(my_window, text = "Where should the cut end:",  bg = "black", fg ="white",font='Helvetica 32')
entry_3 = Entry(my_window, font = 'Helvetica 32 bold')

button_1 = Button(my_window, text = 'Click me to perform the trim',  bg = "black", fg ="white",font='Helvetica 25', command=cut_wav_file)

MyTitle.grid(row=0, column = 0)

label_1.grid(row=1, column=0)
entry_1.grid(row=1, column=1)

label_2.grid(row=2, column=0)

label_3.grid(row=3, column=0)
entry_2.grid(row=3, column=1)

label_4.grid(row=4, column=0)
entry_3.grid(row=4, column=1)

button_1.grid(row=5, column=0)

button_2 = Button(my_window, text="Exit", bg ='black', fg = 'white', font = 'none 20 bold', command=close_window)
button_2.grid(row=6, column= 1)
my_window.mainloop()
