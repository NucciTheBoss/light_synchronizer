# !/home/pi/lightshowpi/web/microweb
# File must be run on Raspberry Pi 2 with lightshowpi preinstalled
# web_app.py has  to be located in the directory specified above
# If it isn't, then the program will not work
# html files are stored in the templates folder
# css files are stored in the static folder

# The program also has to be started from the command line
# The python interpreter will not respond to ^C

from flask import Flask, render_template
import os  # To execute statements in the command line

app = Flask(__name__)

# Function definition for executing songs in the command line
def systemCommand(folder_name, song_name):
    os.system("sudo python py/synchronized_lights.py --file=/home/pi/lightshowpi/music/{}/{}.mp3".format(folder_name, song_name))
    # Will begin playing the song until either the user interrupts the program or the song is finished
    # Each song is stored in a specific folder, depending on the artist
    return  # Allow render_template to return desired html page


@app.route('/')  # For when the user first loads the page
def home_page():
    return render_template('home.html')

@app.route('/ariana_grande')  # ariana song page
def ariana_page():
    return render_template('ariana_grande.html')

# Song commands for ariana grande page
@app.route('/bang_bang')
def ariana_song1():
    systemCommand("ariana_grande", "bang_bang")
    return render_template("ariana_grande.html")

@app.route('/breathin')
def ariana_song2():
    systemCommand("ariana_grande", "breathin")
    return render_template("ariana_grande.html")

@app.route('/into_you')
def ariana_song3():
    systemCommand("ariana_grande", "into_you")
    return render_template("ariana_grande.html")

@app.route('/no_more_tears_left_to_cry')
def ariana_song4():
    systemCommand("ariana_grande", "no_more_tears_left_to cry")
    return render_template("ariana_grande.html")

@app.route('/one_last_time')
def ariana_song5():
    systemCommand("ariana_grande", "one_last_time")
    return render_template("ariana_grande.html")

@app.route('/problem')
def ariana_song6():
    systemCommand("ariana_grande", "problem")
    return render_template("ariana_grande.html")

@app.route('/side_to_side')
def ariana_song7():
    systemCommand("ariana_grande", "side_to_side")
    return render_template("ariana_grande.html")

@app.route('/britney_spears')  # britney song page
def britney_page():
    return render_template('britney_spears.html')

@app.route('/cascada')  # cascada song page
def cascada_page():
    return render_template('cascada.html')

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port='5000', debug=True)
    except KeyboardInterrupt:
        os.system("fuser -k 5000/tcp")  # Clean up port
        app.exit()
    

