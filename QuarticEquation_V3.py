from manim import *

class QuarticEquation_V3(Scene):
    def construct(self):
        # Titolo
        title = Text("Risoluzione di un'equazione di quarto grado", font_size=34)
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))
        self.wait(1)
        
        # Frase di attribuzione sotto il titolo (in rosso)
        attribution = Text("Problema posto da Domenico Annunziata, soluzione proposta da Antonio Fanari.", 
                          font_size=18, color=RED)
        attribution.next_to(title, DOWN, buff=0.4)
        self.play(Write(attribution))
        self.wait(1)
        
        # Equazione iniziale
        eq_initial = MathTex("x^4", "-", "4x^3", "-", "2x^2", "+", "12x", "+", "11", "=", "0")
        eq_initial.scale(1.3)
        self.play(Write(eq_initial))
        self.wait(2)
        
        # Spostiamo tutto in alto
        group_title_attribution = VGroup(title, attribution)
        self.play(
            group_title_attribution.animate.to_edge(UP, buff=0.8),
            eq_initial.animate.scale(0.85).next_to(attribution, DOWN, buff=0.8)
        )
        
        # Passo 1: Riscrittura strategica
        step1_text = Text("Strategia: riscriviamo -2x² come 4x² - 6x²", 
                         font_size=26, color=YELLOW)
        step1_text.next_to(eq_initial, DOWN, buff=0.8)
        self.play(Write(step1_text))
        self.wait(2)
        
        eq_step1 = MathTex("x^4", "-", "4x^3", "+", "4x^2", "-", "6x^2", "+", "12x", "+", "11", "=", "0")
        eq_step1.next_to(step1_text, DOWN, buff=0.6)
        self.play(Write(eq_step1))
        self.wait(2.5)
        
        # Passo 2: Raggruppiamo
        self.play(FadeOut(step1_text))
        
        step2_text = Text("Raggruppando i primi tre termini si ottiene:", 
                         font_size=26, color=YELLOW)
        step2_text.next_to(eq_initial, DOWN, buff=0.8)
        self.play(Write(step2_text))
        self.wait(1)
        
        # Evidenziamo il quadrato perfetto
        highlight_box = SurroundingRectangle(
            VGroup(eq_step1[0], eq_step1[1], eq_step1[2], eq_step1[3], eq_step1[4]),
            color=GREEN, buff=0.1
        )
        self.play(Create(highlight_box))
        self.wait(1.5)
        
        eq_step2 = MathTex("(x^2", "-", "2x)^2", "-", "6x^2", "+", "12x", "+", "11", "=", "0")
        eq_step2.next_to(step2_text, DOWN, buff=0.6)
        self.play(
            FadeOut(highlight_box),
            TransformMatchingTex(eq_step1, eq_step2)
        )
        self.wait(2)
        
        # Passo 3: Fattorizziamo
        self.play(FadeOut(step2_text))
        
        step3_text = Text("Fattorizzando:", font_size=26, color=YELLOW)
        step3_text.next_to(eq_initial, DOWN, buff=0.8)
        self.play(Write(step3_text))
        self.wait(1)
        
        eq_step3 = MathTex("(x^2", "-", "2x)^2", "-", "6", "(x^2", "-", "2x)", "+", "11", "=", "0")
        eq_step3.next_to(step3_text, DOWN, buff=0.6)
        self.play(TransformMatchingTex(eq_step2, eq_step3))
        self.wait(2.5)
        
        # Passo 4: Sostituzione - PULIAMO TUTTO PRIMA
        self.play(
            FadeOut(group_title_attribution),
            FadeOut(eq_initial),
            FadeOut(step3_text),
            FadeOut(eq_step3)
        )
        
        # Nuovo schermo per la sostituzione
        subst_title = Text("Effettuando una sotituzione quadratica:", font_size=32, color=YELLOW)
        subst_title.to_edge(UP, buff=0.8)
        self.play(Write(subst_title))
        
        substitution = MathTex("t", "=", "x^2", "-", "2x", "=", "x(x-2)", color=BLUE)
        substitution.scale(1.2)
        substitution.next_to(subst_title, DOWN, buff=0.8)
        self.play(Write(substitution))
        self.wait(2)
        
        # Equazione trasformata
        eq_transformed = MathTex("t^2", "-", "6t", "+", "11", "=", "0", color=GREEN)
        eq_transformed.scale(1.3)
        eq_transformed.next_to(substitution, DOWN, buff=1.0)
        self.play(Write(eq_transformed))
        self.wait(2.5)
        
        # Passo 5: Risoluzione - PULIAMO
        self.play(
            FadeOut(subst_title),
            FadeOut(substitution)
        )
        
        solve_title = Text("Risolvendo per t", font_size=32, color=YELLOW)
        solve_title.to_edge(UP, buff=0.8)
        self.play(Write(solve_title))
        self.play(eq_transformed.animate.next_to(solve_title, DOWN, buff=0.8))
        
        formula = MathTex("t", "=", r"\frac{6 \pm \sqrt{36-44}}{2}")
        formula.next_to(eq_transformed, DOWN, buff=0.8)
        self.play(Write(formula))
        self.wait(1.5)
        
        formula2 = MathTex("t", "=", r"\frac{6 \pm 2i\sqrt{2}}{2}")
        formula2.next_to(formula, DOWN, buff=0.6)
        self.play(Write(formula2))
        self.wait(1.5)
        
        # Soluzione per t
        solution_t = MathTex("t", "=", "3", r"\pm", "i\sqrt{2}", color=RED)
        solution_t.scale(1.3)
        solution_t.next_to(formula2, DOWN, buff=0.8)
        
        solution_box = SurroundingRectangle(solution_t, color=RED, buff=0.2)
        self.play(Write(solution_t))
        self.play(Create(solution_box))
        self.wait(2)
        
        # Passo 6: CASO 1 - PULIAMO TUTTO
        self.play(
            FadeOut(solve_title),
            FadeOut(eq_transformed),
            FadeOut(formula),
            FadeOut(formula2),
            FadeOut(solution_box),
            FadeOut(solution_t)
        )
        
        case1_title = Text("Caso 1: t = 3 + i√2", font_size=30, color=YELLOW)
        case1_title.to_edge(UP, buff=0.8)
        self.play(Write(case1_title))
        
        back_to_x1 = MathTex("x^2", "-", "2x", "=", "3", "+", "i\sqrt{2}")
        back_to_x1.scale(1.2)
        back_to_x1.next_to(case1_title, DOWN, buff=0.8)
        self.play(Write(back_to_x1))
        self.wait(1.5)
        
        back_to_x2 = MathTex("x^2", "-", "2x", "-", "(3", "+", "i\sqrt{2})", "=", "0")
        back_to_x2.next_to(back_to_x1, DOWN, buff=0.6)
        self.play(Write(back_to_x2))
        self.wait(1.5)
        
        x_result1 = MathTex("x", "=", "1", r"\pm", r"\sqrt{4 + i\sqrt{2}}", color=GREEN)
        x_result1.scale(1.2)
        x_result1.next_to(back_to_x2, DOWN, buff=0.8)
        self.play(Write(x_result1))
        self.wait(2)
        
        # CASO 2 - PULIAMO
        self.play(
            FadeOut(case1_title),
            FadeOut(back_to_x1),
            FadeOut(back_to_x2),
            FadeOut(x_result1)
        )
        
        case2_title = Text("Caso 2: t = 3 - i√2", font_size=30, color=YELLOW)
        case2_title.to_edge(UP, buff=0.8)
        self.play(Write(case2_title))
        
        back_to_x3 = MathTex("x^2", "-", "2x", "=", "3", "-", "i\sqrt{2}")
        back_to_x3.scale(1.2)
        back_to_x3.next_to(case2_title, DOWN, buff=0.8)
        self.play(Write(back_to_x3))
        self.wait(1.5)
        
        x_result2 = MathTex("x", "=", "1", r"\pm", r"\sqrt{4 - i\sqrt{2}}", color=GREEN)
        x_result2.scale(1.2)
        x_result2.next_to(back_to_x3, DOWN, buff=0.8)
        self.play(Write(x_result2))
        self.wait(2)
        
        # SOLUZIONI FINALI IN FORMA RADICALE - PULIAMO TUTTO
        self.play(
            FadeOut(case2_title),
            FadeOut(back_to_x3),
            FadeOut(x_result2)
        )
        
        final_title = Text("Ecco le 4 soluzioni complesse:", font_size=32, color=YELLOW)
        final_title.to_edge(UP, buff=0.8)
        self.play(Write(final_title))
        self.wait(1)
        
        # Soluzioni in forma radicale
        sol1 = MathTex("x_1", "=", "1", "+", r"\sqrt{4 + i\sqrt{2}}", color=GREEN)
        sol2 = MathTex("x_2", "=", "1", "-", r"\sqrt{4 + i\sqrt{2}}", color=GREEN)
        sol3 = MathTex("x_3", "=", "1", "+", r"\sqrt{4 - i\sqrt{2}}", color=GREEN)
        sol4 = MathTex("x_4", "=", "1", "-", r"\sqrt{4 - i\sqrt{2}}", color=GREEN)
        
        # Raggruppiamo le soluzioni
        solutions = VGroup(sol1, sol2, sol3, sol4)
        solutions.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        solutions.move_to(ORIGIN).shift(DOWN*0.3)
        
        final_box = SurroundingRectangle(solutions, color=GREEN, buff=0.3, stroke_width=3)
        
        self.play(Create(final_box))
        for sol in solutions:
            self.play(Write(sol))
            self.wait(0.6)
        
        self.wait(2)
        
        # TRANSIZIONE ALLA FORMA STANDARD a+ib
        self.play(
            FadeOut(final_title),
            FadeOut(final_box),
            FadeOut(solutions)
        )
        
        # Titolo per la forma standard
        standard_title = Text("Esprimendo le soluzioni in forma standard a+ib", 
                            font_size=30, color=YELLOW)
        standard_title.to_edge(UP, buff=0.8)
        self.play(Write(standard_title))
        self.wait(1)
        
        # Calcolo della forma standard - Versione compatta
        step1 = Text("Per √(4 + i√2) = p + iq:", font_size=22, color=BLUE)
        step1.next_to(standard_title, DOWN, buff=0.6)
        self.play(Write(step1))
        self.wait(0.5)
        
        eq1 = MathTex(r"(p+iq)^2 = 4 + i\sqrt{2}", font_size=24)
        eq1.next_to(step1, DOWN, buff=0.3)
        self.play(Write(eq1))
        self.wait(0.5)
        
        eq2 = MathTex(r"p^2 - q^2 = 4,\quad 2pq = \sqrt{2}", font_size=24)
        eq2.next_to(eq1, DOWN, buff=0.2)
        self.play(Write(eq2))
        self.wait(0.5)
        
        eq3 = MathTex(r"p^2 + q^2 = \sqrt{18} = 3\sqrt{2}", font_size=24)
        eq3.next_to(eq2, DOWN, buff=0.2)
        self.play(Write(eq3))
        self.wait(1)
        
        # PULISCO PER FARE SPAZIO
        self.play(
            FadeOut(step1),
            FadeOut(eq1),
            FadeOut(eq2),
            FadeOut(eq3)
        )
        
        # Risoluzione sistema - più compatta
        step2 = Text("Risolvendo il sistema:", font_size=22, color=BLUE)
        step2.next_to(standard_title, DOWN, buff=0.6)
        self.play(Write(step2))
        self.wait(0.5)
        
        eq4 = MathTex(r"p^2 = \frac{4 + 3\sqrt{2}}{2}", font_size=26)
        eq4.next_to(step2, DOWN, buff=0.4)
        self.play(Write(eq4))
        self.wait(0.5)
        
        eq5 = MathTex(r"q^2 = \frac{3\sqrt{2} - 4}{2}", font_size=26)
        eq5.next_to(eq4, DOWN, buff=0.2)
        self.play(Write(eq5))
        self.wait(1)
        
        # PULISCO ANCORA
        self.play(
            FadeOut(step2),
            FadeOut(eq4),
            FadeOut(eq5)
        )
        
        # Risultato finale delle radici
        result_title = Text("Le due radici complesse:", font_size=24, color=YELLOW)
        result_title.next_to(standard_title, DOWN, buff=0.6)
        self.play(Write(result_title))
        self.wait(0.5)
        
        sqrt1 = MathTex(r"\sqrt{4 + i\sqrt{2}} = \alpha + i\beta", 
                       color=GREEN, font_size=26)
        sqrt2 = MathTex(r"\sqrt{4 - i\sqrt{2}} = \alpha - i\beta", 
                       color=GREEN, font_size=26)
        
        sqrt1.next_to(result_title, DOWN, buff=0.4)
        sqrt2.next_to(sqrt1, DOWN, buff=0.2)
        
        self.play(Write(sqrt1))
        self.wait(0.5)
        self.play(Write(sqrt2))
        self.wait(0.5)
        
        # Definizione di α e β
        alpha_def = MathTex(r"\alpha = \sqrt{\frac{4 + 3\sqrt{2}}{2}}", 
                          color=BLUE, font_size=22)
        beta_def = MathTex(r"\beta = \sqrt{\frac{3\sqrt{2} - 4}{2}}", 
                         color=BLUE, font_size=22)
        
        alpha_def.next_to(sqrt2, DOWN, buff=0.6)
        beta_def.next_to(alpha_def, DOWN, buff=0.1)
        
        self.play(Write(alpha_def))
        self.wait(0.5)
        self.play(Write(beta_def))
        self.wait(1.5)
        
        # Pulizia per mostrare le 4 soluzioni finali
        self.play(
            FadeOut(standard_title),
            FadeOut(result_title),
            FadeOut(sqrt1),
            FadeOut(sqrt2),
            FadeOut(alpha_def),
            FadeOut(beta_def)
        )
        
        # Mostriamo le 4 soluzioni in forma standard
        final_solutions_title = Text("Le 4 soluzioni in forma a+ib:", 
                                   font_size=28, color=YELLOW)
        final_solutions_title.to_edge(UP, buff=0.8)
        self.play(Write(final_solutions_title))
        self.wait(0.5)
        
        # Costanti in alto - FORMA ORIGINALE CORRETTA
        const_title = Text("dove:", font_size=20, color=BLUE)
        const_title.next_to(final_solutions_title, DOWN, buff=0.6)
        self.play(Write(const_title))
        
        alpha = MathTex(r"\alpha = \sqrt{\frac{4 + 3\sqrt{2}}{2}}", 
                       color=BLUE, font_size=20)
        beta = MathTex(r"\beta = \sqrt{\frac{3\sqrt{2} - 4}{2}}", 
                      color=BLUE, font_size=20)
        
        alpha.next_to(const_title, DOWN, buff=0.4)
        beta.next_to(alpha, DOWN, buff=0.2)
        
        self.play(Write(alpha))
        self.play(Write(beta))
        self.wait(1)
        
        # Le 4 soluzioni
        x1_std = MathTex(r"x_1 = 1 + \alpha + i\beta", 
                        color=GREEN, font_size=24)
        x2_std = MathTex(r"x_2 = 1 - \alpha - i\beta", 
                        color=GREEN, font_size=24)
        x3_std = MathTex(r"x_3 = 1 + \alpha - i\beta", 
                        color=GREEN, font_size=24)
        x4_std = MathTex(r"x_4 = 1 - \alpha + i\beta", 
                        color=GREEN, font_size=24)
        
        # Disposizione su due colonne - SPOSTATA PIÙ IN BASSO
        col1 = VGroup(x1_std, x2_std).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        col2 = VGroup(x3_std, x4_std).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        solutions_group = VGroup(col1, col2).arrange(RIGHT, buff=1.2)
        solutions_group.next_to(beta, DOWN, buff=0.8)  # Più spazio sopra
        
        # Riquadro verde che racchiude TUTTO (spostato più in basso)
        all_content = VGroup(const_title, alpha, beta, solutions_group)
        final_std_box = SurroundingRectangle(
            all_content, 
            color=GREEN, buff=0.3, stroke_width=3
        )
        
        # Prima crea il riquadro, poi scrivi le soluzioni
        self.play(Create(final_std_box))
        self.wait(0.5)
        
        # Scrive le soluzioni una per una
        self.play(Write(x1_std))
        self.wait(0.3)
        self.play(Write(x2_std))
        self.wait(0.3)
        self.play(Write(x3_std))
        self.wait(0.3)
        self.play(Write(x4_std))
        
        self.wait(3)
        
        # Nota finale - POSIZIONATA IN BASSO (in rosso)
        note = Text("Buon anno 2026", font_size=18, color=RED)
        note.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(note))
        self.wait(30)