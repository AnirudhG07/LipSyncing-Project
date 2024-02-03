# Giving AI Face and Voice
# LipSyncing-Project 
<br> This is a project to develop voice and LipSyncing of text to see if we can create a model where AI can have addition such features. 
This project uses regular python and not Neural Networks and ML.


Final Conclusion of this work is- "Just **speak to your laptop** and **NOW AI HAS A FACE WITH VOICE** with its Output Response!"

The project involves mainly 3 Sub-topics!
<ul><h3>
  1. Text to Lip Mouthing i.e. giving a Face
<br>2. A Voice Behind it
 <br> 3. An AI behind it
</h3></ul>
<br>
<h2>FLOWCHART OF FUNCTIONING:</h2>
YOUR_VOICE / TEXT(input) ---> AI MODEL reponse text ---> LipSyncing+ Voice ---> AI Response with Audio+Face
<h2>STEP 1: LipSyncing(LS)</h2>
I have used freely available png's of a man and depending on the input text. I use METAPHONE library of python to create some level of phonetics
to change input sentences to meta_word or meta_sentence(in my language). Each character is read and images are consecutively printed with fast speed to 
see moving mouth.

<h4>For example:</h4> 'Hello world' translates to 'helo vorlt' <br>
Helo is displayed as:<br>

<br><img width="96" alt="h" align="center" src="https://github.com/AnirudhG07/LipSyncing-Project/assets/146579014/fcb2ad28-ed86-42a4-a920-d7e71e21e80a"> **->**
<img width="96" alt="e" align="center" src="https://github.com/AnirudhG07/LipSyncing-Project/assets/146579014/b4adcd6d-a4ac-4ae0-9fa2-e7e6d23eb545"> **->**
<img width="96" alt="l" align="center" src="https://github.com/AnirudhG07/LipSyncing-Project/assets/146579014/279d0c64-218e-42ba-86fd-e7edaaa1804b"> **->**
<img width="96" alt="o" align="center" src="https://github.com/AnirudhG07/LipSyncing-Project/assets/146579014/236224ac-2d06-42ba-835b-02812cb929a1">

Another attempt as been made to put fade between transition of images. 

<h2>STEP 2: Voice</h2>
Three different voice libraries which are pyttsx3, gtts and whisper AI(from openai) are used to successfully produce voice simultaneously with the text.
<br>The voice and the image projection run independently and hence for each model, the voice has to be adjusted with different speeds manually. The appropriate readings
are written in #comments in the code. You can choose the model and automatically from pre-set data image video and audio will be outputted simulataneously creating
an effect of a speaking man. 
<br>Text without punctuations have proved almost 90% perfect voice and image_video fluency. Text with punctuation may sometime create discrapency due to uneven voice output of models used. 

<h2>STEP 3: AI Model Application</h2>
AI models now can use this above made model and can have a face with a voice now! Just input your question (or prompt) to your AI (preferably text-generation model) and 
it will produce required output with a voice and a face mouthing it! In future as this project goes you may see ChatGPT or other AI's having a face and voice!
One of example models made and pushed is Sentiment Analysis AI. 

<br><h2>Extra Perk: Voice to Text(STT)</h2>
Just speak to your laptop, with python speech recognition and python speech to text, the converted text will go as STEP-3 procedes!

-------------------------------------------------------------------------------

<h2> Scope of improvement</h2>

- The audio libraries used are variable and hard to control as it runs independently. Especially during punctuations, the uneven pause breaks the flow, and some words where it takes an exceptionally long time to speak. For example, the prefix 'un', pyttsx3 speaks as unnnnbiased or unnnable, while my images run u-n-a-b-l-e png's.

- Since voice and image projection run independently, they tend to deviate sometimes in between due to some words spoken differently compared to meta_word and for long texts, it may go out of sync too.

- This is why I am not able to properly fix it to gpt-3.5-turbo or gpt-4 because the text it produces has good quantity of punctuation. To maintain flow of voice you cannot just remove the punctuation to make it perfect (that it will speak perfectly).

- Whisper AI especially is very hard to use because it has an uneven big long pause((for different lengths of sentences) before it starts outputting any voice, so that is not very promising model to use.
