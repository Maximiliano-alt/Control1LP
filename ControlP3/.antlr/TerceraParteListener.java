// Generated from c://Users//Kevin//Desktop//Control1LP//ControlP3//TerceraParte.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link TerceraParteParser}.
 */
public interface TerceraParteListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link TerceraParteParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(TerceraParteParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link TerceraParteParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(TerceraParteParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Mod}
	 * labeled alternative in {@link TerceraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void enterMod(TerceraParteParser.ModContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Mod}
	 * labeled alternative in {@link TerceraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void exitMod(TerceraParteParser.ModContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Dib}
	 * labeled alternative in {@link TerceraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void enterDib(TerceraParteParser.DibContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Dib}
	 * labeled alternative in {@link TerceraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void exitDib(TerceraParteParser.DibContext ctx);
	/**
	 * Enter a parse tree produced by the {@code blank}
	 * labeled alternative in {@link TerceraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void enterBlank(TerceraParteParser.BlankContext ctx);
	/**
	 * Exit a parse tree produced by the {@code blank}
	 * labeled alternative in {@link TerceraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void exitBlank(TerceraParteParser.BlankContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AsignMod}
	 * labeled alternative in {@link TerceraParteParser#modo}.
	 * @param ctx the parse tree
	 */
	void enterAsignMod(TerceraParteParser.AsignModContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AsignMod}
	 * labeled alternative in {@link TerceraParteParser#modo}.
	 * @param ctx the parse tree
	 */
	void exitAsignMod(TerceraParteParser.AsignModContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Pos}
	 * labeled alternative in {@link TerceraParteParser#puntero}.
	 * @param ctx the parse tree
	 */
	void enterPos(TerceraParteParser.PosContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Pos}
	 * labeled alternative in {@link TerceraParteParser#puntero}.
	 * @param ctx the parse tree
	 */
	void exitPos(TerceraParteParser.PosContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Ang}
	 * labeled alternative in {@link TerceraParteParser#puntero}.
	 * @param ctx the parse tree
	 */
	void enterAng(TerceraParteParser.AngContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Ang}
	 * labeled alternative in {@link TerceraParteParser#puntero}.
	 * @param ctx the parse tree
	 */
	void exitAng(TerceraParteParser.AngContext ctx);
	/**
	 * Enter a parse tree produced by the {@code INT}
	 * labeled alternative in {@link TerceraParteParser#puntero}.
	 * @param ctx the parse tree
	 */
	void enterINT(TerceraParteParser.INTContext ctx);
	/**
	 * Exit a parse tree produced by the {@code INT}
	 * labeled alternative in {@link TerceraParteParser#puntero}.
	 * @param ctx the parse tree
	 */
	void exitINT(TerceraParteParser.INTContext ctx);
}