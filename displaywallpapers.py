from flask import Flask, render_template, send_file
import os

app = Flask(__name__)
app.config['WALLPAPERS_FOLDER'] = 'Wallpapers'

@app.route('/')
def index():
    # Get a list of all wallpapers
    wallpapers = os.listdir(app.config['WALLPAPERS_FOLDER'])
    return render_template('home.html', wallpapers=wallpapers)

@app.route('/wallpapers/<filename>')
def wallpaper(filename):
    return send_file(os.path.join(app.config['WALLPAPERS_FOLDER'], filename))

if __name__ == '__main__':
    app.run(debug=True)

'''
from flask import Flask, render_template

app = Flask(__name__)

# Define a list of images to display
images = [
    {'filename': 'C:\\Users\\umama\\OneDrive\\Desktop\\AWSProject\\Wallpapers\\Aesthetic-Background-Laptop-Couple-Anime.jpg', 'caption': 'Image 1'},
    {'filename': 'Aesthetic-Background-Laptop-Couple-Anime.jpg', 'caption': 'Image 2'},
    {'filename': 'Aesthetic-Background-Laptop-Couple-Anime.jpg', 'caption': 'Image 3'}
]

@app.route('/')
def home():
    return render_template('home.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)'''

