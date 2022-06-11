# AUTHOR: BERKE AVCI

def fstr(var:str):
    m_var = var
    lexer = []
    is_column_opened = False
    for i in var:
        if i == "}":
            is_column_opened = False
            lexer.append(i)
        if is_column_opened == True:
            lexer.append(i)
        if i == "{":
            is_column_opened = True
            lexer.append(i)
    lexer_str = "".join(lexer)
    start_column_split = lexer_str.split("{")
    lexer_variables = "".join(start_column_split).split("}")
    lexer_variables.pop()
    lexer_keys = {}
    for i in lexer_variables:
        eval_variable = globals()[i]
        lexer_keys.update({i: eval_variable})
    for i in lexer_variables:
        m_var = m_var.replace("{"+i+"}", lexer_keys[i])
    
# asd = " Avcı"
# HELLO = "NABER R."
# print(fstr("Berke{asd}\n{HELLO}"))
