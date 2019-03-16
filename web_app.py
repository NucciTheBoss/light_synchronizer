# !/home/pi/lightshowpi/web/microweb
# File must be run on Raspberry Pi 2 with lightshowpi preinstalled
# web_app.py has  to be located in the directory specified above
# If it isn't, then the program will not work
# html files are stored in the templates folder
# css files are stored in the static folder

from flask import Flask, render_template
from flask.views import View
import os  # To execute statements in the command line

app = Flask(__name__)

# Function definition for executing songs in the command line
def systemCommand(folder_name, song_name):
    os.system("sudo python py/synchronized_lights.py --file=/home/pi/lightshowpi/music/{}/{}.mp3".format(folder_name, song_name))
    # Will begin playing the song until either the user interrupts the program or the song is finished
    # Each song is stored in a specific folder, depending on the artist
  
  
# Function for returning pages when the hrefs are clicked
def returnPage(pagename):
    # pagename must have the .html extension included
    return render_template(pagename)
    

@app.route('/')  # For when the user first loads the page
def index():
    return render_template('home.html')
    
# url rules for the specific webpages
app.add_url_rule('/', 'home', returnPage("home.html"))
app.add_url_rule('/', 'arianna_grande', returnPage("arianna_grande.html"))
app.add_url_rule('/', 'britney_spears', returnPage("britney_spears.html"))
app.add_url_rule('/', 'cascada', returnPage("cascada.html"))
app.add_url_rule('/', 'demi_lovato', returnPage("demi_lovato.html"))
app.add_url_rule('/', 'daft_punk', returnPage("daft_punk.html"))
app.add_url_rule('/', 'misc', returnPage("misc.html"))

# url rules for arianna_grande.html

# url rules for britney_spears.html

# url rules for cascada.html

# url rules for demi_lovato.html

# url rules for daft_punk.html

# url rules for misc.html


if __name__ == '__main__':
    try:
        app.run(host="0.0.0.0", port=5000, debug=True)
    except KeyboardInterrupt:
        exit()
