import os, time, pickle
from flask import Flask, render_template, request, redirect
import engine

app = Flask(__name__)
app.debug = True

if os.path.exists('trie.out'):
    f = open('trie.out', 'r')
    trie = pickle.loads(f.read())
    f.close()
else:
    trie = engine.build_trie()

    f = open('trie.out', 'wb')
    f.write(pickle.dumps(trie))
    f.close()


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
        prediction = engine.predict(trie, txt_so_far)
    else:
        prediction = []
    
    return ' '.join(prediction)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)

