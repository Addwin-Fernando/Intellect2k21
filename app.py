from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/admin') 
def home():
    return render_template('index.html')

@app.route('/artella') 
def artella():
    return render_template('artella.html')


@app.route('/valo') 
def valo():
    return render_template('valo.html')

@app.route('/') 
def admin():
    return render_template('admin.html')


@app.route('/Cookaholics') 
def Cookaholics():
    return render_template('Cookaholics.html')


@app.route('/essay') 
def essay():
    return render_template('essay.html')


@app.route('/photo') 
def photo():
    return render_template('photo.html')


@app.route('/voice')
def voice():
    return render_template('voice.html')

@app.route('/reels') 
def reels():
    return render_template('reels.html')


@app.route('/meme') 
def meme():
    return render_template('meme.html')


@app.route('/reachout') 
def reachout():
    return render_template('reachout.html')


@app.route('/crossword') 
def crossword():
    return render_template('crossword.html')

@app.route('/winners') 
def winners():
    return render_template('winners.html')

     

@app.route('/about') 
def about_page():
    return render_template('about.html')


@app.route('/secret',methods=["POST","GET"])
def altair():
    return render_template('secret.html')    

"""
http://0.0.0.0:8080/api/saponihimym

"""

@app.route('/api/saponihimym',methods=["POST","GET"])    
def hello_world2():
    key = request.values.get("secret")
    print(key)
    if (key=='pass'):
        return 'Access Granted'
    return render_template('404.html')    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)