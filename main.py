from app import *

if __name__ == '__main__':
    app = Application()

    while app.running:
        app.curr_menu.display_menu()
        app.game_loop()

