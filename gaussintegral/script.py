from manim import *
import numpy as np

class GaussianIntegral(Scene):
    def construct(self):
        # Title
        title = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2}\,dx")
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Axes
        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[0, 1.2, 0.2],
            x_length=10,
            y_length=4.5,
            axis_config={"include_numbers": True},
            tips=False,
        ).shift(DOWN * 0.3)

        labels = axes.get_axis_labels(
            x_label=MathTex("x"),
            y_label=MathTex("y")
        )

        self.play(Create(axes), Write(labels))
        self.wait(0.5)

        # Gaussian curve
        graph = axes.plot(
            lambda x: np.exp(-x**2),
            x_range=[-3.5, 3.5],
            color=YELLOW,
            stroke_width=4,
        )

        graph_label = MathTex(r"y=e^{-x^2}", color=YELLOW).scale(0.8)
        graph_label.next_to(axes, RIGHT).shift(UP * 1.5)

        self.play(Create(graph), FadeIn(graph_label))
        self.wait(1)

        # Area under the curve
        area = axes.get_area(
            graph,
            x_range=[-3.5, 3.5],
            color=BLUE,
            opacity=0.45
        )

        self.play(FadeIn(area), run_time=2)
        self.wait(1)

        # Symmetry note
        symmetry_text = Text("Symmetric bell-shaped curve", font_size=28)
        symmetry_text.next_to(axes, DOWN)
        self.play(Write(symmetry_text))
        self.wait(1.5)
        self.play(FadeOut(symmetry_text))

        # Result
        result = MathTex(r"= \sqrt{\pi}")
        result.next_to(title, RIGHT)

        box = SurroundingRectangle(result, color=GREEN, buff=0.15)

        self.play(Write(result))
        self.play(Create(box))
        self.wait(3)