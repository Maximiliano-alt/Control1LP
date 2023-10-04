// Generated from c:/Users/josem/Documents/Lenguajes de Programacion/Control1LP/ControlP3/TerceraParte.g4 by ANTLR 4.13.1
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
	 * Enter a parse tree produced by the {@code Mov}
	 * labeled alternative in {@link TerceraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void enterMov(TerceraParteParser.MovContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Mov}
	 * labeled alternative in {@link TerceraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void exitMov(TerceraParteParser.MovContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Rot}
	 * labeled alternative in {@link TerceraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void enterRot(TerceraParteParser.RotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Rot}
	 * labeled alternative in {@link TerceraParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void exitRot(TerceraParteParser.RotContext ctx);
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
	 * Enter a parse tree produced by the {@code SntxMov}
	 * labeled alternative in {@link TerceraParteParser#movimiento}.
	 * @param ctx the parse tree
	 */
	void enterSntxMov(TerceraParteParser.SntxMovContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SntxMov}
	 * labeled alternative in {@link TerceraParteParser#movimiento}.
	 * @param ctx the parse tree
	 */
	void exitSntxMov(TerceraParteParser.SntxMovContext ctx);
	/**
	 * Enter a parse tree produced by the {@code INT}
	 * labeled alternative in {@link TerceraParteParser#movimiento}.
	 * @param ctx the parse tree
	 */
	void enterINT(TerceraParteParser.INTContext ctx);
	/**
	 * Exit a parse tree produced by the {@code INT}
	 * labeled alternative in {@link TerceraParteParser#movimiento}.
	 * @param ctx the parse tree
	 */
	void exitINT(TerceraParteParser.INTContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SntxRot}
	 * labeled alternative in {@link TerceraParteParser#rotacion}.
	 * @param ctx the parse tree
	 */
	void enterSntxRot(TerceraParteParser.SntxRotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SntxRot}
	 * labeled alternative in {@link TerceraParteParser#rotacion}.
	 * @param ctx the parse tree
	 */
	void exitSntxRot(TerceraParteParser.SntxRotContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SntxRotOp}
	 * labeled alternative in {@link TerceraParteParser#rotacion}.
	 * @param ctx the parse tree
	 */
	void enterSntxRotOp(TerceraParteParser.SntxRotOpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SntxRotOp}
	 * labeled alternative in {@link TerceraParteParser#rotacion}.
	 * @param ctx the parse tree
	 */
	void exitSntxRotOp(TerceraParteParser.SntxRotOpContext ctx);
}