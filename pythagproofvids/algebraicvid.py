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
        grid = ScreenGrid()
        text = TextMobject("Proof of Pythagoras")
        text.scale(2).to_edge(UP, buff=0.75)
        text[0][7:].set_color(YELLOW)
        triangle1 = Polygon((-3, -1, 0), (-5, -1, 0), (-3, 2, 0))
        triangle2 = Polygon((-3, 0, 0), (-3, 2, 0 ), (0, 0, 0))
        triangle3 = Polygon((-2, 0, 0), (0, 0, 0), (-2, -3, 0))
        triangle4 = Polygon((-2, -1, 0), (-2, -3, 0), (-5, -1, 0))
        triangle1.set_fill(BLUE_B, opacity=0.7).set_stroke(width=1.5)
        triangle2.set_fill(BLUE_B, opacity=0.7).set_stroke(width=1.5)
        triangle3.set_fill(BLUE_B, opacity=0.7).set_stroke(width=1.5)
        triangle4.set_fill(BLUE_B, opacity=0.7).set_stroke(width=1.5)
        square = Square(color=WHITE)
        square.scale(0.5).move_to(2.5*LEFT+0.5*DOWN).set_fill(WHITE, opacity=0.7).set_stroke(width=1.5)
        equation = TexMobject("a^{2}+b^{2}=c^{2}")
        equation.scale(1.5).move_to(3.5*RIGHT)
        logo = ImageMobject("assets/images/circle-cropped.png")
        logo.move_to(5.5*RIGHT+2.5*DOWN)

        #self.add(grid)
        self.add(text)
        self.add(equation)
        self.add(triangle1)
        self.add(triangle2)
        self.add(triangle3)
        self.add(triangle4)
        self.add(square)
        self.add(logo)

class Intro(Scene):
    def construct(self):
        self.proof4wayscopy()
        self.aminusb()

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

    def aminusb(self):
        grid = ScreenGrid()
        square1 = Square(color=RED)
        square2 = Square(color=RED)
        square3 = Square(color=RED)
        square1.scale(2).move_to(2*LEFT)
        square2.scale(1.5).move_to(2.5*LEFT+0.5*UP).set_fill(WHITE, opacity=1)
        square3.scale(0.5).move_to(0.5*LEFT+1.5*DOWN)
        rectangle1 = Polygon((-1, 2, 0), (0, 2, 0), (0, -2, 0), (-1, -2, 0), color=RED)
        rectangle2 = Polygon((0, -2, 0), (-4, -2, 0), (-4, -1, 0), (0, -1, 0), color=RED)
        poly = Polygon((0, -2, 0), (-4, -2, 0), (-4, -1, 0), (-1, -1, 0), (-1, 2, 0), (0, 2, 0), color=RED)
        line1 = Line((-1, 2, 0), (-1, -2, 0), color=RED)
        line2 = Line((-4, -1, 0), (0, -1, 0), color=RED)
        dummyline1 = Line((-4, 2, 0), (-1, 2, 0))
        dummyline2 = Line((0, 2, 0), (-1, 2, 0))
        braceontriangle0 = Brace(dummyline1, UP)
        braceontriangle1 = Brace(dummyline2, UP)
        braceontriangle2 = Brace(square1, UP)
        braceontriangle3 = Brace(square1, RIGHT)
        eqtest0 = braceontriangle0.get_tex("a-b")
        eqtest1 = braceontriangle1.get_tex("b")
        eqtest2 = braceontriangle2.get_tex("a")
        eqtest3 = braceontriangle3.get_tex("a")
        equation1 = TexMobject("(a-b)^{2}=")
        equation2 = TexMobject("a^{2}-2ab+b^{2}")
        equation1.scale(1.2).move_to(3.5*RIGHT+0.55*UP)
        equation2.scale(1.2).move_to(3.5*RIGHT+0.55*DOWN)

        #self.add(grid)
        self.wait()
        self.play(Write(equation1))
        self.wait()
        self.play(ShowCreation(square1))
        self.play(FadeIn(braceontriangle2), Write(eqtest2))
        self.wait()
        self.play(FadeOut(braceontriangle2), Uncreate(eqtest2))
        self.play(FadeIn(braceontriangle1), Write(eqtest1))
        self.play(ShowCreation(line1))
        self.play(FadeIn(braceontriangle0), Write(eqtest0))
        self.wait(3)
        self.play(ShowCreation(line2))
        self.wait(3)
        self.play(FadeIn(square2))
        self.add(rectangle1, rectangle2, square3, poly)
        self.wait()
        self.play(FadeIn(braceontriangle3), Write(eqtest3))
        self.wait()
        self.play(ReplacementTransform(eqtest3.copy(), equation2[0][0]), Write(equation2[0][1]))
        self.wait(3)
        self.play(Indicate(poly))
        self.wait(3)
        self.play(Indicate(rectangle1))
        self.play(
            Write(equation2[0][2]),
            ReplacementTransform(eqtest1.copy(), equation2[0][5]),
            ReplacementTransform(eqtest3.copy(), equation2[0][4])
        )
        self.wait(3)
        self.play(Indicate(rectangle2))
        self.wait()
        self.play(Write(equation2[0][3]))
        self.wait(3)
        self.play(Indicate(square3))
        self.wait()
        self.play(ReplacementTransform(eqtest1.copy(), equation2[0][7]), Write(equation2[0][6]), Write(equation2[0][8:]))
        self.wait(5)
        self.remove(
            square1,
            square2,
            square3,
            rectangle1,
            rectangle2,
            poly,
            equation1,
            equation2,
            braceontriangle0,
            braceontriangle1,
            braceontriangle3,
            eqtest0,
            eqtest1,
            eqtest3,
        )

class Proof4(Scene):
    def construct(self):
        grid = ScreenGrid()
        proof4title = TextMobject("Algebraic Proof")
        proof4title.scale(1.8).move_to(2.9*UP).set_color(YELLOW)
        striangle = Polygon((-1, 1, 0), (-1, -2, 0), (1, -2, 0))
        striangle.set_stroke(width=1.5).set_fill(BLUE, opacity=1)
        braceontriangle0 = Brace(striangle, LEFT)
        braceontriangle1 = Brace(striangle, DOWN)
        braceontriangle2 = Brace(striangle, np.array([3, 2, 0]))
        eqtest0 = braceontriangle0.get_tex("b")
        eqtest1 = braceontriangle1.get_tex("a")
        eqtest2 = braceontriangle2.get_tex("c")
        triangle1 = Polygon((-3, -1, 0), (-5, -1, 0), (-3, 2, 0))
        triangle2 = Polygon((-3, 0, 0), (-3, 2, 0 ), (0, 0, 0))
        triangle3 = Polygon((-2, 0, 0), (0, 0, 0), (-2, -3, 0))
        triangle4 = Polygon((-2, -1, 0), (-2, -3, 0), (-5, -1, 0))
        triangle1.set_fill(BLUE_B, opacity=1).set_stroke(width=1.5)
        triangle2.set_fill(BLUE_B, opacity=1).set_stroke(width=1.5)
        triangle3.set_fill(BLUE_B, opacity=1).set_stroke(width=1.5)
        triangle4.set_fill(BLUE_B, opacity=1).set_stroke(width=1.5)
        square = Square(color=WHITE)
        square.scale(0.5).move_to(2.5*LEFT+0.5*DOWN).set_fill(WHITE, opacity=1).set_stroke(width=1.5)
        line = Line((-3, 0, 0), (-2, 0, 0))
        brace1 = Brace(triangle3, np.array([3, -2, 0]))
        brace2 = Brace(line, DOWN)
        brace2.set_color(BLACK)
        writeb1 = brace1.get_tex("c")
        writeb2 = brace2.get_tex("b-a")
        writeb2.set_color(BLACK)
        equation1 = TexMobject("(b-a)^{2}+4{\\frac {ab}{2}}")
        equation2 = TexMobject("b^{2}-2ab+a^{2}+2ab")
        equation3 = TexMobject("a^{2}+b^{2}")
        equation4 = TexMobject("a^{2}+b^{2}=c^{2}")
        equation1.scale(1.1).move_to(3.5*RIGHT+0.8*UP)
        equation2.scale(1.1).move_to(3.5*RIGHT+0.5*DOWN)
        equation3.scale(1.1).move_to(3.5*RIGHT+1.8*DOWN)
        equation4.scale(2).move_to(3.5*RIGHT+0.5*DOWN)
        arrow1 = Arrow((3.5, 0.5, 0), (3.5, -0.4, 0))
        arrow2 = Arrow((3.5, -0.8, 0), (3.5, -1.7, 0))        
        arrow1.set_stroke(width=5)
        arrow2.set_stroke(width=5)

        #self.add(grid)
        self.wait()
        self.play(Write(proof4title))
        self.play(DrawBorderThenFill(striangle))
        self.play(GrowFromCenter(braceontriangle1), Write(eqtest1))
        self.play(GrowFromCenter(braceontriangle0), Write(eqtest0))
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
        self.wait()
        self.play(
            ReplacementTransform(striangle, triangle1),
            ShowCreation(triangle2),
            ShowCreation(triangle3),
            ShowCreation(triangle4),
            ShowCreation(square)
        )
        self.wait()
        self.play(FadeIn(brace1), Write(writeb1))
        self.wait(2)
        self.play(FadeIn(brace2), Write(writeb2))
        self.wait(9)
        self.play(Write(equation1), run_time=2)
        self.wait(5)
        self.play(Indicate(equation1[0][8:]))
        self.wait(3)
        self.play(ShowCreation(arrow1))
        self.play(Write(equation2), run_time=2)
        self.wait(4)
        self.play(ShowCreation(arrow2))
        self.play(Write(equation3), run_time=2)
        self.wait(4)
        self.play(Indicate(writeb1), run_time=2)
        self.play(
            FadeOut(equation1),
            FadeOut(equation2),
            FadeOut(equation3),
            FadeOut(arrow1),
            FadeOut(arrow2)
        )
        self.play(Write(equation4))
        self.wait(3)