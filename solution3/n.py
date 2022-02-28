import io

from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)


n1 = 0


@app.route('/gallery', methods=['POST', 'GET'])
def index():
    global n1
    list_mars = ["static/img/marss2.png", "static/img/marss3.png"]
    if request.method == 'GET':
        return render_template('index.html', list_mars=list_mars)
    elif request.method == 'POST':
        n1 += 1
        n = (request.files['file']).read()
        im = Image.open(io.BytesIO(n))
        list_mars.append(f"static/img/pic{n1}.png")
        im.save(f"static/img/pic{n1}.png")
        return render_template('index.html', list_mars=list_mars)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')