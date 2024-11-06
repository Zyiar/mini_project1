import math
import cairo

WIDTH, HEIGHT = 800, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

def draw_background(context, color=(0, 0, 0)):
    """Fills the entire background with a solid color."""
    context.set_source_rgb(*color)  # Set the background color
    context.rectangle(0, 0, WIDTH, HEIGHT)  # Define a rectangle that covers the whole surface
    context.fill()  # Fill the rectangle with the color

def draw_backboard(context, x, y, width, height, color=(0.961, 0.855, 0.820), opacity=0.5):
    """Draws a rectangular backboard with a glow effect around the border."""
    # Fill the backboard with the specified color
    context.set_source_rgba(*color, opacity)
    context.rectangle(x, y, width, height)
    context.fill()

    # Draw the glow effect with several rectangles of increasing size and decreasing opacity
    glow_strength = 15  # Number of glow layers for smoother transition
    glow_width = 2  # Distance between each glow layer

    for i in range(glow_strength):
        opacity = (glow_strength - i) / glow_strength * 0.15  # Adjust opacity for softer glow
        context.set_source_rgba(1, 1, 1, opacity)  # White glow
        context.rectangle(x - i * glow_width, y - i * glow_width, width + 2 * i * glow_width, height + 2 * i * glow_width)
        context.set_line_width(2)
        context.stroke()

    # Draw the main border for the backboard
    context.set_line_width(5)
    context.set_source_rgb(1, 1, 1)  # White color for the border
    context.rectangle(x, y, width, height)
    context.stroke()

def draw_innerrectangle(context, x, y, width, height, color=(0.4,0.4,0.4)):
    context.set_source_rgb(*color)
    context.rectangle(x, y, width, height)
    context.stroke()

    context.set_line_width(5)
    context.set_source_rgb(0, 0, 0)
    context.rectangle(x, y, width, height)
    context.stroke()

def draw_sphere(context, center_x, center_y, radius):
    gradient = cairo.RadialGradient(center_x + 40, center_y - 40, 20, center_x, center_y, radius)
    gradient.add_color_stop_rgb(0, 1, 1, 1)
    gradient.add_color_stop_rgb(1, 0.93, 0.43, 0.0)

    context.set_source(gradient)
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    context.fill()

def draw_connector(context, start_x, start_y, end_x, end_y, width=5, color=(0, 0, 0)):
        """Draws a connector from the backboard to the hoop."""
        context.set_line_width(width)
        context.set_source_rgb(*color)
        context.move_to(start_x, start_y)
        context.line_to(end_x, end_y)
        context.stroke()


def draw_hoop1(context, center_x, center_y, width, height, radius):
    context.set_source_rgb(1, 1, 1)
    # Save the original context state
    context.save()

    # Set the center of the hoop
    context.translate(center_x, center_y)
    context.scale(width / 2, height / 2)

    # Draw the glow effect with finer rings and slightly higher opacity
    glow_width = 0.2  # Controls spacing between glow rings
    glow_strength = 3  # Number of glow rings for smoother transition

    for i in range(glow_strength):
        opacity = (glow_strength - i) / glow_strength * 0.15  # Adjust opacity for more visible glow
        context.set_source_rgba(1, 0.816 , 0.757, opacity)
        context.arc(0, 0, radius + i * glow_width, 0, 2 * math.pi)
        context.set_line_width(2)
        context.stroke()

    # Draw the main hoop outline
    context.set_line_width(4)

    context.arc(0, 0, 1, 0, 2 * math.pi)
    context.restore()
    context.stroke()


def draw_hoop2(context, center_x, center_y, width, height, radius):
    context.set_source_rgb(1, 1, 1)
    # Save the original context state
    context.save()
    # Set the center of the hoop
    context.translate(center_x, center_y)
    context.scale(width / 2, height / 2)

    # Draw the glow effect with finer rings and slightly higher opacity
    glow_width = 0.2  # Controls spacing between glow rings
    glow_strength = 3  # Number of glow rings for smoother transition

    for i in range(glow_strength):
        opacity = (glow_strength - i) / glow_strength * 0.15  # Adjust opacity for more visible glow
        context.set_source_rgba(1, 0.816 , 0.757, opacity)  # Light bluish glow
        context.arc(0, 0, radius + i * glow_width, 0, 2 * math.pi)
        context.set_line_width(2)
        context.stroke()

    # Draw the main hoop outline

    context.set_line_width(4)

    context.arc(0, 0, 1, 0, 2 * math.pi)
    context.restore()
    context.stroke()


def draw_hoop3(context, center_x, center_y, width, height, radius):
    context.set_source_rgb(1, 1, 1)
    # Save the original context state
    context.save()

    # Set the center of the hoop
    context.translate(center_x, center_y)
    context.scale(width / 2, height / 2)

    # Draw the glow effect with finer rings and slightly higher opacity
    glow_width = 0.2  # Controls spacing between glow rings
    glow_strength = 3  # Number of glow rings for smoother transition

    for i in range(glow_strength):
        opacity = (glow_strength - i) / glow_strength * 0.15  # Adjust opacity for more visible glow
        context.set_source_rgba(1, 0.816 , 0.757, opacity)  # Light bluish glow
        context.arc(0, 0, radius + i * glow_width, 0, 2 * math.pi)
        context.set_line_width(2)
        context.stroke()

    # Draw the main hoop outline

    context.set_line_width(4)

    context.arc(0, 0, 1, 0, 2 * math.pi)
    context.restore()
    context.stroke()


def draw_hoop4(context, center_x, center_y, width, height, radius):
    context.set_source_rgb(1, 1, 1)
    # Save the original context state
    context.save()

    # Set the center of the hoop
    context.translate(center_x, center_y)
    context.scale(width / 2, height / 2)

    # Draw the glow effect with finer rings and slightly higher opacity
    glow_width = 0.2  # Controls spacing between glow rings
    glow_strength = 3  # Number of glow rings for smoother transition

    for i in range(glow_strength):
        opacity = (glow_strength - i) / glow_strength * 0.15  # Adjust opacity for more visible glow
        context.set_source_rgba(1, 0.816 , 0.757, opacity)  # Light bluish glow
        context.arc(0, 0, radius + i * glow_width, 0, 2 * math.pi)
        context.set_line_width(2)
        context.stroke()

    # Draw the main hoop outline

    context.set_line_width(4)
    context.arc(0, 0, 1, 0, 2 * math.pi)
    context.restore()
    context.stroke()


def draw_curve1(context):
    context.set_line_width(4)
    context.set_source_rgb(0, 0, 0)
    context.move_to(375, 79)
    context.curve_to(315, 100, 290, 225, 325, 298)
    context.set_line_cap(cairo.LINE_CAP_ROUND)
    context.stroke()

def draw_curve2(context):
    context.set_line_width(4)
    context.set_source_rgb(0, 0, 0)
    context.move_to(275, 200)
    context.curve_to(350, 225, 450, 225, 525, 200)
    context.set_line_cap(cairo.LINE_CAP_ROUND)
    context.stroke()

def draw_curve3(context):
    context.set_line_width(4)
    context.set_source_rgb(0, 0, 0)
    context.move_to(300, 125)
    context.curve_to(300, 225, 400, 150, 475, 100)
    context.set_line_cap(cairo.LINE_CAP_ROUND)
    context.stroke()

def draw_curve4(context):
    context.set_line_width(4)
    context.set_source_rgb(0, 0, 0)
    context.move_to(300, 275)
    context.curve_to(300, 225, 425, 300, 475, 300)
    context.set_line_cap(cairo.LINE_CAP_ROUND)
    context.stroke()


def draw_stand(context, x, y, width, height, fill_color=(0.961, 0.855, 0.820), border_color=(0, 0, 0), border_width=3):
    """Draws a rectangular support stand under the backboard with the top connected to the backboard base and a black border."""

    # Set the fill color and draw the filled rectangle
    context.set_source_rgb(*fill_color)
    context.rectangle(x - width // 2, y, width, height)  # Center the rectangle horizontally at x
    context.fill()

    # Set the border color and width, and draw the border outline
    context.set_source_rgb(*border_color)
    context.set_line_width(border_width)
    context.rectangle(x - width // 2, y, width, height)
    context.stroke()

# Set up the background
draw_background(context, color=(0.620, 0.392, 0.317))  # Soft pink background

# Set up basketball and backboard positions
ball_center_x = WIDTH // 2
ball_center_y = HEIGHT // 2 - 100

# Position the backboard directly above the hoop and slightly offset from the ball
backboard_x = ball_center_x - 70  # Centered horizontally around the basketball
backboard_y = ball_center_y - 180  # Position it above the basketball
backboard_width = 430
backboard_height = 330

# Define stand parameters
stand_x = backboard_x + backboard_width // 2  # Centered horizontally under the backboard
stand_y = backboard_y + backboard_height      # Positioned just below the backboard
stand_width = 45                              # Width of the stand
stand_height = 300                            # Height of the stand


# Position the backboard directly above the hoop and slightly offset from the ball
backboard_x = ball_center_x - 70  # Centered horizontally around the basketball
backboard_y = ball_center_y - 180  # Position it above the basketball
backboard_width = 430
backboard_height = 330

#Position the inner rectangle
innerrectangle_x = backboard_x - -100
innerrectangle_y = backboard_y - -170
innerrectangle_width = 230
innerrectangle_height = 130

# Position for connector
connector_start_x = ball_center_x + 140 # Centered horizontally with the ball and hoop
connector_start_y = backboard_y + backboard_height  # Bottom of the backboard
connector_end_x = ball_center_x + 140 # Centered horizontally with the ball and hoop
connector_end_y = ball_center_y + 118  # Top of draw_hoop1 (adjust as needed)


draw_backboard(context, backboard_x, backboard_y, backboard_width, backboard_height)
draw_stand(context, stand_x, stand_y, stand_width, stand_height, fill_color=(0.4, 0.4, 0.4), border_color=(0, 0, 0), border_width=3)
draw_innerrectangle(context, innerrectangle_x, innerrectangle_y, innerrectangle_width, innerrectangle_height)
draw_connector(context, connector_start_x, connector_start_y, connector_end_x, connector_end_y, width=5, color=(0, 0, 0))

# Draw the basketball and hoop
draw_sphere(context, ball_center_x, ball_center_y, 125)
draw_curve1(context)
draw_curve2(context)
draw_curve3(context)
draw_curve4(context)
draw_hoop1(context, ball_center_x, ball_center_y + 150, 300, 40,0.4)
draw_hoop2(context, ball_center_x, ball_center_y + 200, 250, 40, 0.2)
draw_hoop3(context, ball_center_x, ball_center_y + 250, 200, 40,0.1)
draw_hoop4(context, ball_center_x, ball_center_y + 300, 150, 40,0.01)

surface.write_to_png("basketball_with_backboard.png")
print("Basketball with backboard image created!")
