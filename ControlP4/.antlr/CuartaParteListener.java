// Generated from c://Users//Kevin//Desktop//Control1LP//ControlP4//CuartaParte.g4 by ANTLR 4.13.1
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
	 * Enter a parse tree produced by the {@code Dib}
	 * labeled alternative in {@link CuartaParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void enterDib(CuartaParteParser.DibContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Dib}
	 * labeled alternative in {@link CuartaParteParser#dibujo}.
	 * @param ctx the parse tree
	 */
	void exitDib(CuartaParteParser.DibContext ctx);
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
	 * Enter a parse tree produced by {@link CuartaParteParser#repetir}.
	 * @param ctx the parse tree
	 */
	void enterRepetir(CuartaParteParser.RepetirContext ctx);
	/**
	 * Exit a parse tree produced by {@link CuartaParteParser#repetir}.
	 * @param ctx the parse tree
	 */
	void exitRepetir(CuartaParteParser.RepetirContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Pos}
	 * labeled alternative in {@link CuartaParteParser#puntero}.
	 * @param ctx the parse tree
	 */
	void enterPos(CuartaParteParser.PosContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Pos}
	 * labeled alternative in {@link CuartaParteParser#puntero}.
	 * @param ctx the parse tree
	 */
	void exitPos(CuartaParteParser.PosContext ctx);
}