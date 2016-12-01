#Задача 9. Вариант 17.
# Разработайте игру "Крестики-нолики". (см. М.Доусон Программируем на Python гл. 6).


class Game:
    def __init__(self):
        # Крестики-нолики
        # Компьютер играет в крестики-нолики против пользователя
        # глобальные константы
        self.X = "Х"
        self.O = "О"
        self.EMPTY = ' '
        self.TIE = "Ничья"
        self.NUM_SQUARES = 9
        self.board = []

    def display_instructions(self):
        """Выводит на экран инструкцию для игрока."""
        print("""Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времен.
Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики".
Чтобы сделать ход. введи число от О до 8. Числа однозначно соответствуют полям
доски - так. как показано ниже:
        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8
Приготовься к бою. жалкий белковый человечишка. Вот-вот начнется решающее сражение.
""")

    def ask_yes_no(self, question):
        """Задает вопрос с ответом 'Да' или 'Нет'."""
        response = None
        while response not in ("y", "n"):
            response = input(question).lower()
        return response

    def ask_number(self, question, low, high):
        """Просит ввести число из диапазона."""
        response = None
        while response not in range(low, high):
            response = int(input(question))
        return response

    def pieces(self):
        """Определяет принадлежность первого хода."""

        go_first = self.ask_yes_no("Xoчeшь оставить за собой первый ход? (y/n): ")
        if go_first == "y":
            print("\nHy что ж, даю тебе фору: играй крестиками.")
            human = self.X
            computer = self.O
        else:
            print("\nTвoя удаль тебя погубит... Буду начинать я. ")
            computer = self.X
            human = self.O
        return computer, human

    def new_board(self):
        """Создает новую игровую доску."""
        board = []
        for square in range(self.NUM_SQUARES):
            board.append(self.EMPTY)
        return board

    def display_board(self):
        """Отображает игровую доску на экране."""
        print("""
        {} | {} | {}
        ---------
        {} | {} | {}
        ---------
        {} | {} | {}
        """.format(*self.board))

    def legal_moves(self):
        """создает список доступных ходов."""
        moves = []
        for square in range(self.NUM_SQUARES):
            if self.board[square] == self.EMPTY:
                moves.append(square)
        return moves

    def winner(self):
        """Определяет победителя в игре."""
        winner = None
        WAYS_ТО_WIN =  ((0, 1, 2),
                        (3, 4, 5),
                        (6, 7, 8),
                        (0, 3, 6),
                        (1, 4, 7),
                        (2, 5, 8),
                        (0, 4, 8),
                        (2, 4, 6))
        for row in WAYS_ТО_WIN:
            if self.board[row[0]] == self.board[row[1]] == self.board[row[2]] != self.EMPTY:
                winner = self.board[row[0]]
        return winner

    def human_move(self):
        """Получает ход человека. """
        legal = self.legal_moves()
        print(legal)
        move = None
        while move not in legal:
            move = self.ask_number("Tвoй ход. Выбери одно из полей (О - 8): ", 0, self.NUM_SQUARES)
            if move not in legal:
                print("\nСмешной человек! Это поле уже занято. Выбери другое.\n")
        print("Ладно ... ")
        return move

    def computer_move(self, computer, human):
        """Делает ход за компьютерного противника."""

        # создадим рабочую копию доски. потому что функuия будет менять некоторые значения в списке
        board = self.board
        # поля от лучшего к худшему
        BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
        print("Я выберу поле номер", end=" ")
        for move in self.legal_moves():
            board[move] = computer
            # если следующим ходом может победить компьютер. выберем этот ход
            if self.winner() == computer:
                print(move)
                return move
            # выполнив проверку. отменим внесенные изменения
            board[move] = self.EMPTY
        for move in self.legal_moves():
            board[move] = human
            # если следующим ходом может победить человек. блокируем этот ход
            if self.winner() == human:
                print(move)
                return move
            # вь1полнив проверку. отменим внесенные изменения
            board[move] = self.EMPTY
        # поскольку следующим ходом ни одна сторона не может победить.
        # выберем лучшее из доступных полей
        for move in BEST_MOVES:
            if move in self.legal_moves():
                print(move)
                return move

    def next_turn(self, turn):
        """Осуществляет переход хода."""

        if turn == self.X:
            return self.O
        else:
            return self.X

    def congrat_winner(self, the_winner, computer, human):
        """Поздравляет победителя игры."""
        if the_winner != self.TIE:
            print("Tpи", the_winner, "в ряд!\n")
        else:
            print("Hичья!\n")
        if the_winner == computer:
            print("Kaк я и предсказывал. победа в очередной раз осталась за мной.")
            print("Вот еще один довод в пользу того. что компьютеры превосходят людей решительно во всем.")
        elif the_winner == human:
            print("O нет. этого не может быть! Неужели ты как-то сумел перехитрить меня, белковый? ")
            print("Клянусь: я, компьютер, не допущу этого больше никогда!")
        elif the_winner == self.TIE:
            print("Teбe несказанно повезло. дружок: ты сумел свести игру вничью.")
            print("Радуйся же сегодняшнему успеху! Завтра тебе уже не суждено его повторить.")

    def main(self):
        self.display_instructions()
        computer, human = self.pieces()
        turn = self.X
        self.board = self.new_board()
        self.display_board()
        while not self.winner() and len(self.legal_moves()) > 0:
            if turn == human:
                move = self.human_move()
                self.board[move] = human
            else:
                move = self.computer_move(computer, human)
                try:
                    self.board[move] = computer
                except TypeError:
                    break
            self.display_board()
            turn = self.next_turn(turn)
        the_winner = self.winner() or self.TIE
        self.congrat_winner(the_winner, computer, human)

game = Game()
game.main()