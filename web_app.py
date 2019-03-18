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

@app.route('/home')  # To get back to the home page
def return_home_page():
    return render_template('home.html')

###
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

###
@app.route('/britney_spears')  # britney song page
def britney_page():
    return render_template('britney_spears.html')

# Song commmands for Britney Spears songs
@app.route('/baby_one_more_time')
def britney_song1():
    systemCommand("britney_spears", "baby_one_more_time")
    return render_template('britney_spears.html')

@app.route('/circus')
def britney_song2():
    systemCommand("britney_spears", "circus")
    return render_template('britney_spears.html')

@app.route('/gimme_more')
def britney_song3():
    systemCommand("britney_spears", "gimme_more")
    return render_template('britney_spears.html')

@app.route('/hold_it_against_me')
def britney_song4():
    systemCommand("britney_spears", "hold_it_against_me")
    return render_template('britney_spears.html')

@app.route('/i_wanna_go')
def britney_song5():
    systemCommand("britney_spears", "i_wanna_go")
    return render_template('britney_spears.html')

@app.route('/if_u_seek_amy')
def britney_song6():
    systemCommand("britney_spears", "if_u_seek_amy")
    return render_template('britney_spears.html')

@app.route('/oops_i_did_it_again')
def britney_song7():
    systemCommand("britney_spears", "oops_i_did_it_again")
    return render_template('britney_spears.html')

@app.route('/three')
def britney_song8():
    systemCommand("britney_spears", "three")
    return render_template('britney_spears.html')

@app.route('/till_the_world_ends')
def britney_song9():
    systemCommand("britney_spears", "till_the_world_ends")
    return render_template('britney_spears.html')

@app.route('/toxic')
def britney_song10():
    systemCommand("britney_spears", "toxic")
    return render_template('britney_spears.html')

@app.route('/womanizer')
def britney_song11():
    systemCommand("britney_spears", "womanizer")
    return render_template('britney_spears.html')

@app.route('/work_bitch_remix')
def britney_song12():
    systemCommand("britney_spears", "work_bitch_remix")
    return render_template('britney_spears.html')


###
@app.route('/cascada')  # cascada song page
def cascada_page():
    return render_template('cascada.html')

# Song commands for Cascada songs
@app.route('/bad_boy')
def cascada_song1():
    systemCommand("cascada", "bad_boy")
    return render_template('cascada.html')

@app.route('/dangerous')
def cascada_song2():
    systemCommand("cascada", "dangerous")
    return render_template('cascada.html')

@app.route('/evacuate_the_dancefloor')
def cascada_song3():
    systemCommand("cascada", "evacuate_the_dancefloor")
    return render_template('cascada.html')

@app.route('/everytime_we_touch')
def cascada_song4():
    systemCommand("cascada", "everytime_we_touch")
    return render_template('cascada.html')

@app.route('/miracle')
def cascada_song5():
    systemCommand("cascada", "miracle")
    return render_template('cascada.html')

@app.route('/ready_or_not')
def cascada_song6():
    systemCommand("cascada", "ready_or_not")
    return render_template('cascada.html')

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port='5000', debug=True)
    except KeyboardInterrupt:
        os.system("fuser -k 5000/tcp")  # Clean up port
        app.exit()
    

