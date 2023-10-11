// Generated from c://Users//Kevin//Desktop//Control1LP//ControlP3//TerceraParte.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class TerceraParteLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, ENC=4, APAG=5, MOV=6, ROT=7, SUM=8, RES=9, INT=10, 
		NEWLINE=11, WS=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "ENC", "APAG", "MOV", "ROT", "SUM", "RES", "INT", 
			"NEWLINE", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "','", "')'", "'encendido'", "'apagado'", "'mover'", "'rotar'", 
			"'+'", "'-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "ENC", "APAG", "MOV", "ROT", "SUM", "RES", "INT", 
			"NEWLINE", "WS"
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


	public TerceraParteLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "TerceraParte.g4"; }

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
		"\u0004\u0000\fU\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0003\tC"+
		"\b\t\u0001\t\u0004\tF\b\t\u000b\t\f\tG\u0001\n\u0003\nK\b\n\u0001\n\u0001"+
		"\n\u0001\u000b\u0004\u000bP\b\u000b\u000b\u000b\f\u000bQ\u0001\u000b\u0001"+
		"\u000b\u0000\u0000\f\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t"+
		"\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f"+
		"\u0001\u0000\u0002\u0001\u000009\u0002\u0000\t\t  X\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000"+
		"\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000"+
		"\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000"+
		"\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0001\u0019\u0001\u0000\u0000"+
		"\u0000\u0003\u001b\u0001\u0000\u0000\u0000\u0005\u001d\u0001\u0000\u0000"+
		"\u0000\u0007\u001f\u0001\u0000\u0000\u0000\t)\u0001\u0000\u0000\u0000"+
		"\u000b1\u0001\u0000\u0000\u0000\r7\u0001\u0000\u0000\u0000\u000f=\u0001"+
		"\u0000\u0000\u0000\u0011?\u0001\u0000\u0000\u0000\u0013B\u0001\u0000\u0000"+
		"\u0000\u0015J\u0001\u0000\u0000\u0000\u0017O\u0001\u0000\u0000\u0000\u0019"+
		"\u001a\u0005(\u0000\u0000\u001a\u0002\u0001\u0000\u0000\u0000\u001b\u001c"+
		"\u0005,\u0000\u0000\u001c\u0004\u0001\u0000\u0000\u0000\u001d\u001e\u0005"+
		")\u0000\u0000\u001e\u0006\u0001\u0000\u0000\u0000\u001f \u0005e\u0000"+
		"\u0000 !\u0005n\u0000\u0000!\"\u0005c\u0000\u0000\"#\u0005e\u0000\u0000"+
		"#$\u0005n\u0000\u0000$%\u0005d\u0000\u0000%&\u0005i\u0000\u0000&\'\u0005"+
		"d\u0000\u0000\'(\u0005o\u0000\u0000(\b\u0001\u0000\u0000\u0000)*\u0005"+
		"a\u0000\u0000*+\u0005p\u0000\u0000+,\u0005a\u0000\u0000,-\u0005g\u0000"+
		"\u0000-.\u0005a\u0000\u0000./\u0005d\u0000\u0000/0\u0005o\u0000\u0000"+
		"0\n\u0001\u0000\u0000\u000012\u0005m\u0000\u000023\u0005o\u0000\u0000"+
		"34\u0005v\u0000\u000045\u0005e\u0000\u000056\u0005r\u0000\u00006\f\u0001"+
		"\u0000\u0000\u000078\u0005r\u0000\u000089\u0005o\u0000\u00009:\u0005t"+
		"\u0000\u0000:;\u0005a\u0000\u0000;<\u0005r\u0000\u0000<\u000e\u0001\u0000"+
		"\u0000\u0000=>\u0005+\u0000\u0000>\u0010\u0001\u0000\u0000\u0000?@\u0005"+
		"-\u0000\u0000@\u0012\u0001\u0000\u0000\u0000AC\u0005-\u0000\u0000BA\u0001"+
		"\u0000\u0000\u0000BC\u0001\u0000\u0000\u0000CE\u0001\u0000\u0000\u0000"+
		"DF\u0007\u0000\u0000\u0000ED\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000"+
		"\u0000GE\u0001\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000H\u0014\u0001"+
		"\u0000\u0000\u0000IK\u0005\r\u0000\u0000JI\u0001\u0000\u0000\u0000JK\u0001"+
		"\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000LM\u0005\n\u0000\u0000M\u0016"+
		"\u0001\u0000\u0000\u0000NP\u0007\u0001\u0000\u0000ON\u0001\u0000\u0000"+
		"\u0000PQ\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000\u0000QR\u0001\u0000"+
		"\u0000\u0000RS\u0001\u0000\u0000\u0000ST\u0006\u000b\u0000\u0000T\u0018"+
		"\u0001\u0000\u0000\u0000\u0005\u0000BGJQ\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}