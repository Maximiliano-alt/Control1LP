grammar PrimeraParte;

prog: dibujo+ ;

dibujo:   puntero NEWLINE                                         # Dib
      |   NEWLINE                                                 # blank
      ;

puntero: '(' puntero ',' puntero ')' op=('encendido'|'apagado')   # Pos
       | INT                                                      # INT
       ;

ENC :     'encendido' ;
APAG :    'apagado' ;
INT :   [0-9]+ ;
NEWLINE:  '\r'? '\n' ;
WS :      [ \t]+ -> skip ;