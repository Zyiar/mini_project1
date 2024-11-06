import math
import cairo

WIDTH, HEIGHT = 800, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

def draw_background(ctx, color=(0, 0, 0)):
    ctx.set_source_rgb(*color)
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.fill()

def draw_hoop(ctx, center_x, center_y, width, height):
    ctx.save()
    ctx.translate(center_x, center_y)
    ctx.scale(width / 2, height / 2)
    ctx.arc(0, 0, 1, 0, 2 * math.pi)
    ctx.restore()
    ctx.set_line_width(15)
    ctx.set_source_rgb(1, 1, 1)
    ctx.stroke()

def draw_net_line1(ctx):
    ctx.set_line_width(3)
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(250, 400)
    ctx.curve_to(320, 450, 320, 475, 325, 550)

def draw_net_line2(ctx):
    ctx.set_line_width(3)
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(550, 400)
    ctx.curve_to(480, 450, 480, 475, 475, 550)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.stroke()

def draw_net_line3(ctx):
    ctx.set_line_width(3)
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(325, 418)
    ctx.curve_to(362.5, 450, 375, 475, 362.5, 558)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.stroke()

def draw_net_line4(ctx):
    ctx.set_line_width(3)
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(475, 418)
    ctx.curve_to(437.5, 450, 425, 475, 437.5, 558)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.stroke()

def draw_net_line5(ctx):
    ctx.set_line_width(3)
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(325, 384)
    ctx.curve_to(340, 400, 340, 400, 350, 418)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.stroke()

def draw_net_line6(ctx):
    ctx.set_line_width(3)
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(475, 384)
    ctx.curve_to(460, 400, 460, 400, 450, 418)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.stroke()

def draw_hoop2(ctx, center_x, center_y, width, height):
    ctx.save()
    ctx.translate(center_x, center_y)
    ctx.scale(width / 2, height / 2)
    ctx.set_line_width(2)
    ctx.set_source_rgb(0, 1, 0)
    ctx.arc(0, 0, 0.5, 0, 1 * math.pi)
    ctx.restore()
    ctx.set_line_width(3)
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

def draw_hoop3(ctx, center_x, center_y, width, height):
    ctx.save()
    ctx.translate(center_x, center_y)
    ctx.scale(width / 2, height / 2)
    ctx.set_line_width(2)
    ctx.set_source_rgb(0, 0, 0)
    ctx.arc(0, 0, 0.53, 0, 2 * math.pi)
    ctx.restore()
    ctx.set_line_width(3)
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

def draw_hoop4(ctx, center_x, center_y, width, height):
    ctx.save()
    ctx.translate(center_x, center_y)
    ctx.scale(width / 2, height / 2)
    ctx.set_source_rgb(0, 0, 0)
    ctx.arc(0, 0, 0.64, 0, 2 * math.pi)
    ctx.restore()
    ctx.set_line_width(3)
    ctx.set_source_rgb(0, 0, 0)
    ctx.stroke()

def draw_backboard(ctx, x, y, width, height, color=(0.961, 0.855, 0.820)):
    ctx.set_source_rgb(*color)
    ctx.rectangle(x, y, width, height)
    ctx.fill()

    glow_strength = 15
    glow_width = 2

    for i in range(glow_strength):
        opacity = (glow_strength - i) / glow_strength * 0.15
        ctx.set_source_rgba(1, 1, 1, opacity)
        ctx.rectangle(x - i * glow_width, y - i * glow_width, width + 2 * i * glow_width, height + 2 * i * glow_width)
        ctx.set_line_width(2)
        ctx.stroke()

    ctx.set_line_width(5)
    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(x, y, width, height)
    ctx.stroke()

def draw_inner_rectangle(ctx, x, y, width, height, color=(0.4, 0.4, 0.4)):
    ctx.set_source_rgb(*color)
    ctx.rectangle(x, y, width, height)
    ctx.stroke()

    ctx.set_line_width(5)
    ctx.set_source_rgb(0, 0, 0)
    ctx.rectangle(x, y, width, height)
    ctx.stroke()

def draw_curve(ctx, start, control1, control2, end):
    ctx.set_line_width(4)
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(*start)
    ctx.curve_to(*control1, *control2, *end)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.stroke()

def draw_curve1(ctx):
    ctx.set_line_width(4)
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(375, 79)
    ctx.curve_to(315, 100, 290, 225, 325, 298)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.stroke()

def draw_curve2(ctx):
    ctx.set_line_width(4)
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(275, 200)
    ctx.curve_to(350, 225, 450, 225, 525, 200)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.stroke()

def draw_curve3(ctx):
    ctx.set_line_width(4)
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(300, 125)
    ctx.curve_to(300, 225, 400, 150, 475, 100)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.stroke()

def draw_curve4(ctx):
    ctx.set_line_width(4)
    ctx.set_source_rgb(0, 0, 0)
    ctx.move_to(300, 275)
    ctx.curve_to(300, 225, 425, 300, 475, 300)
    ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    ctx.stroke()


def draw_stand(ctx, x, y, width, height, fill_color=(0.961, 0.855, 0.820), border_color=(0, 0, 0), border_width=3):
    ctx.set_source_rgb(*fill_color)
    ctx.rectangle(x - width // 2, y, width, height)
    ctx.fill()

    ctx.set_source_rgb(*border_color)
    ctx.set_line_width(border_width)
    ctx.rectangle(x - width // 2, y, width, height)
    ctx.stroke()

def draw_connector(ctx, width=5, color=(0, 0, 0)):
    ctx.set_line_width(width)
    ctx.set_source_rgb(*color)
    ctx.move_to(525, 275)
    ctx.line_to(475, 384)
    ctx.line_to(525, 390)
    ctx.line_to(575, 275)
    ctx.close_path()
    ctx.move_to(575, 275)
    ctx.line_to(575, 375)
    ctx.line_to(525, 390)
    ctx.fill()

def draw_sphere(ctx, center_x, center_y, radius):
    gradient = cairo.RadialGradient(center_x + 40, center_y - 40, 20, center_x, center_y, radius)
    gradient.add_color_stop_rgb(0, 1, 1, 1)
    gradient.add_color_stop_rgb(1, 0.93, 0.43, 0.0)

    ctx.set_source(gradient)
    ctx.arc(center_x, center_y, radius, 0, 2 * math.pi)
    ctx.fill()

context.set_source_rgb(1, 1, 1)
context.paint()

draw_background(context, color=(0.620, 0.392, 0.317))

ball_center_x = WIDTH // 2
ball_center_y = HEIGHT // 2 - 100


backboard_x = ball_center_x - 70
backboard_y = ball_center_y - 180
backboard_width = 430
backboard_height = 330

stand_x = backboard_x + backboard_width // 2
stand_y = backboard_y + backboard_height
stand_width = 45
stand_height = 300

backboard_x = ball_center_x - 70
backboard_y = ball_center_y - 180
backboard_width = 430
backboard_height = 330

inner_rectangle_x = backboard_x - -100
inner_rectangle_y = backboard_y - -170
inner_rectangle_width = 230
inner_rectangle_height = 130

connector_start_x = ball_center_x + 140
connector_start_y = backboard_y + backboard_height
connector_end_x = ball_center_x + 140
connector_end_y = ball_center_y + 118


draw_backboard(context, backboard_x, backboard_y, backboard_width, backboard_height)
draw_stand(context, stand_x, stand_y, stand_width, stand_height, fill_color=(0.4, 0.4, 0.4), border_color=(0, 0, 0), border_width=3)
draw_inner_rectangle(context, inner_rectangle_x, inner_rectangle_y, inner_rectangle_width, inner_rectangle_height)
draw_connector(context, width=5, color=(0, 0, 0))

draw_sphere(context, ball_center_x, ball_center_y, 127)
draw_net_line1(context)
draw_net_line2(context)
draw_net_line3(context)
draw_net_line4(context)
draw_net_line5(context)
draw_net_line6(context)
draw_curve1(context)
draw_curve2(context)
draw_curve3(context)
draw_curve4(context)

draw_hoop(context, ball_center_x, ball_center_y + 200, 300, 40)
draw_hoop2(context, ball_center_x, ball_center_y + 350, 300, 40)
draw_hoop3(context, ball_center_x, ball_center_y + 300, 300, 40)
draw_hoop4(context, ball_center_x, ball_center_y + 250, 300, 40)

surface.write_to_png("basketball.png")
print("Basketball with light reflection image created!")
