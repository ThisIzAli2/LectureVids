from manim import *

# ---------- Global style ----------
config.frame_rate = 30
config.background_color = "#0f1117"

BG = "#0f1117"
FG = "#f5f5f5"
ACCENT = BLUE_C
ACCENT2 = YELLOW_C
ACCENT3 = GREEN_C

Tex.set_default(color=FG)
MathTex.set_default(color=FG)
Text.set_default(color=FG, font_size=34)


class GaussianIntegralClean(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ---------- Title ----------
        title = Text("The Gaussian Integral", font_size=46, weight=BOLD)
        formula = MathTex(r"I=\int_{-\infty}^{\infty} e^{-x^2}\,dx").scale(1.1)
        formula.set_color_by_tex("I", ACCENT)

        title_group = VGroup(title, formula).arrange(DOWN, buff=0.35)
        self.play(FadeIn(title, shift=UP), Write(formula), run_time=1.8)
        self.wait(1.2)
        self.play(FadeOut(title_group, shift=UP), run_time=0.8)

        # ---------- Step 1 ----------
        step1 = Text("Start with the integral", font_size=30)
        eq1 = MathTex(r"I=\int_{-\infty}^{\infty} e^{-x^2}\,dx").scale(1.15)
        eq1.set_color_by_tex("I", ACCENT)

        group1 = VGroup(step1, eq1).arrange(DOWN, buff=0.4)
        self.play(FadeIn(step1, shift=UP), Write(eq1), run_time=1.6)
        self.wait(1.2)

        # morph eq1 into squared expression, but remove step1 first
        self.play(FadeOut(step1, shift=UP), run_time=0.5)

        # ---------- Step 2 ----------
        eq2 = MathTex(
            r"I^2=",
            r"\left(\int_{-\infty}^{\infty} e^{-x^2}\,dx\right)",
            r"\left(\int_{-\infty}^{\infty} e^{-y^2}\,dy\right)"
        ).scale(0.92)
        eq2.set_color_by_tex("I^2", ACCENT)
        eq2.set_color_by_tex("x", ACCENT2)
        eq2.set_color_by_tex("y", ACCENT3)

        step2 = Text("Square the integral", font_size=30).to_edge(UP)

        self.play(FadeIn(step2, shift=UP), run_time=0.6)
        self.play(TransformMatchingTex(eq1, eq2), run_time=1.8)
        self.wait(1.2)

        # ---------- Step 3 ----------
        eq3 = MathTex(
            r"I^2=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}",
            r"e^{-(x^2+y^2)}",
            r"\,dx\,dy"
        ).scale(0.98)
        eq3.set_color_by_tex("I^2", ACCENT)
        eq3.set_color_by_tex("x", ACCENT2)
        eq3.set_color_by_tex("y", ACCENT3)

        self.play(
            FadeOut(step2, shift=UP),
            FadeIn(Text("Combine them into a double integral", font_size=30).to_edge(UP), shift=UP),
            TransformMatchingTex(eq2, eq3),
            run_time=1.8
        )
        current_step = self.mobjects[-2]  # the new top text may not be reliable by index in all cases

        # safer explicit reference
        self.clear()
        step3 = Text("Combine them into a double integral", font_size=30).to_edge(UP)
        eq3.move_to(ORIGIN)
        self.add(step3, eq3)
        self.wait(1.2)

        # ---------- Step 4 ----------
        plane = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=5,
            background_line_style={
                "stroke_color": GREY_B,
                "stroke_opacity": 0.25,
                "stroke_width": 1,
            },
            axis_config={"color": GREY_A},
        ).scale(0.8)

        circles = VGroup(*[
            Circle(radius=r * 0.55, color=ACCENT, stroke_opacity=0.45)
            for r in [1, 2, 3]
        ])

        plane_group = VGroup(plane, circles)
        circles.move_to(plane.get_center())
        plane_group.to_edge(LEFT).shift(DOWN * 0.3)

        radial_text = Text("The expression depends only on distance from the origin", font_size=26)
        radial_eq = MathTex(r"x^2+y^2=r^2").scale(1.0)
        radial_eq.set_color_by_tex("r", ACCENT)

        right_group = VGroup(radial_text, radial_eq).arrange(DOWN, buff=0.3)
        right_group.to_edge(RIGHT).shift(UP * 0.3)

        self.play(FadeOut(step3, shift=UP), FadeOut(eq3, shift=UP), run_time=0.7)

        step4 = Text("Interpret it over the entire plane", font_size=30).to_edge(UP)
        self.play(
            FadeIn(step4, shift=UP),
            FadeIn(plane, shift=LEFT),
            LaggedStart(*[Create(c) for c in circles], lag_ratio=0.15),
            FadeIn(right_group, shift=RIGHT),
            run_time=2.2
        )
        self.wait(1.4)

        # ---------- Step 5 ----------
        polar_text = Text("Switch to polar coordinates", font_size=30).to_edge(UP)
        polar_eq = MathTex(
            r"x=r\cos\theta,\quad y=r\sin\theta,\quad dx\,dy=r\,dr\,d\theta"
        ).scale(0.88)
        polar_eq.set_color_by_tex("r", ACCENT)

        eq4 = MathTex(
            r"I^2=",
            r"\int_{0}^{2\pi}\int_{0}^{\infty}",
            r"e^{-r^2}",
            r"r\,dr\,d\theta"
        ).scale(0.98)
        eq4.set_color_by_tex("I^2", ACCENT)
        eq4.set_color_by_tex("r", ACCENT2)

        next_group = VGroup(polar_eq, eq4).arrange(DOWN, buff=0.6)

        self.play(
            FadeOut(step4, shift=UP),
            FadeOut(plane_group, shift=LEFT),
            FadeOut(right_group, shift=RIGHT),
            run_time=0.8
        )
        self.play(FadeIn(polar_text, shift=UP), FadeIn(polar_eq, shift=UP), run_time=1.0)
        self.play(Write(eq4), run_time=1.6)
        self.wait(1.2)

        # ---------- Step 6 ----------
        step6 = Text("Separate the angular and radial parts", font_size=30).to_edge(UP)
        eq5 = MathTex(
            r"I^2=",
            r"\left(\int_{0}^{2\pi} d\theta\right)",
            r"\left(\int_{0}^{\infty} e^{-r^2}r\,dr\right)"
        ).scale(0.95)
        eq5.set_color_by_tex("I^2", ACCENT)
        eq5.set_color_by_tex("r", ACCENT2)

        eq6 = MathTex(
            r"I^2=",
            r"2\pi",
            r"\int_{0}^{\infty} e^{-r^2}r\,dr"
        ).scale(1.0)
        eq6.set_color_by_tex("I^2", ACCENT)
        eq6.set_color_by_tex("2\pi", ACCENT3)
        eq6.set_color_by_tex("r", ACCENT2)

        self.play(
            FadeOut(polar_text, shift=UP),
            FadeIn(step6, shift=UP),
            FadeOut(polar_eq, shift=UP),
            TransformMatchingTex(eq4, eq5),
            run_time=1.8
        )
        self.wait(1.0)

        self.play(TransformMatchingTex(eq5, eq6), run_time=1.5)
        self.wait(1.2)

        # ---------- Step 7 ----------
        step7 = Text("Use the substitution  u=r^2", font_size=30).to_edge(UP)
        sub_eq = MathTex(r"u=r^2,\qquad du=2r\,dr").scale(0.95)
        sub_eq.set_color_by_tex("u", ACCENT3)

        eq7 = MathTex(
            r"I^2=",
            r"2\pi\cdot\frac{1}{2}\int_{0}^{\infty} e^{-u}\,du"
        ).scale(1.0)
        eq7.set_color_by_tex("I^2", ACCENT)
        eq7.set_color_by_tex("u", ACCENT3)
        eq7.set_color_by_tex("2\pi", ACCENT2)

        eq8 = MathTex(r"I^2=\pi").scale(1.25)
        eq8.set_color_by_tex("I^2", ACCENT)

        self.play(
            FadeOut(step6, shift=UP),
            FadeIn(step7, shift=UP),
            FadeIn(sub_eq, shift=UP),
            run_time=0.9
        )
        self.play(TransformMatchingTex(eq6, eq7), run_time=1.7)
        self.wait(1.0)

        self.play(FadeOut(sub_eq, shift=UP), run_time=0.6)
        self.play(TransformMatchingTex(eq7, eq8), run_time=1.5)
        self.wait(1.2)

        # ---------- Final ----------
        final_step = Text("Take the positive square root", font_size=30).to_edge(UP)
        final_eq = MathTex(r"I=\sqrt{\pi}").scale(1.55)
        final_eq.set_color(ACCENT)

        final_box = SurroundingRectangle(final_eq, color=ACCENT, buff=0.22)

        self.play(FadeOut(step7, shift=UP), FadeIn(final_step, shift=UP), run_time=0.8)
        self.play(TransformMatchingTex(eq8, final_eq), run_time=1.5)
        self.play(Create(final_box), run_time=0.8)
        self.wait(2)

        closing = Text(
            "That is the famous Gaussian integral.",
            font_size=28
        ).to_edge(DOWN)

        self.play(FadeIn(closing, shift=UP), run_time=0.8)
        self.wait(2)