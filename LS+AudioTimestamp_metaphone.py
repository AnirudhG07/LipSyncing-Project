import cv2
import time, timeit
from metaphone import doublemetaphone
import re
import os
import assemblyai as aai

def exceptional_handling(excep_list:list,word:str)->bool:
    for exc in excep_list:
        if exc in word:
            return False
            break
    return True

def punctuation_handling(word:str)->str:
    freeword=''
    for char in word:
        freeword+=char if 'a'<=char<='z' else ''
    return freeword

def metaphone(word:str)->str:
    metaword=''
    word=word.lower()
    pattern = r'([^aeiou])\1{1,}'

    if '-' in word:
        ind=word.index('-')
        return metaphone(word[:ind])+metaphone(word[ind+1:])
    if not 'a'<=word[-1]<='z':
        word=word[:-1]
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
    exceptional_listfor_y=['cry','dry','fly','sly','try','wry']
    exceptional_listfor_e=['hare','rte','we','qe','he']
    pattern2= r'(sh|th|ch|ph|bh|gn|rh|lh|ck)'
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
            else:
                word=word.replace('gh','')
        if word[-1]=='e' and exceptional_handling(exceptional_listfor_e,word):
            word=word[:-1]
        if word[-1]=='y' and exceptional_handling(exceptional_listfor_y,word):
            word=word[:-1]+'i'
        if word[0]=='y':
            word=word[1:]
        if word[-1]=='w' and len(word)==3:
            word=word[0]+'a'+word[1:-1]
        if word[-1]=='w' and len(word)!=3:
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
                metaword += char
            
        else:
        # If the character is not a vowel (i.e., a consonant), add a consonant from the Metaphone representation           
            metaword += meta[consonant_index]
            consonant_index += 1
    
    return metaword

def linearize(sentence:str)->str:

    parts = re.split(r'(\s+)', sentence)
    converted_sentence,error_count = '',0
    print(parts)   ###
    exceptional_list_dict={
        'dough':'dou',
        'w':'dablu', 
        'A':'a',  
        'I':'ai'  
                           }
    for part in parts:
        if part not in exceptional_list_dict:
            if part!='' and part!=' ':      # only giving words ahead
                part=punctuation_handling(part)
                try:
                    metaphone_word = metaphone(part)
                except:
                    error_count+=1 
                    metaphone_word="oops"    # will output oops instead stopping the code.
                converted_sentence += metaphone_word
            else:
                converted_sentence += part
        else:
            converted_sentence += exceptional_list_dict[part]

    print(converted_sentence, error_count)  ###
    return converted_sentence
def display_metaword(time_ordered:list,meta_sentence:list):
    #create a mouthdict dictionary having png files for each alphabet

    mouthdict={
        ' ':'nothing.png',
        '.':'nothing.png',
        'a':'A,E,I.png',
        'b':'B,M,P.png',
        'c':'C,G,T,Y.png',
        'd':'B,M,P.png',
        'e':'A,E,I.png',
        'f':'F,V.png',
        'g':'C,G,T,Y.png',
    #   'h':'B,M,P.png',
        'i':'A,E,I.png',
        'j':'Ch,J,Sh.png',
        'k':'C,G,T,Y.png',
        'l':'L.png',
        'm':'B,M,P.png',
        'n':'C,G,T,Y.png',  # for this to be better, same c g t y but lesser smile
        'o':'O.png',
        'p':'B,M,P.png',
        'q':'Q,W.png',
        'r':'R.png',
        's':'C,G,T,Y.png', 
        't':'C,G,T,Y.png',
        '0':'Th.png',  #metaphone has Th as 0
        'u':'O.png',   # i need a better u, similar to O but mouth smaller
        'v':'F,V.png',
        'w':'Q,W.png',
        'x':'Ch,J,Sh.png',   #metaphone has sh,ch as X 
        'y':'C,G,T,Y.png',
        'z':'C,G,T,Y.png',
        '1':'U.png'
    }
    deviation=[]
    print(len(meta_sentence),len(time_ordered))
    for i in range(len(meta_sentence)):
        start=timeit.default_timer()
        for char in meta_sentence[i]:
            if char in mouthdict:
                mouth=mouthdict[char]
                print(mouth)
                cv2.imshow(f"{char}", cv2.imread("./LipSyncing/"+mouth))
                cv2.waitKey(49*(time_ordered[i][1]-time_ordered[i][0])//(60*len(meta_sent[i])))
                
                cv2.destroyAllWindows()
        stop=timeit.default_timer()
        print("Time for word",i,":",stop-start,"deviation:",(stop-start)*1000-(time_ordered[i][1]-time_ordered[i][0]))

def audiostamping()->list: # no input. the input is audio file which MUST be called inside
    
    #set API KEY for aai
    aai.settings.api_key = "d945aa928bb34618b90e7f0b4483279e"

    transcriber=aai.Transcriber()
    #transcript=transcriber.transcribe("LINK https://linkname.com/.../().mp3") #.mp3 at the end is important
    transcript= transcriber.transcribe("./LipSyncing/harvard.mp3")
    global audiotext
    audiotext=transcript.text
    print(audiotext)   ###
    audiotext_ls=audiotext.split()

    word_time=[]
    timestamps=[]
    for i  in range (len(audiotext_ls)):
        word_time=transcript.word_search([audiotext_ls[i]])
        for time in word_time:
            timestamps.append(time.timestamps)
    print(timestamps)
    unpacked_time = []
    for sublist in timestamps:
        for item in sublist:
            if item not in unpacked_time:
                unpacked_time.append(item)

    # Sort the unpacked data
    sorted_data = sorted(unpacked_time)

    # Add in tuples covering the in between gaps
    time_order,start =[],0
    for i in range(len(sorted_data)):
        if sorted_data[i][0]!=start:
            time_order.append((start,sorted_data[i][0]))
            time_order.append((sorted_data[i][0],sorted_data[i][1]))
            start=sorted_data[i][1]
    
    #we will get an order of words with time, no duplicates in order
    print(time_order)    # prints correctly. [(0,1),(1,3)..etc]
    return time_order

if __name__=="__main__":
    ordered_time,meta_sent=[],''
    ordered_time=audiostamping()
    print(ordered_time)
    meta_sent=linearize(audiotext)
    meta_sent = [' ']+re.split(r'(\s+)', meta_sent)
    print(meta_sent)

    display_metaword(ordered_time,meta_sent)
    