# uas-teknik-kompilasi

## 1. Pilihan Konstruksi
**Konstruksi yang dipilih:**  `Deklarasi fungsi/metode`

## 2. Pattern (Pola Sintaks)
**Pola didefinisikan menggunakan pendekatan Backus-Naur Form (BNF)**:

```text
<function> ::= <type> <identifier> "(" <parameter_list> ")" "{" <statement> "}"

<parameter_list> ::= <parameter>
                   | <parameter> "," <parameter_list>
                   | ε

<parameter> ::= <type> <identifier>

<statement> ::= "return" <expression> ";"

<expression> ::= <identifier>
               | <identifier> "+" <identifier>

<type> ::= int
         | float
         | string
         | void

<identifier> ::= letter(letter|digit)*


### 3. Implementasi Program


```python
import re

# ==========================================
# LEXICAL ANALYZER
# ==========================================

token_specification = [
    ('KEYWORD', r'\b(int|float|string|void|return)\b'),
    ('IDENTIFIER', r'[A-Za-z_][A-Za-z0-9_]*'),
    ('NUMBER', r'\d+'),
    ('PLUS', r'\+'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('COMMA', r','),
    ('SEMICOLON', r';'),
    ('SKIP', r'[ \t\n]+'),
]

regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

code = '''
int tambah(int a, int b){
    return a + b;
}
'''

tokens = []

for mo in re.finditer(regex, code):
    kind = mo.lastgroup
    value = mo.group()

    if kind != 'SKIP':
        tokens.append((kind,value))

print("===== TOKEN =====")
for t in tokens:
    print(t)

# ==========================================
# AST
# ==========================================

AST = {
    "Function":{
        "ReturnType":"int",
        "Name":"tambah",
        "Parameters":[
            ("int","a"),
            ("int","b")
        ],
        "Body":{
            "Return":{
                "Operator":"+",
                "Left":"a",
                "Right":"b"
            }
        }
    }
}

print("\n===== AST =====")
print(AST)

# ==========================================
# SEMANTIC ANALYSIS
# ==========================================

symbol_table = {
    "a":"int",
    "b":"int"
}

left_type = symbol_table["a"]
right_type = symbol_table["b"]

print("\n===== SEMANTIC =====")

if left_type == right_type:
    print("Semantic Analysis : VALID")
else:
    print("Semantic Error")

# ==========================================
# TAC
# ==========================================

print("\n===== THREE ADDRESS CODE =====")

print("t1 = a + b")
print("return t1")
