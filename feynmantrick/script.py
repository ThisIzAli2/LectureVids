from manim import *
import numpy as np

class SincIntegral(Scene):
    def construct(self):
        # Title
        title = MathTex(r"\int_{0}^{\infty} \frac{\sin x}{x} \, dx")
        title.to_edge(UP)
        self.play(Write(title))

        # Axes
        axes = Axes(
            x_range=[0, 20, 5],
            y_range=[-0.5, 1.5, 0.5],
            x_length=10,
            y_length=4,
            axis_config={"color": BLUE},
        ).shift(DOWN)

        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        self.play(Create(axes), Write(labels))

        # Define sinc function (handle x=0 separately)
        def sinc(x):
            return np.sin(x) / x if x != 0 else 1

        graph = axes.plot(sinc, color=YELLOW, x_range=[0, 20])

        self.play(Create(graph), run_time=3)

        # Shade area under curve
        area = axes.get_area(graph, x_range=[0, 20], color=BLUE, opacity=0.5)

        self.play(FadeIn(area), run_time=2)

        # Highlight oscillation decay
        note = Text("Oscillations decay slowly", font_size=28)
        note.next_to(axes, DOWN)
        self.play(Write(note))

        self.wait(2)
        self.play(FadeOut(note))

        # Final result
        result = MathTex(r"= \frac{\pi}{2}")
        result.next_to(title, RIGHT)

        self.play(Write(result), run_time=2)

        self.wait(3)