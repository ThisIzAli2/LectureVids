from manim import *

# ---------- Global style ----------
config.background_color = "#0f1117"

FG = "#f5f5f5"
ACCENT = BLUE_C
ACCENT2 = YELLOW_C
ACCENT3 = GREEN_C
SOFT_RED = "#ff6b6b"

Tex.set_default(color=FG)
MathTex.set_default(color=FG)
Text.set_default(color=FG, font_size=34)


class GaussianIntegral(Scene):
    def construct(self):
        self.camera.background_color = "#0f1117"

        # -------------------------------------------------
        # Title card
        # -------------------------------------------------
        title = Text("The Gaussian Integral", font_size=44, weight=BOLD)
        formula = MathTex(r"I=\int_{-\infty}^{\infty} e^{-x^2}\,dx").scale(1.1)
        formula.set_color_by_tex("I", ACCENT)

        title_group = VGroup(title, formula).arrange(DOWN, buff=0.4)
        self.play(FadeIn(title, shift=UP), Write(formula), run_time=2)
        self.wait(1)
        self.play(title_group.animate.to_edge(UP), run_time=1)

        # -------------------------------------------------
        # Step 1: Define the integral
        # -------------------------------------------------
        step1 = Text("Start with the integral we want to compute:", font_size=30)
        step1.next_to(title_group, DOWN, buff=0.7)

        eq1 = MathTex(r"I=\int_{-\infty}^{\infty} e^{-x^2}\,dx").scale(1.0)
        eq1.set_color_by_tex("I", ACCENT)
        eq1.next_to(step1, DOWN, buff=0.45)

        self.play(FadeIn(step1, shift=UP), Write(eq1), run_time=1.8)
        self.wait(1)

        # -------------------------------------------------
        # Step 2: Square it
        # -------------------------------------------------
        step2 = Text("Instead of evaluating it directly, square it.", font_size=30)
        step2.next_to(eq1, DOWN, buff=0.9)

        eq2 = MathTex(
            r"I^2=",
            r"\left(\int_{-\infty}^{\infty} e^{-x^2}\,dx\right)",
            r"\left(\int_{-\infty}^{\infty} e^{-y^2}\,dy\right)"
        ).scale(0.9)
        eq2.set_color_by_tex("I^2", ACCENT)
        eq2.set_color_by_tex("x", ACCENT2)
        eq2.set_color_by_tex("y", ACCENT3)
        eq2.next_to(step2, DOWN, buff=0.45)

        self.play(FadeIn(step2, shift=UP), Write(eq2), run_time=2)
        self.wait(1)

        # Combine exponentials
        eq3 = MathTex(
            r"I^2=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}",
            r"e^{-(x^2+y^2)}",
            r"\,dx\,dy"
        ).scale(0.95)
        eq3.set_color_by_tex("I^2", ACCENT)
        eq3.set_color_by_tex("x", ACCENT2)
        eq3.set_color_by_tex("y", ACCENT3)
        eq3.next_to(eq2, DOWN, buff=0.6)

        self.play(Write(eq3), run_time=1.8)
        self.wait(1)

        # -------------------------------------------------
        # Step 3: Show the plane and radial symmetry
        # -------------------------------------------------
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

        plane.to_edge(LEFT).shift(DOWN * 0.6)

        circles = VGroup(*[
            Circle(radius=r * 0.55, color=ACCENT, stroke_opacity=0.45)
            for r in [1, 2, 3]
        ])
        circles.move_to(plane.get_center())

        symmetry_text = Text("Now this becomes a 2D integral over the plane.", font_size=28)
        symmetry_text.to_edge(RIGHT).shift(UP * 1.2)

        radial_text = Text("The integrand depends only on", font_size=28)
        radial_eq = MathTex(r"x^2+y^2=r^2").scale(1.0)
        radial_eq.set_color_by_tex("r", ACCENT)
        radial_group = VGroup(radial_text, radial_eq).arrange(DOWN, buff=0.25)
        radial_group.next_to(symmetry_text, DOWN, buff=0.5)

        box_eq3 = SurroundingRectangle(eq3, color=ACCENT, buff=0.15)

        self.play(Create(box_eq3), run_time=1)
        self.play(
            FadeIn(plane, shift=LEFT),
            LaggedStart(*[Create(c) for c in circles], lag_ratio=0.2),
            FadeIn(symmetry_text, shift=RIGHT),
            FadeIn(radial_group, shift=RIGHT),
            run_time=2.2
        )
        self.wait(1.5)

        # -------------------------------------------------
        # Step 4: Polar coordinates
        # -------------------------------------------------
        polar_text = Text("Switch to polar coordinates:", font_size=30)
        polar_eq = MathTex(
            r"x=r\cos\theta,\quad y=r\sin\theta,\quad dx\,dy=r\,dr\,d\theta"
        ).scale(0.85)
        polar_eq.set_color_by_tex("r", ACCENT)

        polar_group = VGroup(polar_text, polar_eq).arrange(DOWN, buff=0.35)
        polar_group.next_to(radial_group, DOWN, buff=0.7)

        self.play(FadeIn(polar_group, shift=UP), run_time=1.6)
        self.wait(1)

        eq4 = MathTex(
            r"I^2=",
            r"\int_{0}^{2\pi}\int_{0}^{\infty}",
            r"e^{-r^2}",
            r"r\,dr\,d\theta"
        ).scale(0.95)
        eq4.set_color_by_tex("I^2", ACCENT)
        eq4.set_color_by_tex("r", ACCENT2)
        eq4.to_edge(RIGHT).shift(DOWN * 0.6)

        self.play(Write(eq4), run_time=1.8)
        self.wait(1)

        # -------------------------------------------------
        # Step 5: Separate integrals
        # -------------------------------------------------
        eq5 = MathTex(
            r"I^2=",
            r"\left(\int_{0}^{2\pi} d\theta\right)",
            r"\left(\int_{0}^{\infty} e^{-r^2}r\,dr\right)"
        ).scale(0.95)
        eq5.set_color_by_tex("I^2", ACCENT)
        eq5.set_color_by_tex("r", ACCENT2)
        eq5.move_to(eq4)

        self.play(TransformMatchingTex(eq4, eq5), run_time=1.8)
        self.wait(1)

        eq6 = MathTex(
            r"I^2=",
            r"2\pi",
            r"\int_{0}^{\infty} e^{-r^2}r\,dr"
        ).scale(0.98)
        eq6.set_color_by_tex("I^2", ACCENT)
        eq6.set_color_by_tex("2\pi", ACCENT3)
        eq6.move_to(eq5)

        self.play(TransformMatchingTex(eq5, eq6), run_time=1.5)
        self.wait(1)

        # -------------------------------------------------
        # Step 6: u-substitution
        # -------------------------------------------------
        u_text = Text("Use the substitution", font_size=30)
        u_eq = MathTex(r"u=r^2,\quad du=2r\,dr").scale(0.95)
        u_eq.set_color_by_tex("u", ACCENT3)
        u_group = VGroup(u_text, u_eq).arrange(DOWN, buff=0.3)
        u_group.next_to(eq6, DOWN, buff=0.7)

        self.play(FadeIn(u_group, shift=UP), run_time=1.5)
        self.wait(1)

        eq7 = MathTex(
            r"I^2=",
            r"2\pi",
            r"\cdot",
            r"\frac{1}{2}\int_{0}^{\infty} e^{-u}\,du"
        ).scale(0.95)
        eq7.set_color_by_tex("I^2", ACCENT)
        eq7.set_color_by_tex("u", ACCENT3)
        eq7.move_to(eq6)

        self.play(TransformMatchingTex(eq6, eq7), run_time=1.8)
        self.wait(1)

        eq8 = MathTex(
            r"I^2=",
            r"2\pi",
            r"\cdot",
            r"\frac{1}{2}",
            r"\cdot",
            r"1"
        ).scale(1.0)
        eq8.set_color_by_tex("I^2", ACCENT)
        eq8.set_color_by_tex("2\pi", ACCENT3)
        eq8.move_to(eq7)

        self.play(TransformMatchingTex(eq7, eq8), run_time=1.5)
        self.wait(1)

        eq9 = MathTex(r"I^2=\pi").scale(1.2)
        eq9.set_color_by_tex("I^2", ACCENT)
        eq9.move_to(eq8)

        self.play(TransformMatchingTex(eq8, eq9), run_time=1.4)
        self.wait(1)

        # -------------------------------------------------
        # Step 7: Final answer
        # -------------------------------------------------
        final_eq = MathTex(
            r"I=\sqrt{\pi}"
        ).scale(1.5)
        final_eq.set_color(ACCENT)

        final_box = SurroundingRectangle(final_eq, color=ACCENT, buff=0.25)
        final_text = Text("Therefore,", font_size=30)

        final_group = VGroup(final_text, final_eq).arrange(DOWN, buff=0.35)
        final_group.move_to(RIGHT * 3 + DOWN * 1.4)

        self.play(FadeOut(u_group), FadeOut(eq9), run_time=0.8)
        self.play(FadeIn(final_text, shift=UP), Write(final_eq), run_time=1.8)
        self.play(Create(final_box), run_time=1)
        self.wait(2)

        # -------------------------------------------------
        # Ending
        # -------------------------------------------------
        closing = Text("A beautiful trick: square first, then switch to polar.", font_size=28)
        closing.to_edge(DOWN)

        self.play(FadeIn(closing, shift=UP), run_time=1.2)
        self.wait(2)