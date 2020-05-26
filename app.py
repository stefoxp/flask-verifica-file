import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    file_list = []

    # apre il file
    with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), encoding="windows-1252") as file_input:
        for line in file_input:
            file_list.append(line)

    # aggiunge una riga
    file_list.append("ELABORATO")

    # salva in un nuovo file
    with open(os.path.join(app.config['UPLOAD_FOLDER'], "ELAB_" + filename), encoding="utf8", mode="w") as file_output:
        for row in file_list:
            print(row, file=file_output)

        file_output.write("file elaborato correttamente")

    # visualizza il file elaborato
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               "ELAB_" + filename)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
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
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Verifica un file</title>
    <h1>Verifica un file</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Verifica>
    </form>
    '''