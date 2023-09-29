# Generated from PrimeraParte.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,66,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,
        5,1,5,1,5,1,5,1,6,4,6,51,8,6,11,6,12,6,52,1,7,3,7,56,8,7,1,7,1,7,
        1,8,4,8,61,8,8,11,8,12,8,62,1,8,1,8,0,0,9,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,17,9,1,0,2,1,0,48,57,2,0,9,9,32,32,68,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,0,3,21,1,0,0,0,5,23,
        1,0,0,0,7,25,1,0,0,0,9,35,1,0,0,0,11,43,1,0,0,0,13,50,1,0,0,0,15,
        55,1,0,0,0,17,60,1,0,0,0,19,20,5,40,0,0,20,2,1,0,0,0,21,22,5,44,
        0,0,22,4,1,0,0,0,23,24,5,41,0,0,24,6,1,0,0,0,25,26,5,101,0,0,26,
        27,5,110,0,0,27,28,5,99,0,0,28,29,5,101,0,0,29,30,5,110,0,0,30,31,
        5,100,0,0,31,32,5,105,0,0,32,33,5,100,0,0,33,34,5,111,0,0,34,8,1,
        0,0,0,35,36,5,97,0,0,36,37,5,112,0,0,37,38,5,97,0,0,38,39,5,103,
        0,0,39,40,5,97,0,0,40,41,5,100,0,0,41,42,5,111,0,0,42,10,1,0,0,0,
        43,44,5,109,0,0,44,45,5,111,0,0,45,46,5,118,0,0,46,47,5,101,0,0,
        47,48,5,114,0,0,48,12,1,0,0,0,49,51,7,0,0,0,50,49,1,0,0,0,51,52,
        1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,14,1,0,0,0,54,56,5,13,0,0,
        55,54,1,0,0,0,55,56,1,0,0,0,56,57,1,0,0,0,57,58,5,10,0,0,58,16,1,
        0,0,0,59,61,7,1,0,0,60,59,1,0,0,0,61,62,1,0,0,0,62,60,1,0,0,0,62,
        63,1,0,0,0,63,64,1,0,0,0,64,65,6,8,0,0,65,18,1,0,0,0,4,0,52,55,62,
        1,6,0,0
    ]

class PrimeraParteLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    ENC = 4
    APAG = 5
    MOV = 6
    INT = 7
    NEWLINE = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "','", "')'", "'encendido'", "'apagado'", "'mover'" ]

    symbolicNames = [ "<INVALID>",
            "ENC", "APAG", "MOV", "INT", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "ENC", "APAG", "MOV", "INT", "NEWLINE", 
                  "WS" ]

    grammarFileName = "PrimeraParte.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


