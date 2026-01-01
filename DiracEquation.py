from manim import *

class DiracEquation(Scene):
    def construct(self):
        # Titolo
        title = Text("L'Equazione di Dirac", font_size=40, color=BLUE)
        subtitle = Text("Meccanica Quantistica Relativistica", font_size=24, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        
        # L'equazione di Dirac in forma compatta
        intro_text = Text("Formulata da Paul Dirac nel 1928", font_size=28)
        intro_text.next_to(subtitle, DOWN, buff=0.8)
        self.play(Write(intro_text))
        self.wait(1.5)
        self.play(FadeOut(intro_text))
        
        # Equazione principale
        dirac_eq = MathTex(
            r"(i\hbar\gamma^\mu\partial_\mu - mc)\psi = 0"
        )
        dirac_eq.scale(1.5)
        dirac_eq.shift(UP * 0.5)
        self.play(Write(dirac_eq))
        self.wait(3)
        
        # Forma alternativa più esplicita
        alt_text = Text("Forma esplicita:", font_size=26)
        alt_text.next_to(dirac_eq, DOWN, buff=0.8)
        self.play(Write(alt_text))
        
        dirac_explicit = MathTex(
            r"i\hbar\frac{\partial\psi}{\partial t} = ",
            r"\left(-i\hbar c\vec{\alpha}\cdot\vec{\nabla} + mc^2\beta\right)\psi"
        )
        dirac_explicit.next_to(alt_text, DOWN, buff=0.4)
        self.play(Write(dirac_explicit))
        self.wait(3)
        
        # Puliamo per mostrare i componenti
        self.play(
            FadeOut(alt_text), FadeOut(dirac_explicit),
            dirac_eq.animate.shift(UP * 1.5)
        )
        
        # Box per i componenti
        components_title = Text("Componenti dell'equazione:", font_size=28, color=YELLOW)
        components_title.next_to(dirac_eq, DOWN, buff=1)
        self.play(Write(components_title))
        self.wait(1)
        
        # Componente 1: i (unità immaginaria)
        comp1_eq = MathTex("i", color=RED).scale(1.2)
        comp1_text = Text("unità immaginaria", font_size=22)
        comp1_desc = Text("(caratteristica quantistica)", font_size=18, color=GRAY)
        
        comp1_group = VGroup(comp1_eq, comp1_text, comp1_desc)
        comp1_text.next_to(comp1_eq, RIGHT, buff=0.3)
        comp1_desc.next_to(comp1_text, DOWN, buff=0.2)
        comp1_group.arrange(DOWN, center=False, buff=0.15)
        comp1_group.next_to(components_title, DOWN, buff=0.5)
        comp1_group.to_edge(LEFT, buff=1)
        
        self.play(FadeIn(comp1_group))
        self.wait(2)
        
        # Componente 2: ℏ (costante di Planck ridotta)
        comp2_eq = MathTex(r"\hbar", color=GREEN).scale(1.2)
        comp2_text = Text("costante di Planck ridotta", font_size=22)
        comp2_desc = MathTex(r"\hbar = \frac{h}{2\pi} \approx 1.055 \times 10^{-34}\text{ J·s}", 
                            font_size=20, color=GRAY)
        
        comp2_group = VGroup(comp2_eq, comp2_text, comp2_desc)
        comp2_text.next_to(comp2_eq, RIGHT, buff=0.3)
        comp2_desc.next_to(comp2_text, DOWN, buff=0.2)
        comp2_group.arrange(DOWN, center=False, buff=0.15)
        comp2_group.next_to(comp1_group, DOWN, buff=0.4, aligned_edge=LEFT)
        
        self.play(FadeIn(comp2_group))
        self.wait(2)
        
        # Scroll - rimuoviamo i primi componenti
        self.play(FadeOut(comp1_group), FadeOut(comp2_group))
        
        # Componente 3: γ^μ (matrici di Dirac)
        comp3_eq = MathTex(r"\gamma^\mu", color=BLUE).scale(1.2)
        comp3_text = Text("matrici di Dirac (4×4)", font_size=22)
        comp3_desc = Text("descrivono lo spin relativistico", font_size=18, color=GRAY)
        
        comp3_group = VGroup(comp3_eq, comp3_text, comp3_desc)
        comp3_text.next_to(comp3_eq, RIGHT, buff=0.3)
        comp3_desc.next_to(comp3_text, DOWN, buff=0.2)
        comp3_group.arrange(DOWN, center=False, buff=0.15)
        comp3_group.next_to(components_title, DOWN, buff=0.5)
        comp3_group.to_edge(LEFT, buff=1)
        
        self.play(FadeIn(comp3_group))
        self.wait(2)
        
        # Componente 4: ∂_μ (derivata parziale)
        comp4_eq = MathTex(r"\partial_\mu", color=ORANGE).scale(1.2)
        comp4_text = Text("derivata spazio-temporale", font_size=22)
        comp4_desc = MathTex(r"\partial_\mu = \left(\frac{1}{c}\frac{\partial}{\partial t}, \vec{\nabla}\right)", 
                            font_size=20, color=GRAY)
        
        comp4_group = VGroup(comp4_eq, comp4_text, comp4_desc)
        comp4_text.next_to(comp4_eq, RIGHT, buff=0.3)
        comp4_desc.next_to(comp4_text, DOWN, buff=0.2)
        comp4_group.arrange(DOWN, center=False, buff=0.15)
        comp4_group.next_to(comp3_group, DOWN, buff=0.4, aligned_edge=LEFT)
        
        self.play(FadeIn(comp4_group))
        self.wait(2)
        
        # Scroll
        self.play(FadeOut(comp3_group), FadeOut(comp4_group))
        
        # Componente 5: m (massa)
        comp5_eq = MathTex("m", color=PURPLE).scale(1.2)
        comp5_text = Text("massa della particella", font_size=22)
        comp5_desc = Text("(es: elettrone, positrone)", font_size=18, color=GRAY)
        
        comp5_group = VGroup(comp5_eq, comp5_text, comp5_desc)
        comp5_text.next_to(comp5_eq, RIGHT, buff=0.3)
        comp5_desc.next_to(comp5_text, DOWN, buff=0.2)
        comp5_group.arrange(DOWN, center=False, buff=0.15)
        comp5_group.next_to(components_title, DOWN, buff=0.5)
        comp5_group.to_edge(LEFT, buff=1)
        
        self.play(FadeIn(comp5_group))
        self.wait(2)
        
        # Componente 6: c (velocità della luce)
        comp6_eq = MathTex("c", color=YELLOW).scale(1.2)
        comp6_text = Text("velocità della luce", font_size=22)
        comp6_desc = MathTex(r"c \approx 3 \times 10^8 \text{ m/s}", 
                            font_size=20, color=GRAY)
        
        comp6_group = VGroup(comp6_eq, comp6_text, comp6_desc)
        comp6_text.next_to(comp6_eq, RIGHT, buff=0.3)
        comp6_desc.next_to(comp6_text, DOWN, buff=0.2)
        comp6_group.arrange(DOWN, center=False, buff=0.15)
        comp6_group.next_to(comp5_group, DOWN, buff=0.4, aligned_edge=LEFT)
        
        self.play(FadeIn(comp6_group))
        self.wait(2)
        
        # Componente 7: ψ (funzione d'onda)
        comp7_eq = MathTex(r"\psi", color=TEAL).scale(1.2)
        comp7_text = Text("funzione d'onda (spinore)", font_size=22)
        comp7_desc = Text("descrive lo stato della particella", font_size=18, color=GRAY)
        
        comp7_group = VGroup(comp7_eq, comp7_text, comp7_desc)
        comp7_text.next_to(comp7_eq, RIGHT, buff=0.3)
        comp7_desc.next_to(comp7_text, DOWN, buff=0.2)
        comp7_group.arrange(DOWN, center=False, buff=0.15)
        comp7_group.next_to(comp6_group, DOWN, buff=0.4, aligned_edge=LEFT)
        
        self.play(FadeIn(comp7_group))
        self.wait(3)
        
        # Puliamo per il finale
        self.play(
            FadeOut(components_title),
            FadeOut(comp5_group), FadeOut(comp6_group), FadeOut(comp7_group)
        )
        
        # Significato dell'equazione
        self.play(dirac_eq.animate.shift(DOWN * 1))
        
        meaning_title = Text("Significato fisico:", font_size=30, color=YELLOW)
        meaning_title.next_to(dirac_eq, DOWN, buff=1)
        self.play(Write(meaning_title))
        
        meaning1 = Text("• Descrive particelle con spin 1/2", font_size=24)
        meaning1.next_to(meaning_title, DOWN, buff=0.5)
        meaning1.to_edge(LEFT, buff=1.5)
        self.play(FadeIn(meaning1, shift=RIGHT))
        self.wait(1.5)
        
        meaning2 = Text("• Unifica meccanica quantistica e relatività", font_size=24)
        meaning2.next_to(meaning1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeIn(meaning2, shift=RIGHT))
        self.wait(1.5)
        
        meaning3 = Text("• Predice l'esistenza dell'antimateria", font_size=24)
        meaning3.next_to(meaning2, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeIn(meaning3, shift=RIGHT))
        self.wait(1.5)
        
        meaning4 = Text("• Base della elettrodinamica quantistica (QED)", font_size=24)
        meaning4.next_to(meaning3, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeIn(meaning4, shift=RIGHT))
        self.wait(3)
        
        # Finale
        self.play(
            FadeOut(meaning_title), FadeOut(meaning1), 
            FadeOut(meaning2), FadeOut(meaning3), FadeOut(meaning4)
        )
        
        # Equazione finale con box
        final_box = Rectangle(
            width=10, height=1.8,
            color=BLUE,
            fill_opacity=0.1,
            stroke_width=4
        )
        
        self.play(dirac_eq.animate.scale(1.2).move_to(ORIGIN))
        final_box.move_to(dirac_eq.get_center())
        
        self.play(Create(final_box))
        
        final_text = Text("Paul Dirac, 1928", font_size=24, color=GRAY)
        final_text.next_to(final_box, DOWN, buff=0.5)
        self.play(FadeIn(final_text))
        
        self.wait(3)