from manimlib import *
import numpy as np

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

class Kuramoto(Scene):
    def construct(self):

        kuramoto = "$\\dot\\theta_{n}=\\omega_{n} + \\frac{K}{N} \\sum_{m=0}^{N} \\sin(\\theta_{m}-\\theta_{n})$"
        text = Write(TexText(kuramoto, font_size=100),run_time=10)
        self.play(text)
        self.wait(3)

class ExplanationTex(Scene):
    def construct(self):


        lines = VGroup(
            Tex("{\\theta} = {0^{\\circ}}", font_size=100),
            Tex("{\\theta} = {180^{\\circ}}", font_size=100),
            # TexText("$\\theta = 0$", font_size=100),
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)

        text = Write(lines, run_time=10)
        self.play(text)
        self.wait(1)
        self.play(FadeOut(lines))
