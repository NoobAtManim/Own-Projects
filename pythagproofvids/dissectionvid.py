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
        triangle = Polygon((-2, 1, 0), (-2, -2, 0), (-1, -2, 0))
        triangle.set_stroke(width=1.5).set_fill(BLUE, opacity=0.7)
        square1 = Square(color=RED)
        square2 = Square(color=RED)
        square3 = Square(color=RED)
        square1.scale(1.5).move_to(3.5*LEFT+0.5*DOWN).set_stroke(width=2).set_fill(ORANGE, opacity=0.7)
        square2.scale(0.5).move_to(1.5*LEFT+2.5*DOWN).set_stroke(width=2).set_fill(ORANGE, opacity=0.7)
        square3.scale(math.sqrt(10)/2).rotate(np.arcsin(1/math.sqrt(10))).set_stroke(width=2).set_fill(ORANGE, opacity=0.7)
        polygon1 = Polygon((-3, 1, 0), (-2, 1, 0), (-2.9, 0.7, 0), color=BLUE)
        polygon2 = Polygon((-3, 1, 0), (-5, 1, 0), (-5, 0, 0), (-2.9, 0.7, 0), color=BLUE)
        polygon3 = Polygon((-5, 0, 0), (-5, -2, 0), (-2, -2, 0), (-2.9, 0.7, 0), color=BLUE)
        polygon4 = Polygon((-2, -2, 0), (-2, 1, 0), (-2.9, 0.7, 0), color=BLUE)
        polygon1.set_stroke(width=2).shift(1.9*RIGHT+2.7*DOWN)
        polygon2.set_stroke(width=2).shift(4.9*RIGHT+1.7*DOWN)
        polygon3.set_stroke(width=2).shift(3.9*RIGHT+1.3*UP)
        polygon4.set_stroke(width=2).shift(0.9*RIGHT+0.3*UP)
        #line1 = Line((-2, 1, 0), (-5, 0, 0), color=RED)
        #line2 = Line((-3, 1, 0), (-2, -2, 0), color=RED)
        equation = TexMobject("a^{2}+b^{2}=c^{2}")
        equation.scale(1.5).move_to(4.25*RIGHT+0.5*UP)
        logo = ImageMobject("assets/images/circle-cropped.png")
        logo.move_to(5.5*RIGHT+2.5*DOWN)
        # funny coordinate x=2.1, y=2.7 when bottom left corner hit origin
        #self.add(grid)
        self.add(text)
        self.add(triangle)
        self.add(square1)
        self.add(square2)
        self.add(square3)
        self.add(polygon1)
        self.add(polygon2)
        self.add(polygon3)
        self.add(polygon4)
        self.add(equation)
        self.add(logo)

# Logo + End Scenes use from similartrianglesvid

class Proof3(Scene):
    def construct(self):
        self.proof4wayscopy()
        self.proofpart()

    def proofpart(self):
        grid = ScreenGrid()
        proof3title = TextMobject("Dissection Proof")
        proof3title.scale(1.8).move_to(2.9*UP).set_color(YELLOW)
        a = TexMobject("a^{2}")
        b = TexMobject("b^{2}")
        c = TexMobject("c^{2}")
        a.move_to(1.5*LEFT+2.5*DOWN).set_color(BLACK)
        b.move_to(3.5*LEFT+0.5*DOWN).set_color(BLACK)
        c.set_color(BLACK)
        triangle = Polygon((-2, 1, 0), (-2, -2, 0), (-1, -2, 0))
        triangle.set_stroke(width=1.5).set_fill(BLUE, opacity=0.7)
        braceontriangle0 = Brace(triangle, LEFT)
        braceontriangle1 = Brace(triangle, DOWN)
        braceontriangle2 = Brace(triangle, np.array([3, 1, 0]))
        eqtest0 = braceontriangle0.get_tex("b")
        eqtest1 = braceontriangle1.get_tex("a")
        eqtest2 = braceontriangle2.get_tex("c")
        rightangle = Polygon((-2.9, 0.7, 0), (-2.9+3/(5*math.sqrt(10)), 0.7+1/(5*math.sqrt(10)), 0), (-2.9+4/(5*math.sqrt(10)), 0.7-2/(5*math.sqrt(10)), 0), (-2.9+1/(5*math.sqrt(10)), 0.7-3/(5*math.sqrt(10)), 0), color=BLUE)
        rightangle.set_stroke(width=1.5)
        square1 = Square(color=BLUE)
        square2 = Square(color=BLUE)
        square3 = Square(color=BLUE)
        square4 = Square(color=BLUE)
        square1.scale(1.5).move_to(3.5*LEFT+0.5*DOWN).set_stroke(width=2).set_fill(ORANGE, opacity=0.7)
        square2.scale(0.5).move_to(1.5*LEFT+2.5*DOWN).set_stroke(width=2).set_fill(ORANGE, opacity=0.7)
        square3.scale(math.sqrt(10)/2).rotate(np.arcsin(1/math.sqrt(10))).set_stroke(width=2).set_fill(YELLOW_B, opacity=0.7)
        square4.scale(0.5).move_to(0.6*LEFT+1.2*DOWN).set_stroke(width=2).set_fill(ORANGE, opacity=0.5)
        polygon1 = Polygon((-3, 1, 0), (-2, 1, 0), (-2.9, 0.7, 0), color=BLUE)
        polygon2 = Polygon((-3, 1, 0), (-5, 1, 0), (-5, 0, 0), (-2.9, 0.7, 0), color=BLUE)
        polygon3 = Polygon((-5, 0, 0), (-5, -2, 0), (-2, -2, 0), (-2.9, 0.7, 0), color=BLUE)
        polygon4 = Polygon((-2, -2, 0), (-2, 1, 0), (-2.9, 0.7, 0), color=BLUE)
        polygon5 = Polygon((-3, 1, 0), (-2, 1, 0), (-2.9, 0.7, 0), color=BLUE)
        polygon6 = Polygon((-3, 1, 0), (-5, 1, 0), (-5, 0, 0), (-2.9, 0.7, 0), color=BLUE)
        polygon7 = Polygon((-5, 0, 0), (-5, -2, 0), (-2, -2, 0), (-2.9, 0.7, 0), color=BLUE)
        polygon8 = Polygon((-2, -2, 0), (-2, 1, 0), (-2.9, 0.7, 0), color=BLUE)
        polygon1.set_stroke(width=2).shift(1.9*RIGHT+2.7*DOWN).set_fill(ORANGE, opacity=0.5)
        polygon2.set_stroke(width=2).shift(4.9*RIGHT+1.7*DOWN).set_fill(ORANGE, opacity=0.5)
        polygon3.set_stroke(width=2).shift(3.9*RIGHT+1.3*UP).set_fill(ORANGE, opacity=0.5)
        polygon4.set_stroke(width=2).shift(0.9*RIGHT+0.3*UP).set_fill(ORANGE, opacity=0.5)
        polygon5.set_stroke(width=1.5)
        polygon6.set_stroke(width=1.5)
        polygon7.set_stroke(width=1.5)
        polygon8.set_stroke(width=1.5)
        line1 = Line((-2, 1, 0), (-5, 0, 0), color=BLUE)
        line2 = Line((-3, 1, 0), (-2, -2, 0), color=BLUE)
        line1.set_stroke(width=1.5)
        line2.set_stroke(width=1.5)
        equation = TexMobject("a^{2}+b^{2}=c^{2}")
        equation.scale(1.5).move_to(4.25*RIGHT+0.5*UP)
        # funny coordinate x=2.1, y=2.7 when bottom left corner hit origin
        #self.add(grid)
        self.play(Write(proof3title))
        self.play(DrawBorderThenFill(triangle))
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
        self.play(DrawBorderThenFill(square2))
        self.play(DrawBorderThenFill(square1))
        self.play(DrawBorderThenFill(square3))
        self.wait(3)
        self.play(Write(a))
        self.play(Write(b))
        self.play(Write(c))
        self.wait(3)
        self.play(ShowCreation(line1))
        self.wait(6)
        self.play(ShowCreation(line2))
        self.wait()
        self.play(ShowCreation(rightangle))
        self.add(polygon5)
        self.add(polygon6)
        self.add(polygon7)
        self.add(polygon8)
        self.wait(7)
        self.play(
            Indicate(polygon5),
            Indicate(polygon6),
            Indicate(polygon7),
            Indicate(polygon8),
            lag_ratio=0.5
        )
        self.wait()
        self.play(Indicate(polygon5))
        self.play(Transform(polygon5, polygon1))
        self.play(Indicate(polygon6))
        self.play(Transform(polygon6, polygon2))
        self.play(Indicate(polygon7))
        self.play(Transform(polygon7, polygon3))
        self.play(Indicate(polygon8))
        self.play(Transform(polygon8, polygon4))
        self.wait()
        self.play(Indicate(square2))
        self.play(Transform(square2.copy(), square4))
        self.wait(7)
        self.play(Write(equation))
        self.wait(2)

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

class TryThisAtHome(Scene):
    def construct(self):
        text1 = TextMobject("Try this at home!")
        text1.scale(2)
        text2 = TextMobject("See if the proof works out for you")
        text2.scale(1.2).set_color(BLUE_B)
        text3 = TextMobject("Before we start")
        text3.scale(2).move_to(2.8*UP).set_color(YELLOW)
        circle = Ellipse(width=9, height=2.5)
        circle.set_color(RED)

        self.wait()
        self.play(Write(text3))
        self.wait()
        self.play(Write(text1), ShowCreation(circle))
        self.wait(4)
        self.play(Uncreate(text1), Uncreate(circle))
        self.play(Write(text2))
        self.wait(2)
        self.play(Uncreate(text2), Uncreate(text3))
        self.wait()