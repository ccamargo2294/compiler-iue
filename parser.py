import ply.yacc as yacc
import ply.lex as lex
import tokrules

tokens = tokrules.tokens
# Build the lexer
lexer = lex.lex(module=tokrules)
# 3 + 5 * ( 10 - 20 )

def p_finalline_semicolon(p):
    '''finalline : term SEMICOLON'''
    print('call semicolon')
    p[0] = p[1]

def p_term_plus(p):
    '''term : term PLUS factor'''
    print("call this plus", p[1], p[3])
    p[0] = p[1] + p[3]

def p_term_factor(p):
    '''term : factor'''
    print("call this term_factor")
    p[0] = p[1]

def p_factor_num(p):
    '''factor : NUMBER'''
    print("call this factor_num", p[1]) 
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print('error', p)
    print("Syntax error in input!")

data = '''
2 + 1 + 1;
2 + 2;
'''

parser = yacc.yacc()

result = parser.parse(data)
print(result)
