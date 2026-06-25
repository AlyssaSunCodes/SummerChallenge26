# %% [markdown]
# ### Tic Tac Toe

# %%
import pygame, sys 

pygame.init()

screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Tic Tac Toe")

board = pygame.image.load("Board.png")
x_image = pygame.image.load("X.png")
o_image = pygame.image.load("O.png")

BG_COLOR = (255, 255, 255)

screen.fill(BG_COLOR)
screen.blit(board, (64, 64))

pygame.display.update()

# %%
board = {
  1: None,
  2: None,
  3: None,
  4: None,
  5: None,
  6: None,
  7: None,
  8: None,
  9: None
}

# print(board[1])
# print(board.get(1))

# %%
x_or_y = "X"

image_rendering = {
    "X": x_image, 
    "O": o_image
}

win_status = False 

# %%
def check_rows():
    global win_status
    if board[1] == board[2] == board[3] != None:
        print(board[1] + " wins!")
        return True 
    
    elif board[4] == board[5] == board[6] != None:
        print(board[4] + " wins!")
        return True 

    elif board[7] == board[8] == board[9] != None: 
        print(board[7] + " wins!")
        return True 

    return False 

def check_columns():
    global win_status
    if board[1] == board[4] == board[7] != None:
        print(board[1] + " wins!")
        return True 
    
    elif board[2] == board[5] == board[8] != None:
        print(board[2] + " wins!")
        return True


    elif board[3] == board[6] == board[9] != None:
        print(board[3] + " wins!")
        return True

    return False


def check_diagonals():
    global win_status
    if board[1] == board[5] == board[9] != None:
        print(board[1] + " wins!")
        return True

    elif board[3] == board[5] == board[7] != None:
        print(board[3] + " wins!")
        return True

    return False


# %%
def check_mouse():
    position = pygame.mouse.get_pos()

    if position[1] < 300:
        if position[0] < 300:
            if board[1] is None:
                board[1] = x_or_y 
                screen.blit(image_rendering[board[1]], (100, 100)) 

        elif position[0] < 600 and position[0] > 300:
            if board[2] is None:
                board[2] = x_or_y
                screen.blit(image_rendering[board[2]], (400, 100))
        else:
            if board[3] is None:
                board[3] = x_or_y
                screen.blit(image_rendering[board[3]], (700, 100))     



    if position[1] < 600 and position[1] > 300: 
        if position[0] < 300:
            if board[4] is None:
                board[4] = x_or_y 
                screen.blit(image_rendering[board[4]], (100, 375))     
        elif position[0] < 600 and position[0] > 300:
            if board[5] is None:
                board[5] = x_or_y
                screen.blit(image_rendering[board[5]], (400, 375))
        else:
            if board[6] is None:
                board[6] = x_or_y
                screen.blit(image_rendering[board[6]], (700, 375))


    if position[1] < 900 and position[1] > 600: 
        if position[0] < 300:
            if board[7] is None:
                board[7] = x_or_y 
                screen.blit(image_rendering[board[7]], (100, 675))

        elif position[0] < 600 and position[0] > 300:
            if board[8] is None:
                board[8] = x_or_y
                screen.blit(image_rendering[board[8]], (400, 675))
        else:
            if board[9] is None:
                board[9] = x_or_y
                screen.blit(image_rendering[board[9]], (700, 675))

# %%
while win_status == False:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            win_status = True 
    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse()

            if x_or_y == "X":
                x_or_y = "O"
            else:
                x_or_y = "X"
            
            if (
                check_rows() or check_columns() or check_diagonals()
            ):
                win_status = True 

            pygame.display.update()


# (So it doesn't immediately close)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

# %% [markdown]
# 


