// Generated from c://Users//Kevin//Desktop//Control1LP//ControlP4//CuartaParte.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CuartaParteParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, ENC=4, APAG=5, MOV=6, REP=7, INT=8, NEWLINE=9, 
		WS=10;
	public static final int
		RULE_prog = 0, RULE_dibujo = 1, RULE_modo = 2, RULE_repetir = 3, RULE_puntero = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "dibujo", "modo", "repetir", "puntero"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "','", "'encendido'", "'apagado'", "'mover'", "'repetir'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "ENC", "APAG", "MOV", "REP", "INT", "NEWLINE", 
			"WS"
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
	public String getGrammarFileName() { return "CuartaParte.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CuartaParteParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
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
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CuartaParteListener ) ((CuartaParteListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CuartaParteListener ) ((CuartaParteListener)listener).exitProg(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(11); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(10);
				dibujo();
				}
				}
				setState(13); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 624L) != 0) );
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

	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
	public static class ModContext extends DibujoContext {
		public ModoContext modo() {
			return getRuleContext(ModoContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(CuartaParteParser.NEWLINE, 0); }
		public ModContext(DibujoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CuartaParteListener ) ((CuartaParteListener)listener).enterMod(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CuartaParteListener ) ((CuartaParteListener)listener).exitMod(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BlankContext extends DibujoContext {
		public TerminalNode NEWLINE() { return getToken(CuartaParteParser.NEWLINE, 0); }
		public BlankContext(DibujoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CuartaParteListener ) ((CuartaParteListener)listener).enterBlank(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CuartaParteListener ) ((CuartaParteListener)listener).exitBlank(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DibContext extends DibujoContext {
		public PunteroContext puntero() {
			return getRuleContext(PunteroContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(CuartaParteParser.NEWLINE, 0); }
		public DibContext(DibujoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CuartaParteListener ) ((CuartaParteListener)listener).enterDib(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CuartaParteListener ) ((CuartaParteListener)listener).exitDib(this);
		}
	}

	public final DibujoContext dibujo() throws RecognitionException {
		DibujoContext _localctx = new DibujoContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_dibujo);
		try {
			setState(22);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ENC:
			case APAG:
				_localctx = new ModContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(15);
				modo();
				setState(16);
				match(NEWLINE);
				}
				break;
			case MOV:
				_localctx = new DibContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(18);
				puntero();
				setState(19);
				match(NEWLINE);
				}
				break;
			case NEWLINE:
				_localctx = new BlankContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(21);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ModoContext extends ParserRuleContext {
		public ModoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modo; }
	 
		public ModoContext() { }
		public void copyFrom(ModoContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AsignModContext extends ModoContext {
		public Token op;
		public TerminalNode ENC() { return getToken(CuartaParteParser.ENC, 0); }
		public TerminalNode APAG() { return getToken(CuartaParteParser.APAG, 0); }
		public AsignModContext(ModoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CuartaParteListener ) ((CuartaParteListener)listener).enterAsignMod(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CuartaParteListener ) ((CuartaParteListener)listener).exitAsignMod(this);
		}
	}

	public final ModoContext modo() throws RecognitionException {
		ModoContext _localctx = new ModoContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_modo);
		int _la;
		try {
			_localctx = new AsignModContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			((AsignModContext)_localctx).op = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==ENC || _la==APAG) ) {
				((AsignModContext)_localctx).op = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
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

	@SuppressWarnings("CheckReturnValue")
	public static class RepetirContext extends ParserRuleContext {
		public TerminalNode REP() { return getToken(CuartaParteParser.REP, 0); }
		public TerminalNode INT() { return getToken(CuartaParteParser.INT, 0); }
		public RepetirContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repetir; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CuartaParteListener ) ((CuartaParteListener)listener).enterRepetir(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CuartaParteListener ) ((CuartaParteListener)listener).exitRepetir(this);
		}
	}

	public final RepetirContext repetir() throws RecognitionException {
		RepetirContext _localctx = new RepetirContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_repetir);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			match(REP);
			setState(27);
			match(T__0);
			setState(28);
			match(INT);
			setState(29);
			match(T__1);
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

	@SuppressWarnings("CheckReturnValue")
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
	@SuppressWarnings("CheckReturnValue")
	public static class PosContext extends PunteroContext {
		public TerminalNode MOV() { return getToken(CuartaParteParser.MOV, 0); }
		public List<TerminalNode> INT() { return getTokens(CuartaParteParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(CuartaParteParser.INT, i);
		}
		public PosContext(PunteroContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof CuartaParteListener ) ((CuartaParteListener)listener).enterPos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof CuartaParteListener ) ((CuartaParteListener)listener).exitPos(this);
		}
	}

	public final PunteroContext puntero() throws RecognitionException {
		PunteroContext _localctx = new PunteroContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_puntero);
		try {
			_localctx = new PosContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			match(MOV);
			setState(32);
			match(T__0);
			setState(33);
			match(INT);
			setState(34);
			match(T__2);
			setState(35);
			match(INT);
			setState(36);
			match(T__1);
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
		"\u0004\u0001\n\'\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0001"+
		"\u0000\u0004\u0000\f\b\u0000\u000b\u0000\f\u0000\r\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"\u0017\b\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0000\u0000\u0005\u0000"+
		"\u0002\u0004\u0006\b\u0000\u0001\u0001\u0000\u0004\u0005$\u0000\u000b"+
		"\u0001\u0000\u0000\u0000\u0002\u0016\u0001\u0000\u0000\u0000\u0004\u0018"+
		"\u0001\u0000\u0000\u0000\u0006\u001a\u0001\u0000\u0000\u0000\b\u001f\u0001"+
		"\u0000\u0000\u0000\n\f\u0003\u0002\u0001\u0000\u000b\n\u0001\u0000\u0000"+
		"\u0000\f\r\u0001\u0000\u0000\u0000\r\u000b\u0001\u0000\u0000\u0000\r\u000e"+
		"\u0001\u0000\u0000\u0000\u000e\u0001\u0001\u0000\u0000\u0000\u000f\u0010"+
		"\u0003\u0004\u0002\u0000\u0010\u0011\u0005\t\u0000\u0000\u0011\u0017\u0001"+
		"\u0000\u0000\u0000\u0012\u0013\u0003\b\u0004\u0000\u0013\u0014\u0005\t"+
		"\u0000\u0000\u0014\u0017\u0001\u0000\u0000\u0000\u0015\u0017\u0005\t\u0000"+
		"\u0000\u0016\u000f\u0001\u0000\u0000\u0000\u0016\u0012\u0001\u0000\u0000"+
		"\u0000\u0016\u0015\u0001\u0000\u0000\u0000\u0017\u0003\u0001\u0000\u0000"+
		"\u0000\u0018\u0019\u0007\u0000\u0000\u0000\u0019\u0005\u0001\u0000\u0000"+
		"\u0000\u001a\u001b\u0005\u0007\u0000\u0000\u001b\u001c\u0005\u0001\u0000"+
		"\u0000\u001c\u001d\u0005\b\u0000\u0000\u001d\u001e\u0005\u0002\u0000\u0000"+
		"\u001e\u0007\u0001\u0000\u0000\u0000\u001f \u0005\u0006\u0000\u0000 !"+
		"\u0005\u0001\u0000\u0000!\"\u0005\b\u0000\u0000\"#\u0005\u0003\u0000\u0000"+
		"#$\u0005\b\u0000\u0000$%\u0005\u0002\u0000\u0000%\t\u0001\u0000\u0000"+
		"\u0000\u0002\r\u0016";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}