from flask import Flask, render_template, request, jsonify
import ply.lex as lex
import tokrules

app = Flask(__name__)

@app.route('/compile', methods=['POST'])
def compile():
    # print(request.json['text'])
    lexer = lex.lex(module=tokrules)
    # Give the lexer some input
    lexer.input(request.json['text'])

    # Tokenize
    token_chain = ''
    tokens_arr = []

    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        # print(tok.type, ',', tok.value)

        tokens_arr.append({
            'type': tok.type,
            'value': tok.value 
        })

        if tok.type == 'STRING' or tok.type == 'NUMBER':
            token_chain += tok.type + ' '
        else:
            token_chain += tok.value + ' '

    json_response = {
        'tokens': tokens_arr,
        'token_chain': token_chain
    }

    return jsonify(json_response)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/hv')
def hv():
    return render_template('hv.html')

@app.route('/terminos')
def terminos():
    return render_template('terminos.html')

@app.route('/alphabet-soup')
def alphabet_soup():
    return render_template('alphabet-soup.html')

if __name__ == '__main__':
    app.run()
