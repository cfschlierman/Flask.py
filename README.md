from flask import Flask, render_template, JOSONify
import sqlite3
app = Flask(__name__)

@app.route('/user/<username>')
def hello_world():
    return 'Hello World!'

#returns an html webpage
@app.route('/')
def Native(username):
    return render_template('profile.html'
                                           name=username)'

#returns a piece of data in JSON format
@app.route('/data')
def my_influencers{ 'stuart edge' : 26,
                          'ryan higa' : 25,
                          'Felix Arvid Ulf Kjellberg' : 25,
                          'jenna marbles' : 28}
return jsonify (my_influencers)

if __name__ == '__main__':
    app.run(debug=True)











templates/profile.html

<html>

<head>
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>

<script type="text/javascript">
$(document).ready(function() [
$("#getdata").click(function() [

$.getjson('/data', function(data) {
console.log("ajax received data!");
console.dir(dat);
});
});

});
</script>

</head>

<body>
{% if name %}
<h1 style = "color: red;">hello, {{ name }} ! </h1>
</body>
