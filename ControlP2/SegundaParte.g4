grammar SegundaParte;

prog: dibujo+ ;

dibujo:   modo NEWLINE                                            # Mod
      |   puntero NEWLINE                                         # Dib
      |   NEWLINE                                                 # blank
      ;

modo: op=('encendido'|'apagado')                                  # AsignMod
    ;                                 

puntero: MOV '(' puntero (',' puntero)? ')' # Mov // Como estaba antes: op=('mover'|'rotar')'(' puntero (',' puntero)? ')' # Pos
       | ROT '(' puntero (',' puntero)? ')' # Rot
       | INT                                # INT
       ;

ENC :     'encendido' ;
APAG :    'apagado' ;
MOV:      'mover' ;
ROT:      'rotar' ;
INT :   '-'? [0-9]+ ;
NEWLINE:  '\r'? '\n' ;
WS :      [ \t]+ -> skip ;