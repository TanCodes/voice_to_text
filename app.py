from flask import Flask , render_template , request
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/speech' , methods=["POST"])
def speech():
    if request.method == "POST":
        r = sr.Recognizer()
        engine = pyttsx3.init()

        with sr.Microphone() as source:
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                result = text
                rate = engine.getProperty("rate")
                engine.setProperty("rate",100)
                engine.say(text)
                engine.runAndWait()
                return render_template('home.html', result=result)

            except:
                error = "Sorry, can't read"
                engine.say(error)
                engine.runAndWait()
                return render_template('home.html', error=error)

    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
