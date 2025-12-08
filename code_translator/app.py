
from flask import Flask, render_template, request
from translator import translate_code


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    output_code = ''
    source_language = 'C'
    target_language = 'Python'
    if request.method == 'POST':
        source_code = request.form['source_code']
        source_language = request.form['source_language']
        target_language = request.form['target_language']
        output_code = translate_code(source_code, source_language, target_language)
    return render_template('index.html', output_code=output_code, source_language=source_language, target_language=target_language)


if __name__ == '__main__':
    app.run(debug=True)
