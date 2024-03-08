import pyttsx3
import PyPDF2

pdfreader = PyPDF2.PdfReader(open('Manual.pdf', 'rb'))
speaker = pyttsx3.init()

# Print information about all available voices
voices = speaker.getProperty('voices')
for index, voice in enumerate(voices):
    print(f"Voice {index} - ID: {voice.id}, Name: {voice.name}, Lang: {voice.languages}")

# Set the voice to Spanish (replace the index based on your identification)
spanish_voice_index = 2  # Change this to the correct index
speaker.setProperty('voice', voices[spanish_voice_index].id)

# Adjust the speed (you can experiment with the values)
speed = 120  # Adjust as needed, higher values for faster speed
speaker.setProperty('rate', speed)

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
    
    # Add each page's text to the audio file
    speaker.save_to_file(clean_text, f'CssAudioBook_page_{page_num + 1}.mp3')

speaker.runAndWait()

speaker.stop()
