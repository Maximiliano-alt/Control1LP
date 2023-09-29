grammar PrimeraParte;

prog: dibujo+ ;

dibujo:   modo NEWLINE                                            # Mod
      |   puntero NEWLINE                                         # Dib
      |   NEWLINE                                                 # blank
      ;

modo: op=('encendido'|'apagado')                                  # AsignMod
<<<<<<< HEAD
    ;                                 

puntero: op=('mover'|'rotar')'(' puntero (',' puntero)? ')'       # Pos
=======
    ;  

puntero: MOV '(' puntero ',' puntero ')'                          # Pos
>>>>>>> 7483039019a702f260c0e1e044ebd4ebb7e8ccaf
       | INT                                                      # INT
       ;

ENC :     'encendido' ;
APAG :    'apagado' ;
MOV:      'mover' ;
<<<<<<< HEAD
ROT:      'rotar' ;
=======
>>>>>>> 7483039019a702f260c0e1e044ebd4ebb7e8ccaf
INT :   [0-9]+ ;
NEWLINE:  '\r'? '\n' ;
WS :      [ \t]+ -> skip ;
