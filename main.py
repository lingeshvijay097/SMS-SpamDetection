from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
CV = pickle.load(open('CV1.pkl', 'rb'))
model = pickle.load(open('SpamPkl.pkl', 'rb'))


@app.route('/')
def ShowHome():
    return render_template('index.html')


@app.route('/pred', methods=['POST'])
def ShowRes():
    word = request.form['inp']
    print("he")
    print(word)
    word1 = CV.transform([word])
    print(word1.toarray())
    pred = model.predict(word1)
    print(pred[0])
    if pred[0]==0:
        res="Not a spam message"
    else:
        res="Be aware it is spam message"
    return render_template('index.html',res=res)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
