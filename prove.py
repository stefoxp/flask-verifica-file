import re

html = "0åbàcádâeãfägæh [ÓÒÖÔÕ] at@at canc#canc"

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
                        # (@"[^\u0000-\u007F]", " "),
                )
    for value in tup_to_change:
        row_verified = re.sub(value[0], value[1], row_verified)
        # row_verified.replace(value[0], value[1])
    
    return row_verified


print(html)

html_verified = row_verify(html)

# html = re.sub(r"[åàáâãäæ]", "a", html)

print(html_verified)