import cv2
import time
from metaphone import doublemetaphone
import re
import os, numpy as np
from ManLypsinc import linearize
def display_metaword(metaword):
    #create a mouthdict dictionary having png files for each alphabet

    mouthdict={
        ' ':'nothing.png',
        '.':'nothing.png',
        'a':'a.png',
        'b':'b.png',
        'c':'c.png',
        'd':'d.png',
        'e':'e.png',
        'f':'f.png',
        'g':'g.png',
        'h':'h.png',
        'i':'i.png',
        'j':'j.png',
        'k':'k.png',
        'l':'l.png',
        'm':'m.png',
        'n':'n.png',
        'o':'o.png',
        'p':'p.png',
        'q':'q.png',
        'r':'r.png',
        's':'s.png',
        't':'t.png',
        'u':'u.png',
        'v':'v.png',
        'w':'w.png',
        'x':'x.png',
        'y':'y.png',
        'z':'z.png',  # for ch, sh. x.png is fine
        '0':'t.png'   # for th
    }
    
    for index, char in enumerate(metaword):
        if char in mouthdict:
            mouth_from=mouthdict[char]
            print(mouth_from)

            if index<len(metaword)-1:
                cv2.imshow(f"{char}", cv2.imread("/Volumes/Anirudh/VS_Code/Lipsyncing/SpeechMouthMan/"+mouth_from))
                cv2.waitKey(20)
                mouth_to = mouthdict[metaword[index+1]]
                image_from= cv2.imread("/Volumes/Anirudh/VS_Code/Lipsyncing/SpeechMouthMan/"+mouth_from)
                image_to = cv2.imread("/Volumes/Anirudh/VS_Code/Lipsyncing/SpeechMouthMan/"+mouth_to)

                # Create a list of alpha values
                alpha_values = np.linspace(0, 1, 10)
                #print(alpha_values)
                # Blend the images for each alpha value
                for alpha in alpha_values:
                    blended_image = cv2.addWeighted(image_from, 1 - alpha, image_to, alpha, 0.0)
                    cv2.imshow('', blended_image)
                    cv2.waitKey(1)

                # Close all windows
                cv2.destroyAllWindows()
            else:
                mouth=mouthdict[char]
                print(mouth)
                cv2.imshow(f"{char}", cv2.imread("/Volumes/Anirudh/VS_Code/Lipsyncing/SpeechMouthMan/"+mouth))
                cv2.waitKey(20)
                
                cv2.destroyAllWindows()
    return

if __name__=="__main__":
    input_sent=input('Enter a sentence:')
    key=linearize(input_sent)
    import timeit
    start=timeit.default_timer()
    display_metaword(key) 
    stop=timeit.default_timer()
    print(stop-start)
  