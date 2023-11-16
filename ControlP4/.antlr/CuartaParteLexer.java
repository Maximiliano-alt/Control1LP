// Generated from c:/Users/josem/Documents/Lenguajes de Programacion/Control1LP/ControlP4/CuartaParte.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class CuartaParteLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, SUM=5, REST=6, ENC=7, APAG=8, MOV=9, ROT=10, 
		REP=11, INT=12, NEWLINE=13, WS=14;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "SUM", "REST", "ENC", "APAG", "MOV", 
			"ROT", "REP", "INT", "NEWLINE", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "','", "')'", "':'", "'+'", "'-'", "'encendido'", "'apagado'", 
			"'mover'", "'rotar'", "'repetir'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, "SUM", "REST", "ENC", "APAG", "MOV", "ROT", 
			"REP", "INT", "NEWLINE", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public CuartaParteLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "CuartaParte.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u000ec\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0003\u000bQ\b\u000b\u0001\u000b\u0004\u000bT\b\u000b\u000b\u000b\f\u000b"+
		"U\u0001\f\u0003\fY\b\f\u0001\f\u0001\f\u0001\r\u0004\r^\b\r\u000b\r\f"+
		"\r_\u0001\r\u0001\r\u0000\u0000\u000e\u0001\u0001\u0003\u0002\u0005\u0003"+
		"\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015"+
		"\u000b\u0017\f\u0019\r\u001b\u000e\u0001\u0000\u0002\u0001\u000009\u0002"+
		"\u0000\t\t  f\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0001\u001d\u0001\u0000\u0000\u0000\u0003\u001f\u0001\u0000\u0000\u0000"+
		"\u0005!\u0001\u0000\u0000\u0000\u0007#\u0001\u0000\u0000\u0000\t%\u0001"+
		"\u0000\u0000\u0000\u000b\'\u0001\u0000\u0000\u0000\r)\u0001\u0000\u0000"+
		"\u0000\u000f3\u0001\u0000\u0000\u0000\u0011;\u0001\u0000\u0000\u0000\u0013"+
		"A\u0001\u0000\u0000\u0000\u0015G\u0001\u0000\u0000\u0000\u0017P\u0001"+
		"\u0000\u0000\u0000\u0019X\u0001\u0000\u0000\u0000\u001b]\u0001\u0000\u0000"+
		"\u0000\u001d\u001e\u0005(\u0000\u0000\u001e\u0002\u0001\u0000\u0000\u0000"+
		"\u001f \u0005,\u0000\u0000 \u0004\u0001\u0000\u0000\u0000!\"\u0005)\u0000"+
		"\u0000\"\u0006\u0001\u0000\u0000\u0000#$\u0005:\u0000\u0000$\b\u0001\u0000"+
		"\u0000\u0000%&\u0005+\u0000\u0000&\n\u0001\u0000\u0000\u0000\'(\u0005"+
		"-\u0000\u0000(\f\u0001\u0000\u0000\u0000)*\u0005e\u0000\u0000*+\u0005"+
		"n\u0000\u0000+,\u0005c\u0000\u0000,-\u0005e\u0000\u0000-.\u0005n\u0000"+
		"\u0000./\u0005d\u0000\u0000/0\u0005i\u0000\u000001\u0005d\u0000\u0000"+
		"12\u0005o\u0000\u00002\u000e\u0001\u0000\u0000\u000034\u0005a\u0000\u0000"+
		"45\u0005p\u0000\u000056\u0005a\u0000\u000067\u0005g\u0000\u000078\u0005"+
		"a\u0000\u000089\u0005d\u0000\u00009:\u0005o\u0000\u0000:\u0010\u0001\u0000"+
		"\u0000\u0000;<\u0005m\u0000\u0000<=\u0005o\u0000\u0000=>\u0005v\u0000"+
		"\u0000>?\u0005e\u0000\u0000?@\u0005r\u0000\u0000@\u0012\u0001\u0000\u0000"+
		"\u0000AB\u0005r\u0000\u0000BC\u0005o\u0000\u0000CD\u0005t\u0000\u0000"+
		"DE\u0005a\u0000\u0000EF\u0005r\u0000\u0000F\u0014\u0001\u0000\u0000\u0000"+
		"GH\u0005r\u0000\u0000HI\u0005e\u0000\u0000IJ\u0005p\u0000\u0000JK\u0005"+
		"e\u0000\u0000KL\u0005t\u0000\u0000LM\u0005i\u0000\u0000MN\u0005r\u0000"+
		"\u0000N\u0016\u0001\u0000\u0000\u0000OQ\u0005-\u0000\u0000PO\u0001\u0000"+
		"\u0000\u0000PQ\u0001\u0000\u0000\u0000QS\u0001\u0000\u0000\u0000RT\u0007"+
		"\u0000\u0000\u0000SR\u0001\u0000\u0000\u0000TU\u0001\u0000\u0000\u0000"+
		"US\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000V\u0018\u0001\u0000"+
		"\u0000\u0000WY\u0005\r\u0000\u0000XW\u0001\u0000\u0000\u0000XY\u0001\u0000"+
		"\u0000\u0000YZ\u0001\u0000\u0000\u0000Z[\u0005\n\u0000\u0000[\u001a\u0001"+
		"\u0000\u0000\u0000\\^\u0007\u0001\u0000\u0000]\\\u0001\u0000\u0000\u0000"+
		"^_\u0001\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000_`\u0001\u0000\u0000"+
		"\u0000`a\u0001\u0000\u0000\u0000ab\u0006\r\u0000\u0000b\u001c\u0001\u0000"+
		"\u0000\u0000\u0005\u0000PUX_\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}