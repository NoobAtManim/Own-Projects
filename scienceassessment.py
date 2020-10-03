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

class Test(Scene):
    def construct(self):
        v = ValueTracker(10)
        a = Integer().add_updater(lambda m:m.set_value(v.get_value()))
        self.add(a)
        self.play(v.set_value, 100)
        triangle = Polygon(ORIGIN, RIGHT, RIGHT+UP)
        elbow = Elbow(color=RED)
        elbow.set_points_as_corners([ORIGIN, RIGHT, RIGHT+UP])
        elbow.set_width(elbow.width, about_point=RIGHT+np.array([-0.1, 0.1, 0.0]))
        self.add(triangle)
        self.add(elbow)
        self.wait(2)

class Photo(Scene):
    def construct(self):
        text1 = TextMobject("Changes in the")
        text2 = TextMobject("Physical and Chemical World")
        text3 = TextMobject("by Jerry Jin")
        text1.scale(2).move_to(1.5*UP).set_color_by_gradient(GREEN_B, YELLOW)
        text2.scale(2).set_color_by_gradient(BLUE, YELLOW)
        text3.move_to(2*DOWN+3*RIGHT).set_color(GRAY)
        box = Polygon((1.5, -2.4, 0), (4.5, -2.4, 0), (4.5, -1.6, 0), (1.5, -1.6, 0), color=DARK_BLUE)

        self.add(text1)
        self.add(text2)
        self.add(text3)
        self.add(box)

class Title(Scene):
    def construct(self):
        #grid = ScreenGrid()
        text1 = TextMobject("Changes in the")
        text2 = TextMobject("Physical and Chemical World")
        text3 = TextMobject("by Jerry Jin")
        text1.scale(2).move_to(1.5*UP).set_color_by_gradient(GREEN_B, YELLOW)
        text2.scale(2).set_color_by_gradient(BLUE, YELLOW)
        text3.move_to(2*DOWN+3*RIGHT).set_color(GRAY)
        box = Polygon((1.5, -2.4, 0), (4.5, -2.4, 0), (4.5, -1.6, 0), (1.5, -1.6, 0), color=DARK_BLUE)
        
        #self.add(grid)
        self.play(Write(text1), Write(text2))
        self.play(Write(text3), ShowCreation(box))
        self.wait(3)
        self.play(
            Uncreate(text1),
            Uncreate(text2),
            Uncreate(text3),
            Uncreate(box)
        )

class Matter(ThreeDScene):
    CONFIG={
        "plane_kwargs" : {
            "color" : RED_B
        },
        "point_change_loc" : 0.5*RIGHT+-1.5*UP,
    }
    def construct(self):
        self.matter()
        self.mass()
        self.massmeasure()
        self.menu()
        self.volume()

    def matter(self):
        #grid = ScreenGrid()
        title = TextMobject("What is Matter?")
        title.scale(1.8)
        circle = Ellipse(width=8, height=2)
        title[0][6:].set_color(YELLOW)
        line = Line((-6, 2, 0), (6, 2, 0))
        title1 = TextMobject("Matter is anything")
        title1.scale(2).move_to(2.9*UP)
        title1.set_color(YELLOW)
        proofs = TextMobject(
            "1. That has mass\\\\",
            "\\\\"
            "2. That has volume\\\\",
            alignment="",
        )

        proofs.arrange_submobjects(DOWN, buff=0.9, aligned_edge=LEFT).scale(1.3).move_to(0.5*DOWN)
        proofs[0][9:].set_color(BLUE)
        proofs[1][9:].set_color(BLUE)

        #self.add(grid)
        self.play(Write(title), ShowCreation(circle), run_time=0.75)
        self.wait()
        self.play(Uncreate(title), Uncreate(circle), run_time=0.75)
        self.wait()
        self.play(Write(title1), ShowCreation(line))
        self.play(Write(proofs[0]))
        self.play(Indicate(proofs[0][9:]))
        self.play(Write(proofs[1]))
        self.play(Indicate(proofs[1][9:]))
        self.wait(0.5)
        self.play(FadeOut(proofs), FadeOut(title1), Uncreate(line))
        self.wait()

    def mass(self):
        #grid = ScreenGrid()
        text1 = TextMobject("Mass")
        text2 = TextMobject('"Heavy"')
        text3 = TextMobject('"Light"')
        text1.scale(1.5).move_to(4*LEFT+1*UP)
        text2.scale(1.5).move_to(2*UP).set_color(YELLOW)
        text3.scale(1.5).move_to(2*UP+4*RIGHT).set_color(YELLOW)
        number1 = TextMobject("1")
        number1.move_to(2.5*DOWN+1*LEFT)
        weightmeasure1 = TextMobject("kg")
        weightmeasure1.move_to(1*DOWN+0.6*RIGHT)
        numwei1 = TextMobject("1g")
        numwei1.move_to(1*DOWN+4*RIGHT)
        cube = Cube(color=GREY)
        cube.rotate(PI/4, UP).rotate(-PI/6, RIGHT).flip(UP).scale(0.5).move_to(2.5*DOWN).set_fill(WHITE, opacity=0.7)
        image1 = ImageMobject("assets/images/download.jfif")
        image2 = ImageMobject("assets/images/download (1).jfif") 
        image3 = ImageMobject("assets/images/Da90E.jpg") 
        image1.move_to(4*LEFT+0.5*DOWN)
        image2.move_to(0.5*UP).scale(0.75)
        image3.move_to(0.5*UP+4*RIGHT).scale(0.75)
        v = ValueTracker(1)
        a = Integer().add_updater(lambda m:m.set_value(v.get_value()))
        a.move_to(1*DOWN+0.8*LEFT)

        #self.add(grid)
        self.play(Write(text1))
        self.play(FadeIn(image1))
        self.play(FadeIn(image2), run_time=2)
        self.play(FadeIn(cube), Write(number1))
        self.wait(2)
        self.play(Write(a), Write(weightmeasure1))
        self.play(v.set_value, 7300)
        self.wait()
        self.play(FadeInFrom(text2, UP))
        self.wait(2)
        self.play(FadeIn(image3), run_time=2)
        self.wait()
        self.play(Write(numwei1))
        self.wait()
        self.play(FadeInFrom(text3, UP))
        self.wait(2)
        self.play(
            Uncreate(text1),
            Uncreate(text2),
            Uncreate(text3),
            FadeOut(image1),
            FadeOut(image2),
            FadeOut(image3),
            FadeOut(number1),
            FadeOut(weightmeasure1),
            FadeOut(numwei1),
            FadeOut(a),
            FadeOut(cube)
        )

    def massmeasure(self):
        #grid = ScreenGrid()
        grams = TextMobject("g for grams")
        grams.scale(3)
        table = TexMobject(r"\begin{bmatrix}... & ...\\mg & 0.001g\\ g & 1g\\ kg & 1000g\\... & ... \end{bmatrix}")
        table.scale(1.8)

        #self.add(grid)
        self.play(Write(grams))
        self.wait(2)
        self.play(Uncreate(grams))
        self.play(ShowCreation(table))
        self.wait(4.5)
        self.play(Indicate(table[0][19]), Indicate(table[0][22]), Indicate(table[0][29]), run_time=2)
        self.wait(0.5)
        self.remove(table)

    def menu(self):
        line = Line((-6, 2, 0), (6, 2, 0))
        title1 = TextMobject("Matter is anything")
        title1.scale(2).move_to(2.9*UP)
        title1.set_color(YELLOW)
        proofs = TextMobject(
            "1. That has mass\\\\",
            "\\\\"
            "2. That has volume\\\\",
            alignment="",
        )

        proofs.arrange_submobjects(DOWN, buff=0.9, aligned_edge=LEFT).scale(1.3).move_to(0.5*DOWN)
        proofs[0][9:].set_color(BLUE)
        proofs[1][9:].set_color(BLUE)

        self.add(title1)
        self.add(line)
        self.add(proofs)
        self.wait(0.5)
        self.play(proofs[0][9:].set_color, GREEN)
        self.wait()
        self.play(Indicate(proofs[1][9:]))
        self.wait(0.5)
        self.play(FadeOut(proofs), FadeOut(title1), Uncreate(line))
        self.wait()

    def volume(self):
        #grid = ScreenGrid()
        text1 = TextMobject("Volume = Space")
        text2 = TextMobject('"Small"')
        text3 = TextMobject('"Large"')
        text4 = TextMobject("<")
        text1.scale(2).set_color_by_gradient(RED, BLUE).move_to(3*UP)
        text2.scale(1.5).move_to(5*LEFT).set_color(YELLOW)
        text3.scale(1.5).move_to(5*RIGHT).set_color(YELLOW)
        text4.scale(1.2)
        image1 = ImageMobject("assets/images/vz_eliquid_juicy_red_apple.jpg")
        image2 = ImageMobject("assets/images/image.jpg")
        image1.move_to(2*LEFT).scale(0.75)
        image2.move_to(2*RIGHT).scale(0.75)
        weightmeasure1 = TexMobject("cm^{3}")
        weightmeasure2 = TexMobject("cm^{3}")
        weightmeasure1.move_to(1.4*LEFT+1.1*DOWN)
        weightmeasure2.move_to(3.1*RIGHT+1.1*DOWN)
        v = ValueTracker(1)
        a = Integer().add_updater(lambda m:m.set_value(v.get_value()))
        a.move_to(1.15*DOWN+2.7*LEFT)
        v1 = ValueTracker(1)
        a1 = Integer().add_updater(lambda m:m.set_value(v1.get_value()))
        a1.move_to(1.2*DOWN+0.6*RIGHT)

        #self.add(grid)
        self.play(Write(text1), run_time=3)
        self.play(FadeIn(image1))
        self.wait()
        self.play(Write(a), Write(weightmeasure1))
        self.play(v.set_value, 187)
        self.play(FadeInFrom(text2, LEFT))
        self.wait(2)
        self.play(FadeIn(image2))
        self.play(Write(a1), Write(weightmeasure2))
        self.play(v1.set_value, 3200000)
        self.play(FadeInFrom(text3, RIGHT))
        self.wait(3)
        self.play(FadeInFromPoint(text4, [0, 0, 0]), run_time=2)
        self.wait(3)
        
class Changes(Scene):
    def construct(self):
        self.sizeshape()
        self.state()

    def sizeshape(self):
        #grid = ScreenGrid()
        text1 = TextMobject("Matter can change\\\\", "size, shape and state")
        text2 = TextMobject("Change\\\\" "size")
        text3 = TextMobject("Change\\\\" "shape")
        text1.scale(1.5).set_color_by_gradient(ORANGE, YELLOW).move_to(2.5*UP)
        text2.move_to(4.8*LEFT+0.5*DOWN).set_color(GREEN)
        text3.move_to(4.8*RIGHT+0.5*DOWN).set_color(GREEN)
        arrow1 = Arrow((-2.5, 0, 0), (-2.5, -1, 0))
        arrow2 = Arrow((2.5, 0, 0), (2.5, -1, 0))
        arrow1.set_stroke(width=5)
        arrow2.set_stroke(width=5)
        triangle1 = Polygon((2, 0, 0), (3, 0, 0), (2.5, 1, 0))
        triangle2 = Polygon((1.5, -1, 0), (1.5, -3, 0), (3.5, -3, 0))
        circle1 = Circle(color=BLUE)
        circle2 = Circle(color=BLUE)
        circle1.move_to(2.5*LEFT+0.5*UP).scale(0.5)
        circle2.move_to(2.5*LEFT+2*DOWN)

        #self.add(grid)
        self.play(Write(text1))
        self.wait()
        self.play(ShowCreation(circle1))
        self.play(ShowCreation(arrow1))
        self.play(ReplacementTransform(circle1.copy(), circle2))
        self.play(FadeInFrom(text2, LEFT))
        self.play(ShowCreation(triangle1))
        self.play(ShowCreation(arrow2))
        self.play(ReplacementTransform(triangle1.copy(), triangle2))
        self.play(FadeInFrom(text3, RIGHT))
        self.wait(0.5)
        self.remove(
            circle1,
            circle2,
            arrow1,
            arrow2,
            triangle1,
            triangle2,
            text2,
            text3
        )
        self.wait(0.5)

    def state(self):
        ice = ImageMobject("assets/images/Ice-cubes-background.jpg")
        water = ImageMobject("assets/images/7360.jpg")
        watervapour = ImageMobject("assets/images/download (2).jfif")
        ice.scale(0.75).move_to(0.5*DOWN+3.5*LEFT)
        water.scale(0.75).move_to(0.5*DOWN)
        watervapour.scale(0.75).move_to(0.5*DOWN+3.7*RIGHT)
        arrow1 = Arrow((-2.5, -0.5, 0), (-0.8, -0.5, 0))
        arrow2 = Arrow((0.8, -0.5, 0), (2.5, -0.5, 0))
        text1 = TextMobject("Solid")
        text2 = TextMobject("Liquid")
        text3 = TextMobject("Gas")
        text4 = TextMobject("Change\\\\" "state")
        text1.scale(1.2).move_to(3.5*LEFT+2*DOWN)
        text2.scale(1.2).move_to(2*DOWN)
        text3.scale(1.2).move_to(3.7*RIGHT+2*DOWN)
        text4.move_to(5.8*LEFT+0.5*DOWN).set_color(GREEN)

        self.play(FadeIn(ice), Write(text1))
        self.play(ShowCreation(arrow1), run_time=0.5)
        self.play(FadeIn(water), Write(text2))
        self.play(ShowCreation(arrow2), run_time=0.5)
        self.play(FadeIn(watervapour), Write(text3))
        self.wait(0.5)
        self.play(FadeInFrom(text4, LEFT))
        self.wait(0.5)

class StatePhysical(Scene):
    def construct(self):
        grid = ScreenGrid()
        text1 = TextMobject("The matter changes form")
        text2 = TextMobject("NOT")
        text3 = TextMobject("The matter changes type")
        text1.scale(1.4).set_color(GREEN).move_to(2*UP)
        text2.scale(1.4).set_color(YELLOW)
        text3.scale(1.4).set_color(RED).move_to(2*DOWN)

        #self.add(grid)
        self.wait(3)
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
        self.wait()

class ExampleOfPhysical(Scene):
    def construct(self):
        self.water()
        self.paper()

    def water(self):
        grid = ScreenGrid()
        ice = ImageMobject("assets/images/Ice-cubes-background.jpg")
        water = ImageMobject("assets/images/7360.jpg")
        ice.scale(0.8).move_to(2*LEFT+0.5*DOWN)
        water.scale(0.8).move_to(2*RIGHT+0.5*DOWN)
        dot = Dot(color=YELLOW)
        dot.scale(1.5).move_to(2*UP+4*LEFT)
        text1 = TextMobject("Solid Water")
        text2 = TextMobject("Liquid Water")
        text3 = TextMobject("Sun")
        text4 = TextMobject("Physical Change")
        text1.move_to(2*LEFT+2*DOWN)
        text2.move_to(2*RIGHT+2*DOWN)
        text3.scale(1.2).move_to(2*LEFT+2*UP).set_color(YELLOW)
        text4.scale(1.5).move_to(2.5*UP).set_color(GREEN_B)
        arrow1 = Arrow((-0.7, -0.5, 0), (0.9, -0.5, 0))
        arrow2 = Arrow((-2.5, 2, 0), (-4, 2, 0))
        arrow3 = Arrow((0.9, -0.5, 0), (-0.7, -0.5, 0))

        #self.add(grid)
        self.play(FadeIn(ice), Write(text1))
        self.play(ShowCreation(dot))
        self.play(ShowCreation(arrow2), Write(text3))
        self.wait()
        self.play(Uncreate(arrow2))
        self.play(Flash(dot))
        self.play(Flash(dot), ShowCreation(arrow1))
        self.play(Flash(dot), FadeIn(water), Write(text2), Uncreate(text3))
        self.wait(2)
        self.play(Write(text4))
        self.wait(5.5)
        self.play(Indicate(text1[0][5:]), Indicate(text2[0][6:]), Uncreate(dot))
        self.wait(2.5)
        self.play(Uncreate(arrow1), ShowCreation(arrow3))
        self.wait(2.5)
        self.play(Uncreate(text1), Uncreate(text2), run_time=0.5)
        self.remove(
            arrow3,
            ice,
            water
        )

    def paper(self):
        grid = ScreenGrid()
        paper = ImageMobject("assets/images/paper.png")
        foldedpaper = ImageMobject("assets/images/folding_paper.jpg")
        paper.scale(0.8).move_to(3*LEFT+0.5*DOWN)
        foldedpaper.scale(0.8).move_to(3*RIGHT+0.5*DOWN)
        arrow1 = Arrow((-1.8, 0, 0), (2, 0, 0))
        arrow2 = Arrow((2, -1, 0), (-1.8, -1, 0))
        text1 = TextMobject("Fold")
        text2 = TextMobject("Unfold")
        text3 = TextMobject("Original")
        text4 = TextMobject("In half")
        text1.move_to(0.5*UP)
        text2.move_to(1.5*DOWN)
        text3.move_to(3*LEFT+1.8*DOWN).set_color(RED)
        text4.move_to(3*RIGHT+1.8*DOWN).set_color(RED)

        #self.add(grid)
        self.wait(0.5)
        self.play(FadeIn(paper), Write(text3))
        self.wait(0.5)
        self.play(ShowCreation(arrow1), Write(text1), FadeIn(foldedpaper), Write(text4))
        self.wait(3)
        self.play(ShowCreation(arrow2), Write(text2))
        self.wait(5)

class Chemical(Scene):
    def construct(self):
        self.intro()
        self.irreversible()
        self.properties()

    def intro(self):
        grid = ScreenGrid()
        text1 = TextMobject("Chemical Change")
        text2 = TextMobject("Product")
        text1.set_color(YELLOW).move_to(2.75*UP).scale(1.75)
        text2.move_to(4.5*RIGHT+2*DOWN)
        atom1 = Circle(color=RED)
        atom2 = Circle(color=BLUE)
        atom3 = Circle(color=PURPLE)
        atom1.scale(0.5).set_fill(RED, opacity=1).move_to(2.5*LEFT)
        atom2.scale(0.5).set_fill(BLUE, opacity=1)
        atom3.scale(0.5).set_fill(PURPLE, opacity=1).move_to(2.5*RIGHT)
        plus = TexMobject("+")
        equals = TexMobject("=")
        plus.move_to(1.25*LEFT).scale(1.5)
        equals.move_to(1.25*RIGHT).scale(1.5)
        arrow1 = Arrow((4.7, -1.7, 0), (2.8, -0.3, 0))
        

        #self.add(grid)
        self.play(Write(text1, run_time=2))
        self.wait()
        self.play(FadeInFromPoint(atom1, [-1.5, 0, 0]), FadeInFromPoint(atom2, [-1.5, 0, 0]))
        self.wait(0.5)
        self.play(Write(plus))
        self.wait(0.5)
        self.play(Write(equals))
        self.play(DrawBorderThenFill(atom3))
        self.play(ShowCreation(arrow1), Write(text2))
        self.wait()
        self.remove(
            text1,
            text2,
            atom1,
            atom2,
            atom3,
            plus,
            equals,
            arrow1
        )

    def irreversible(self):
        grid = ScreenGrid()
        text1 = TextMobject("Irreversible!")
        text1.set_color(RED).scale(2).move_to(2.5*UP)
        atom1 = Circle(color=RED)
        atom2 = Circle(color=BLUE)
        atom3 = Circle(color=PURPLE)
        atom1.scale(0.5).set_fill(RED, opacity=1).move_to(2.5*RIGHT)
        atom2.scale(0.5).set_fill(BLUE, opacity=1)
        atom3.scale(0.5).set_fill(PURPLE, opacity=1).move_to(2.5*LEFT)
        plus = TexMobject("+")
        plus.move_to(1.25*RIGHT).scale(1.5)
        arrow1 = Arrow((-2, 0, 0), (-0.5, 0, 0))
        line1 = Line((-1.7, 0.15, 0), (-1.0, -0.15, 0), color=RED)
        line2 = Line((-1.7, -0.15, 0), (-1.0, 0.15, 0), color=RED)
        cross = VGroup(line1, line2)

        #self.add(grid)
        self.wait()
        self.play(Write(text1))
        self.play(DrawBorderThenFill(atom3))
        self.play(ShowCreation(arrow1))
        self.play(
            ShowCreation(cross),
            FadeInFromPoint(atom1, [1.25, 0 ,0]),
            FadeInFromPoint(plus, [1.25, 0 ,0]),
            FadeInFromPoint(atom2, [1.25, 0 ,0])
        )
        self.wait(5)
        self.remove(
            text1,
            atom1,
            atom2,
            atom3,
            arrow1,
            cross,
            plus
        )

    def properties(self):
        grid = ScreenGrid()
        text1 = TextMobject("Signs of a chemical change include:")
        text2 = TextMobject("Change in\\\\" "colour")
        text3 = TextMobject("Change in\\\\" "smell")
        text4 = TextMobject("Change in\\\\" "taste")
        text5 = TextMobject("Gas bubbles\\\\" "appearing")
        text1.scale(1.5).move_to(2.75*UP).set_color(YELLOW)
        text2.move_to(4.5*LEFT+1*DOWN)
        text3.move_to(1.5*LEFT+0.8*UP)
        text4.move_to(1.5*RIGHT+1*DOWN)
        text5.move_to(4.5*RIGHT+0.8*UP)
        colour = ImageMobject("assets/images/download (4).jfif")
        smell = ImageMobject("assets/images/05angier02_600.jpg")
        taste = ImageMobject("assets/images/download (3).jfif")
        gasbubble = ImageMobject("assets/images/19111974-gas-bubbles-going-up-in-mineral-water.jpg")
        colour.scale(0.8).move_to(4.5*LEFT+0.5*UP)
        smell.scale(0.8).move_to(1.5*LEFT+0.7*DOWN)
        taste.scale(0.8).move_to(1.5*RIGHT+0.5*UP)
        gasbubble.scale(0.8).move_to(4.5*RIGHT+0.7*DOWN)

        #self.add(grid)
        self.play(Write(text1), run_time=2)
        self.wait(3)
        self.play(Write(text2), FadeIn(colour))
        self.wait()
        self.play(Write(text3), FadeIn(smell))
        self.wait()
        self.play(Write(text4), FadeIn(taste))
        self.wait()
        self.play(Write(text5), FadeIn(gasbubble))
        self.wait()

class ChemicalExample(Scene):
    def construct(self):
        self.cake()
        self.eggs()

    def cake(self):
        grid = ScreenGrid()
        text1 = TextMobject("Chemical Change")
        text2 = TextMobject("Batter")
        text3 = TextMobject("Cake")
        text4 = TextMobject("No unbaking!")
        text1.set_color(YELLOW).move_to(2.75*UP).scale(1.75)
        text2.move_to(4*LEFT+1.2*DOWN)
        text3.move_to(1.2*DOWN)
        text4.move_to(4*RIGHT).set_color(RED).scale(1.5)
        cakebatter = ImageMobject("assets/images/vanilla-cake-batter.jpg")
        cake = ImageMobject("assets/images/54f4a5df2e61b_-_gettyimages_182875449.jpg")
        cakebatter.scale(0.8).move_to(4*LEFT)
        cake.scale(0.8)
        arrow1 = Arrow((-3.5, 0, 0), (-1.2, 0 ,0))
        bulletlist = BulletedList("Changed colour\\\\", "Smells better\\\\", "Tastes better\\\\", "Bubbles in the cake\\\\", buff=MED_LARGE_BUFF)
        bulletlist.move_to(4.3*RIGHT+0.5*DOWN).set_color(BLUE)

        #self.add(grid)
        self.play(Write(text1))
        self.play(FadeIn(cakebatter), Write(text2))
        self.play(ShowCreation(arrow1))
        self.play(FadeIn(cake), Write(text3))
        self.wait()
        self.play(Write(bulletlist), run_time=2)
        self.wait(5)
        self.play(Uncreate(bulletlist))
        self.play(Write(text4))
        self.wait(4)
        self.play(
            Uncreate(text2),
            Uncreate(text3),
            Uncreate(text4),
            Uncreate(arrow1),
            FadeOut(cakebatter),
            FadeOut(cake)
        )
        self.wait()
        self.remove(text1)

    def eggs(self):
        grid = ScreenGrid()
        text1 = TextMobject("Raw egg")
        text2 = TextMobject("Fried egg")
        text3 = TextMobject("No unfrying!")
        text4 = TextMobject("Chemical Change")
        text1.move_to(4*LEFT+1.2*DOWN)
        text2.move_to(1.2*DOWN)
        text3.move_to(4*RIGHT).set_color(RED).scale(1.5)
        text4.set_color(YELLOW).move_to(2.75*UP).scale(1.75)
        rawegg = ImageMobject("assets/images/cracked-raw-egg.png")
        friedegg = ImageMobject("assets/images/crispy-fried-egg-recipe.jpg")
        rawegg.move_to(4*LEFT).scale(0.8)
        friedegg.scale(0.8)
        arrow1 = Arrow((-2.4, 0, 0), (-0.6, 0, 0))
        bulletlist = BulletedList("Becomes white\\\\", "Smells more eggy\\\\", "Tastes better\\\\", "Bubbles in the egg white\\\\", buff=MED_LARGE_BUFF)
        bulletlist.move_to(4.3*RIGHT+0.5*DOWN).set_color(BLUE)


        #self.add(grid)
        self.add(text4)
        self.play(FadeIn(rawegg), Write(text1))
        self.play(ShowCreation(arrow1))
        self.play(FadeIn(friedegg), Write(text2))
        self.wait()
        self.play(Write(bulletlist), run_time=2)
        self.wait(5)
        self.play(Uncreate(bulletlist))
        self.play(Write(text3))
        self.wait(4)
        self.play(
            Uncreate(text1),
            Uncreate(text2),
            Uncreate(text3),
            Uncreate(text4),
            Uncreate(arrow1),
            FadeOut(rawegg),
            FadeOut(friedegg)
        )
        self.wait()

class EndingScene(Scene):
    def construct(self):
        grid = ScreenGrid()
        text1 = TextMobject("So what have we learnt?")
        text2 = TextMobject("Mass = Heavy or Light")
        text3 = TextMobject("Volume = Space it takes up")
        text4 = TextMobject("Physical change is")
        text5 = TextMobject("Chemical change is")
        text6 = TextMobject("Two types of changes")
        text7 = TextMobject("Physical change")
        text8 = TextMobject("Chemical change")
        bulletlist1 = BulletedList("A change in size\\\\", "A change in shape\\\\", "A change in state\\\\", "Reversible\\\\", buff=MED_LARGE_BUFF)
        bulletlist2 = BulletedList("A change in colour\\\\", "A change in smell\\\\", "A change in taste\\\\", "Gas bubbles appearing", "Irreversible\\\\", buff=MED_LARGE_BUFF)
        text1.scale(1.5).set_color(RED)
        text2.move_to(1.5*UP).scale(1.5)
        text3.move_to(1.5*DOWN).scale(1.5)
        text4.scale(2).move_to(2.9*UP).set_color(YELLOW)
        text5.scale(2).move_to(2.9*UP).set_color(YELLOW)
        text6.move_to(2.75*UP).scale(1.5).set_color(GREEN)
        text7.move_to(3*LEFT+0.5*DOWN)
        text8.move_to(3*RIGHT+0.5*DOWN)
        bulletlist1.set_color(BLUE_B).move_to(1*DOWN)
        bulletlist2.set_color(BLUE_B).move_to(1*DOWN)
        line = Line((-6, 2, 0), (6, 2, 0))
        line1 = Line((-6, 2, 0), (6, 2, 0))
        title1 = TextMobject("Matter is anything")
        title1.scale(2).move_to(2.9*UP)
        title1.set_color(YELLOW)
        proofs = TextMobject(
            "1. That has mass\\\\",
            "\\\\"
            "2. That has volume\\\\",
            alignment="",
        )

        proofs.arrange_submobjects(DOWN, buff=0.9, aligned_edge=LEFT).scale(1.3).move_to(0.5*DOWN)
        proofs[0][9:].set_color(BLUE)
        proofs[1][9:].set_color(BLUE)

        #self.add(grid)
        self.play(Write(text1))
        self.wait(0.5)
        self.play(Uncreate(text1))
        self.play(Write(title1), ShowCreation(line))
        self.play(Write(proofs[0]))
        self.play(Indicate(proofs[0][9:]))
        self.play(Write(proofs[1]))
        self.play(Indicate(proofs[1][9:]))
        self.wait(0.5)
        self.play(FadeOut(proofs), FadeOut(title1), Uncreate(line))
        self.wait()
        self.play(Write(text2))
        self.wait()
        self.play(Write(text3))
        self.wait()
        self.play(FadeOut(text2), FadeOut(text3))
        self.play(Write(text6))
        self.play(Write(text7), Write(text8))
        self.play(Indicate(text7), run_time=2)
        self.play(Indicate(text8), run_time=2)
        self.play(
            Uncreate(text6),
            Uncreate(text7),
            Uncreate(text8)
        )
        self.play(Write(text4), ShowCreation(line1))
        self.play(Write(bulletlist1), run_time=2)
        self.wait(3)
        self.play(Uncreate(text4), Uncreate(bulletlist1))
        self.play(Write(text5))
        self.play(Write(bulletlist2), run_time=2)
        self.wait(5)
        self.play(Uncreate(text5), Uncreate(line1), Uncreate(bulletlist2))
        self.wait()

class End(Scene):
    def construct(self):
        text = TextMobject("Thanks for\\\\" "Watching!")
        text.scale(2).set_color_by_gradient(GREEN, BLUE)
        text1 = TextMobject("video powered by manim")
        text1.set_color(YELLOW).move_to(3.25*DOWN+4.5*RIGHT).scale(0.75)

        self.play(Write(text))
        self.wait(3)
        self.play(Write(text1))
        self.wait(3)