from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('welcome.html', name=name)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()


<!-- templates/index.html -->
<!doctype html>
<html>
  <body>
    <form action="/" method="post">
      <label for="name">Enter your name:</label>
      <input type="text" id="name" name="name">
      <button type="submit">Submit</button>
    </form>
  </body>
</html>

<!-- templates/welcome.html -->
<!doctype html>
<html>
  <body>
    <h1>Welcome {{ name }}!</h1>
  </body>
</html>

