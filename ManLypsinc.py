import cv2
import time
from metaphone import doublemetaphone
import re
import os

def exceptional_handling(excep_list:list,word):
    for exc in excep_list:
        if exc in word:
            return False
            break
    return True

def punctuation_handling(word):
    word=word.lower()
    freeword=''
    for char in word:
        freeword+=char if 'a'<=char<='z' else ''
    return freeword

def metaphone(word):
    metaword=''
    word=word.lower()
    pattern = r'([^aeiou])\1{1,}'

    # Use the sub function to remove double consonants while preserving double vowels
    word = re.sub(pattern, r'\1', word)
    meta=doublemetaphone(word)[0].lower()
    print(meta)       ###
    if meta[0]=='a' and meta!='a':
        meta=meta[1:]
    else:
        meta=meta
    print(meta)       ###
    vowels = "aeiouwxy"

    # Combine consonants from Metaphone and vowels from the word
    consonant_index = 0
    exceptional_listfor_y=['cry','dry','fly','sly','try','wry','my']
    exceptional_listfor_e=['hare','rte','we','qe','he','me']
    pattern2= r'(sh|th|ch|ph|bh|gn|rh|lh|ck|kn)'
    # Use the sub function to replace all "sh," "th," or "ch" with "q"
    word = re.sub(pattern2,'q', word)

    print(word)    ### 
    if len(word)==1:
        word=word
    elif word[:2]=='wh':
        meta='vh'+meta
    else:
        if 'dh' in word:
            word = word.replace('dh', 'q')
            meta=meta.replace('T','0')
        if 'kh' in word:
            word=word.replace('kh','k')
        if 'gh' in word:
            if word[:2]=='gh':
                word=word.replace('gh','g')
            elif 'igh'in word:
                word = re.sub(r'igh', 'ai', word)
            else:
                word=word.replace('gh','')
        if word[-1]=='e' and exceptional_handling(exceptional_listfor_e,word):
            word=word[:-1]
        if word[-1]=='y' and exceptional_handling(exceptional_listfor_y,word):
            word=word[:-1]+'i'
        if word[0]=='y':
            word=word[1:]
        if word[-1]=='w' and len(word)==3:
            if word[-2:]=='ew':
                word=word[:-1]+'u'
            else:
                word=word[0]+'a'+word[1:-1]
        if word[-1]=='w' and len(word)!=3:
            if word[-2:]=='ew':
                word=word[:-1]+'u'
            else:
                word=word[:-1]
        if word[0]=='w':
            word='v'+word[1:]
            meta='v'+meta
        if word[:2]=='pn' or word[:2]=='ps':
            word='n'+word[2:]
        else:
            word=word
    print(word)   ###
    for char in word:
        if char in vowels:
        # If the character is a vowel, add a vowel from the original word
            if char=='y':                       #  Y HANDLING
        #if y is at the end of word, then add 'i' else 'ai'
                if word[:2]=='sy' or word[:2]=='qy':
                    char='i'
                    metaword+=char
                else:
                    char='ai'  
                    metaword += char 
            elif char=='x':                                 # X HANDLING
                if word[0]!='x':
                    if 'xc' in word:
                        metaword+=char
                        meta=meta.replace('ks','k')
                    else:
                        char='ks'
                        metaword += char
                        meta=meta.replace('ks','')
            elif char=='w':
                metaword+='v'
            else:
                word = re.sub(r'ow', 'ao', word) if 'ow' in word else word
                metaword += char
            
        else:
        # If the character is not a vowel (i.e., a consonant), add a consonant from the Metaphone representation           
            metaword += meta[consonant_index]
            consonant_index += 1
    
    return metaword

def linearize(sentence):
    punctuation=['',' ','.','!',',',', ','?',';',':','"','" ','" ','"']
    parts = re.split(r'(\s+|\W)', sentence)
    converted_sentence,error_count = '',0
    print(parts)   ###
    exceptional_list_dict={
        'dough':'dou',
        'w':'dablu',
        'A':'a',        
        'i':'ai',
        'hi':'ai',          
        }
    for part in parts:
        if part not in exceptional_list_dict:
            if part not in punctuation:  
                part=punctuation_handling(part)
                try:
                    metaphone_word = metaphone(part)
                except:
                    error_count+=1 
                    metaphone_word="oops"
                converted_sentence += metaphone_word
            else:
                converted_sentence += part
        else:
            converted_sentence += exceptional_list_dict[part]
    print(converted_sentence, error_count)  ###
    return converted_sentence
def display_metaword(metaword):
    #create a mouthdict dictionary having png files for each alphabet

    mouthdict={
        ' ':'nothing.png',
        '.':'nothing.png',
        '!':'nothing.png',
        '?':'nothing.png',
        ',':'nothing.png',
        ', ':'nothing.png',
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
        '0':'t.png',   # for th
        'u':'u.png',
        'v':'v.png',
        'w':'w.png',
        'x':'x.png',  # for ch, sh. x.png is fine
        'y':'y.png',
        'z':'z.png'
    }
    
    for char in metaword:
        if char in mouthdict:
            mouth=mouthdict[char]
            print(mouth)
            cv2.imshow(f"{char}", cv2.imread("/Volumes/Anirudh/VS_Code/LipSyncing/SpeechMouthMan/"+mouth))
            cv2.waitKey(100)
            
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
  