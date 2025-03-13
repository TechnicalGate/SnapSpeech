import cv2 #image processing
import pytesseract #image to text
import langdetect

#Replace with your tesseract path (brew info tesseract)
pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/Cellar/tesseract/5.5.0/bin/tesseract"

def process_image(image): #By Charis
    #open image for processing
    img = cv2.imread(image)
    
    #Image Processing
    #make image black and white
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY)

    return binary

def get_fancy_text(image):#by fern
    #gets confidence levels of the data stuff
    img = process_image(image)
    
    #get text and confidence level
    data = pytesseract.image_to_data(img, config="--oem 3 --psm 3 ")

    #Remove unimportant data (everything thats not text or confidence level)
    lines = data.strip().split("\n")

    #identify column positions
    header = lines[0].split("\t")
    text_index = header.index("text")
    conf_index = header.index("conf")

    #remove low confidence rows and rows with no text
    result = []
    for line in lines[1:]:
        columns = line.split("\t")
        if len(columns) > text_index and columns[conf_index] != "-1" and columns[text_index].strip():
            text = columns[text_index]
            conf = columns[conf_index]
            result.append((text, conf))

    #get text and language
    text,lang = get_text(image)

    return result,text,lang

def get_text(image):#by fern
    #returns normal text
    img = process_image(image)
    
    #get tex
    text = pytesseract.image_to_string(img, config="--oem 3 --psm 3 ")

    #uncomment to see the proccessed image V
    #cv2.imshow("img", img); cv2.waitKey(0); cv2.destroyAllWindows()

    #detect language for text to speech
    #no language if no result
    if text:
        lang = langdetect.detect(str(text))
    else:
        lang = None


    return text,lang
