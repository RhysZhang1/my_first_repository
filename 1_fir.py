from manim import *
class First(Scene):         #新建类
    def construct(self):
        first_tit=Text("2026/1/10",font_size=20)        #文本（内容，字号
        first_cir=Circle(radius=2,color=WHITE,fill_opacity=0)     #圆（半径，颜色，图形内部填充颜色深度
        first_squ=Square(side_length=3,color=GREEN,fill_opacity=0.1)     #方（边长，颜色，图形内部填充颜色深度
        self.play(Write(first_tit))                 #渲染文本
        self.wait(1)            #等两秒
        self.play(first_tit.animate.to_edge(UP))        #把文本移到最上方
        self.play(Create(VGroup(first_cir,first_squ).arrange(RIGHT)))       #渲染圆和方（对齐
        self.wait(1)
        self.play(first_cir.animate.move_to(first_squ.get_center()))        #把圆移动到正方形中心
        self.wait(1)
        self.play(Transform(first_cir,first_squ))           #让圆变成方
        self.wait(1)
        self.play(FadeOut(first_cir,first_squ,first_tit))       #让圆，方文字，缓慢消失
        self.wait(1)
config.preview = True           #预览
first_1=First()                 #创建对象
first_1.render()      #渲染