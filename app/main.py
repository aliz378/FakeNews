import os
# import tempfile
# import tensorflow as tf

# from tensorflow import keras
from flask import Flask, request, render_template


# UPLOAD_FOLDER = './static/files' 
# ALLOWED_EXTENSIONS = {'pdf'}

# load_dotenv(dotenv_path = '.env')
# tmpdir = tempfile.mkdtemp()
# mobilenet_save_path = os.path.join(tmpdir, "./models")
# model = tf.keras.models.load_model('./app/models/saved_model_2.pb')

app = Flask(__name__, template_folder='./templates')

@app.route('/quote', methods = ['GET'])
def quote():
    return render_template('html/get-a-quote.html')

@app.route('/contact', methods = ['GET'])
def contact():
    return render_template('html/contact.html')

@app.route('/services', methods = ['GET'])
def services():
    return render_template('html/services.html')

@app.route('/about', methods = ['GET'])
def about():
    return render_template('html/about.html')

@app.route('/', methods = ['GET','POST'])
def main():
    classification = ''
    if request.method == 'POST':
        text = request.form['statement']
        if text == '':
            classification = 'Inchequeable'
        else:
            classification = model.predict(text)

    return render_template('/html/index.html', classification=classification)

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=True, port=server_port, host='0.0.0.0')