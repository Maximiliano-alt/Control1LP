// Generated from c:/Users/josem/Documents/Lenguajes de Programacion/Control1LP/ControlP4/TerceraParte.g4 by ANTLR 4.13.1
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
		T__0=1, T__1=2, T__2=3, SUM=4, REST=5, ENC=6, APAG=7, MOV=8, ROT=9, INT=10, 
		NEWLINE=11, WS=12;
	public static final int
		RULE_prog = 0, RULE_dibujo = 1, RULE_modo = 2, RULE_movimiento = 3, RULE_rotacion = 4;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "dibujo", "modo", "movimiento", "rotacion"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "','", "')'", "'+'", "'-'", "'encendido'", "'apagado'", 
			"'mover'", "'rotar'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, "SUM", "REST", "ENC", "APAG", "MOV", "ROT", "INT", 
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
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 4032L) != 0) );
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
	public static class MovContext extends DibujoContext {
		public MovimientoContext movimiento() {
			return getRuleContext(MovimientoContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(TerceraParteParser.NEWLINE, 0); }
		public MovContext(DibujoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).enterMov(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).exitMov(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class RotContext extends DibujoContext {
		public RotacionContext rotacion() {
			return getRuleContext(RotacionContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(TerceraParteParser.NEWLINE, 0); }
		public RotContext(DibujoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).enterRot(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).exitRot(this);
		}
	}

	public final DibujoContext dibujo() throws RecognitionException {
		DibujoContext _localctx = new DibujoContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_dibujo);
		try {
			setState(25);
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
			case INT:
				_localctx = new MovContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(18);
				movimiento();
				setState(19);
				match(NEWLINE);
				}
				break;
			case ROT:
				_localctx = new RotContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(21);
				rotacion();
				setState(22);
				match(NEWLINE);
				}
				break;
			case NEWLINE:
				_localctx = new BlankContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(24);
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
			setState(27);
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
	public static class MovimientoContext extends ParserRuleContext {
		public MovimientoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_movimiento; }
	 
		public MovimientoContext() { }
		public void copyFrom(MovimientoContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SntxMovContext extends MovimientoContext {
		public TerminalNode MOV() { return getToken(TerceraParteParser.MOV, 0); }
		public List<TerminalNode> INT() { return getTokens(TerceraParteParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(TerceraParteParser.INT, i);
		}
		public SntxMovContext(MovimientoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).enterSntxMov(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).exitSntxMov(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class INTContext extends MovimientoContext {
		public TerminalNode INT() { return getToken(TerceraParteParser.INT, 0); }
		public INTContext(MovimientoContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).enterINT(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).exitINT(this);
		}
	}

	public final MovimientoContext movimiento() throws RecognitionException {
		MovimientoContext _localctx = new MovimientoContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_movimiento);
		int _la;
		try {
			setState(38);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MOV:
				_localctx = new SntxMovContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(29);
				match(MOV);
				setState(30);
				match(T__0);
				setState(31);
				match(INT);
				setState(34);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1) {
					{
					setState(32);
					match(T__1);
					setState(33);
					match(INT);
					}
				}

				setState(36);
				match(T__2);
				}
				break;
			case INT:
				_localctx = new INTContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(37);
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

	@SuppressWarnings("CheckReturnValue")
	public static class RotacionContext extends ParserRuleContext {
		public RotacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rotacion; }
	 
		public RotacionContext() { }
		public void copyFrom(RotacionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SntxRotOpContext extends RotacionContext {
		public Token op;
		public TerminalNode ROT() { return getToken(TerceraParteParser.ROT, 0); }
		public List<MovimientoContext> movimiento() {
			return getRuleContexts(MovimientoContext.class);
		}
		public MovimientoContext movimiento(int i) {
			return getRuleContext(MovimientoContext.class,i);
		}
		public TerminalNode REST() { return getToken(TerceraParteParser.REST, 0); }
		public TerminalNode SUM() { return getToken(TerceraParteParser.SUM, 0); }
		public SntxRotOpContext(RotacionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).enterSntxRotOp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).exitSntxRotOp(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SntxRotContext extends RotacionContext {
		public TerminalNode ROT() { return getToken(TerceraParteParser.ROT, 0); }
		public List<TerminalNode> INT() { return getTokens(TerceraParteParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(TerceraParteParser.INT, i);
		}
		public SntxRotContext(RotacionContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).enterSntxRot(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof TerceraParteListener ) ((TerceraParteListener)listener).exitSntxRot(this);
		}
	}

	public final RotacionContext rotacion() throws RecognitionException {
		RotacionContext _localctx = new RotacionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_rotacion);
		int _la;
		try {
			setState(55);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				_localctx = new SntxRotContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(40);
				match(ROT);
				setState(41);
				match(T__0);
				setState(42);
				match(INT);
				setState(45);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__1) {
					{
					setState(43);
					match(T__1);
					setState(44);
					match(INT);
					}
				}

				setState(47);
				match(T__2);
				}
				break;
			case 2:
				_localctx = new SntxRotOpContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(48);
				match(ROT);
				setState(49);
				match(T__0);
				setState(50);
				movimiento();
				setState(51);
				((SntxRotOpContext)_localctx).op = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==SUM || _la==REST) ) {
					((SntxRotOpContext)_localctx).op = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(52);
				movimiento();
				setState(53);
				match(T__2);
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
		"\u0004\u0001\f:\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0001"+
		"\u0000\u0004\u0000\f\b\u0000\u000b\u0000\f\u0000\r\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u0001\u001a\b\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003"+
		"#\b\u0003\u0001\u0003\u0001\u0003\u0003\u0003\'\b\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004.\b\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0003\u00048\b\u0004\u0001\u0004\u0000\u0000\u0005"+
		"\u0000\u0002\u0004\u0006\b\u0000\u0002\u0001\u0000\u0006\u0007\u0001\u0000"+
		"\u0004\u0005<\u0000\u000b\u0001\u0000\u0000\u0000\u0002\u0019\u0001\u0000"+
		"\u0000\u0000\u0004\u001b\u0001\u0000\u0000\u0000\u0006&\u0001\u0000\u0000"+
		"\u0000\b7\u0001\u0000\u0000\u0000\n\f\u0003\u0002\u0001\u0000\u000b\n"+
		"\u0001\u0000\u0000\u0000\f\r\u0001\u0000\u0000\u0000\r\u000b\u0001\u0000"+
		"\u0000\u0000\r\u000e\u0001\u0000\u0000\u0000\u000e\u0001\u0001\u0000\u0000"+
		"\u0000\u000f\u0010\u0003\u0004\u0002\u0000\u0010\u0011\u0005\u000b\u0000"+
		"\u0000\u0011\u001a\u0001\u0000\u0000\u0000\u0012\u0013\u0003\u0006\u0003"+
		"\u0000\u0013\u0014\u0005\u000b\u0000\u0000\u0014\u001a\u0001\u0000\u0000"+
		"\u0000\u0015\u0016\u0003\b\u0004\u0000\u0016\u0017\u0005\u000b\u0000\u0000"+
		"\u0017\u001a\u0001\u0000\u0000\u0000\u0018\u001a\u0005\u000b\u0000\u0000"+
		"\u0019\u000f\u0001\u0000\u0000\u0000\u0019\u0012\u0001\u0000\u0000\u0000"+
		"\u0019\u0015\u0001\u0000\u0000\u0000\u0019\u0018\u0001\u0000\u0000\u0000"+
		"\u001a\u0003\u0001\u0000\u0000\u0000\u001b\u001c\u0007\u0000\u0000\u0000"+
		"\u001c\u0005\u0001\u0000\u0000\u0000\u001d\u001e\u0005\b\u0000\u0000\u001e"+
		"\u001f\u0005\u0001\u0000\u0000\u001f\"\u0005\n\u0000\u0000 !\u0005\u0002"+
		"\u0000\u0000!#\u0005\n\u0000\u0000\" \u0001\u0000\u0000\u0000\"#\u0001"+
		"\u0000\u0000\u0000#$\u0001\u0000\u0000\u0000$\'\u0005\u0003\u0000\u0000"+
		"%\'\u0005\n\u0000\u0000&\u001d\u0001\u0000\u0000\u0000&%\u0001\u0000\u0000"+
		"\u0000\'\u0007\u0001\u0000\u0000\u0000()\u0005\t\u0000\u0000)*\u0005\u0001"+
		"\u0000\u0000*-\u0005\n\u0000\u0000+,\u0005\u0002\u0000\u0000,.\u0005\n"+
		"\u0000\u0000-+\u0001\u0000\u0000\u0000-.\u0001\u0000\u0000\u0000./\u0001"+
		"\u0000\u0000\u0000/8\u0005\u0003\u0000\u000001\u0005\t\u0000\u000012\u0005"+
		"\u0001\u0000\u000023\u0003\u0006\u0003\u000034\u0007\u0001\u0000\u0000"+
		"45\u0003\u0006\u0003\u000056\u0005\u0003\u0000\u000068\u0001\u0000\u0000"+
		"\u00007(\u0001\u0000\u0000\u000070\u0001\u0000\u0000\u00008\t\u0001\u0000"+
		"\u0000\u0000\u0006\r\u0019\"&-7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}