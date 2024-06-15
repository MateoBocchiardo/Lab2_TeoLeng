# -*- coding: utf-8 -*-
import re
import sys
import io
import nltk
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

# 0 0 1 1 2 2 2

# grammar definition
grammar ="""
S -> Asignacion | EstructuraDeControl
Asignacion -> Var AsigOperador Num | Var AsigOperador Var
EstructuraDeControl -> "if" "(" BoolExpr ")" ":" | "elif" "(" BoolExpr ")" ":" | "while" "(" BoolExpr ")" ":" | "for" "(" Var "in" "range" "(" Num ")" ")" ":"
BoolExpr -> Num BoolOp Num | Num BoolOp Var | Var BoolOp Num | Var BoolOp Var
Var -> "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z"
Num -> "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "10" | "11" | "12" | "13" | "14" | "15" | "16" | "17" | "18" | "19" | "20" | "21" | "22" | "23" | "24" | "25" | "26" | "27" | "28" | "29" | "30" | "31" | "32" | "33" | "34" | "35" | "36" | "37" | "38" | "39" | "40" | "41" | "42" | "43" | "44" | "45" | "46" | "47" | "48" | "49" | "50" | "51" | "52" | "53" | "54" | "55" | "56" | "57" | "58" | "59" | "60" | "61" | "62" | "63" | "64" | "65" | "66" | "67" | "68" | "69" | "70" | "71" | "72" | "73" | "74" | "75" | "76" | "77" | "78" | "79" | "80" | "81" | "82" | "83" | "84" | "85" | "86" | "87" | "88" | "89" | "90" | "91" | "92" | "93" | "94" | "95" | "96" | "97" | "98" | "99" | "100"
BoolOp -> "<" | "<=" | ">" | ">=" | "==" | "!="
AsigOperador -> "=" | "+=" | "-="
"""

def custom_tokenize(s):
    # Combina operadores
    s = re.sub(r'<=|>=|==|!=|\+=|-=|\*=', lambda m: f' {m.group()} ', s)
    s = re.sub(r'([()])', r' \1 ', s)  # Espacio en parentesis
    s = re.sub(r'(:)', r' \1 ', s)     # Espacio en dos puntos
    return s.split()


def parse(s, grammar):

    # parser
    grammar = nltk.CFG.fromstring(grammar)
    parser = nltk.LeftCornerChartParser(grammar)

    # tokenize
    s_tokenized = custom_tokenize(s)
    print(f"Tokenized input: {s_tokenized}")

    # parse
    tree = list(parser.parse(s_tokenized))[:1]
    return tree

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
      tree = parse(s, grammar)
      if tree:
          salida = "PERTENECE"
      else:
          salida = "NO PERTENECE"
    except ValueError as e:
      salida = "NO PERTENECE - FUERA DE ALFABETO"
      print(f"ValueError: {e}")
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()