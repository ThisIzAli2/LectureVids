from manim import *

# ---------- Global style ----------
config.frame_rate = 30

BG = "#0f1117"
FG = "#e8e6e3"
ACCENT = BLUE_C
ACCENT2 = YELLOW_C
ACCENT3 = GREEN_C

Tex.set_default(color=FG)
MathTex.set_default(color=FG)
Text.set_default(color=FG, font_size=36)

class BaseScene(Scene):
    def setup(self):
        self.camera.background_color = BG

    def title_card(self, title_tex, subtitle=None):
        title = MathTex(title_tex).scale(1.15)
        if subtitle:
            sub = Text(subtitle, font_size=30).next_to(title, DOWN, buff=0.4)
            group = VGroup(title, sub)
        else:
            group = VGroup(title)

        self.play(FadeIn(group, shift=UP), run_time=1.2)
        self.wait(0.6)
        return group
    
from manim import rate_functions

class IntegralIntro(BaseScene):
    def construct(self):
        title_group = self.title_card(
            r"\int_0^1 \frac{\arctan x}{x}\,dx",
            subtitle="A clean Feynman-style setup"
        )

        self.play(title_group.animate.scale(0.72).to_edge(UP), run_time=1)

        eq1 = MathTex(
            r"I", r"=", r"\int_0^1 \frac{\arctan x}{x}\,dx"
        ).scale(1.0)
        eq1[0].set_color(ACCENT2)
        eq1[2].set_color(ACCENT)
        self.play(Write(eq1), run_time=1.6)
        self.wait(0.5)

        box = SurroundingRectangle(eq1[2], color=ACCENT, buff=0.18)
        self.play(Create(box), run_time=0.8)
        self.wait(0.4)

        eq2 = MathTex(
            r"\arctan x", r"=", r"\int_0^x \frac{1}{1+t^2}\,dt"
        ).scale(0.95)
        eq2.next_to(eq1, DOWN, buff=1.0)
        eq2[0].set_color(ACCENT2)
        eq2[2].set_color(ACCENT3)

        arrow = Arrow(
            box.get_bottom(),
            eq2.get_top(),
            buff=0.15,
            color=FG,
            stroke_width=4
        )

        self.play(GrowArrow(arrow), FadeIn(eq2, shift=UP), run_time=1.2)
        self.wait(1)

        eq3 = MathTex(
            r"I",
            r"=",
            r"\int_0^1 \frac{1}{x}\left(\int_0^x \frac{1}{1+t^2}\,dt\right)dx"
        ).scale(0.88)
        eq3[0].set_color(ACCENT2)
        eq3[2].set_color(ACCENT3)
        eq3.next_to(eq2, DOWN, buff=0.9)

        self.play(ReplacementTransform(eq1.copy(), eq3[:2]), run_time=1.0)
        self.play(Write(eq3[2]), run_time=2.0)
        self.wait(1)

        brace = Brace(eq3[2], DOWN)
        note = Text("Now switch the order of integration", font_size=28)
        note.next_to(brace, DOWN, buff=0.2)

        self.play(GrowFromCenter(brace), FadeIn(note), run_time=1)
        self.wait(1.5)

        fade_group = VGroup(eq2, arrow, box, brace, note)
        self.play(FadeOut(fade_group), run_time=0.8)

        region_text = MathTex(
            r"0 \le t \le x \le 1"
        ).scale(1.0).set_color(ACCENT)
        region_text.next_to(eq3, DOWN, buff=0.8)

        self.play(FadeIn(region_text, shift=UP), run_time=1)
        self.wait(1)

        eq4 = MathTex(
            r"I",
            r"=",
            r"\int_0^1 \left(\int_t^1 \frac{1}{x(1+t^2)}\,dx\right)dt"
        ).scale(0.88)
        eq4[0].set_color(ACCENT2)
        eq4[2].set_color(ACCENT3)
        eq4.move_to(eq3)

        self.play(
            TransformMatchingTex(eq3, eq4, path_arc=PI/4),
            FadeOut(region_text),
            run_time=2.0
        )
        self.wait(1)

        eq5 = MathTex(
            r"I",
            r"=",
            r"\int_0^1 \frac{1}{1+t^2}\left(\int_t^1 \frac{1}{x}\,dx\right)dt"
        ).scale(0.88)
        eq5[0].set_color(ACCENT2)
        eq5[2].set_color(ACCENT3)
        eq5.move_to(eq4)

        self.play(TransformMatchingTex(eq4, eq5), run_time=1.8)
        self.wait(1)

        inner = MathTex(
            r"\int_t^1 \frac{1}{x}\,dx",
            r"=",
            r"-\ln t"
        ).scale(0.95)
        inner.next_to(eq5, DOWN, buff=0.9)
        inner[0].set_color(ACCENT)
        inner[2].set_color(ACCENT2)

        self.play(FadeIn(inner, shift=UP), run_time=1.2)
        self.wait(1)

        eq6 = MathTex(
            r"I",
            r"=",
            r"\int_0^1 \frac{-\ln t}{1+t^2}\,dt"
        ).scale(1.0)
        eq6[0].set_color(ACCENT2)
        eq6[2].set_color(ACCENT)

        eq6.move_to(eq5)

        self.play(
            FadeOut(inner),
            TransformMatchingTex(eq5, eq6),
            run_time=1.8
        )
        self.wait(1)

        final_box = SurroundingRectangle(eq6, color=ACCENT2, buff=0.2)
        self.play(Create(final_box), run_time=0.8)
        self.wait(2)