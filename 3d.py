import pygame

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
LINE_COLOR = (255, 255, 255)  # White
BG_COLOR = (0, 0, 0)  # Black
CENTER_X = WINDOW_WIDTH // 2
CENTER_Y = WINDOW_HEIGHT // 2
SECTION_WIDTH = WINDOW_WIDTH // 8
WALL_DEPTH = 50  # Depth of the wall in pixels

# Wireframe drawing function
def draw_wireframe(screen, wire_string):
    """
    Draw the wireframe based on the input string (8 characters).
    '#' represents a wall; ' ' (space) represents no wall.
    """
    w=WINDOW_WIDTH//2
    w=w//8
    x=w
    counter=0
    nnn=1.555
    for i, char in enumerate(wire_string):
        

        if char == "#":
            # Draw two horizontal lines to represent the wall
            
            pygame.draw.line(screen, LINE_COLOR, (x,CENTER_Y-(8-counter)*(w/nnn)), (x,CENTER_Y+(8-counter)*(w/nnn) ), 1)
            pygame.draw.line(screen, LINE_COLOR, (WINDOW_WIDTH-x,CENTER_Y-(8-counter)*(w/nnn)), (WINDOW_WIDTH-x,CENTER_Y+(8-counter)*(w/nnn) ), 1)
            pass
        x=x+w
        counter+=1
        nnn=nnn+0.1
    # Draw the center cross
    pygame.draw.line(screen, LINE_COLOR, (0, 0), (WINDOW_WIDTH, WINDOW_HEIGHT), 1)
    pygame.draw.line(screen, LINE_COLOR, (0, WINDOW_HEIGHT), (WINDOW_WIDTH, 0), 1)

def main():
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Wireframe 3D Wall Viewer")

    # Input string (8 characters, '#' or ' ')
    wire_string = "# # # # "  # Example input: "#" for wall, " " for no wall

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(BG_COLOR)

        # Draw the wireframe
        draw_wireframe(screen, wire_string)

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()

