grammar SegundaParte;

prog: dibujo+ ;

dibujo:   modo NEWLINE                                            # Mod
      |   puntero NEWLINE                                         # Dib
      |   NEWLINE                                                 # blank
      ;

modo: op=('encendido'|'apagado')                                  # AsignMod
    ;                                 

puntero: op=('mover'|'rotar')'(' puntero (',' puntero)? ')'       # Pos
       | INT                                                      # INT
       ;

ENC :     'encendido' ;
APAG :    'apagado' ;
MOV:      'mover' ;
ROT:      'rotar' ;
INT :   [0-9]+ ;
NEWLINE:  '\r'? '\n' ;
WS :      [ \t]+ -> skip ;