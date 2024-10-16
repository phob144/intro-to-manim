from manim import *

class SumOfOddNumbers(Scene):
    def construct(self):
        # your code here
###
from manim import *

class SumOfOddNumbers(Scene):
    def construct(self):
        square = Square()

        self.add(square)
###
from manim import *

class SumOfOddNumbers(Scene):
    def construct(self):
        square = Square(1)

        height_label = MathTex("1")
        height_label.shift(LEFT)
        width_label = MathTex("1")
        width_label.shift(UP)

        self.add(square, height_label, width_label)
###
from manim import *

class SumOfOddNumbers(Scene):
    def construct(self):
        # ...
        self.add(square, height_label, width_label)

        height_label_2 = MathTex("2")
        height_label_2.shift(LEFT + 0.5 * DOWN)
        width_label_2 = MathTex("2")
        width_label_2.shift(UP + 0.5 * RIGHT)

        group = VGroup()
        group.add(square.copy())
        
        self.play(square.animate.shift(RIGHT + DOWN))

        extra_squares = VGroup()
        extra_squares.add(square.copy().shift(RIGHT))
        extra_squares.add(square.copy().shift(DOWN))
        group.add(extra_squares)

        self.play(
            FadeIn(extra_squares),
            ReplacementTransform(height_label, height_label_2),
            ReplacementTransform(width_label, width_label_2),
        )
###
from manim import *

class SumOfOddNumbers(Scene):
    def construct(self):
        # ...
        height_label_3 = MathTex("3")
        height_label_3.shift(LEFT + 1 * DOWN)
        width_label_3 = MathTex("3")
        width_label_3.shift(UP + 1 * RIGHT)

        group_2 = VGroup()
        group_2.add(group.copy())

        self.play(group_2.animate.shift(RIGHT + DOWN))

        extra_squares_2 = VGroup()
        extra_squares_2.add(square.copy().shift(2 * RIGHT))
        extra_squares_2.add(square.copy().shift(2 * DOWN))
        group_2.add(extra_squares_2)

        self.play(
            FadeIn(extra_squares_2),
            ReplacementTransform(height_label_2, height_label_3),
            ReplacementTransform(width_label_2, width_label_3),
        )
###
class SumOfOddNumbers(Scene):
    def animate_iteration(self, num, square, prev_height_label, prev_width_label, prev_group):
        width_label_shift = UP + num * RIGHT / 2
        height_label_shift = LEFT + num * DOWN / 2

        width_label = MathTex(str(num + 1))
        width_label.shift(width_label_shift)
        height_label = MathTex(str(num + 1))
        height_label.shift(height_label_shift)

        group = VGroup()
        group.add(prev_group.copy())

        self.play(group.animate.shift(DOWN + RIGHT))

        extra_squares = VGroup()
        extra_squares.add(square.copy().shift(num * DOWN))
        extra_squares.add(square.copy().shift(num * RIGHT))
        group.add(extra_squares)

        self.play(
            FadeIn(extra_squares),
            ReplacementTransform(prev_height_label, height_label),
            ReplacementTransform(prev_width_label, width_label)
        )

        return [ height_label, width_label, group ]

    def construct(self):
        square = Square(1)

        height_label = MathTex("1")
        height_label.shift(LEFT)
        width_label = MathTex("1")
        width_label.shift(UP)

        self.add(square, height_label, width_label)

        result = [ height_label, width_label, square ]

        for i in range(1, 5):
            result = animate_iteration(self, i, square, result[0], result[1], result[2])