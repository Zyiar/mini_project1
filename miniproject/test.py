import cairo
import math

WIDTH, HEIGHT = 800, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)


def draw_grid(ctx, width, height, spacing):
    ctx.set_source_rgb(0.8, 0.8, 0.8)
    ctx.set_line_width(1)

    for x in range(0, width, spacing):
        ctx.move_to(x, 0)
        ctx.line_to(x, height)

    for y in range(0, height, spacing):
        ctx.move_to(0, y)
        ctx.line_to(width, y)

    ctx.stroke()

ball_center_x = WIDTH // 2
ball_center_y = HEIGHT // 2 - 100

def draw_sphere(ctx, center_x, center_y, radius):
    gradient = cairo.RadialGradient(center_x + 40, center_y - 40, 20, center_x, center_y, radius)
    gradient.add_color_stop_rgb(0, 1, 1, 1)
    gradient.add_color_stop_rgb(1, 0.93, 0.43, 0.0)

    ctx.set_source(gradient)
    ctx.arc(center_x, center_y, radius, 0, 2 * math.pi)
    ctx.fill()

draw_grid(context, WIDTH, HEIGHT, 25)
draw_sphere(context, ball_center_x, ball_center_y, 127)

surface.write_to_png("hand.png")
print("Grid image created!")
