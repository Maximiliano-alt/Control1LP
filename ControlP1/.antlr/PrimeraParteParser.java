// Generated from c:/Users/josem/Documents/Lenguajes de Programacion/Control1LP/ControlP1/PrimeraParte.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PrimeraParteParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, ENC=4, APAG=5, MOV=6, INT=7, NEWLINE=8, WS=9;
	public static final int
		RULE_prog = 0, RULE_dibujo = 1, RULE_modo = 2, RULE_puntero = 3;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "dibujo", "modo", "puntero"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "','", "')'", "'encendido'", "'apagado'", "'mover'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "ENC", "APAG", "MOV", "INT", "NEWLINE", "WS"
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
			if ( listener instanceof PrimeraParteListener ) ((PrimeraParteListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PrimeraParteListener ) ((PrimeraParteListener)listener).exitProg(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(9); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(8);
				dibujo();
				}
				}
				setState(11); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 368L) != 0) );
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
		public TerminalNode NEWLINE() { return getToken(PrimeraParteParser.NEWLINE, 0); }
		public ModContext(DibujoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PrimeraParteListener ) ((PrimeraParteListener)listener).enterMod(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PrimeraParteListener ) ((PrimeraParteListener)listener).exitMod(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BlankContext extends DibujoContext {
		public TerminalNode NEWLINE() { return getToken(PrimeraParteParser.NEWLINE, 0); }
		public BlankContext(DibujoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PrimeraParteListener ) ((PrimeraParteListener)listener).enterBlank(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PrimeraParteListener ) ((PrimeraParteListener)listener).exitBlank(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DibContext extends DibujoContext {
		public PunteroContext puntero() {
			return getRuleContext(PunteroContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(PrimeraParteParser.NEWLINE, 0); }
		public DibContext(DibujoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PrimeraParteListener ) ((PrimeraParteListener)listener).enterDib(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PrimeraParteListener ) ((PrimeraParteListener)listener).exitDib(this);
		}
	}

	public final DibujoContext dibujo() throws RecognitionException {
		DibujoContext _localctx = new DibujoContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_dibujo);
		try {
			setState(20);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ENC:
			case APAG:
				_localctx = new ModContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(13);
				modo();
				setState(14);
				match(NEWLINE);
				}
				break;
			case MOV:
				_localctx = new DibContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(16);
				puntero();
				setState(17);
				match(NEWLINE);
				}
				break;
			case NEWLINE:
				_localctx = new BlankContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(19);
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
		public TerminalNode ENC() { return getToken(PrimeraParteParser.ENC, 0); }
		public TerminalNode APAG() { return getToken(PrimeraParteParser.APAG, 0); }
		public AsignModContext(ModoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PrimeraParteListener ) ((PrimeraParteListener)listener).enterAsignMod(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PrimeraParteListener ) ((PrimeraParteListener)listener).exitAsignMod(this);
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
			setState(22);
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
		public TerminalNode MOV() { return getToken(PrimeraParteParser.MOV, 0); }
		public List<TerminalNode> INT() { return getTokens(PrimeraParteParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(PrimeraParteParser.INT, i);
		}
		public PosContext(PunteroContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof PrimeraParteListener ) ((PrimeraParteListener)listener).enterPos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof PrimeraParteListener ) ((PrimeraParteListener)listener).exitPos(this);
		}
	}

	public final PunteroContext puntero() throws RecognitionException {
		PunteroContext _localctx = new PunteroContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_puntero);
		try {
			_localctx = new PosContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			match(MOV);
			setState(25);
			match(T__0);
			setState(26);
			match(INT);
			setState(27);
			match(T__1);
			setState(28);
			match(INT);
			setState(29);
			match(T__2);
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
		"\u0004\u0001\t \u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0001\u0000\u0004\u0000\n\b"+
		"\u0000\u000b\u0000\f\u0000\u000b\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u0015\b\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0000\u0000\u0004\u0000\u0002"+
		"\u0004\u0006\u0000\u0001\u0001\u0000\u0004\u0005\u001e\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0002\u0014\u0001\u0000\u0000\u0000\u0004\u0016\u0001\u0000"+
		"\u0000\u0000\u0006\u0018\u0001\u0000\u0000\u0000\b\n\u0003\u0002\u0001"+
		"\u0000\t\b\u0001\u0000\u0000\u0000\n\u000b\u0001\u0000\u0000\u0000\u000b"+
		"\t\u0001\u0000\u0000\u0000\u000b\f\u0001\u0000\u0000\u0000\f\u0001\u0001"+
		"\u0000\u0000\u0000\r\u000e\u0003\u0004\u0002\u0000\u000e\u000f\u0005\b"+
		"\u0000\u0000\u000f\u0015\u0001\u0000\u0000\u0000\u0010\u0011\u0003\u0006"+
		"\u0003\u0000\u0011\u0012\u0005\b\u0000\u0000\u0012\u0015\u0001\u0000\u0000"+
		"\u0000\u0013\u0015\u0005\b\u0000\u0000\u0014\r\u0001\u0000\u0000\u0000"+
		"\u0014\u0010\u0001\u0000\u0000\u0000\u0014\u0013\u0001\u0000\u0000\u0000"+
		"\u0015\u0003\u0001\u0000\u0000\u0000\u0016\u0017\u0007\u0000\u0000\u0000"+
		"\u0017\u0005\u0001\u0000\u0000\u0000\u0018\u0019\u0005\u0006\u0000\u0000"+
		"\u0019\u001a\u0005\u0001\u0000\u0000\u001a\u001b\u0005\u0007\u0000\u0000"+
		"\u001b\u001c\u0005\u0002\u0000\u0000\u001c\u001d\u0005\u0007\u0000\u0000"+
		"\u001d\u001e\u0005\u0003\u0000\u0000\u001e\u0007\u0001\u0000\u0000\u0000"+
		"\u0002\u000b\u0014";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}