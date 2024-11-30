import pygame
import sys
from logic.components.button import Button
from game import run

pygame.init()

display = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Dogtective: Main Menu")
background = pygame.image.load("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/images/menu/city_backgroud.png").convert()
background= pygame.transform.smoothscale(background, display.get_size())


def pixel_font(size):
    return pygame.font.Font("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/StayPixelRegular.ttf", size)

def play():
    while True:
        mouse_pos_play = pygame.mouse.get_pos()

        display.fill("blue4")

        text_play = pixel_font(50).render("Play screen", True, "blue4")
        rect_play = text_play.get_rect(center=(640,240))
        display.blit(text_play, rect_play)

        go_back = Button(pos_x = 640, pos_y = 240, font=pygame.font.Font("/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/StayPixelRegular.ttf"), colour = "black", click_colour = "white", text = "BACK")
        go_back.click_colour(mouse_pos_play)
        go_back.update_button(display)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if go_back.check_input(mouse_pos_play):
                    menu()
        pygame.display.update()


def credit_screen():
    while True:
        mouse_pos_credits = pygame.mouse.get_pos()

        display.fill("blue4")

        text_credits = pixel_font(50).render("Credits screen", True, "blue4")
        rect_credits = text_credits.get_rect(center=(640, 240))
        display.blit(text_credits, rect_credits)

        go_back = Button(pos_x=640, pos_y=240, text="BACK", font=pygame.font.Font(
            "/Users/sallydavies/Desktop/PycharmProjects/CFGDegree-GroupProjectTeam5/logic/assets/StayPixelRegular.ttf"),
                         colour="black", click_colour="white")
        go_back.click_colour(mouse_pos_credits)
        go_back.update_button(display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if go_back.check_input(mouse_pos_credits):
                    menu()
        pygame.display.update()


def leaderboard():
    while True:
        mouse_pos_ldr = pygame.mouse.get_pos()

        display.fill("blue4")

        text_ldr = pixel_font(50).render("Leaderboard screen", True, "blue4")
        rect_ldr = text_ldr.get_rect(center=(640, 240))
        display.blit(text_ldr, rect_ldr)

        go_back = Button(pos_x=640, pos_y=240, font=pixel_font(100),
                         colour="black", click_colour="white", text="BACK")
        go_back.click_colour(mouse_pos_ldr)
        go_back.update_button(display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if go_back.check_input(mouse_pos_ldr):
                    menu()
        pygame.display.update()

def menu():
    while True:
        display.blit(background, (0, 0))

        mouse_pos_menu = pygame.mouse.get_pos()

        text_menu = pixel_font(100).render("MENU", True, "teal")
        rect_menu = text_menu.get_rect(center=(640,100))

        button_play = Button(pos_x = 640, pos_y = 300, font=pixel_font(100),
         colour="black", click_colour="white", text="play")
        button_ldr = Button(pos_x = 640, pos_y = 400, font=pixel_font(100),
         colour="black", click_colour="white", text="LEADERBOARD")
        button_credits = Button(pos_x = 640, pos_y = 500, font=pixel_font(100),
         colour="black", click_colour="white", text="CREDITS")


        display.blit(text_menu, rect_menu)

        # for button in [button_play, button_ldr, button_credits]:
        #     button.click_colour(mouse_pos_menu)
        #     button.update_button(display)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.check_input(mouse_pos_menu):
                    run()
                if button_ldr.check_input(mouse_pos_menu):
                    leaderboard()
                if button_credits.check_input(mouse_pos_menu):
                    credits()
        pygame.display.update()

menu()

