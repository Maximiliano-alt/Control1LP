// Generated from c:/Users/josem/Documents/Lenguajes de Programacion/Control1LP/ControlP1/PrimeraParte.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PrimeraParteParser}.
 */
public interface PrimeraParteListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PrimeraParteParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(PrimeraParteParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link PrimeraParteParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(PrimeraParteParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Mod}
	 * labeled alternative in {@link PrimeraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void enterMod(PrimeraParteParser.ModContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Mod}
	 * labeled alternative in {@link PrimeraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void exitMod(PrimeraParteParser.ModContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Dib}
	 * labeled alternative in {@link PrimeraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void enterDib(PrimeraParteParser.DibContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Dib}
	 * labeled alternative in {@link PrimeraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void exitDib(PrimeraParteParser.DibContext ctx);
	/**
	 * Enter a parse tree produced by the {@code blank}
	 * labeled alternative in {@link PrimeraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void enterBlank(PrimeraParteParser.BlankContext ctx);
	/**
	 * Exit a parse tree produced by the {@code blank}
	 * labeled alternative in {@link PrimeraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void exitBlank(PrimeraParteParser.BlankContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AsignMod}
	 * labeled alternative in {@link PrimeraParteParser#modo}.
	 * @param ctx the parse tree
	 */
	void enterAsignMod(PrimeraParteParser.AsignModContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AsignMod}
	 * labeled alternative in {@link PrimeraParteParser#modo}.
	 * @param ctx the parse tree
	 */
	void exitAsignMod(PrimeraParteParser.AsignModContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Pos}
	 * labeled alternative in {@link PrimeraParteParser#puntero}.
	 * @param ctx the parse tree
	 */
	void enterPos(PrimeraParteParser.PosContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Pos}
	 * labeled alternative in {@link PrimeraParteParser#puntero}.
	 * @param ctx the parse tree
	 */
	void exitPos(PrimeraParteParser.PosContext ctx);
}