from flask import Flask, render_template, request
import main_methods

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/calc', methods=['POST'])
def run_code():
    string = request.form['string']
    char = request.form['character']
    leng = main_methods.word_length(string)
    matching = main_methods.matching_char(string, char)
    palin = main_methods.palindrome_or_not(string)
    rever = main_methods.reverse(string)
    caps = main_methods.capitalize_string(string)
    return render_template('pass.html', l=leng, m=matching, p=palin, r=rever, c=caps)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

