from manim import *
from math import *
from manim_slides import Slide
from manim_slides import ThreeDSlide

class Intro(ThreeDSlide):
    def crossfade(self, mobj1, mobj2):
        self.play(FadeOut(mobj1), FadeIn(mobj2))

    def construct(self):
        self.wait_time_between_slides = 0.1

        intro_banner = ManimBanner()
        intro_text = Text("A brief introduction", font_size=48)
        intro_text.shift(DOWN + 1 * LEFT)
        
        # SLIDE 1 - INTRO
        
        self.play(intro_banner.create())
        self.wait(duration=0.5)
        self.play(intro_banner.expand())
        self.play(Write(intro_text))

        self.next_slide(auto_next=True) # SLIDE 1 -> TRANSITION

        self.play(Unwrite(intro_banner, run_time=1), Unwrite(intro_text, run_time=1))
        
        equation = MathTex(*("(a+b)(a-b) = a^2 -b^2".split(" ")), font_size=72)
        lhs = MathTex(*("( a +b )( a -b )".split(" ")), font_size=72)
        intermediate_rhs = MathTex(*("a^2 -ab +ab -b^2".split(" ")), font_size=72)
        final_rhs = MathTex(*("a^2 -b^2".split(" ")), font_size=72)

        intermediate_rhs.shift(1 * DOWN)
        final_rhs.shift(1 * DOWN)
        self.play(Write(lhs))

        vars = [lhs[1], lhs[2], lhs[4], lhs[5]]

        def animate_product(mobj1, mobj2, mobjdest, run_time = 0.5):
            animations = Succession(*[
                AnimationGroup(*[
                    FadeToColor(mobj1, YELLOW),
                    FadeToColor(mobj2, YELLOW)
                ], run_time=run_time),

                AnimationGroup(*[
                    mobj1.animate.move_to(mobjdest),
                    mobj2.animate.move_to(mobjdest),
                    Transform(mobj1, mobjdest),
                    Transform(mobj2, mobjdest)
                ], run_time=run_time),

                AnimationGroup(*[
                    FadeOut(mobj1),
                    FadeOut(mobj2),
                    FadeIn(mobjdest),
                ], run_time=run_time),
            ],)

            self.play(animations)

        self.next_slide(loop=True) # SLIDE 2.1 - WHAT CAN YOU DO WITH IT - (a+b)(a-b) ANIMATION
        
        animate_product(vars[0].copy(), vars[2].copy(), intermediate_rhs[0])
        animate_product(vars[0].copy(), vars[3].copy(), intermediate_rhs[1])
        animate_product(vars[1].copy(), vars[2].copy(), intermediate_rhs[2])
        animate_product(vars[1].copy(), vars[3].copy(), intermediate_rhs[3])

        self.play(FadeToColor(intermediate_rhs[1], RED), FadeToColor(intermediate_rhs[2], RED))
        self.play(
            FadeOut(intermediate_rhs[1]),
            FadeOut(intermediate_rhs[2]), 
            intermediate_rhs[0].animate.move_to(final_rhs[0]),
            intermediate_rhs[3].animate.move_to(final_rhs[1])
        )
        self.wait()
        self.play(
            FadeIn(equation[1]),
            lhs.animate.move_to(equation[0]),
            intermediate_rhs[0].animate.move_to(equation[2]),
            intermediate_rhs[3].animate.move_to(equation[3])
        )
        self.wait()
        self.play(
            FadeOut(equation[1]),
            FadeOut(intermediate_rhs[0]),
            FadeOut(intermediate_rhs[3]),
            lhs.animate.move_into_position()
        )

        self.next_slide(auto_next=True) # SLIDE 2.1 -> TRANSITION

        self.play(Unwrite(lhs))

        trig_value = ValueTracker(0)

        sin_function = MathTex(r"f(x)=\sin{x}")
        sin_function.shift(5 * LEFT + 2 * UP)

        number_plane = NumberPlane(x_range=[0, 12])
        number_plane.shift(3 * RIGHT)
        sin_plot = always_redraw(lambda: number_plane.plot(lambda x: -sin(x - trig_value.get_value()), x_range=[0, 12]))

        circle = Circle()
        circle.shift(5 * LEFT)
        circle_dot = always_redraw(lambda: Dot(np.array([-5 + cos(trig_value.get_value()), sin(trig_value.get_value()), 0])))
        y_axis_dot = always_redraw(lambda: Dot(np.array([-3, sin(trig_value.get_value()), 0])))
        connecting_line = always_redraw(lambda: Line(np.array([-5 + cos(trig_value.get_value()), sin(trig_value.get_value()), 0]), np.array([-3, sin(trig_value.get_value()), 0])))

        self.play(
            Create(number_plane),
            Create(connecting_line),
            Create(circle),
            Create(circle_dot),
            Create(y_axis_dot),
            Create(sin_plot),
            Write(sin_function)
        )

        self.next_slide(loop=True) # SLIDE 2.2 - WHAT CAN YOU DO WITH IT - sin(x) CONSTRUCTION

        self.play(trig_value.animate.set_value(PI * 8), run_time=20, rate_func=linear)

        self.next_slide(auto_next=True) # SLIDE 2.2 - TRANSITION

        self.play(
            Unwrite(sin_function),
            Uncreate(number_plane),
            Uncreate(connecting_line),
            Uncreate(circle),
            Uncreate(circle_dot),
            Uncreate(y_axis_dot),
            Uncreate(sin_plot)
        )

        axes_3d = ThreeDAxes()
        cube = Cube()

        self.play(Create(axes_3d), Create(cube))
        self.move_camera(phi=PI / 3, theta=PI / 3)

        self.next_slide(loop=True) # SLIDE 2.3 - WHAT YOU CAN DO WITH IT - 3D

        self.move_camera(theta=PI / 3 + 2 * PI, run_time=10, rate_func=linear)

        self.next_slide() # SLIDE 3 - VISUAL PROOF THAT THE SUM OF ODD INTEGERS UP TO 2N-1 = N^2

        self.move_camera(phi=0, theta=-PI / 2)
        self.play(Uncreate(axes_3d), Uncreate(cube))

        code = open("visualproof.py").read()
        code_segments = code.split("###")

        def get_code_segment_mobj(num, corner=True):
            result = Code(code=code_segments[num], language="python")
            result.scale(0.5)

            if corner:
                result.to_corner(LEFT + DOWN)

            return result
        
        code_mobj_segments = [get_code_segment_mobj(i) for i in range(len(code_segments) - 1)]

        sum_of_odd_title_1 = Text("How to visualize")
        sum_of_odd_formula = MathTex(r"\sum_{k=1}^{n}{2k-1}=n^2", font_size=72)
        sum_of_odd_title_2 = Text("using Manim")
        sum_of_odd_title_1.shift(1.75 * UP)
        sum_of_odd_title_2.shift(1.75 * DOWN)

        self.play(Write(sum_of_odd_title_1), Write(sum_of_odd_formula), Write(sum_of_odd_title_2))

        self.next_slide() # SLIDE 3.1

        self.play(FadeOut(sum_of_odd_title_1), FadeOut(sum_of_odd_title_2))
        self.play(sum_of_odd_formula.animate.scale(0.5).to_corner(UP + LEFT))
        self.play(Create(code_mobj_segments[0]))

        self.next_slide()

        square_f = Square(1)
        square_f.shift(3 * RIGHT)

        self.crossfade(code_mobj_segments[0], code_mobj_segments[1])
        self.play(FadeIn(square_f))

        self.next_slide()

        height_label_f = MathTex("1")
        width_label_f = MathTex("1")
        height_label_f.shift(2 * RIGHT)
        width_label_f.shift(3 * RIGHT + UP)

        self.crossfade(code_mobj_segments[1], code_mobj_segments[2])
        self.play(Write(height_label_f), Write(width_label_f))

        self.next_slide(auto_next=True)

        self.play(
            square_f.animate.shift(UP + LEFT),
            height_label_f.animate.shift(UP + LEFT),
            width_label_f.animate.shift(UP + LEFT)
        )

        self.crossfade(code_mobj_segments[2], code_mobj_segments[3])

        self.next_slide(loop=True)

        group = VGroup()
        group.add(square_f.copy())

        self.play(group.animate.shift(DOWN + RIGHT))

        extra_squares = VGroup()
        extra_squares.add(square_f.copy().shift(RIGHT))
        extra_squares.add(square_f.copy().shift(DOWN))
        group.add(extra_squares)

        height_label_2 = MathTex("2")
        height_label_2.shift(1 * RIGHT + 0.5 * UP)
        width_label_2 = MathTex("2")
        width_label_2.shift(2.5 * RIGHT + 2 * UP)

        self.play(
            FadeIn(extra_squares),
            ReplacementTransform(width_label_f, width_label_2),
            ReplacementTransform(height_label_f, height_label_2),
        )
        self.wait()

        self.next_slide(auto_next=True)

        self.crossfade(code_mobj_segments[3], code_mobj_segments[4])

        self.next_slide(loop=True)

        height_label_3 = MathTex("3")
        height_label_3.shift(1 * RIGHT)
        width_label_3 = MathTex("3")
        width_label_3.shift(3 * RIGHT + 2 * UP)

        group_2 = VGroup()
        group_2.add(group.copy())

        self.play(group_2.animate.shift(RIGHT + DOWN))

        extra_squares_2 = VGroup()
        extra_squares_2.add(square_f.copy().shift(2 * RIGHT))
        extra_squares_2.add(square_f.copy().shift(2 * DOWN))
        group_2.add(extra_squares_2)

        self.play(
            FadeIn(extra_squares_2),
            ReplacementTransform(height_label_2, height_label_3),
            ReplacementTransform(width_label_2, width_label_3),
        )
        self.wait()

        self.next_slide()

        self.play(
            Uncreate(code_mobj_segments[4]),
            Uncreate(square_f),
            Uncreate(group),
            Uncreate(extra_squares),
            Uncreate(group_2),
            Uncreate(extra_squares_2),
            Unwrite(height_label_3),
            Unwrite(width_label_3),
            Unwrite(sum_of_odd_formula)
        )

        big_code_block = get_code_segment_mobj(5, False)

        self.play(Create(big_code_block))

        self.next_slide(auto_next=True)

        self.play(Uncreate(big_code_block))
              
        origin = 2 * LEFT + 2 * UP

        def animate_iteration(self, num, square, prev_height_label, prev_width_label, prev_group):
            width_label_shift = origin + UP + num * RIGHT / 2
            height_label_shift = origin + LEFT + num * DOWN / 2

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
            
        square_f = Square(1)
        square_f.shift(origin)

        height_label_f = MathTex("1")
        height_label_f.shift(origin + LEFT)
        width_label_f = MathTex("1")
        width_label_f.shift(origin + UP)

        self.play(FadeIn(square_f), FadeIn(height_label_f), FadeIn(width_label_f))

        self.next_slide(loop=True)

        result = [ height_label_f, width_label_f, square_f ]
        to_deconstruct = []

        for i in range(1, 5):
            result = animate_iteration(self, i, square_f, result[0], result[1], result[2])
            to_deconstruct.append(result[2])

        self.wait()

        height_label_f = MathTex("1")
        height_label_f.shift(origin + LEFT)
        width_label_f = MathTex("1")
        width_label_f.shift(origin + UP)

        self.play(
            *[Transform(mob, square_f) for mob in to_deconstruct],
            Transform(result[0], height_label_f),
            Transform(result[1], width_label_f)
        )

        self.next_slide()

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        self.play(
            Write(Text("Thank you", font_size=144)),
            Write(Text("this took too long", font_size=12).shift(3 * DOWN))
        )
