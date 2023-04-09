from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Got any creative ideas for a 10 year old’s birthday continue the groovy script by adding a deleting stage for the images after creation tested and it all deploy according to jenkins pipeline'

if __name__ == '__main__':
    app.run()