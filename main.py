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
    # return 'Hello world'
    pred=["alarm clock","bicycle","bed","airplane","apple","belt","banana","cake"]
    i=pred[random.randint(0,7)]
    j=pred[random.randint(0,7)]
    k=pred[random.randint(0,7)]
    if request.method == 'GET':
    # return '%s'%result
        return render_template('index.html', u=i,v=j,w=k)
    # t=pictionary().run()

    if request.method == 'POST':
        draw=request.form.get("pict")
        # print(draw)
        # guess=values['guess']
        # draw=values["draw"]
        if(draw == 'draw'):
            result=subprocess.check_output('python3 /home/diksha/pictionary/begard.py', shell=True)
            s=result.decode("utf-8").split()
            s=s[len(s)-2]
            return render_template('index.html', t=s, u=i,v=j,w=k)
        else:
            return redirect(url_for('guess'))

@app.route('/guess')
def guess():
    # return 'hello'
    images=["basket.gif","book.gif","jpg_to_gif.gif"]
    str=images[random.randint(0,10)]
    src = os.path.join(app.config['UPLOAD_FOLDER'],str)
    # src=r'/home/diksha/python/jpg_to_gif.gif'
    return render_template('one.html', image=src)

@app.route('/check',methods=['POST','GET'])
def check():
    if request.method == 'POST':
        guess=request.form["guess"]
        # if guess ==



if __name__ == '__main__':
    app.run('localhost',5000,True)
