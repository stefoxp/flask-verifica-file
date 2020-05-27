import os, re

from flask import Flask, flash, redirect, request, url_for, render_template, make_response
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)

def transform_file(file_in):
    '''
        grazie a https://stackoverflow.com/questions/27628053/uploading-and-downloading-files-with-flask
    '''
    # legge il file
    file_input = file_in.stream.read().decode("windows-1252")

    file_verified = char_replace(file_input)

    # visualizza il file elaborato
    return file_verified

def char_replace(file_content):
    file_content_verified = file_content
    tup_to_change = (
                        ("[åàáâãäæ]", "a"),
                        ("[ÁÀÄÃÅÂ]", "A"),
                        ("[èéêë]", "e"),
                        ("[ÈÉËÊ]", "E"),
                        ("[ìíîï]", "i"),
                        ("[ÍÌÏÎ]", "I"),
                        ("[òóôõö]", "o"),
                        ("[ÓÒÖÔÕ]", "O"),
                        ("[ùúûü]", "u"),
                        ("[ÚÙÛÜ]", "U"),
                        ("[¥]", "N"),
                        ("[ý]", "y"),
                        ("[Š]", "S"),
                        ("[š]", "s"),
                        ("[ç]", "c"),
                        ("[ñ]", "n"),
                        ("[Ñ]", "N"),
                        ("[ž]", "z"),
                        ("[[]", "("),
                        ("[]]", ")"),
                        ("[@]", " "),
                        ("[#]", " "),
                        ("[ø]", " "),
                        # (@"[^\u0000-\u007F]", " "),
                )
    for value in tup_to_change:
        file_content_verified = re.sub(value[0], value[1], file_content_verified)

    file_content_verified = file_content_verified.replace("\n\n", "\n")
    
    return file_content_verified

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('Nessun file selezionato')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # verifica, modifica e restituisce il file
            result = transform_file(file)
            response = make_response(result)
            response.headers["Content-Disposition"] = "attachment; filename=VERIFICATO_" + file.filename + ""
            return response

    return render_template("home.html")
