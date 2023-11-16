// Generated from c:/Users/josem/Documents/Lenguajes de Programacion/Control1LP/ControlP4/CuartaParte.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CuartaParteParser}.
 */
public interface CuartaParteListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CuartaParteParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(CuartaParteParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link CuartaParteParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(CuartaParteParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Mod}
	 * labeled alternative in {@link CuartaParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void enterMod(CuartaParteParser.ModContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Mod}
	 * labeled alternative in {@link CuartaParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void exitMod(CuartaParteParser.ModContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Mov}
	 * labeled alternative in {@link CuartaParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void enterMov(CuartaParteParser.MovContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Mov}
	 * labeled alternative in {@link CuartaParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void exitMov(CuartaParteParser.MovContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Rot}
	 * labeled alternative in {@link CuartaParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void enterRot(CuartaParteParser.RotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Rot}
	 * labeled alternative in {@link CuartaParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void exitRot(CuartaParteParser.RotContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Rep}
	 * labeled alternative in {@link CuartaParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void enterRep(CuartaParteParser.RepContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Rep}
	 * labeled alternative in {@link CuartaParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void exitRep(CuartaParteParser.RepContext ctx);
	/**
	 * Enter a parse tree produced by the {@code blank}
	 * labeled alternative in {@link CuartaParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void enterBlank(CuartaParteParser.BlankContext ctx);
	/**
	 * Exit a parse tree produced by the {@code blank}
	 * labeled alternative in {@link CuartaParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void exitBlank(CuartaParteParser.BlankContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AsignMod}
	 * labeled alternative in {@link CuartaParteParser#modo}.
	 * @param ctx the parse tree
	 */
	void enterAsignMod(CuartaParteParser.AsignModContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AsignMod}
	 * labeled alternative in {@link CuartaParteParser#modo}.
	 * @param ctx the parse tree
	 */
	void exitAsignMod(CuartaParteParser.AsignModContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SntxMov}
	 * labeled alternative in {@link CuartaParteParser#movimiento}.
	 * @param ctx the parse tree
	 */
	void enterSntxMov(CuartaParteParser.SntxMovContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SntxMov}
	 * labeled alternative in {@link CuartaParteParser#movimiento}.
	 * @param ctx the parse tree
	 */
	void exitSntxMov(CuartaParteParser.SntxMovContext ctx);
	/**
	 * Enter a parse tree produced by the {@code INT}
	 * labeled alternative in {@link CuartaParteParser#movimiento}.
	 * @param ctx the parse tree
	 */
	void enterINT(CuartaParteParser.INTContext ctx);
	/**
	 * Exit a parse tree produced by the {@code INT}
	 * labeled alternative in {@link CuartaParteParser#movimiento}.
	 * @param ctx the parse tree
	 */
	void exitINT(CuartaParteParser.INTContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SntxRot}
	 * labeled alternative in {@link CuartaParteParser#rotacion}.
	 * @param ctx the parse tree
	 */
	void enterSntxRot(CuartaParteParser.SntxRotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SntxRot}
	 * labeled alternative in {@link CuartaParteParser#rotacion}.
	 * @param ctx the parse tree
	 */
	void exitSntxRot(CuartaParteParser.SntxRotContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SntxRotOp}
	 * labeled alternative in {@link CuartaParteParser#rotacion}.
	 * @param ctx the parse tree
	 */
	void enterSntxRotOp(CuartaParteParser.SntxRotOpContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SntxRotOp}
	 * labeled alternative in {@link CuartaParteParser#rotacion}.
	 * @param ctx the parse tree
	 */
	void exitSntxRotOp(CuartaParteParser.SntxRotOpContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SntxRepMov}
	 * labeled alternative in {@link CuartaParteParser#repetir}.
	 * @param ctx the parse tree
	 */
	void enterSntxRepMov(CuartaParteParser.SntxRepMovContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SntxRepMov}
	 * labeled alternative in {@link CuartaParteParser#repetir}.
	 * @param ctx the parse tree
	 */
	void exitSntxRepMov(CuartaParteParser.SntxRepMovContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SntxRepRot}
	 * labeled alternative in {@link CuartaParteParser#repetir}.
	 * @param ctx the parse tree
	 */
	void enterSntxRepRot(CuartaParteParser.SntxRepRotContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SntxRepRot}
	 * labeled alternative in {@link CuartaParteParser#repetir}.
	 * @param ctx the parse tree
	 */
	void exitSntxRepRot(CuartaParteParser.SntxRepRotContext ctx);
}