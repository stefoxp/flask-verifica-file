import os, re

def uploaded_file(filename):
    file_list = []
    filename_out = "ELAB_" + filename + "z"
    UPLOAD_FOLDER = 'uploads'

    # apre il file
    with open(os.path.join(UPLOAD_FOLDER, filename), encoding="windows-1252") as file_input:
        for line in file_input:
            file_list.append(line)

    # salva in un nuovo file
    with open(os.path.join(UPLOAD_FOLDER, filename_out), encoding="utf8", mode="w") as file_output:
        for row in file_list:
            row_verified = row_verify(row)
            row_verified = row_verified[:-1]
            print(row_verified)
            print(row_verified, file=file_output)

        file_output.write("file elaborato correttamente")

def row_verify(row):
    row_verified = row
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
                        ("[å]", "SOLA"),
                        # (@"[^\u0000-\u007F]", " "),
                )
    
    for value in tup_to_change:
        row_verified = re.sub(value[0], value[1], row_verified)

    # row_verified = row_verified.replace("\n", " ")

    return row_verified

if __name__ == '__main__':
    uploaded_file("file_banca_prova.txt")