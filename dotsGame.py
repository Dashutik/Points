import gameField
import Player
import startGUI
import gameLogic

class GameDots:
    def __init__(self):
        self.play_game()

    def play_game(self):
        gf = gameField.GameField(20, 2)  # Инициализация игрового поля
        gui0 = startGUI.StartGUI(24, gf)

        while True:
            # выбор режима игры (доступен только робот)
            if gf.is_game_mode:
                gui0.draw_dropdown(gf.screen, "Режим игры", ["с компьютером"], "Продолжить", "с компьютером", 30, 40)
                gf.is_game_mode = False  # Переходим к следующему этапу после выбора режима

            elif gf.is_game_option:
                gf.with_bot = True
                gui1 = startGUI.StartGUI(24, gf)
                gui1.draw_dropdown(gf.screen, "Сложность", ["легко", "тяжело"], "Продолжить", "легко", 30, 40)
                gf.is_game_option = False  # Переходим к следующему этапу после выбора сложности

            elif gf.is_grid_size:
                gui2 = startGUI.StartGUI(24, gf)
                gui2.draw_dropdown(gf.screen, "Размер поля",
                                   ["10", "13", "15", "18", "21", "23", "26", "28", "31", "33", "36", "38", "40"],
                                   "Начать игру", "10", 30, 40)
                gf.is_grid_size = False  # Переходим к началу игры

            else:
                players = Player.Players(gf.grid_size, gf)  # Передаем gf в Players для доступа к GUI

                # Запрашиваем имена игроков
                num_players = 2
                #players.input_player_names(num_players)  # Метод для ввода имен игроков

                # Инициализируем логику игры
                game = gameLogic.GameLogic(gf, players)

                # Очищаем экран
                gf.screen.fill((255, 250, 250))

                # Рисуем сетку
                gf.draw_grid()

                # Запускаем игровой цикл
                game.game_loop()


