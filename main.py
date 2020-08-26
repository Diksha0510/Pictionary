from flask import Flask, render_template, Response, request
import subprocess
import random
from random import randint
# from a import pictionary

app=Flask(__name__, template_folder='templates')

@app.route('/',methods=['POST','GET'])
def index():
    # return 'Hello world'
    if request.method == 'GET':
    # return '%s'%result
        pred=["alarm clock","bicycle","bed","airplane","apple","belt","banana","cake"]
        i=pred[random.randint(0,7)]
        j=pred[random.randint(0,7)]
        k=pred[random.randint(0,7)]
        return render_template('index.html', u=i,v=j,w=k)
    # t=pictionary().run()

    if request.method == 'POST':
        result=subprocess.check_output('python3 /home/diksha/pictionary/begard.py', shell=True)
        s=result.decode("utf-8").split('\n')
        s=s[len(s)-2]
        return render_template('index.html', t=s)
        # return redirect(url_for('base'))

# @app.route('/result',methods=['POST','GET'])
# def result():


@app.route('/base')
def base():
    return 'hello'
    # return render_template('hello.html')


#
# def gen():
#     while True:
#         frame=pictionary().run()
#         yield(b'--frame\r\n'
#               b'Content-Type:image/jpeg\r\n\r\n'+ frame +b'\r\n\r\n')

# @app.route('/camera_feed')
# def camera_feed():
#     t=pictionary.ru()
#     return render_template('index.html', t=t)
    # return '%s'%t
    # return Response(gen(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run('localhost',5000,True)
