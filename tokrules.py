reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'string': 'STRINGTYPE',
    'int': 'INTTYPE',
    'class': 'CLASS',
    'static': 'STATIC',
    'void': 'VOID',
    'using': 'USING',
    'namespace': 'NAMESPACE',
    'Program': 'PROGRAM',
    'Main': 'MAIN'
} 

tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'ASSIGN',
    'COMMA',
    'SEMICOLON',
    "SYSTEM",
    "SYSTEMCOLLECTION",
    "SYSTEMLINQ",
    "SYSTEMTEXT",
    "SYSTEMTHREADING",
    "CONSOLEWRITE",
    "CONSOLEREADLINE",
    "CONSOLEWRITELINE",
    "CONSOLEREADKEY",
    "INTPARSE",
    "COMMENT",
    'VARIABLE',
    'STRING',
    'VAR'
 ] + list(reserved.values())

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_ASSIGN = r'\='
t_COMMA = r'\,'
t_SEMICOLON = r'\;'

def t_VAR(t):
    r'var'
    return t

def t_SYSTEM(t):
    r'system'
    return t
    
def t_SYSTEMCOLLECTION(t):
    r'System\.Collections\.Generic'
    return t

def t_SYSTEMLINQ(t):
    r'System\.Linq'
    return t

def t_SYSTEMTEXT(t):
    r'System\.Text'
    return t

def t_SYSTEMTHREADING(t):
    r'System\.Threading\.Task'
    return t

def t_CONSOLEWRITE(t):
    r'Console\.Write'
    return t

def t_CONSOLEREADLINE(t):
    r'Console\.ReadLine'
    return t

def t_CONSOLEWRITELINE(t):
    r'Console\.WriteLine'
    return t

def t_CONSOLEREADKEY(t):
    r'Console\.ReadKey'
    return t

def t_INTPARSE(t):
    r'int\.Parse'
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

def t_STRING(t):
    r'(("[^"]*")|(\'[^\']*\'))'
    return t

def t_COMMENT(t):
	r'\#.*'
	return t
 
# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
