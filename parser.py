import ply.yacc as yacc 
import ply.lex as lex
import tokrules

tokens = tokrules.tokens
# Build the lexer
lexer = lex.lex(module=tokrules)
# 3 + 5 * ( 10 - 20 )

precedence = (
    ('right', 'MAIN'),
    ('right', 'VAR'),
    ('right', 'ASSIGN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

def p_program(p):
    '''program : blocklist'''
    print('program')

def p_block1(p):
    '''block : vardef'''
    print('block1')

def p_block2(p):
    '''block : main'''
    print('block2')

def p_blockempty(p):
    '''block : empty'''
    print('blockempty')

def p_blocklist1(p):
    '''blocklist : block'''
    print('blocklist1')

def p_blocklist2(p):
    '''blocklist : blocklist block'''
    print("blocklist")

def p_vardef(p):
    '''vardef : VAR idlist SEMICOLON'''
    print("vardef")

def p_idlist1(p):
    '''idlist : VARIABLE ASSIGN NUMBER'''
    print("idlist1")

def p_idlist2(p):
    '''idlist : idlist COMMA VARIABLE ASSIGN NUMBER'''
    print("idlist2")

def p_main(p):
    '''main : MAIN LBRACE statementlist RBRACE'''
    print('main')

def p_statement1(p):
    '''statement : expr'''

def p_statementEmpty(p):
    '''statement : empty'''
    print('statementempty')

def p_statementlist1(p):
    '''statementlist : statement'''
    print('statementlist1')

def p_statementlist2(p):
    '''statementlist : statementlist SEMICOLON statement'''
    print('statementlist2')

def p_expr_plus(p):
    '''expr : expr PLUS term'''
    print("plus")
    # p[0] = p[1] + p[3]

def p_expr_minus(p):
    '''expr : expr MINUS term'''
    print("minus")
    # p[0] = p[1] + p[3]

def p_expr_term(p):
    '''expr : term'''
    print("expr_term")
    # p[0] = p[1]

def p_expr_empty(p):
    '''expr : empty'''
    print('expr_empty')
    # p[0] = 0

def p_term_times(p):
    '''term : term TIMES factor'''
    print('term_times')
    # p[0] = p[1] * p[3]

def p_term_div(p):
    '''term : term DIVIDE factor'''
    print('term_div')
    # p[0] = p[1] / p[2]

def p_term_factor(p):
    '''term : factor'''
    print("term_factor")
    # p[0] = p[1]

def p_factor_num(p):
    '''factor : NUMBER'''
    print("factor_num")
    # p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print('error', p)
    print("Syntax error in input!")

def p_empty(p):
    '''empty :'''
    pass

data = '''
var a = 1, b = 2;
var c = 3;
Main {
    2 + 3 - 4;
    1 + 1 * 5;
}
'''

parser = yacc.yacc(debug=True)

result = parser.parse(data)
print(result)
