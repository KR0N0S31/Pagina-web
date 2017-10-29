from flask import Flask, render_template
from pScraping import scraping

app = Flask(__name__)
PORT = 5000
DEBUG = False

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route(r'/', methods =['GET'])
def index():
    return render_template('page.html', cursos = scraping() )

if __name__ == '__main__':
    app.run(port = PORT, debug = DEBUG)
