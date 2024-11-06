import cairo

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

draw_grid(context, WIDTH, HEIGHT, 25)

surface.write_to_png("grid.png")
print("Grid image created!")
