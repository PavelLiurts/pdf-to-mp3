from pip import main
import pdfplumber
from gtts import gTTS


def conversion():

    with pdfplumber.open("w3c.pdf") as pdf:
        # extract the text of all pages
        for page in pdf.pages:
            example_text = ""
            example_text += page.extract_text()

    tts = gTTS(text=example_text, lang='en')
    tts.save('conversion_audio.mp3')
    return 'MP3 saved successfully'


def main():
    print(conversion())


if __name__ == '__main__':
    main()
