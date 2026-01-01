from manim import *

class QuadraticEquation(Scene):
    def construct(self):
        # Titolo
        title = Text("Risoluzione di un'Equazione di Secondo Grado", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Equazione iniziale
        eq1 = MathTex("x^2", "-", "5x", "+", "6", "=", "0")
        eq1.scale(1.5)
        self.play(Write(eq1))
        self.wait(2)
        
        # Identifichiamo i coefficienti
        self.play(eq1.animate.shift(UP * 2))
        
        coeff_text = Text("Identifichiamo i coefficienti:", font_size=28)
        coeff_text.next_to(eq1, DOWN, buff=0.8)
        self.play(Write(coeff_text))
        
        coeffs = MathTex("a = 1,", "\\quad b = -5,", "\\quad c = 6")
        coeffs.next_to(coeff_text, DOWN)
        self.play(Write(coeffs))
        self.wait(2)
        
        # Formula risolutiva
        self.play(FadeOut(coeff_text), FadeOut(coeffs))
        
        formula_text = Text("Usiamo la formula risolutiva:", font_size=28)
        formula_text.next_to(eq1, DOWN, buff=0.8)
        self.play(Write(formula_text))
        
        formula = MathTex("x", "=", "\\frac{-b \\pm \\sqrt{b^2 - 4ac}}{2a}")
        formula.next_to(formula_text, DOWN)
        self.play(Write(formula))
        self.wait(2)
        
        # Sostituiamo i valori
        self.play(FadeOut(formula_text))
        
        subst_text = Text("Sostituiamo i valori:", font_size=28)
        subst_text.next_to(eq1, DOWN, buff=0.8)
        self.play(Write(subst_text))
        
        step1 = MathTex("x", "=", "\\frac{-(-5) \\pm \\sqrt{(-5)^2 - 4(1)(6)}}{2(1)}")
        step1.next_to(subst_text, DOWN)
        self.play(TransformMatchingTex(formula, step1))
        self.wait(2)
        
        # Semplifichiamo
        self.play(FadeOut(subst_text))
        
        calc_text = Text("Calcoliamo il discriminante:", font_size=28)
        calc_text.next_to(eq1, DOWN, buff=0.8)
        self.play(Write(calc_text))
        
        step2 = MathTex("x", "=", "\\frac{5 \\pm \\sqrt{25 - 24}}{2}")
        step2.next_to(calc_text, DOWN)
        self.play(TransformMatchingTex(step1, step2))
        self.wait(2)
        
        step3 = MathTex("x", "=", "\\frac{5 \\pm \\sqrt{1}}{2}")
        step3.next_to(calc_text, DOWN)
        self.play(TransformMatchingTex(step2, step3))
        self.wait(1)
        
        step4 = MathTex("x", "=", "\\frac{5 \\pm 1}{2}")
        step4.next_to(calc_text, DOWN)
        self.play(TransformMatchingTex(step3, step4))
        self.wait(2)
        
        # Soluzioni finali
        self.play(FadeOut(calc_text), FadeOut(step4))
        
        sol_text = Text("Le due soluzioni sono:", font_size=28)
        sol_text.next_to(eq1, DOWN, buff=0.8)
        self.play(Write(sol_text))
        
        sol1 = MathTex("x_1", "=", "\\frac{5 + 1}{2}", "=", "3")
        sol1.next_to(sol_text, DOWN, buff=0.5)
        
        sol2 = MathTex("x_2", "=", "\\frac{5 - 1}{2}", "=", "2")
        sol2.next_to(sol1, DOWN)
        
        self.play(Write(sol1))
        self.wait(1)
        self.play(Write(sol2))
        self.wait(2)
        
        # Verifica grafica (opzionale)
        self.play(
            FadeOut(eq1), FadeOut(sol_text), 
            FadeOut(sol1), FadeOut(sol2), FadeOut(title)
        )
        
        verify_title = Text("Verifica grafica:", font_size=32)
        verify_title.to_edge(UP)
        self.play(Write(verify_title))
        
        # Grafico della parabola
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[-1, 3, 1],
            x_length=6,
            y_length=4,
            tips=False
        )
        
        parabola = axes.plot(lambda x: x**2 - 5*x + 6, color=BLUE)
        parabola_label = MathTex("y = x^2 - 5x + 6", color=BLUE)
        parabola_label.next_to(axes, UP)
        
        # Punti delle soluzioni
        dot1 = Dot(axes.c2p(2, 0), color=RED)
        dot2 = Dot(axes.c2p(3, 0), color=RED)
        label1 = MathTex("x = 2", color=RED).next_to(dot1, DOWN)
        label2 = MathTex("x = 3", color=RED).next_to(dot2, DOWN)
        
        self.play(Create(axes))
        self.play(Create(parabola), Write(parabola_label))
        self.wait(1)
        self.play(
            FadeIn(dot1), FadeIn(dot2),
            Write(label1), Write(label2)
        )
        self.wait(3)