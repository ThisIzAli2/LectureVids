from manim import *

# -----------------------------
# Global style
# -----------------------------
config.background_color = "#0f1117"
config.frame_rate = 30

FG = "#f5f5f5"
ACCENT = BLUE_C
ACCENT2 = YELLOW_C
ACCENT3 = GREEN_C
SOFT_RED = "#ff6b6b"

Tex.set_default(color=FG)
MathTex.set_default(color=FG)
Text.set_default(color=FG, font="Arial")

# -----------------------------
# Helper base scene
# -----------------------------
class StyledScene(Scene):
    def make_title(self, title, subtitle=None):
        title_tex = Tex(title, font_size=54, color=FG)
        if subtitle:
            sub = Tex(subtitle, font_size=28, color=GRAY_B)
            group = VGroup(title_tex, sub).arrange(DOWN, buff=0.25)
        else:
            group = VGroup(title_tex)
        group.to_edge(UP)
        return group

    def glow_box(self, mob, color=ACCENT, buff=0.25):
        return SurroundingRectangle(
            mob,
            buff=buff,
            color=color,
            stroke_width=2.5,
            corner_radius=0.15,
        )

# -----------------------------
# Main video
# -----------------------------
class SinxOverXVideo(StyledScene):
    def construct(self):
        self.intro_scene()
        self.parameter_scene()
        self.differentiate_scene()
        self.solve_derivative_scene()
        self.integrate_back_scene()
        self.find_constant_scene()
        self.final_scene()

    def intro_scene(self):
        title = self.make_title("The famous integral", "Solved with the Feynman trick")
        integral = MathTex(
            r"\int_0^\infty \frac{\sin x}{x}\,dx \;=\; ?",
            font_size=68
        )
        integral.set_color_by_tex(r"\frac{\sin x}{x}", ACCENT)

        self.play(FadeIn(title, shift=UP), run_time=1.0)
        self.play(Write(integral), run_time=2.0)
        self.wait(1)

        note = Tex(
            "Direct attack is hard... so we add a parameter.",
            font_size=32,
            color=GRAY_A
        ).next_to(integral, DOWN, buff=0.6)

        self.play(FadeIn(note, shift=UP), run_time=1.0)
        self.wait(1.2)

        self.play(
            FadeOut(note),
            integral.animate.scale(0.8).to_edge(UP).shift(DOWN * 0.9),
            FadeOut(title),
            run_time=1.0
        )

        self.current_integral = integral

    def parameter_scene(self):
        definition = MathTex(
            r"I(t)=\int_0^\infty e^{-tx}\frac{\sin x}{x}\,dx,\qquad t>0",
            font_size=56
        )
        definition.set_color_by_tex(r"I(t)", ACCENT2)
        definition.set_color_by_tex(r"e^{-tx}", ACCENT3)

        arrow = Arrow(
            self.current_integral.get_bottom(),
            definition.get_top(),
            buff=0.2,
            color=GRAY_B
        )

        self.play(GrowArrow(arrow), run_time=0.8)
        self.play(TransformMatchingTex(self.current_integral.copy(), definition), run_time=1.8)
        self.wait(0.8)

        box = self.glow_box(definition, color=ACCENT3)
        self.play(Create(box), run_time=0.8)

        caption = Tex(
            "The exponential makes the integral well-behaved.",
            font_size=30,
            color=GRAY_A
        ).next_to(definition, DOWN, buff=0.5)

        self.play(FadeIn(caption, shift=UP), run_time=0.8)
        self.wait(1.3)

        self.play(
            FadeOut(arrow),
            FadeOut(caption),
            definition.animate.to_edge(UP).shift(DOWN * 0.7),
            box.animate.move_to(definition),
            run_time=1.0
        )

        self.definition = definition
        self.definition_box = box

    def differentiate_scene(self):
        step1 = MathTex(
            r"I'(t)=\frac{d}{dt}\int_0^\infty e^{-tx}\frac{\sin x}{x}\,dx",
            font_size=50
        )
        step2 = MathTex(
            r"I'(t)=\int_0^\infty \frac{\partial}{\partial t}\left(e^{-tx}\frac{\sin x}{x}\right)\,dx",
            font_size=50
        )
        step3 = MathTex(
            r"I'(t)=\int_0^\infty \left(-x e^{-tx}\right)\frac{\sin x}{x}\,dx",
            font_size=50
        )
        step4 = MathTex(
            r"I'(t)=-\int_0^\infty e^{-tx}\sin x\,dx",
            font_size=56
        )

        for mob in [step1, step2, step3, step4]:
            mob.set_color_by_tex(r"I'(t)", ACCENT2)
            mob.set_color_by_tex(r"e^{-tx}", ACCENT3)
            mob.move_to(ORIGIN + DOWN * 0.3)

        explain = Tex(
            "Differentiate under the integral sign.",
            font_size=30,
            color=GRAY_A
        ).next_to(step1, DOWN, buff=0.5)

        self.play(Write(step1), FadeIn(explain, shift=UP), run_time=1.6)
        self.wait(0.8)

        self.play(TransformMatchingTex(step1, step2), run_time=1.4)
        self.wait(0.8)

        self.play(TransformMatchingTex(step2, step3), run_time=1.4)
        self.wait(0.8)

        cancel_x = Tex("The $x$ cancels", font_size=28, color=SOFT_RED).next_to(step3, DOWN, buff=0.45)
        self.play(FadeIn(cancel_x, shift=UP), run_time=0.7)
        self.wait(0.7)

        self.play(
            FadeOut(cancel_x),
            TransformMatchingTex(step3, step4),
            run_time=1.4
        )
        self.wait(1.0)

        self.play(FadeOut(explain), run_time=0.5)
        self.derivative_eq = step4

    def solve_derivative_scene(self):
        known = MathTex(
            r"\int_0^\infty e^{-tx}\sin x\,dx=\frac{1}{1+t^2}",
            font_size=56
        )
        known.set_color_by_tex(r"e^{-tx}", ACCENT3)
        known.set_color_by_tex(r"\frac{1}{1+t^2}", ACCENT)

        implies = MathTex(
            r"I'(t)=-\frac{1}{1+t^2}",
            font_size=62
        )
        implies.set_color_by_tex(r"I'(t)", ACCENT2)
        implies.set_color_by_tex(r"\frac{1}{1+t^2}", ACCENT)

        known.next_to(self.derivative_eq, DOWN, buff=0.8)
        implies.move_to(self.derivative_eq)

        self.play(FadeIn(known, shift=UP), run_time=1.0)
        self.wait(1.0)

        self.play(
            FadeOut(known),
            TransformMatchingTex(self.derivative_eq, implies),
            run_time=1.4
        )
        self.wait(1.2)

        self.derivative_eq = implies

    def integrate_back_scene(self):
        int_back = MathTex(
            r"I(t)= -\int \frac{1}{1+t^2}\,dt",
            font_size=58
        )
        solved = MathTex(
            r"I(t)=C-\arctan t",
            font_size=62
        )
        solved.set_color_by_tex(r"I(t)", ACCENT2)
        solved.set_color_by_tex(r"\arctan t", ACCENT)

        int_back.move_to(self.derivative_eq)
        solved.move_to(self.derivative_eq)

        self.play(TransformMatchingTex(self.derivative_eq, int_back), run_time=1.2)
        self.wait(0.8)

        self.play(TransformMatchingTex(int_back, solved), run_time=1.4)
        self.wait(1.2)

        box = self.glow_box(solved, color=ACCENT2)
        self.play(Create(box), run_time=0.8)
        self.wait(0.8)

        self.play(FadeOut(box), run_time=0.5)
        self.general_solution = solved

    def find_constant_scene(self):
        limit1 = MathTex(
            r"\lim_{t\to\infty} I(t)=\lim_{t\to\infty}\int_0^\infty e^{-tx}\frac{\sin x}{x}\,dx = 0",
            font_size=44
        )
        limit2 = MathTex(
            r"\lim_{t\to\infty}\left(C-\arctan t\right)=0",
            font_size=54
        )
        limit3 = MathTex(
            r"C-\frac{\pi}{2}=0",
            font_size=60
        )
        limit4 = MathTex(
            r"C=\frac{\pi}{2}",
            font_size=64
        )

        for mob in [limit1, limit2, limit3, limit4]:
            mob.move_to(ORIGIN + DOWN * 0.4)

        limit4.set_color_by_tex(r"\frac{\pi}{2}", ACCENT)

        self.play(
            self.general_solution.animate.to_edge(UP).shift(DOWN * 0.6),
            run_time=0.8
        )

        self.play(Write(limit1), run_time=1.6)
        self.wait(1.0)

        self.play(TransformMatchingTex(limit1, limit2), run_time=1.4)
        self.wait(0.8)

        self.play(TransformMatchingTex(limit2, limit3), run_time=1.0)
        self.wait(0.8)

        self.play(TransformMatchingTex(limit3, limit4), run_time=1.0)
        self.wait(1.0)

        self.constant_eq = limit4

    def final_scene(self):
        substitute = MathTex(
            r"I(t)=\frac{\pi}{2}-\arctan t",
            font_size=60
        )
        final1 = MathTex(
            r"I(0)=\frac{\pi}{2}-\arctan(0)=\frac{\pi}{2}",
            font_size=58
        )
        final2 = MathTex(
            r"\int_0^\infty \frac{\sin x}{x}\,dx=\frac{\pi}{2}",
            font_size=72
        )

        substitute.set_color_by_tex(r"I(t)", ACCENT2)
        substitute.set_color_by_tex(r"\frac{\pi}{2}", ACCENT)
        substitute.set_color_by_tex(r"\arctan t", ACCENT3)

        final1.set_color_by_tex(r"I(0)", ACCENT2)
        final1.set_color_by_tex(r"\frac{\pi}{2}", ACCENT)

        final2.set_color_by_tex(r"\frac{\sin x}{x}", ACCENT3)
        final2.set_color_by_tex(r"\frac{\pi}{2}", ACCENT)

        substitute.move_to(ORIGIN + UP * 0.8)
        final1.move_to(ORIGIN)
        final2.move_to(ORIGIN)

        self.play(
            FadeOut(self.general_solution),
            FadeOut(self.constant_eq),
            FadeIn(substitute, shift=UP),
            run_time=1.0
        )
        self.wait(0.8)

        self.play(FadeIn(final1, shift=UP), run_time=1.0)
        self.wait(1.0)

        self.play(
            FadeOut(substitute),
            FadeOut(final1),
            FadeIn(final2, scale=0.9),
            run_time=1.2
        )

        final_box = self.glow_box(final2, color=ACCENT, buff=0.3)
        self.play(Create(final_box), run_time=0.8)
        self.wait(2)

        outro = Tex(
            "That is the Feynman trick.",
            font_size=30,
            color=GRAY_A
        ).next_to(final2, DOWN, buff=0.6)

        self.play(FadeIn(outro, shift=UP), run_time=0.8)
        self.wait(2)