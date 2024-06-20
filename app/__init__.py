import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


# Links declared for dynamic rendering in template
nav_menu = [
    {'name': 'Home', 'url': '/'},
    {'name': 'Hobbies', 'url': '/hobbies'},
    {'name': 'Experience', 'url': '/experience'},
    {'name': 'Education', 'url': '/education'}
]


# Function that sets one link to active based on the rendered page
def active_menu(menu, url):
    for item in menu:
        if item['url'] == url:
            item['active'] = True
        else:
            item['active'] = False
    return menu


@app.route('/')
def index():
    print(active_menu(nav_menu, '/'))
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"), menu=active_menu(nav_menu, '/'))


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', title="Hobbies", url=os.getenv("URL"), menu=active_menu(nav_menu, '/hobbies'))


@app.route('/experience')
def hobbies():
    return render_template('experience.html', title="Hobbies", url=os.getenv("URL"), menu=active_menu(nav_menu, '/experience'))


@app.route('/education')
def hobbies():
    return render_template('experience.html', title="Hobbies", url=os.getenv("URL"), menu=active_menu(nav_menu, '/education'))
