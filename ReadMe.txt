THINGS NEEDED TO BE INSTALLED:
Tesseract OCR needs to be installed for this program to work. Please install Tesseract OCR by inputting "brew install tesseract" into terminal

Tkinter needs to be installed for this program to work. Please install Tkinter by inputting "brew install python-tk" into terminal

How to use:
Run MAIN.py. If an error appears or nothing appears, edit the 6th line of image_recognition.py and replace the path (r".../.../...") with your tesseract path (use brew info tesseract to obtain)

When the window with the header "Image to Text to Speech Converter" appears, tick the "More Data" checkbox to see how confident the AI is of the words. Press "Select An Image" to select an image to extract text from. 

After an image is selected, the text and language of the text will appear if it is able to extract text. 

Otherwise, no text will appear, and the language will be "None". To listen to the words being read, scroll to the bottom of all the words and press "Play Sound". "Play Sound" button will not appear if it is unable to extract text.

Playing sound requires internet, but detecting text from image and choosing image does not require internet.