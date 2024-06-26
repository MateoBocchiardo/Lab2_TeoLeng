# -*- coding: utf-8 -*-

import sys
import io
import nltk
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')


grammar ="""

S -> S '+' S | S '*' S | S '/' S | S '-' S | A | '(' S ')'

A -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | '11' | '12' | '13' | '14' | '15' | '16' | '17' | '18' | '19' | '20' | '21' | '22' | '23' | '24' | '25' | '26' | '27' | '28' | '29' | '30' | '31' | '32' | '33' | '34' | '35' | '36' | '37' | '38' | '39' | '40' | '41' | '42' | '43' | '44' | '45' | '46' | '47' | '48' | '49' | '50' | '51' | '52' | '53' | '54' | '55' | '56' | '57' | '58' | '59' | '60' | '61' | '62' | '63' | '64' | '65' | '66' | '67' | '68' | '69' | '70' | '71' | '72' | '73' | '74' | '75' | '76' | '77' | '78' | '79' | '80' | '81' | '82' | '83' | '84' | '85' | '86' | '87' | '88' | '89' | '90' | '91' | '92' | '93' | '94' | '95' | '96' | '97' | '98' | '99' | '100'
"""

def parse(s, grammar):

    # parser
    grammar = nltk.CFG.fromstring(grammar)
    parser = nltk.LeftCornerChartParser(grammar)

    # tokenize
    s_tokenized = nltk.word_tokenize(s)

    # parse
    tree = list(parser.parse(s_tokenized))[:1]
    return tree

def format_tree(tree):
    if isinstance(tree, nltk.Tree):
        if tree.height() == 2:  # Es una hoja
            return tree[0]
        else:
            label = tree.label()
            children = [format_tree(child) for child in tree]
            if label == 'S':
                if len(children) == 3 and children[1] in {'+', '-', '*', '/'}:
                    # Detectar operador en el nodo 'S'
                    operador = children[1]
                    operando1 = children[0]
                    operando2 = children[2]
                    return f"{operador}({operando1},{operando2})" #convierte 10 OP 2 en OP(10,2)
                elif len(children) == 3 and children[0] == '(' and children[2] == ')':
                    # Caso de paréntesis
                    return f"{children[1]}"  # Devolver solo la expresión dentro de los paréntesis
                else:
                    return ''.join(children)
            else:
                return ''.join(children)
    else:
        return tree

def printArbol(tree):
    if tree:
        formatted_tree = format_tree(tree)
        print(formatted_tree, end='')  # " end='' " Evita el salto de línea adicional

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
      tree = parse(s, grammar)
      if tree:
          printArbol(tree)
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO PERTENECE - FUERA DE ALFABETO"
      f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
      f.write(salida)
      f.close()

