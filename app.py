import os, time, pickle, json
from flask import Flask, render_template, request, redirect
import engine

app = Flask(__name__)
app.debug = True


if True:
    ext = 'pickle'
    dump = pickle.dumps
    load = pickle.loads
else:
    # FIXME: needs custom JSONEncoder/Decoder
    ext = 'json'
    dump = json.dumps
    load = json.loads

fn = "trie.%s" % ext

if os.path.exists(fn):
    f = open(fn, 'r')
    trie = load(f.read())
    f.close()
else:
    trie = engine.build_trie()

    f = open(fn, 'wb')
    f.write(dump(trie))
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

