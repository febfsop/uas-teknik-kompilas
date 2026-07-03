import re

print("===== SIMULASI KOMPILER =====")

source = input("Masukkan deklarasi fungsi:\n")

# =====================================
# LEXICAL ANALYSIS
# =====================================

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

regex = '|'.join(
    '(?P<%s>%s)' % pair for pair in token_specification
)

tokens = []

for mo in re.finditer(regex, source):

    kind = mo.lastgroup
    value = mo.group()

    if kind != 'SKIP':
        tokens.append((kind,value))

print("\n===== HASIL TOKEN =====")

for t in tokens:
    print(t)

# =====================================
# PARSER SEDERHANA
# =====================================

pattern = r'(int|float|string|void)\s+([A-Za-z_]\w*)\s*\((.*?)\)\s*\{\s*return\s+([A-Za-z_]\w*)\s*\+\s*([A-Za-z_]\w*)\s*;\s*\}'

m = re.match(pattern, source)

if not m:
    print("\nSyntax Error")
    # Removed exit() and enclosed subsequent code in else block
else:
    return_type = m.group(1)
    func_name = m.group(2)
    parameter = m.group(3)
    left = m.group(4)
    right = m.group(5)

    print("\n===== ABSTRACT SYNTAX TREE =====")

    ast = {
        "Function":func_name,
        "ReturnType":return_type,
        "Parameters":parameter,
        "Return":{
            "Operator":"+",
            "Left":left,
            "Right":right
        }
    }

    print(ast)

    # =====================================
    # SEMANTIC ANALYSIS
    # =====================================

    print("\n===== SEMANTIC ANALYSIS =====")

    params = {}

    # Handle cases where parameter string might be empty or malformed before splitting
    if parameter:
        for p in parameter.split(","):
            p = p.strip()
            if p: # Ensure p is not an empty string after stripping
                # Added a check to prevent ValueError if p.split() doesn't return two values
                parts = p.split()
                if len(parts) == 2:
                    t, n = parts
                    params[n] = t
                else:
                    print(f"Semantic Error: Malformed parameter declaration '{p}'")
                    # You might want to exit or handle this error more robustly
    
    if left not in params:

        print("Semantic Error :",left,"belum dideklarasikan")

    elif right not in params:

        print("Semantic Error :",right,"belum dideklarasikan")

    elif params[left]!=params[right]:

        print("Semantic Error : tipe data berbeda")

    else:

        print("Semantic Analysis : VALID")

        # =====================================
        # TAC
        # =====================================

        print("\n===== THREE ADDRESS CODE =====")

        print("t1 =",left,"+",right)
        print("return t1")
