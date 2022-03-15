# Package import

from flask import Flask, render_template, send_file, make_response, url_for, Response, redirect, request
from find_eo import *
# initialise app
app = Flask(__name__)


# decorator for homepage
@app.route('/')
def index():
    return render_template('index.html', value="",
                           PageTitle="Landing page")


# These functions will run when POST method is used.
@app.route('/', methods=["POST"])
def make_eo():
    scr = request.form.get("scramble").rstrip()
    try:
        eos, eos_dict = find_eo(scr)
        noeos = len(eos)
        no0, no1, no2, no3, no4, no5 = 0, 0, 0, 0, 0, 0
        if "eoskip" in eos:
            no0 = 1
        for eo in eos:
            if len(eo.split()) == 1:
                no1 = no1 + 1
            if len(eo.split()) == 2:
                no2 = no2 + 1
            if len(eo.split()) == 3:
                no3 = no3 + 1
            if len(eo.split()) == 4:
                no4 = no4 + 1
            if len(eo.split()) == 5:
                no5 = no5 + 1

        return render_template('index.html', scr = scr, value=eos, noeos = noeos, no0 = no0, no1 = no1, no2 = no2, no3 = no3, no4 = no4, no5 = no5,
                               PageTitle="Landing page")
    except KeyError:
        return render_template('index.html', value="",
                               PageTitle="Landing page")
        # The created image will be opened on a new page

    # This just reloads the page if no file is selected and the user tries to POST.
if __name__ == '__main__':
    app.run(debug=True)