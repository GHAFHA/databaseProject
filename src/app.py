from flask import Flask, render_template
from flask import request
from db_actions import search_books

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search')
def search():
    search_query = request.args.get('query')
    search_results = search_books(search_query)
    return render_template('search_results.html', results=search_results)


if __name__ == '__main__':
    app.run(debug=True)
