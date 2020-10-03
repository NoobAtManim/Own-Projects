from manimlib.imports import *

class Grid(VMobject):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        VMobject.__init__(self, **kwargs)

    def generate_points(self):
        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows":8,
        "columns":14,
        "height": FRAME_Y_RADIUS*2,
        "width": 14,
        "grid_stroke":0.5,
        "grid_color":WHITE,
        "axis_color":RED,
        "axis_stroke":2,
        "show_points":False,
        "point_radius":0,
        "labels_scale":0.5,
        "labels_buff":0,
        "number_decimals":2
    }

    def __init__(self,**kwargs):
        VGroup.__init__(self,**kwargs)
        rows=self.rows
        columns=self.columns
        grilla=Grid(width=self.width,height=self.height,rows=rows,columns=columns).set_stroke(self.grid_color,self.grid_stroke)

        vector_ii=ORIGIN+np.array((-self.width/2,-self.height/2,0))
        vector_id=ORIGIN+np.array((self.width/2,-self.height/2,0))
        vector_si=ORIGIN+np.array((-self.width/2,self.height/2,0))
        vector_sd=ORIGIN+np.array((self.width/2,self.height/2,0))

        ejes_x=Line(LEFT*self.width/2,RIGHT*self.width/2)
        ejes_y=Line(DOWN*self.height/2,UP*self.height/2)

        ejes=VGroup(ejes_x,ejes_y).set_stroke(self.axis_color,self.axis_stroke)

        divisiones_x=self.width/columns
        divisiones_y=self.height/rows

        direcciones_buff_x=[UP,DOWN]
        direcciones_buff_y=[RIGHT,LEFT]
        dd_buff=[direcciones_buff_x,direcciones_buff_y]
        vectores_inicio_x=[vector_ii,vector_si]
        vectores_inicio_y=[vector_si,vector_sd]
        vectores_inicio=[vectores_inicio_x,vectores_inicio_y]
        tam_buff=[0,0]
        divisiones=[divisiones_x,divisiones_y]
        orientaciones=[RIGHT,DOWN]
        puntos=VGroup()
        leyendas=VGroup()


        for tipo,division,orientacion,coordenada,vi_c,d_buff in zip([columns,rows],divisiones,orientaciones,[0,1],vectores_inicio,dd_buff):
            for i in range(1,tipo):
                for v_i,direcciones_buff in zip(vi_c,d_buff):
                    ubicacion=v_i+orientacion*division*i
                    punto=Dot(ubicacion,radius=self.point_radius)
                    coord=round(punto.get_center()[coordenada],self.number_decimals)
                    leyenda=TextMobject("%s"%coord).scale(self.labels_scale)
                    leyenda.next_to(punto,direcciones_buff,buff=self.labels_buff)
                    puntos.add(punto)
                    leyendas.add(leyenda)

        self.add(grilla,ejes,leyendas)
        if self.show_points==True:
            self.add(puntos)

class Thumbnail(Scene):
    def construct(self):
        #grid = ScreenGrid()
        text = TextMobject("Proof of Pythagoras")
        text.scale(2).to_edge(UP, buff=0.75)
        text[0][7:].set_color(YELLOW)
        triangle1 = Polygon((-4.5, 1.5, 0), (-0.5, -1.5, 0), (-4.5, -1.5, 0), color=RED)
        triangle1.set_stroke(width=2.5).set_fill(ORANGE, opacity=0.5)
        triangle2 = Polygon((0.9, -1.4, 0), (0.9, 1.6, 0), (12/5*np.cos(np.arctan(4/3))+0.9, 12/5*np.sin(np.arctan(4/3))-1.4, 0), color=RED)
        triangle2.set_stroke(width=2.5).set_fill(ORANGE, opacity=0.5)
        triangle3 = Polygon((1, -1.5, 0), (5, -1.5, 0), (12/5*np.cos(np.arctan(4/3))+1, 12/5*np.sin(np.arctan(4/3))-1.5, 0), color=RED)
        triangle3.set_stroke(width=2.5).set_fill(ORANGE, opacity=0.5)
        arrow = Arrow((-0.75,0,0), (0.75,0,0))
        arrow.set_stroke(width=5)
        equation = TexMobject("a^{2}+b^{2}=c^{2}")
        equation.scale(1.5).move_to(3*DOWN)
        logo = ImageMobject("assets/images/circle-cropped.png")
        logo.move_to(5.5*RIGHT+2.5*DOWN)

        #self.add(grid)
        self.add(text)
        self.add(triangle1)
        self.add(triangle2)
        self.add(triangle3)
        self.add(arrow)
        self.add(equation)
        self.add(logo)

class LogoScene(Scene):
    def construct(self):
        #grid = ScreenGrid()
        logo = ImageMobject("assets/images/circle-cropped.png")
        logo.scale(2.5).move_to(3.5*LEFT)
        text = TextMobject("Aussie MathsKid")
        text.move_to(2.8*RIGHT+1*UP).scale(1.5)
        text1 = TextMobject("Proof of the")
        text1.move_to(2.8*RIGHT+0.7*DOWN)
        text2 = TextMobject("Pythagorean Theorem")
        text2.move_to(2.8*RIGHT+1.4*DOWN).set_color_by_gradient(PURPLE, RED)
        box = Polygon((0, -2, 0), (0, -0.1, 0), (5.6, -0.1, 0), (5.6, -2, 0), color=DARK_BLUE)

        #self.add(grid)
        self.play(FadeIn(logo))
        self.wait()
        self.play(Write(text))
        self.play(FadeIn(text1), Write(text2), ShowCreation(box))
        self.wait(4)
        self.play(FadeOut(logo), Uncreate(text), Uncreate(box), FadeOutAndShiftDown(text1), FadeOutAndShiftDown(text2))
        self.wait(1)

class Proof2(MovingCameraScene):
    def construct(self):
        self.proof4wayscopy()
        self.similarproof()
        self.proofpart()

    def proofpart(self):
        grid = ScreenGrid()
        triangle20 = Polygon((-5, 1, 0), (-5, -2, 0), (-3.56, -0.08, 0), color=BLUE_D)
        triangle30 = Polygon((-3.56, -0.08, 0), (-5, -2, 0), (-1, -2, 0), color=BLUE_D)
        triangle20.set_fill(BLUE_C, opacity=1).set_stroke(width=1.5)
        triangle30.set_fill(BLUE_C, opacity=1).set_stroke(width=1.5)
        brace1 = Brace(triangle20, LEFT)
        brace2 = Brace(triangle30, DOWN)
        brace3 = Brace(triangle20, np.array([1.08, 1.56, 0]))
        brace4 = Brace(triangle30, np.array([1.92, 2.44, 0]))
        writebrace1 = brace1.get_tex("a")
        writebrace2 = brace2.get_tex("b")
        writebrace3 = brace3.get_tex("c_{1}")
        writebrace4 = brace4.get_tex("c_{2}")
        equation1 = TexMobject("\\frac{c_{1}}{a}=\\frac{a}{c}")
        equation2 = TexMobject("\\frac{c_{2}}{b}=\\frac{b}{c}")
        equation3 = TexMobject("c=c_{1}+c_{2}")
        equation4 = TexMobject("a^{2}=c_{1}\\times c")
        equation5 = TexMobject("b^{2}=c_{2}\\times c")
        equation6 = TexMobject("a^{2}+b^{2}=c_{1}\\times c+c_{2}\\times c")
        equation7 = TexMobject("a^{2}+b^{2}=c(c_{1}+c_{2})")
        equation8 = TexMobject("a^{2}+b^{2}=c^{2}")
        equation1.move_to(3*RIGHT+1.6*DOWN).scale(1.1)
        equation2.move_to(3*RIGHT+1.6*DOWN).scale(1.1)
        equation3.move_to(3*RIGHT+1*UP).scale(1.1)
        equation4.move_to(3*RIGHT+2.9*DOWN).scale(1.1)
        equation5.move_to(3*RIGHT+2.9*DOWN).scale(1.1)
        equation6.move_to(3*RIGHT+1.6*DOWN).scale(1.1)
        equation7.move_to(3*RIGHT+2.9*DOWN).scale(1.1)
        equation8.move_to(3*RIGHT+1*DOWN).scale(2)
        arrow1 = Arrow((1.4, -0.7, 0), (2.5, -1.4, 0))
        arrow2 = Arrow((4.6, -0.7, 0), (3.5, -1.4, 0))
        arrow30 = Arrow((3, -2, 0), (3, -2.8, 0))
        arrow31 = Arrow((3, -2, 0), (3, -2.8, 0))
        arrow32 = Arrow((3, -2, 0), (3, -2.8, 0))
        arrow4 = Arrow((3, 0.5, 0), (3, -2.5, 0))
        arrow1.set_stroke(width=5)
        arrow2.set_stroke(width=5)
        arrow30.set_stroke(width=5)
        arrow31.set_stroke(width=5)
        arrow32.set_stroke(width=5)
        arrow4.set_stroke(width=5)
        plus = TexMobject("+")
        plus.scale(1.1).move_to(3*RIGHT+0.4*DOWN)

        #self.add(grid)
        self.add(triangle20)
        self.add(triangle30)
        self.play(
            FadeIn(brace1),
            FadeIn(brace2),
            FadeIn(brace3),
            FadeIn(brace4),
            Write(writebrace1),
            Write(writebrace2),
            Write(writebrace3),
            Write(writebrace4)
        )
        self.wait(5)
        self.play(Write(equation3))
        self.wait(3)
        self.play(Write(equation1))
        self.wait(10)
        self.play(ShowCreation(arrow30))
        self.play(Write(equation4))
        self.wait(3)
        self.play(Uncreate(arrow30))
        self.play(equation4.move_to, 1.2*RIGHT+0.3*DOWN, FadeOut(equation1))
        self.wait(3)
        self.play(Write(equation2))
        self.wait(3)
        self.play(ShowCreation(arrow31))
        self.play(Write(equation5))
        self.wait()
        self.play(Uncreate(arrow31))
        self.play(equation5.move_to, 4.8*RIGHT+0.3*DOWN, FadeOut(equation2))
        self.wait(2)
        self.play(FadeIn(plus))
        self.wait(2)
        self.play(ShowCreation(arrow1), ShowCreation(arrow2))
        self.play(Write(equation6))
        self.wait(6)
        self.play(ShowCreation(arrow32))
        self.play(Write(equation7))
        self.wait(2)
        self.play(Uncreate(arrow1), Uncreate(arrow2), Uncreate(arrow32))
        self.play(FadeOutAndShift(equation6, RIGHT), Uncreate(equation4), Uncreate(equation5), Uncreate(plus))
        self.wait(2)
        self.play(Indicate(equation3))
        self.wait(2)
        self.play(ShowCreation(arrow4))
        self.wait()
        self.play(Uncreate(arrow4))
        self.play(Transform(equation7, equation8), FadeOut(equation3))
        self.wait(2)

    def similarproof(self):
        grid = ScreenGrid()
        proof2title = TextMobject("Similar Triangles Proof")
        proof2title.scale(1.8).move_to(2.9*UP).set_color(YELLOW)
        triangle1 = Polygon((-2, 1.5, 0), (-2, -1.5, 0), (2, -1.5, 0), color=BLUE_D)
        triangle2 = Polygon((-2, 1.5, 0), (-2, -1.5, 0), (-0.56, 0.42, 0), color=BLUE_D)
        triangle3 = Polygon((-0.56, 0.42, 0), (-2, -1.5, 0), (2, -1.5, 0), color=BLUE_D)
        triangle20 = Polygon((-5, 1, 0), (-5, -2, 0), (-3.56, -0.08, 0), color=BLUE_D)
        triangle30 = Polygon((-3.56, -0.08, 0), (-5, -2, 0), (-1, -2, 0), color=BLUE_D)
        triangle4 = Polygon((-2, 1.5, 0), (-2, -1.5, 0), (2, -1.5, 0), color=RED)
        triangle5 = Polygon((-2, 1.5, 0), (-2, -1.5, 0), (-0.56, 0.42, 0), color=RED)
        triangle6 = Polygon((-0.56, 0.42, 0), (-2, -1.5, 0), (2, -1.5, 0), color=RED)
        triangle1.set_fill(BLUE_C, opacity=1).set_stroke(width=1.5)
        triangle2.set_fill(BLUE_C, opacity=1).set_stroke(width=1.5)
        triangle3.set_fill(BLUE_C, opacity=1).set_stroke(width=1.5)
        triangle20.set_fill(BLUE_C, opacity=1).set_stroke(width=1.5)
        triangle30.set_fill(BLUE_C, opacity=1).set_stroke(width=1.5)
        triangle4.set_fill(RED, opacity=1).set_stroke(width=3)
        triangle5.set_fill(RED, opacity=1).set_stroke(width=3)
        triangle6.set_fill(RED, opacity=1).set_stroke(width=3)
        # Right Angle ends in 0, small angle in 1, large angle in 2
        # Big triangle starts with 0, small triangle with 1, large triangle with 0
        angle00 = Arc(radius=0.3,angle=TAU/4)
        angle01 = Arc(radius=0.3,angle=np.arctan(3/4))
        angle02 = Arc(radius=0.3,angle=np.arctan(4/3))
        angle10 = Arc(radius=0.4,angle=TAU/4)
        angle11 = Arc(radius=0.4,angle=np.arctan(3/4))
        angle12 = Arc(radius=0.4,angle=np.arctan(4/3))
        angle20 = Arc(radius=0.5,angle=TAU/4)
        angle21 = Arc(radius=0.5,angle=np.arctan(3/4))
        angle22 = Arc(radius=0.5,angle=np.arctan(4/3))
        angle00.move_arc_center_to(2*LEFT+1.5*DOWN).set_color(ORANGE)
        angle01.rotate_about_origin(PI-np.arctan(3/4)).move_arc_center_to(2*RIGHT+1.5*DOWN).set_color(PURPLE)
        angle02.rotate_about_origin(3*TAU/4).move_arc_center_to(2*LEFT+1.5*UP).set_color(GREEN)
        angle10.rotate_about_origin(PI-np.arctan(3/4)).move_arc_center_to(0.56*LEFT+0.42*UP).set_color(ORANGE)
        angle11.rotate_about_origin(np.arctan(4/3)).move_arc_center_to(2*LEFT+1.5*DOWN).set_color(PURPLE)
        angle12.rotate_about_origin(3*TAU/4).move_arc_center_to(2*LEFT+1.5*UP).set_color(GREEN)
        angle20.rotate_about_origin(PI+np.arctan(4/3)).move_arc_center_to(0.56*LEFT+0.42*UP).set_color(ORANGE)
        angle21.rotate_about_origin(PI-np.arctan(3/4)).move_arc_center_to(2*RIGHT+1.5*DOWN).set_color(PURPLE)
        angle22.move_arc_center_to(2*LEFT+1.5*DOWN).set_color(GREEN)
        braceontriangle0 = Brace(triangle1, LEFT)
        braceontriangle1 = Brace(triangle1, DOWN)
        braceontriangle2 = Brace(triangle1, np.array([3, 4, 0]))
        eqtest0 = braceontriangle0.get_tex("a")
        eqtest1 = braceontriangle1.get_tex("b")
        eqtest2 = braceontriangle2.get_tex("c")
        #line1 = Line((-2, -1.5, 0), (12/5*np.cos(np.arctan(4/3))-2, 12/5*np.sin(np.arctan(4/3))-1.5, 0))
        
        self.play(Write(proof2title))
        self.wait()
        #self.add(grid)
        self.play(DrawBorderThenFill(triangle1))
        self.play(GrowFromCenter(braceontriangle0), Write(eqtest0))
        self.play(GrowFromCenter(braceontriangle1), Write(eqtest1))
        self.play(GrowFromCenter(braceontriangle2), Write(eqtest2))
        self.wait()
        self.play(
            ShrinkToCenter(braceontriangle0),
            ShrinkToCenter(braceontriangle1),
            ShrinkToCenter(braceontriangle2),
            FadeOut(eqtest0),
            FadeOut(eqtest1),
            FadeOut(eqtest2)
        )
        self.play(ShowCreation(triangle2), ShowCreation(triangle3))
        #self.play(ShowCreation(line1))
        #self.play(line1.set_color, BLUE_D)
        self.play(FadeOut(triangle1))
        self.wait(2)
        self.play(ShowCreation(angle00), ShowCreation(angle01), ShowCreation(angle02))
        self.play(ShowCreation(angle10), ShowCreation(angle11), ShowCreation(angle12))
        self.play(ShowCreation(angle20), ShowCreation(angle21), ShowCreation(angle22))
        self.wait()
        # Save the state of camera
        self.camera_frame.save_state()
        # Animation of the camera
        self.play(
            # Set the size with the width of a object
            self.camera_frame.set_width,triangle2.get_width()*5,
            # Move the camera to the object
            self.camera_frame.move_to,triangle2
        )
        self.wait()
        self.play(ShowCreationThenFadeOut(triangle4))
        self.play(ShowCreationThenFadeOut(triangle5))
        self.play(Indicate(angle00, run_time=2), Indicate(angle10, run_time=2))
        self.play(Indicate(angle02, run_time=2), Indicate(angle12, run_time=2))
        self.play(Indicate(angle01, run_time=2), Indicate(angle11, run_time=2))
        self.wait(2)
        self.play(ShowCreationThenFadeOut(triangle4))
        self.play(ShowCreationThenFadeOut(triangle6))
        self.play(Indicate(angle00, run_time=2), Indicate(angle20, run_time=2))
        self.play(Indicate(angle01, run_time=2), Indicate(angle21, run_time=2))
        self.play(Indicate(angle02, run_time=2), Indicate(angle22, run_time=2))
        self.wait(3)                
        # Restore the state saved
        self.play(Restore(self.camera_frame))
        self.wait()
        self.play(
            Uncreate(angle00),
            Uncreate(angle01),
            Uncreate(angle02),
            Uncreate(angle10),
            Uncreate(angle11),
            Uncreate(angle12),
            Uncreate(angle20),
            Uncreate(angle21),
            Uncreate(angle22)
        )
        self.play(
            Transform(triangle2, triangle20),
            Transform(triangle3, triangle30)
        )
    
    def proof4wayscopy(self):
        #grid = ScreenGrid()
        line = Line((-6, 2, 0), (6, 2, 0))
        title1 = TextMobject("The 4 Proofs")
        title1.scale(2).move_to(2.9*UP)
        title1.set_color(YELLOW)
        proofs = TextMobject(
            "1. Rearrangement Proof\\\\",
            "2. Similar Triangles Proof\\\\",
            "3. Dissection Proof\\\\",
            "4. Algebraic Proof\\\\",
            alignment="",
        )

        proofs.arrange_submobjects(DOWN, buff=0.5, aligned_edge=LEFT).scale(1.3).move_to(0.5*DOWN)
        proofs[0].set_color(BLUE_A)
        proofs[1].set_color(BLUE_B)
        proofs[2].set_color(BLUE_C)
        proofs[3].set_color(BLUE_D)

        #self.add(grid)
        self.play(ShowCreation(line))
        self.play(Write(proofs))
        self.play(Write(title1))
        self.wait(5)
        self.play(FadeOut(proofs[0:]), FadeOut(title1), Uncreate(line))
        self.wait()

class EndScene(Scene):
    def construct(self):
        #grid = ScreenGrid()
        title = TextMobject("Click on These")
        title.scale(2).move_to(2.8*UP).set_color_by_gradient(GREEN, BLUE)
        text1 = TextMobject("video powered by manim")
        text1.set_color(YELLOW).move_to(3.25*DOWN+4.5*RIGHT).scale(0.75)
        box = Polygon((-3.5, 3.4, 0), (3.5, 3.4, 0), (3.5, 2.2, 0), (-3.5, 2.2, 0))
        box.set_color(RED)
        arrow1 = Arrow((-1, 1.5, 0), (-2.5, 0.5, 0))
        arrow1.scale(2)
        arrow2 = Arrow((0, 1.5, 0), (0, 0, 0))
        arrow2.scale(2)
        arrow3 = Arrow((1, 1.5, 0), (2.5, 0.5, 0))
        arrow3.scale(2)

        #self.add(grid)
        self.play(Write(title), ShowCreation(box))
        self.play(
            FadeIn(arrow1),
            FadeIn(arrow2),
            FadeIn(arrow3),
        )
        self.wait(2)
        self.play(Write(text1))
        self.wait(5)