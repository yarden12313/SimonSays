

class Circle:
    def __init__(self, quarter_circle1, quarter_circle2, quarter_circle3, quarter_circle4):
        pass

class QuarterCircle:
    def __init__(self, shape, color):
        pass

if __name__ == '__main__':

    main_screen()

    while player_loos is True:
        circle_clean()
        draw(Circle())
        player_loos = user_draw()
        if player_loos is True:
            points += 1

    game_over()
    main_screen()
