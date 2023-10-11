// Generated from c://Users//Kevin//Desktop//Control1LP//ControlP3//TerceraParte.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class TerceraParteParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, ENC=4, APAG=5, MOV=6, ROT=7, SUM=8, RES=9, INT=10, 
		NEWLINE=11, WS=12;
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

	@Override
	public String getGrammarFileName() { return "TerceraParte.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TerceraParteParser(TokenStream input) {
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
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).exitProg(this);
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
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 3312L) != 0) );
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
		public TerminalNode NEWLINE() { return getToken(TerceraParteParser.NEWLINE, 0); }
		public ModContext(DibujoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).enterMod(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).exitMod(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BlankContext extends DibujoContext {
		public TerminalNode NEWLINE() { return getToken(TerceraParteParser.NEWLINE, 0); }
		public BlankContext(DibujoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).enterBlank(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).exitBlank(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class DibContext extends DibujoContext {
		public PunteroContext puntero() {
			return getRuleContext(PunteroContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(TerceraParteParser.NEWLINE, 0); }
		public DibContext(DibujoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).enterDib(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).exitDib(this);
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
			case ROT:
			case INT:
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
		public TerminalNode ENC() { return getToken(TerceraParteParser.ENC, 0); }
		public TerminalNode APAG() { return getToken(TerceraParteParser.APAG, 0); }
		public AsignModContext(ModoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).enterAsignMod(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).exitAsignMod(this);
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
		public Token op;
		public List<PunteroContext> puntero() {
			return getRuleContexts(PunteroContext.class);
		}
		public PunteroContext puntero(int i) {
			return getRuleContext(PunteroContext.class,i);
		}
		public TerminalNode MOV() { return getToken(TerceraParteParser.MOV, 0); }
		public TerminalNode ROT() { return getToken(TerceraParteParser.ROT, 0); }
		public PosContext(PunteroContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).enterPos(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).exitPos(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AngContext extends PunteroContext {
		public Token op;
		public TerminalNode ROT() { return getToken(TerceraParteParser.ROT, 0); }
		public TerminalNode MOV() { return getToken(TerceraParteParser.MOV, 0); }
		public List<PunteroContext> puntero() {
			return getRuleContexts(PunteroContext.class);
		}
		public PunteroContext puntero(int i) {
			return getRuleContext(PunteroContext.class,i);
		}
		public TerminalNode SUM() { return getToken(TerceraParteParser.SUM, 0); }
		public TerminalNode RES() { return getToken(TerceraParteParser.RES, 0); }
		public AngContext(PunteroContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).enterAng(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).exitAng(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class INTContext extends PunteroContext {
		public TerminalNode INT() { return getToken(TerceraParteParser.INT, 0); }
		public INTContext(PunteroContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).enterINT(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).exitINT(this);
		}
	}

	public final PunteroContext puntero() throws RecognitionException {
		PunteroContext _localctx = new PunteroContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_puntero);
		int _la;
		try {
			setState(46);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				_localctx = new PosContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(24);
				((PosContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==MOV || _la==ROT) ) {
					((PosContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(25);
				match(T__0);
				setState(26);
				puntero();
				setState(29);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1) {
					{
					setState(27);
					match(T__1);
					setState(28);
					puntero();
					}
				}

				setState(31);
				match(T__2);
				}
				break;
			case 2:
				_localctx = new AngContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(33);
				match(ROT);
				setState(34);
				match(T__0);
				setState(35);
				match(MOV);
				setState(36);
				match(T__0);
				setState(37);
				puntero();
				setState(38);
				match(T__1);
				setState(39);
				puntero();
				setState(40);
				match(T__2);
				setState(41);
				((AngContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==SUM || _la==RES) ) {
					((AngContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(42);
				puntero();
				setState(43);
				match(T__2);
				}
				break;
			case 3:
				_localctx = new INTContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(45);
				match(INT);
				}
				break;
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
		"\u0004\u0001\f1\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0001\u0000\u0004\u0000\n\b"+
		"\u0000\u000b\u0000\f\u0000\u000b\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u0015\b\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0003\u0003\u001e\b\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003"+
		"\u0003/\b\u0003\u0001\u0003\u0000\u0000\u0004\u0000\u0002\u0004\u0006"+
		"\u0000\u0003\u0001\u0000\u0004\u0005\u0001\u0000\u0006\u0007\u0001\u0000"+
		"\b\t2\u0000\t\u0001\u0000\u0000\u0000\u0002\u0014\u0001\u0000\u0000\u0000"+
		"\u0004\u0016\u0001\u0000\u0000\u0000\u0006.\u0001\u0000\u0000\u0000\b"+
		"\n\u0003\u0002\u0001\u0000\t\b\u0001\u0000\u0000\u0000\n\u000b\u0001\u0000"+
		"\u0000\u0000\u000b\t\u0001\u0000\u0000\u0000\u000b\f\u0001\u0000\u0000"+
		"\u0000\f\u0001\u0001\u0000\u0000\u0000\r\u000e\u0003\u0004\u0002\u0000"+
		"\u000e\u000f\u0005\u000b\u0000\u0000\u000f\u0015\u0001\u0000\u0000\u0000"+
		"\u0010\u0011\u0003\u0006\u0003\u0000\u0011\u0012\u0005\u000b\u0000\u0000"+
		"\u0012\u0015\u0001\u0000\u0000\u0000\u0013\u0015\u0005\u000b\u0000\u0000"+
		"\u0014\r\u0001\u0000\u0000\u0000\u0014\u0010\u0001\u0000\u0000\u0000\u0014"+
		"\u0013\u0001\u0000\u0000\u0000\u0015\u0003\u0001\u0000\u0000\u0000\u0016"+
		"\u0017\u0007\u0000\u0000\u0000\u0017\u0005\u0001\u0000\u0000\u0000\u0018"+
		"\u0019\u0007\u0001\u0000\u0000\u0019\u001a\u0005\u0001\u0000\u0000\u001a"+
		"\u001d\u0003\u0006\u0003\u0000\u001b\u001c\u0005\u0002\u0000\u0000\u001c"+
		"\u001e\u0003\u0006\u0003\u0000\u001d\u001b\u0001\u0000\u0000\u0000\u001d"+
		"\u001e\u0001\u0000\u0000\u0000\u001e\u001f\u0001\u0000\u0000\u0000\u001f"+
		" \u0005\u0003\u0000\u0000 /\u0001\u0000\u0000\u0000!\"\u0005\u0007\u0000"+
		"\u0000\"#\u0005\u0001\u0000\u0000#$\u0005\u0006\u0000\u0000$%\u0005\u0001"+
		"\u0000\u0000%&\u0003\u0006\u0003\u0000&\'\u0005\u0002\u0000\u0000\'(\u0003"+
		"\u0006\u0003\u0000()\u0005\u0003\u0000\u0000)*\u0007\u0002\u0000\u0000"+
		"*+\u0003\u0006\u0003\u0000+,\u0005\u0003\u0000\u0000,/\u0001\u0000\u0000"+
		"\u0000-/\u0005\n\u0000\u0000.\u0018\u0001\u0000\u0000\u0000.!\u0001\u0000"+
		"\u0000\u0000.-\u0001\u0000\u0000\u0000/\u0007\u0001\u0000\u0000\u0000"+
		"\u0004\u000b\u0014\u001d.";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}