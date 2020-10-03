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
        text[7:].set_color(YELLOW)
        square1 = Square(color=RED)
        square2 = Square(color=RED)
        square1.set_stroke(width=3)
        square2.set_stroke(width=3)
        square1.scale(2)
        square2.scale(2)
        square1.move_to(3*LEFT)
        square2.move_to(3*RIGHT)
        polygon1 = Polygon((-5, 1, 0), (-5, 2, 0), (-2, 2, 0))
        polygon2 = Polygon((-2, 2, 0), (-1,-1, 0), (-1, 2, 0))
        polygon3 = Polygon((-1, -1, 0), (-4, -2, 0), (-1, -2, 0))
        polygon4 = Polygon((-4, -2, 0), (-5, 1, 0), (-5, -2, 0))
        polygon5 = Polygon((4, 2, 0), (5, 2, 0), (4, -1, 0))
        polygon6 = Polygon((5, 2, 0), (4, -1, 0), (5, -1, 0))
        polygon7 = Polygon((4, -1, 0), (4, -2, 0), (1, -2, 0))
        polygon8 = Polygon((1, -2, 0), (1, -1, 0), (4, -1, 0))
        trianglea = VGroup(polygon1, polygon2, polygon3, polygon4)
        triangleb = VGroup(polygon5, polygon6, polygon7, polygon8)
        trianglea.set_fill(YELLOW, opacity=1).set_stroke(width=1.5)
        triangleb.set_fill(YELLOW, opacity=1).set_stroke(width=1.5)
        arrow = Arrow((-0.75,0,0), (0.75,0,0))
        arrow.set_stroke(width=5)
        equation = TexMobject("a^{2}+b^{2}=c^{2}")
        equation.scale(1.5).move_to(3*DOWN)
        logo = ImageMobject("assets/images/circle-cropped.png")
        logo.move_to(5.5*RIGHT+2.5*DOWN)

        self.add(square1)
        self.add(square2)
        self.add(text)
        self.add(arrow)
        self.add(trianglea)
        self.add(triangleb)
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
        
class Quote(OpeningQuote):
    CONFIG = {
        "quote" : [
            "Reason", "is immortal, all else mortal."
        ],
        "quote_arg_separator" : " ",
        "highlighted_quote_terms" : {
            "Reason" : BLUE
        },
        "author" : "Pythagoras",
    }

class Intro(Scene):
    def construct(self):
        #More to come
        #grid = ScreenGrid()
        image1 = ImageMobject("assets/images/pythagoraspic.jpg")
        image1.scale(2).move_to(3*LEFT)
        text1 = TextMobject("Pythagoras of Samos")
        text1.move_to(3*LEFT+2.8*DOWN) 
        text2 = TexMobject("a^{2}+b^{2}=c^{2}")
        text2.scale(1.8).move_to(3*RIGHT)
        text3 = TextMobject("Pythagorean")
        text3.move_to(3*RIGHT+2.5*UP).set_color(TEAL_D).scale(1.3)
        text4 = TextMobject("Theorem")
        text4.move_to(3*RIGHT+1.8*UP).set_color(TEAL_C).scale(1.3)
        text5 = TextMobject("But why?")
        text5.scale(3)
        circle = Ellipse(width=6, height=2, color=RED)
        circle.move_to(3*RIGHT)
        circle1 = Ellipse(width=8, height=3)
        triangle = Polygon((-3, -1.5, 0), (3, -1.5, 0), (3, 1.5, 0))
        triangle.set_fill(GREEN, opacity=0.4).set_stroke(width=1.5)
        braceontriangle0 = Brace(triangle, RIGHT)
        braceontriangle1 = Brace(triangle, DOWN)
        braceontriangle2 = Brace(triangle, np.array([-3, 6, 0]))
        eqtest0 = braceontriangle0.get_tex("a")
        eqtest1 = braceontriangle1.get_tex("b")
        eqtest2 = braceontriangle2.get_tex("c")
        
        #self.add(grid)
        self.play(FadeIn(image1))
        self.play(Write(text1))
        self.wait(2)
        self.play(GrowFromCenter(text2))
        self.play(ShowCreation(circle))
        self.play(Write(text3), Write(text4))
        self.wait()
        self.play(FadeOut(image1), Uncreate(text1), FadeOutAndShiftDown(text2), Uncreate(circle), ShrinkToCenter(text3), ShrinkToCenter(text4))
        self.wait(2)
        self.play(DrawBorderThenFill(triangle))
        self.play(GrowFromCenter(braceontriangle0), Write(eqtest0))
        self.play(GrowFromCenter(braceontriangle1), Write(eqtest1))
        self.play(GrowFromCenter(braceontriangle2), Write(eqtest2))
        self.wait()
        self.play(Uncreate(triangle), ShrinkToCenter(braceontriangle0), ShrinkToCenter(braceontriangle1), ShrinkToCenter(braceontriangle2), FadeOut(eqtest0), FadeOut(eqtest1), FadeOut(eqtest2))
        self.wait(2)
        self.play(FadeIn(text5))
        self.play(ShowCreation(circle1))
        self.wait()


class Proofs(Scene):
    def proof4wayscopy(self):
        #grid = ScreenGrid()
        line = Line((-6, 2, 0), (6, 2, 0))
        title1 = TextMobject("The 4 Proofs")
        title1.scale(2).move_to(2.9*UP)
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
        title1.set_color(YELLOW)

        #self.add(grid)
        self.play(ShowCreation(line))
        self.play(Write(proofs))
        self.play(Write(title1))

class Proof1(Scene):
    def construct(self):
        self.proof4ways()
        self.the1proof()
    
    def the1proof(self):
        #grid = ScreenGrid()
        square0 = Square(color=RED)
        square1 = Square(color=RED)
        square2 = Square(color=RED)
        square0.set_stroke(width=3)
        square1.set_stroke(width=3)
        square2.set_stroke(width=3)
        square0.scale(2)
        square1.scale(2)
        square2.scale(2)
        square1.move_to(3*LEFT)
        square2.move_to(3*RIGHT)
        specialpolygon1 = Polygon((-3, -1, 0), (3, -1, 0), (3, 1, 0))
        specialpolygon2 = Polygon((-1.5, -0.5, 0), (1.5, -0.5, 0), (1.5, 0.5, 0))
        specialpolygon3 = Polygon((-5.5, -0.5, 0), (-2.5, -0.5, 0), (-2.5, 0.5, 0))
        polygon1 = Polygon((-5, 1, 0), (-5, 2, 0), (-2, 2, 0))
        polygon2 = Polygon((-2, 2, 0), (-1,-1, 0), (-1, 2, 0))
        polygon3 = Polygon((-1, -1, 0), (-4, -2, 0), (-1, -2, 0))
        polygon4 = Polygon((-4, -2, 0), (-5, 1, 0), (-5, -2, 0))
        polygon9 = Polygon((-2, 1, 0), (-2, 2, 0), (1, 2, 0))
        polygon10 = Polygon((1, 2, 0), (2,-1, 0), (2, 2, 0))
        polygon11 = Polygon((2, -1, 0), (-1, -2, 0), (2, -2, 0))
        polygon12 = Polygon((-1, -2, 0), (-2, 1, 0), (-2, -2, 0))
        polygon5 = Polygon((4, 2, 0), (5, 2, 0), (4, -1, 0))
        polygon6 = Polygon((5, 2, 0), (4, -1, 0), (5, -1, 0))
        polygon7 = Polygon((4, -1, 0), (4, -2, 0), (1, -2, 0))
        polygon8 = Polygon((1, -2, 0), (1, -1, 0), (4, -1, 0))
        trianglea = VGroup(polygon1, polygon2, polygon3, polygon4)
        triangleb = VGroup(polygon5, polygon6, polygon7, polygon8)
        trianglec = VGroup(polygon9, polygon10, polygon11, polygon12)
        trianglea.set_fill(YELLOW, opacity=1).set_stroke(width=1.5)
        triangleb.set_fill(YELLOW, opacity=1).set_stroke(width=1.5)
        trianglec.set_fill(YELLOW, opacity=1).set_stroke(width=1.5)
        specialpolygon1.set_fill(BLUE, opacity=1)
        specialpolygon2.set_fill(BLUE, opacity=1)
        specialpolygon3.set_fill(YELLOW, opacity=1)
        braces = Brace(specialpolygon1, RIGHT)
        braces1 = Brace(specialpolygon1, DOWN)
        braces2 = Brace(square1, LEFT)
        braces3 = Brace(square2, LEFT)
        braces4 = Brace(specialpolygon1, np.array([-2, 6, 0]))
        eq_text = braces.get_tex("a")
        eq_text1 = braces1.get_tex("b")
        eq_text2 = braces2.get_tex("a+b")
        eq_text3 = braces3.get_tex("a+b")
        eq_text4 = braces4.get_tex("c")
        squarea = Square(color=ORANGE)
        squarea.scale(0.5).move_to(4.5*RIGHT+1.5*DOWN).set_fill(ORANGE, opacity=0.5)
        squareb = Square(color=ORANGE)
        squareb.scale(1.5).move_to(2.5*RIGHT+0.5*UP).set_fill(ORANGE, opacity=0.5)
        squarec = Square(color=ORANGE)
        squarec.scale(math.sqrt(10)/2).move_to(3*LEFT).set_fill(ORANGE, opacity=0.5).rotate(np.arcsin(1/math.sqrt(10)))
        tbraces1 = Brace(polygon1, LEFT)
        tbraces2 = Brace(polygon4, LEFT)
        tbraces3 = Brace(polygon7, LEFT)
        tbraces4 = Brace(squareb, LEFT)
        teq_text1 = tbraces1.get_tex("a")
        teq_text2 = tbraces2.get_tex("b")
        teq_text3 = tbraces3.get_tex("a")
        teq_text4 = tbraces4.get_tex("b")
        area1 = TexMobject("\\left(a+b\\right)^{2}")
        area1.move_to(3*LEFT+2.5*DOWN)
        area2 = TexMobject("\\left(a+b\\right)^{2}")
        area2.move_to(3*RIGHT+2.5*DOWN)
        asquared = TexMobject("a^2")
        asquared.move_to(4.5*RIGHT+1.5*DOWN)
        bsquared = TexMobject("b^{2}")
        bsquared.move_to(2.5*RIGHT+0.5*UP)
        csquared = TexMobject("c^{2}")
        csquared.move_to(3*LEFT)
        allsquared = VGroup(asquared, bsquared, csquared)
        theorem = TexMobject("a^{2}+b^{2}=c^{2}")
        theorem.move_to(3*DOWN).scale(1.5)

        #self.add(grid)
        self.play(DrawBorderThenFill(specialpolygon1))
        self.wait()
        self.play(GrowFromCenter(braces), Write(eq_text), GrowFromCenter(braces1), Write(eq_text1), GrowFromCenter(braces4), Write(eq_text4))
        self.wait(3)
        self.play(ShrinkToCenter(braces), FadeOut(eq_text), ShrinkToCenter(braces1), FadeOut(eq_text1), ShrinkToCenter(braces4), FadeOut(eq_text4))
        self.play(ReplacementTransform(specialpolygon1, specialpolygon2))
        self.play(ReplacementTransform(specialpolygon2, specialpolygon3))
        self.wait(1.5)
        self.play(ShowCreation(square0))
        self.wait(1.5)
        self.play(ReplacementTransform(specialpolygon3, trianglec))
        self.play(Transform(square0, square1), Transform(trianglec,trianglea))
        self.wait(1.5)
        self.play(ReplacementTransform(square1.copy(), square2))
        self.wait(1.5)
        self.play(ReplacementTransform(trianglea.copy(), triangleb))
        self.wait(3)
        self.play(
            GrowFromCenter(tbraces1),
            GrowFromCenter(tbraces2),
            GrowFromCenter(tbraces3),
            GrowFromCenter(tbraces4),
            Write(teq_text1),
            Write(teq_text2),
            Write(teq_text3),
            Write(teq_text4),
        )
        self.wait(3)
        self.play(
            FadeOut(tbraces1),
            FadeOut(tbraces3),
            Uncreate(teq_text1),
            Uncreate(teq_text3),
            Transform(tbraces2, braces2),
            Transform(tbraces4, braces3),
            Transform(teq_text2, eq_text2),
            Transform(teq_text4, eq_text3),
        )
        self.play(Write(area1), Write(area2))
        self.wait(4)
        self.play(
            FadeIn(asquared), 
            FadeIn(bsquared), 
            FadeIn(csquared), 
            DrawBorderThenFill(squarea), 
            DrawBorderThenFill(squareb), 
            DrawBorderThenFill(squarec),
            FadeOut(area1),
            FadeOut(area2),
        )
        self.wait(4)
        self.play(Write(theorem))
        self.wait(4)
    
    def proof4ways(self):
        #grid = ScreenGrid()
        line = Line((-6, 2, 0), (6, 2, 0))
        title1 = TextMobject("The 4 Proofs")
        title1.scale(2).move_to(2.9*UP).set_color(YELLOW)
        proof1title = TextMobject("Rearrangement Proof")
        proof1title.scale(1.8).move_to(2.9*UP).set_color(YELLOW)
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
        self.play(Transform(proofs[0], proof1title), FadeOut(proofs[1:]), FadeOut(title1), Uncreate(line))
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
        arrow2 = Arrow((0, 1, 0), (0, -0.5, 0))
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

class Test(Scene):
    def construct(self):
        self.show_proof()

    def show_proof(self):
        triangle = Polygon(
            ORIGIN, 12*RIGHT, 12*RIGHT+10*UP,
            stroke_color = WHITE,
            stroke_width = 2,
            fill_color = WHITE,
            fill_opacity = 0.5
        )
        triangle.set_height(3)
        triangle.center()
        side_labels = self.get_triangle_side_labels(triangle)

        self.add(triangle)
        self.play(Write(side_labels))
        self.wait(2)
    
    def get_triangle_side_labels(self, triangle):
        a, b, c = list(map(TexMobject, "abc"))
        a.next_to(triangle, RIGHT)
        b.next_to(triangle, DOWN)
        c.next_to(triangle.get_center(), LEFT, buff=0.6)
        return VGroup(a, b, c)