// Generated from c:\Users\Kevin\Downloads\Control1LP\ControlP1\PrimeraParte.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class PrimeraParteParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, ENC=4, APAG=5, INT=6, NEWLINE=7, WS=8;
	public static final int
		RULE_prog = 0, RULE_dibujo = 1, RULE_puntero = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "dibujo", "puntero"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "','", "')'", "'encendido'", "'apagado'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "ENC", "APAG", "INT", "NEWLINE", "WS"
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

	@Override
	public String getGrammarFileName() { return "PrimeraParte.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PrimeraParteParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public List<DibujoContext> dibujo() {
			return getRuleContexts(DibujoContext.class);
		}
		public DibujoContext dibujo(int i) {
			return getRuleContext(DibujoContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(7); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(6);
				dibujo();
				}
				}
				setState(9); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << INT) | (1L << NEWLINE))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DibujoContext extends ParserRuleContext {
		public DibujoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dibujo; }
	 
		public DibujoContext() { }
		public void copyFrom(DibujoContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class BlankContext extends DibujoContext {
		public TerminalNode NEWLINE() { return getToken(PrimeraParteParser.NEWLINE, 0); }
		public BlankContext(DibujoContext ctx) { copyFrom(ctx); }
	}
	public static class DibContext extends DibujoContext {
		public PunteroContext puntero() {
			return getRuleContext(PunteroContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(PrimeraParteParser.NEWLINE, 0); }
		public DibContext(DibujoContext ctx) { copyFrom(ctx); }
	}

	public final DibujoContext dibujo() throws RecognitionException {
		DibujoContext _localctx = new DibujoContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_dibujo);
		try {
			setState(15);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
			case INT:
				_localctx = new DibContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(11);
				puntero();
				setState(12);
				match(NEWLINE);
				}
				break;
			case NEWLINE:
				_localctx = new BlankContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(14);
				match(NEWLINE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PunteroContext extends ParserRuleContext {
		public PunteroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_puntero; }
	 
		public PunteroContext() { }
		public void copyFrom(PunteroContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PosContext extends PunteroContext {
		public Token op;
		public List<PunteroContext> puntero() {
			return getRuleContexts(PunteroContext.class);
		}
		public PunteroContext puntero(int i) {
			return getRuleContext(PunteroContext.class,i);
		}
		public TerminalNode ENC() { return getToken(PrimeraParteParser.ENC, 0); }
		public TerminalNode APAG() { return getToken(PrimeraParteParser.APAG, 0); }
		public PosContext(PunteroContext ctx) { copyFrom(ctx); }
	}
	public static class INTContext extends PunteroContext {
		public TerminalNode INT() { return getToken(PrimeraParteParser.INT, 0); }
		public INTContext(PunteroContext ctx) { copyFrom(ctx); }
	}

	public final PunteroContext puntero() throws RecognitionException {
		PunteroContext _localctx = new PunteroContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_puntero);
		int _la;
		try {
			setState(25);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				_localctx = new PosContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(17);
				match(T__0);
				setState(18);
				puntero();
				setState(19);
				match(T__1);
				setState(20);
				puntero();
				setState(21);
				match(T__2);
				setState(22);
				((PosContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==ENC || _la==APAG) ) {
					((PosContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case INT:
				_localctx = new INTContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(24);
				match(INT);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\n\36\4\2\t\2\4\3"+
		"\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3\3\3\3\3\3\3\3\5\3\22\n\3\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\34\n\4\3\4\2\2\5\2\4\6\2\3\3\2\6\7\2"+
		"\35\2\t\3\2\2\2\4\21\3\2\2\2\6\33\3\2\2\2\b\n\5\4\3\2\t\b\3\2\2\2\n\13"+
		"\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\3\3\2\2\2\r\16\5\6\4\2\16\17\7\t"+
		"\2\2\17\22\3\2\2\2\20\22\7\t\2\2\21\r\3\2\2\2\21\20\3\2\2\2\22\5\3\2\2"+
		"\2\23\24\7\3\2\2\24\25\5\6\4\2\25\26\7\4\2\2\26\27\5\6\4\2\27\30\7\5\2"+
		"\2\30\31\t\2\2\2\31\34\3\2\2\2\32\34\7\b\2\2\33\23\3\2\2\2\33\32\3\2\2"+
		"\2\34\7\3\2\2\2\5\13\21\33";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}