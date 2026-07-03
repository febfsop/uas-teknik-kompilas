# uas-teknik-kompilasi

## 1. Pilihan Konstruksi
**Konstruksi yang dipilih:**  `Deklarasi fungsi/metode`

2. Pattern (Pola Sintaks)
Pola didefinisikan menggunakan pendekatan Backus-Naur Form (BNF):

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
