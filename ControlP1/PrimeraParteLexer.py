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
        4,0,8,58,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,4,5,43,8,5,11,
        5,12,5,44,1,6,3,6,48,8,6,1,6,1,6,1,7,4,7,53,8,7,11,7,12,7,54,1,7,
        1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,0,2,1,0,48,57,2,0,
        9,9,32,32,60,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,19,
        1,0,0,0,5,21,1,0,0,0,7,23,1,0,0,0,9,33,1,0,0,0,11,42,1,0,0,0,13,
        47,1,0,0,0,15,52,1,0,0,0,17,18,5,40,0,0,18,2,1,0,0,0,19,20,5,44,
        0,0,20,4,1,0,0,0,21,22,5,41,0,0,22,6,1,0,0,0,23,24,5,101,0,0,24,
        25,5,110,0,0,25,26,5,99,0,0,26,27,5,101,0,0,27,28,5,110,0,0,28,29,
        5,100,0,0,29,30,5,105,0,0,30,31,5,100,0,0,31,32,5,111,0,0,32,8,1,
        0,0,0,33,34,5,97,0,0,34,35,5,112,0,0,35,36,5,97,0,0,36,37,5,103,
        0,0,37,38,5,97,0,0,38,39,5,100,0,0,39,40,5,111,0,0,40,10,1,0,0,0,
        41,43,7,0,0,0,42,41,1,0,0,0,43,44,1,0,0,0,44,42,1,0,0,0,44,45,1,
        0,0,0,45,12,1,0,0,0,46,48,5,13,0,0,47,46,1,0,0,0,47,48,1,0,0,0,48,
        49,1,0,0,0,49,50,5,10,0,0,50,14,1,0,0,0,51,53,7,1,0,0,52,51,1,0,
        0,0,53,54,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,56,1,0,0,0,56,57,
        6,7,0,0,57,16,1,0,0,0,4,0,44,47,54,1,6,0,0
    ]

class PrimeraParteLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    ENC = 4
    APAG = 5
    INT = 6
    NEWLINE = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "','", "')'", "'encendido'", "'apagado'" ]

    symbolicNames = [ "<INVALID>",
            "ENC", "APAG", "INT", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "ENC", "APAG", "INT", "NEWLINE", 
                  "WS" ]

    grammarFileName = "PrimeraParte.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


