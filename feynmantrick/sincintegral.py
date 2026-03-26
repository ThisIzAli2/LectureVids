from manim import *
import numpy as np

class SincGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-10, 10],
            y_range=[-0.5, 1.5],
            x_length=10,
            y_length=4,
            tips=False,
        )

        # Define safe sinc function
        def sinc(x):
            return np.sin(x)/x if x != 0 else 1

        graph = axes.plot(
            sinc,
            x_range=[-10, 10],
            color=YELLOW,
        )

        label = MathTex(r"\frac{\sin x}{x}").to_corner(UR)

        self.play(Create(axes))
        self.play(Create(graph), Write(label))
        self.wait()