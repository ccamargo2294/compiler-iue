import ply.lex as lex
import tokrules
 
# Build the lexer
lexer = lex.lex(module=tokrules)

# Test it out
data = '''
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Task;

namespace SumaProductosNumeros
{
  class Program 
  {
    static void Main(string[] args)
    {
      int num1, num2, suma, producto;
      string linea;
      Console.Write("Ingrese primer valor");
      linea = Console.ReadLine();
      num1 = int.Parse(linea);
      Console.Write("Ingrese Segundo Valor");
      linea = Console.ReadLine();
      num2 = int.Parse(linea);
      suma = num1 + num2;
      Console.WriteLine("La suma de los dos valores es:");
      Console.WriteLine(suma);
      Console.WriteLine("El producto de los dos valores es:");
      Console.WriteLine(product);
      Console.ReadKey();
    }
  }
}
'''
 
# Give the lexer some input
lexer.input(data)

# Tokenize
token_chain = ''
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.type, ',', tok.value)
    if tok.type == 'STRING' or tok.type == 'NUMBER':
      token_chain += tok.type + ' '
    else:
      token_chain += tok.value + ' '

print(token_chain)