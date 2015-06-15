from flask import Flask, render_template, jsonify
import sqlite3
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

#returns an html webpage
@app.route('/user/<username>')
def Native(username):
    return render_template('profile.html', name=username)

#returns a piece of data in JSON format
@app.route('/data')
def my_influencers():
    return jsonify({
        'stuart edge' : 26,
        'ryan higa' : 25,
        'Felix Arvid Ulf Kjellberg' : 25,
        'jenna marbles' : 28
    })

if __name__ == '__main__':
    app.run(debug=True)
