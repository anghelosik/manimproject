from manim import *

class IndefiniteIntegral(Scene):
    def construct(self):
        # Titolo
        title = Text("Integrale Indefinito", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Problema iniziale
        problem = MathTex(r"\int", r"\sin(2x)", r"\,dx")
        problem.scale(1.8)
        self.play(Write(problem))
        self.wait(2)
        
        # Spostiamo in alto
        self.play(problem.animate.scale(0.7).shift(UP * 2.5))
        
        # Metodo: Sostituzione
        method_text = Text("Metodo: Sostituzione", font_size=28, color=YELLOW)
        method_text.next_to(problem, DOWN, buff=0.8)
        self.play(Write(method_text))
        self.wait(1)
        
        # Passo 1: Definiamo u
        step1_text = Text("Poniamo:", font_size=24)
        step1_text.next_to(method_text, DOWN, buff=0.6)
        self.play(Write(step1_text))
        
        substitution = MathTex("u", "=", "2x")
        substitution.next_to(step1_text, DOWN, buff=0.3)
        self.play(Write(substitution))
        self.wait(1.5)
        
        # Passo 2: Calcoliamo du
        step2_text = Text("Quindi:", font_size=24)
        step2_text.next_to(substitution, DOWN, buff=0.5)
        self.play(Write(step2_text))
        
        du_calc = MathTex(r"\frac{du}{dx}", "=", "2")
        du_calc.next_to(step2_text, DOWN, buff=0.3)
        self.play(Write(du_calc))
        self.wait(1)
        
        du_result = MathTex("du", "=", "2", "dx")
        du_result.next_to(du_calc, DOWN, buff=0.3)
        self.play(Write(du_result))
        self.wait(1)
        
        dx_isolated = MathTex("dx", "=", r"\frac{du}{2}")
        dx_isolated.next_to(du_result, DOWN, buff=0.3)
        self.play(Write(dx_isolated))
        self.wait(2)
        
        # Puliamo lo schermo
        self.play(
            FadeOut(method_text), FadeOut(step1_text), FadeOut(substitution),
            FadeOut(step2_text), FadeOut(du_calc), FadeOut(du_result), FadeOut(dx_isolated)
        )
        
        # Passo 3: Sostituiamo
        subst_text = Text("Sostituiamo nell'integrale:", font_size=26)
        subst_text.next_to(problem, DOWN, buff=0.8)
        self.play(Write(subst_text))
        
        integral_subst = MathTex(r"\int", r"\sin(u)", r"\cdot", r"\frac{du}{2}")
        integral_subst.next_to(subst_text, DOWN, buff=0.4)
        self.play(Write(integral_subst))
        self.wait(2)
        
        # Semplifichiamo
        integral_simple = MathTex(r"\frac{1}{2}", r"\int", r"\sin(u)", r"\,du")
        integral_simple.next_to(integral_subst, DOWN, buff=0.4)
        self.play(Write(integral_simple))
        self.wait(2)
        
        # Puliamo
        self.play(FadeOut(subst_text), FadeOut(integral_subst))
        self.play(integral_simple.animate.shift(UP * 0.8))
        
        # Passo 4: Integriamo
        integrate_text = Text("Integriamo:", font_size=26)
        integrate_text.next_to(integral_simple, DOWN, buff=0.6)
        self.play(Write(integrate_text))
        
        # Ricordiamo la formula
        formula_reminder = MathTex(r"\int \sin(u)\,du = -\cos(u) + C", color=BLUE)
        formula_reminder.scale(0.8)
        formula_reminder.next_to(integrate_text, DOWN, buff=0.4)
        self.play(Write(formula_reminder))
        self.wait(2)
        
        # Risultato intermedio
        result_u = MathTex(r"\frac{1}{2}", r"\cdot", r"(-\cos(u))", r"+ C")
        result_u.next_to(formula_reminder, DOWN, buff=0.5)
        self.play(Write(result_u))
        self.wait(1.5)
        
        result_u_simple = MathTex(r"-\frac{1}{2}", r"\cos(u)", r"+ C")
        result_u_simple.next_to(result_u, DOWN, buff=0.4)
        self.play(Write(result_u_simple))
        self.wait(2)
        
        # Puliamo
        self.play(
            FadeOut(integrate_text), FadeOut(formula_reminder), 
            FadeOut(integral_simple), FadeOut(result_u)
        )
        self.play(result_u_simple.animate.shift(UP * 1.5))
        
        # Passo 5: Torniamo alla variabile x
        back_text = Text("Sostituiamo u = 2x:", font_size=26, color=YELLOW)
        back_text.next_to(result_u_simple, DOWN, buff=0.6)
        self.play(Write(back_text))
        self.wait(1)
        
        # Soluzione finale
        final_box = Rectangle(
            width=8, height=1.5, 
            color=GREEN, 
            fill_opacity=0.1,
            stroke_width=3
        )
        
        final_result = MathTex(
            r"\int \sin(2x)\,dx", "=", 
            r"-\frac{1}{2}\cos(2x)", "+", "C",
            color=GREEN
        )
        final_result.scale(1.3)
        final_result.next_to(back_text, DOWN, buff=0.6)
        
        final_box.move_to(final_result.get_center())
        
        self.play(Create(final_box))
        self.play(Write(final_result))
        self.wait(3)
        
        # Verifica (opzionale - derivata)
        self.play(
            FadeOut(problem), FadeOut(result_u_simple), 
            FadeOut(back_text), FadeOut(final_box), FadeOut(final_result),
            FadeOut(title)
        )
        
        verify_title = Text("Verifica (deriviamo il risultato):", font_size=32)
        verify_title.to_edge(UP)
        self.play(Write(verify_title))
        
        verify_start = MathTex(
            r"\frac{d}{dx}\left[-\frac{1}{2}\cos(2x)\right]"
        )
        verify_start.shift(UP)
        self.play(Write(verify_start))
        self.wait(1)
        
        verify_step1 = MathTex(
            r"= -\frac{1}{2} \cdot (-\sin(2x)) \cdot 2"
        )
        verify_step1.next_to(verify_start, DOWN, buff=0.5)
        self.play(Write(verify_step1))
        self.wait(1.5)
        
        verify_step2 = MathTex(r"= \sin(2x)", color=GREEN)
        verify_step2.scale(1.3)
        verify_step2.next_to(verify_step1, DOWN, buff=0.5)
        
        checkmark = MathTex(r"\checkmark", color=GREEN).scale(2)
        checkmark.next_to(verify_step2, RIGHT, buff=0.5)
        
        self.play(Write(verify_step2))
        self.play(FadeIn(checkmark, scale=0.5))
        self.wait(3)