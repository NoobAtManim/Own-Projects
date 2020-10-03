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
        text = TextMobject("Thales's Theorem")
        text.scale(2).to_edge(UP, buff=0.75).set_color(YELLOW)
        circle = Circle(color=BLUE)
        circle.scale(2).move_to(0.5*DOWN).set_stroke(width=2).set_fill(BLUE_B, opacity=0.5)
        triangle = Polygon((0, 1.5, 0), (-2, -0.5, 0), (2, -0.5, 0))
        triangle.set_stroke(width=2).set_color(WHITE)
        square = Square(color=WHITE)
        square.scale(0.1).set_stroke(width=2).move_to(1.5*UP).shift(0.1*math.sqrt(2)*DOWN).rotate_in_place(PI/4)
        logo = ImageMobject("assets/images/circle-cropped.png")
        logo.move_to(5.5*RIGHT+2.5*DOWN)

        #self.add(grid)
        self.add(text)
        self.add(triangle)
        self.add(square)
        self.add(circle)
        self.add(logo)

class LogoScene(Scene):
    def construct(self):
        grid = ScreenGrid()
        logo = ImageMobject("assets/images/circle-cropped.png")
        logo.scale(2.5).move_to(3.5*LEFT)
        text = TextMobject("Aussie MathsKid")
        text.move_to(2.8*RIGHT+1*UP).scale(1.5)
        text1 = TextMobject("Proof of")
        text1.move_to(2.8*RIGHT+0.7*DOWN)
        text2 = TextMobject("Thales's Theorem")
        text2.move_to(2.8*RIGHT+1.4*DOWN).set_color_by_gradient(PURPLE, RED)
        box = Polygon((0.5, -2, 0), (0.5, -0.1, 0), (5.1, -0.1, 0), (5.1, -2, 0), color=DARK_BLUE)

        #self.add(grid)
        self.play(FadeIn(logo))
        self.wait()
        self.play(Write(text))
        self.play(FadeIn(text1), Write(text2), ShowCreation(box))
        self.wait(4)
        self.play(FadeOut(logo), Uncreate(text), Uncreate(box), FadeOutAndShiftDown(text1), FadeOutAndShiftDown(text2))
        self.wait(1)

class Intro(Scene):
    def construct(self):
        circle = Circle(radius = 3, color = BLUE)
        circle.set_stroke(width=2)
        diameter = Line(circle.get_left(), circle.get_right(), color=YELLOW)
        center = Dot(circle.get_center(), color = WHITE)
        fp1 = Dot(circle.get_top())
        fp2 = Dot(circle.get_left())
        fp3 = Dot(circle.get_right())
        point = VectorizedPoint(circle.get_top())
        triangle = Polygon(LEFT, RIGHT, UP)
        triangle.set_stroke(WHITE, width=2)
        def update_triangle(triangle):
            triangle.set_points_as_corners([
                circle.get_left(), circle.get_right(),
                point.get_center(), circle.get_left(),
            ])
        triangle_update_anim = Mobject.add_updater(
            triangle, update_triangle
        )
        triangle_update_anim.update(0)
        perp_mark = VMobject()
        perp_mark.set_points_as_corners([LEFT, DOWN, RIGHT])
        perp_mark.shift(DOWN).set_stroke(width=2)
        perp_mark.scale(0.15, about_point = ORIGIN)
        perp_mark.shift(point.get_center())
        perp_mark.add(point.copy())
        
        self.play(ShowCreation(circle), ShowCreation(center), run_time=2)       
        self.add_foreground_mobject(center)
        self.play(ShowCreation(triangle), run_time=2)
        self.play(Indicate(fp1))
        self.play(Indicate(fp2))
        self.play(Indicate(fp3))
        self.wait()
        self.play(ShowCreationThenFadeOut(diameter), run_time=2)
        self.play(ShowCreation(perp_mark))
        self.add_foreground_mobjects(perp_mark)
        self.add(triangle_update_anim)
        for angle in 0.225*TAU, -0.45*TAU, 0.45*TAU, -0.225*TAU:
            point.generate_target()
            point.target.rotate(angle, about_point = circle.get_center())
            fp1.generate_target()
            fp1.target.rotate(angle, about_point = circle.get_center())

            perp_mark.generate_target()
            perp_mark.target.rotate(angle, about_point = circle.get_center())
            perp_mark.target.rotate(-angle/2, about_point = point.target.get_center())


            self.play(
                MoveToTarget(point),
                MoveToTarget(fp1),
                MoveToTarget(perp_mark),
                path_arc = angle,
                run_time = 2.5,
            )
        self.wait()

class Proof(Scene):
    def construct(self):
        #grid = ScreenGrid()
        circle = Circle(color=BLUE)
        circle.scale(3).set_stroke(width=2)
        center = Dot((-2, 0, 0))
        triangle0 = Polygon((-3, 0, 0), (3, 0, 0), (1.5, 3*math.sqrt(3)/2, 0))
        triangle0.set_color(WHITE).set_stroke(width=2)
        triangle1 = Polygon((-3, 0, 0), ORIGIN, (1.5, 3*math.sqrt(3)/2, 0)) # Left
        triangle1.set_color(RED).set_stroke(width=2)
        triangle2 = Polygon(ORIGIN, (3, 0, 0), (1.5, 3*math.sqrt(3)/2, 0)) # Right
        triangle2.set_color(RED).set_stroke(width=2)
        triangles = VGroup(triangle0, triangle1, triangle2)
        line = Line(ORIGIN, (1.5, 3*math.sqrt(3)/2, 0))
        line.set_stroke(width=2)
        A = TextMobject("A")
        B = TextMobject("B")
        C = TextMobject("C")
        O = TextMobject("O")
        A.move_to(3.35*LEFT)
        B.move_to(1.15*1.5*RIGHT+(1.15*3*math.sqrt(3)/2)*UP)
        C.move_to(3.35*RIGHT)
        O.move_to(0.4*DOWN)
        letters = VGroup(A, B, C, O)
        angle00 = Arc(radius=0.4, angle=PI/6)
        angle01 = Arc(radius=0.4, angle=PI/6)
        angle10 = Arc(radius=0.5, angle=PI/3)
        angle11 = Arc(radius=0.5, angle=PI/3)
        angles = VGroup(
            angle00,
            angle01,
            angle10,
            angle11
        )
        angles.set_stroke(width=2)
        angle00.move_arc_center_to(3*LEFT)
        angle01.rotate_about_origin(210*DEGREES).move_arc_center_to(1.5*RIGHT+(3*math.sqrt(3)/2)*UP)
        angle10.rotate_about_origin(240*DEGREES).move_arc_center_to(1.5*RIGHT+(3*math.sqrt(3)/2)*UP)
        angle11.rotate_about_origin(120*DEGREES).move_arc_center_to(3*RIGHT)
        alpha0 = TexMobject("\\alpha")
        alpha1 = TexMobject("\\alpha")
        beta0 = TexMobject("\\beta")
        beta1 = TexMobject("\\beta")
        alpha0.move_to(2.35*LEFT+(0.65*(math.sqrt(3)-1)/(math.sqrt(3)+1))*UP).scale(0.8)
        alpha1.move_to(1*RIGHT+((3*math.sqrt(3)/2)-0.5)*UP).scale(0.8)
        beta0.move_to(1.5*RIGHT+1.8*UP).scale(0.8)
        beta1.move_to(2.35*RIGHT+(0.65/math.sqrt(3))*UP).scale(0.8)
        signab = VGroup(alpha1, beta0)
        signs = VGroup(alpha0, alpha1, beta0, beta1)
        diagram = VGroup(circle, triangles, line, letters, angles, signs)
        diagram.shift(2*LEFT)
        rad1 = Line(ORIGIN, (-3, 0, 0))
        rad2 = Line(ORIGIN, (1.5, 3*math.sqrt(3)/2, 0))
        rad3 = Line(ORIGIN, (3, 0, 0))
        rads = VGroup(rad1, rad2, rad3)
        rads.shift(2*LEFT).set_stroke(width=2).set_color(YELLOW)
        equation1 = TexMobject("\\alpha+(\\alpha+\\beta)+\\beta=180^{\\circ}")
        equation1.move_to(4*RIGHT+1.5*UP)
        equation2 = TexMobject("2\\alpha+2\\beta=180^{\\circ}")
        equation2.move_to(4*RIGHT+0.5*UP)
        equation3 = TexMobject("2(\\alpha+\\beta)=180^{\\circ}")
        equation3.move_to(4*RIGHT+0.5*DOWN)
        equation4 = TexMobject("\\alpha+\\beta=90^{\\circ}")
        equation4.move_to(4*RIGHT+1.5*DOWN)
        equation5 = TexMobject("\\overline{OA}=\\overline{OB}=\\overline{OC}")
        equation5.move_to(4*RIGHT+1*UP)
        equation6 = TexMobject("\\angle OBA=\\angle OAB")
        equation6.move_to(4*RIGHT)
        equation7 = TexMobject("\\angle OBC=\\angle OCB")
        equation7.move_to(4*RIGHT+1*DOWN)
        #equation8 = TexMobject("\\triangle OBA=\\triangle OAB")
        equation9 = TexMobject("\\alpha=\\angle OBA")
        equation9.move_to(4*RIGHT+0.5*UP)
        equation10 = TexMobject("\\beta=\\angle OBC")
        equation10.move_to(4*RIGHT+0.5*DOWN)
        equation11 = TexMobject("\\alpha, \\alpha+\\beta, \\beta")
        equation11.move_to(4*RIGHT+2.5*UP)
        equation12 = TexMobject("\\alpha+\\beta=?")
        equation12.move_to(4*RIGHT+1.5*UP)
        box = Rectangle(width=3, height=0.6, color=YELLOW)
        box.move_to(4*RIGHT+1.5*DOWN)

        #self.add(grid)
        self.wait()
        self.play(ShowCreation(triangle0))
        self.wait()
        self.play(ShowCreation(circle), ShowCreation(center))
        self.wait(2)
        self.play(Write(letters), run_time=3)
        self.wait(4)
        self.play(ShowCreation(line))
        self.wait()      
        self.play(FadeIn(rads))
        self.play(Write(equation5), run_time=2)
        self.wait(2)
        self.play(FadeOut(rads))
        self.wait(4)
        self.play(ShowCreationThenFadeOut(triangle1))
        self.play(ShowCreationThenFadeOut(triangle2))
        self.wait(2)
        self.play(ShowCreation(angles))
        self.wait(2)
        self.play(Write(equation6), Indicate(angle00), Indicate(angle01), run_time=2)
        self.wait(2)
        self.play(Write(equation7), Indicate(angle10), Indicate(angle11), run_time=2)
        self.wait()
        self.play(Uncreate(equation5))
        self.wait()
        self.play(FadeOut(equation6[0][4:]), ReplacementTransform(equation6[0][0:4], equation9[0][2:]), Write(equation9[0][0:2]))
        self.wait(2)
        self.play(FadeOut(equation7[0][4:]), ReplacementTransform(equation7[0][0:4], equation10[0][2:]), Write(equation10[0][0:2]))
        self.wait(2)
        self.play(Write(signs), run_time=3)
        self.wait(3)
        self.play(ReplacementTransform(alpha0.copy(), equation11[0][0]), Write(equation11[0][1]))
        self.play(ReplacementTransform(signab.copy(), equation11[0][2:5]), Write(equation11[0][5]))
        self.play(ReplacementTransform(beta0.copy(), equation11[0][6]))
        self.wait(2)
        self.play(Write(equation12))
        self.wait()
        self.play(Uncreate(equation12), Uncreate(equation9), Uncreate(equation10))
        self.wait(3)
        self.play(FadeInFrom(equation1, LEFT))
        self.wait(9)
        self.play(FadeInFromPoint(equation2, point=np.array([4, 1.5, 0])))
        self.wait(6)
        self.play(FadeInFromPoint(equation3, point=np.array([4, 0.5, 0])))
        self.wait(8)
        self.play(FadeInFromPoint(equation4, point=np.array([4, -0.5, 0])), ShowCreation(box))
        self.wait(5)