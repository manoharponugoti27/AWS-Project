from flask import Flask, render_template, send_file
import os

app = Flask(__name__)

# Set the folder path where the images are located
IMAGE_FOLDER = os.path.join('static', 'images')

# Define a route to display the home page with all the images
@app.route('/')
def home():
    # Get a list of all the image filenames in the folder
    image_names = os.listdir(IMAGE_FOLDER)
    # Render the home.html template with the list of image filenames
    return render_template('home.html', image_names=image_names)

# Define a route to download a specific image file
@app.route('/download/<filename>')
def download(filename):
    # Generate the file path for the requested image
    file_path = os.path.join(IMAGE_FOLDER, filename)
    # Send the file for download
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
