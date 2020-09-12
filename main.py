from flask import Flask, render_template, request, redirect, url_for
import subprocess
import random
from random import randint
import os

PEOPLE_FOLDER = os.path.join('static', 'people_photo')

app=Flask(__name__, template_folder='templates')
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route('/',methods=['POST','GET'])
def index():
    pred=["alarm clock","bicycle","bed","airplane","apple","belt","banana","cake"]
    # TODO: Take an list having the number and if you find the first number using random, remove that from the list and then find the other from (n-1) elements.
    i=pred[random.randint(0,7)]
    j=pred[random.randint(0,7)]
    k=pred[random.randint(0,7)]
    if request.method == 'GET':
        return render_template('index.html', u=i,v=j,w=k)

    if request.method == 'POST':
        draw=request.form.get("pict")
        if(draw == 'draw'):
            result=subprocess.check_output('python3 ./pictionary.py', shell=True)
            s=result.decode("utf-8").split()
            s=s[len(s)-2]
            return render_template('index.html', t=s, u=i,v=j,w=k)
        else:
            return redirect(url_for('guess'))

@app.route('/guess')
def guess():
    global str,src
    images=["basket.gif","book.gif","jpg_to_gif.gif"]
    str = images[random.randint(0,3)]
    src = os.path.join(app.config['UPLOAD_FOLDER'],str)
    return render_template('one.html', image=src)

@app.route('/check',methods=['POST','GET'])
def check():
    global str,src
    str=str.split('.')[0]
    if request.method == 'POST':
        guess=request.form["guess"]
        if guess == str:
            ans="Yes! You guessed it right."
            return render_template('one.html', image=src, answer=ans)
        else:
            ans="Sorry, You guessed it wrong."
            return render_template('one.html', image=src, answer=ans)
        

if __name__ == '__main__':
    app.run('localhost',5000,True)
