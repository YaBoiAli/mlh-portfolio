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
    hobbies = {
        "Creative Pursuits": [
            {"name": "Calligraphy", "description": "Practicing beautiful handwriting and letter design.", "image": "./static/img/57810812c56f8f67b043e6c95a802408.jpg"},
            {"name": "Poetry", "description": "Crafting verses and exploring literary expressions.", "image": "./static/img/images.jpeg"},
            {"name": "Painting", "description": "Experimenting with colors and techniques on canvas.", "image": "./static/img/painting.jpeg"}
        ],
        "Active and Culinary": [
            {"name": "Basketball", "description": "Playing games and staying active on the court.", "image": "./static/img/MBB-WBB_BallHoop.jpeg"},
            {"name": "Cooking/Baking", "description": "Trying out new recipes and baking delicious treats.", "image": "./static/img/cooking.jpg"}
        ],
    }
    return render_template('hobbies.html', hobbies=hobbies, menu=active_menu(nav_menu, '/hobbies'))


@app.route('/experience')
def experience():
    return render_template('experience.html', title="Experience", url=os.getenv("URL"), menu=active_menu(nav_menu, '/experience'))


@app.route('/education')
def education():
    return render_template('education.html', title="Education", url=os.getenv("URL"), menu=active_menu(nav_menu, '/education'))
