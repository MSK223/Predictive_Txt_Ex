import os
from flask import Flask, render_template, request, redirect
import engine

app = Flask(__name__)
app.debug = True

#Index page
@app.route('/', methods=['POST','GET'])
def hello():
    return render_template("index.html")

# Posts back the predictive results from model to ajax
@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    txt_so_far = None

    if request.method == 'POST':
        txt_so_far = str(request.form['msg'])
    
    if txt_so_far:
        predict = engine.predict(txt_so_far)
    else:
        predict = []
    
    return ' '.join(predict)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

