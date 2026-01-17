from manim import *
# class First(Scene):         #新建类
#     def construct(self):
#         first_tit=Text("2026/1/10",font_size=20)        #文本（内容，字号
#         first_cir=Circle(radius=2,color=WHITE,fill_opacity=0)     #圆（半径，颜色，图形内部填充颜色深度
#         first_squ=Square(side_length=3,color=GREEN,fill_opacity=0.1)     #方（边长，颜色，图形内部填充颜色深度
#         self.play(Write(first_tit))                 #渲染文本
#         self.wait(1)            #等两秒
#         self.play(first_tit.animate.to_edge(UP))        #把文本移到最上方
#         self.play(Create(VGroup(first_cir,first_squ).arrange(RIGHT)))       #渲染圆和方（对齐
#         self.wait(1)
#         self.play(first_cir.animate.move_to(first_squ.get_center()))        #把圆移动到正方形中心
#         self.wait(1)
#         self.play(Transform(first_cir,first_squ))           #让圆变成方
#         self.wait(1)
#         self.play(FadeOut(first_cir,first_squ,first_tit))       #让圆，方文字，缓慢消失
#         self.wait(1)
# config.preview = True           #预览
# first_1=First()                 #创建对象
# first_1.render()      #渲染

class QR(Scene):
    def construct(self):
        date_text = Text("2026.1.13", font_size=40)
        date_text.move_to(ORIGIN)

        self.play(Write(date_text))  # 生成文字
        self.wait(1)  # 等待1秒
        self.play(date_text.animate.to_edge(UP))  # 移动到最上方

        # 创建29x29方格表
        grid_size = 29
        square_size = 0.18
        grid = VGroup()  # 创建一个组来容纳所有方格

        # 创建方格并整体下移1.5个单位
        grid_center = DOWN * 1.3
        for i in range(grid_size):
            for j in range(grid_size):
                square = Square(
                    side_length=square_size,
                    color=WHITE,
                    stroke_width=1,
                    fill_opacity=0
                )
                square.move_to([
                    (i - grid_size / 2 + 0.5) * square_size,
                    (j - grid_size / 2 + 0.5) * square_size,
                    0
                ])
                grid.add(square)

        grid.move_to(grid_center)  # 整体下移

        # 计算表格的边界位置
        grid_top = grid_center[1] + (grid_size / 2) * square_size
        grid_bottom = grid_center[1] - (grid_size / 2) * square_size
        grid_left = grid_center[0] - (grid_size / 2) * square_size
        grid_right = grid_center[0] + (grid_size / 2) * square_size

        # 创建上方标注数字（1到29）
        top_labels = VGroup()
        for i in range(1, grid_size + 1):
            label = Text(str(i), font_size=12)  # 减小字号
            # 计算每列的中心x坐标
            col_x = grid_center[0] + (i - grid_size / 2 - 0.5) * square_size
            # 将数字放在对应列的上方，位于表格顶部之上
            label.move_to([col_x, grid_top + 0.2, 0])  # 增加y坐标使其位于表格上方
            top_labels.add(label)

        # 创建左侧标注数字（1到29）
        left_labels = VGroup()
        for j in range(1, grid_size + 1):
            label = Text(str(j), font_size=12)  # 减小字号
            # 计算每行的中心y坐标
            row_y = grid_center[1] + (grid_size / 2 - j + 0.5) * square_size
            # 将数字放在对应行的左侧，位于表格左侧之外
            label.move_to([grid_left - 0.2, row_y, 0])  # 减小x坐标使其位于表格左侧
            left_labels.add(label)

        # 动画效果：创建方格和标注
        self.play(Create(grid))
        self.play(Write(top_labels), Write(left_labels))
if __name__=="__main__":
    config.preview = True           #预览
    first_1=QR()                 #创建对象
    first_1.render()      #渲染