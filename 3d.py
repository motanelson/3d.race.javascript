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
    # Draw the center cross
    pygame.draw.line(screen, LINE_COLOR, (0, 0), (WINDOW_WIDTH, WINDOW_HEIGHT), 1)
    pygame.draw.line(screen, LINE_COLOR, (0, WINDOW_HEIGHT), (WINDOW_WIDTH, 0), 1)


    BLACK = (0, 0, 0)
    mm=[260,224,186,150,112,76,36,0,0,0,0,0]
    for i, char in enumerate(wire_string):
        

        if char == "#":
            # Draw two horizontal lines to represent the wall
            pygame.draw.rect(screen, BLACK, (x, 0,w,WINDOW_HEIGHT ))
            pygame.draw.rect(screen, BLACK, (WINDOW_WIDTH-x-w, 0,w,WINDOW_HEIGHT ))
            pygame.draw.line(screen, LINE_COLOR, (x,CENTER_Y-mm[counter]), (x,CENTER_Y+mm[counter] ), 1)
            
            pygame.draw.line(screen, LINE_COLOR, (WINDOW_WIDTH-x,CENTER_Y-mm[counter]), (WINDOW_WIDTH-x,CENTER_Y+mm[counter] ), 1)

            pygame.draw.line(screen, LINE_COLOR, (x+w,CENTER_Y-mm[counter+1]), (x+w,CENTER_Y+mm[counter+1] ), 1)
            
            pygame.draw.line(screen, LINE_COLOR, (WINDOW_WIDTH-x-w,CENTER_Y-mm[counter+1]), (WINDOW_WIDTH-x-w,CENTER_Y+mm[counter+1] ), 1)
            pygame.draw.line(screen, LINE_COLOR, (x,CENTER_Y-mm[counter+1]), (x+w,CENTER_Y-mm[counter+1] ), 1)
            pygame.draw.line(screen, LINE_COLOR, (x,CENTER_Y+mm[counter+1]), (x+w,CENTER_Y+mm[counter+1] ), 1)
            pygame.draw.line(screen, LINE_COLOR, (WINDOW_WIDTH-x,CENTER_Y-mm[counter+1]), (WINDOW_WIDTH-x-w,CENTER_Y-mm[counter+1] ), 1)
            pygame.draw.line(screen, LINE_COLOR, (WINDOW_WIDTH-x,CENTER_Y+mm[counter+1]), (WINDOW_WIDTH-x-w,CENTER_Y+mm[counter+1] ), 1)

            pass
        x=x+w
        counter+=1
        
        
def main():
    pygame.init()

    # Set up the screen
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Wireframe 3D Wall Viewer")

    # Input string (8 characters, '#' or ' ')
    wire_string = " # # # #"  # Example input: "#" for wall, " " for no wall

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

