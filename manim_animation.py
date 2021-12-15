from manim import *
%manim -h
%%manim OpeningManim -qm -v WARNING

class OpeningManim(Scene):
    def construct(self):
        title = Tex(r"What is Pulse Width Modulation?", color = BLUE)
        self.play(
            Write(title),
        )
        self.wait()
        
        transform_title = Tex(r"Pulse width modulation, or PWM is a type of digital signal that can be used to mimick analog signals", font_size=120, tex_to_color_map={"PWM": YELLOW}).scale(.7)
        transform_title.to_corner(UP)
        self.play(
            Transform(title, transform_title),
        )
        self.wait()
        
        path = VMobject()
        dot = Dot(point=LEFT)
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_start()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        
        for i in range(2):
            self.play(dot.animate.shift(UP))
            self.play(dot.animate.shift(RIGHT))
            self.play(dot.animate.shift(DOWN))
            self.play(dot.animate.shift(RIGHT))
            
        for i in range(2):
            self.play(dot.animate.shift(UP))
            self.play(dot.animate.shift(0.5*RIGHT))
            self.play(dot.animate.shift(DOWN))
            self.play(dot.animate.shift(RIGHT))
            
        self.wait()
        

        
        
        
