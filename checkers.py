import re  # Импорт модуля регулярных выражений (re) для работы с текстовыми паттернами.

class Checkers:
    def __init__(self):
        # Инициализация объекта Checkers, представляющего игру в шашки.
        self.board = [
            [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],  # Начальное распределение черных шашек.
            ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
            [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Пустая строка, разделяющая доску.
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' '],  # Начальное распределение белых шашек.
            [' ', 'w', ' ', 'w', ' ', 'w', ' ', 'w'],
            ['w', ' ', 'w', ' ', 'w', ' ', 'w', ' ']
        ]
        self.players = {'w': "Игрок 1", 'b': "Игрок 2"}  # Сопоставление цветов шашек с именами игроков.
        self.turn = 'w'  # Определение, чей ход (начальный ход за белых).
        self.queens = {'w': 'W', 'b': 'B'}  # Определение символов для дамок белых и черных шашек.
        self.account = {'Игрок 1': 0, 'Игрок 2': 0}  # Инициализация счетчика захваченных шашек для каждого игрока.

    def print_instruction(self):
        """Выводит инструкции по игре в шашки.

            Этот метод выводит инструкции по игре в шашки, включая формат совершения ходов
            и правила завершения игры.

            :return: None
            """
        # Метод для вывода в консоль инструкций по игре.
        print("Добро пожаловать в Шашки!")
        print("Инструкция:")
        print("1. Введите свои ходы в формате 'a5 b4', где 'a5' - начальная позиция, а 'b4' - конечная.")
        print("2. Игра заканчивается, если один из игроков захватит 12 фигур противника.")
        print("3. Вы можете ввести 'end' в свой ход, чтобы завершить игру и увидеть итоговый счет.")
        print("Пусть игра начнется!\n")

    def print_board(self):
        """Выводит текущее состояние шахматной доски.

            Этот метод отображает текущее распределение фигур на доске,
            включая метки для столбцов и номера строк.

            :return: None
            """
        # Метод для вывода в консоль текущего состояния игровой доски.
        print("  A  B  C  D  E  F  G  H")  # Изменить метки столбцов
        for i, row in enumerate(self.board):
            print(i + 1, end=' ')
            for piece in row:
                print(f'{piece}|', end=' ')
            print()

    def is_valid_move(self, start_x, start_y, end_x, end_y):
        """Проверяет, является ли ход допустимым согласно правилам шашек.

            Этот метод проверяет, соответствует ли ход из начальной позиции в конечную
            правилам шашек, учитывая типы фигур и возможные захваты.

            :param start_x: X-координата начальной позиции.
            :type start_x: int
            :param start_y: Y-координата начальной позиции.
            :type start_y: int
            :param end_x: X-координата конечной позиции.
            :type end_x: int
            :param end_y: Y-координата конечной позиции.
            :type end_y: int
            :return: True, если ход допустим, False в противном случае.
            :rtype: bool
            """
        # Метод для проверки валидности хода согласно правилам шашек.
        # Проверка, что ход находится в пределах доски
        if 0 <= start_x < 8 and 0 <= start_y < 8 and 0 <= end_x < 8 and 0 <= end_y < 8:
            # Проверка, что конечная позиция пуста
            if self.board[end_x][end_y] == ' ':
                # Проверка, что ход является диагональным для обычных шашек и дамок
                if abs(start_x - end_x) == abs(start_y - end_y):
                    # Дамки могут двигаться в любом направлении по диагонали
                    return True
                # Проверка, что ход составляет ровно один квадрат по диагонали для обычных шашек
                elif abs(start_x - end_x) == 1 and abs(start_y - end_y) == 1:
                    # Убедитесь, что обычные шашки могут двигаться только вперед
                    if (
                        (self.turn == 'w' and start_x > end_x) or
                        (self.turn == 'b' and start_x < end_x)
                    ):
                        return True
                # Проверка, что ход - прыжок через фигуру противника для обычных шашек и дамок
                elif abs(start_x - end_x) == 2 and abs(start_y - end_y) == 2:
                    jumped_x = (start_x + end_x) // 2
                    jumped_y = (start_y + end_y) // 2
                    if self.board[jumped_x][jumped_y] != ' ' and self.board[jumped_x][jumped_y].lower() != self.turn:
                        return True
        return False

    def make_move(self, start_x, start_y, end_x, end_y):
        def make_move(self, start_x, start_y, end_x, end_y):
            """Выполняет ход и обновляет состояние шахматной доски.

            Этот метод выполняет ход из начальной позиции в конечную,
            обновляя состояние шахматной доски. Также обрабатывает захват фигур противника
            и превращение фигур в дамки, когда это необходимо.

            :param start_x: X-координата начальной позиции.
            :type start_x: int
            :param start_y: Y-координата начальной позиции.
            :type start_y: int
            :param end_x: X-координата конечной позиции.
            :type end_x: int
            :param end_y: Y-координата конечной позиции.
            :type end_y: int
            :return: True, если игрок может совершить дополнительные ходы, False в противном случае.
            :rtype: bool
            """

        # Метод для выполнения хода и обновления состояния доски.
        if self.is_valid_move(start_x, start_y, end_x, end_y):
            self.board[end_x][end_y] = self.board[start_x][start_y]
            self.board[start_x][start_y] = ' '

            # Удаление убитых фигур
            if abs(start_x - end_x) == 2:
                killed_x = (start_x + end_x) // 2
                killed_y = (start_y + end_y) // 2
                self.board[killed_x][killed_y] = ' '

                # Увеличение счета для игрока
                self.account[self.players[self.turn]] += 1

                # Проверка на возможность дополнительных прыжков для одного игрока
                if self.can_hit_again(end_x, end_y):
                    return True

            # Проверка, становится ли фигура дамкой
            if (self.turn == 'w' and end_x == 0) or (self.turn == 'b' and end_x == 7):
                self.board[end_x][end_y] = self.queens[self.turn]

            return False
        else:
            print("Недопустимый ход. Попробуйте еще раз.")
            return True

    def can_hit_again(self, x, y):
        """Проверяет, может ли текущий игрок совершить дополнительные захваты.

            Этот метод определяет, может ли текущий игрок, после совершения захвата,
            совершить дополнительные последовательные захваты.

            :param x: X-координата текущей позиции.
            :type x: int
            :param y: Y-координата текущей позиции.
            :type y: int
            :return: True, если возможны дополнительные захваты, False в противном случае.
            :rtype: bool
            """
        # Метод проверяет, может ли текущий игрок сделать дополнительные ходы захвата.
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in directions:
            distance = 1
            while self.is_valid_move(x, y, x + distance * dx, y + distance * dy):
                target_x = x + distance * dx
                target_y = y + distance * dy
                jumped_x = (x + target_x) // 2
                jumped_y = (y + target_y) // 2
                if self.board[target_x][target_y] != ' ' and self.board[jumped_x][jumped_y] != ' ' and self.board[target_x][target_y].lower() != self.turn:
                    return True
                distance += 1
        return False

    def parse_move(self, move):
        """Анализирует ввод игрока и возвращает координаты хода.

            Этот метод анализирует ввод игрока, который должен быть в формате 'a5 b4',
            и возвращает координаты начальной и конечной позиций хода.

            :param move: Ввод игрока, представляющий ход.
            :type move: str
            :return: Кортеж start_x, start_y, end_x, end_y или None, если ввод недопустим.
            :rtype: tuple or None
            """
        # Метод для парсинга ввода игрока и возврата координат начальной и конечной позиций хода.
        match = re.match(r'^([a-hA-H][1-8])\s+([a-hA-H][1-8])$', move)
        if match:
            start_coord, end_coord = match.groups()
            start_x, start_y = int(start_coord[1]) - 1, ord(start_coord[0].upper()) - ord('A')
            end_x, end_y = int(end_coord[1]) - 1, ord(end_coord[0].upper()) - ord('A')
            return start_x, start_y, end_x, end_y
        return None

    def print_score(self):
        """Выводит итоговый счет игры в консоль.

            Этот метод выводит итоговый счет игры в формате "Игрок 1:Игрок 2".

            :return: None
            """
        # Выводит итоговый счет игры в консоль.
        print(f"Итоговый счет: {self.account['Игрок 1']}:{self.account['Игрок 2']}")

    def play(self):
        """Запускает и управляет игрой в шашки.

            Этот метод инициирует и контролирует игру в шашки, включая вывод инструкций,
            отображение доски, ввод игрока и определение победителя.

            :return: None
            """
        # Основной метод для запуска игры и управления ею.
        self.print_instruction()
        while True:
            self.print_board()
            player = self.players[self.turn]
            print(f"Ход {player} ({self.turn})")
            move = input("Введите ход (например, a5 b4) или введите 'end' для завершения игры: ")

            if move.lower() == 'end':
                self.print_score()
                break

            parsed_move = self.parse_move(move)

            if parsed_move:
                start_x, start_y, end_x, end_y = parsed_move

                # Проверка, что это ход правильного игрока
                if self.board[start_x][start_y].lower() != self.turn:
                    print("Недопустимый ход. Не ваш ход.")
                    continue

                while self.make_move(start_x, start_y, end_x, end_y):
                    # Запрос на дополнительные ходы, пока игрок может делать последовательные захваты
                    self.print_board()
                    print(f"Ход {player} ({self.turn})")
                    move = input("Введите ход (например, a5 b4) или введите 'end' для завершения игры: ")

                    if move.lower() == 'end':
                        self.print_score()
                        return

                    parsed_move = self.parse_move(move)

                    if parsed_move:
                        start_x, start_y, end_x, end_y = parsed_move

                        # Проверка, что это ход правильного игрока
                        if self.board[start_x][start_y].lower() != self.turn:
                            print("Недопустимый ход. Не ваш ход.")
                            break

                        # Если ход успешен, продолжаем цикл для последовательных захватов
                        if not self.make_move(start_x, start_y, end_x, end_y):
                            break
                    else:
                        print("Недопустимый ввод. Пожалуйста, введите ход в формате 'a5 b4'.")
                        break

                # Смена хода, только если нет больше прыжков
                self.turn = 'w' if self.turn == 'b' else 'b'
            else:
                print("Недопустимый ввод. Пожалуйста, введите ход в формате 'a5 b4'.")

            if self.account['Игрок 1'] >= 12:
                print("Игрок 1 выиграл!")
                self.print_score()
                break
            elif self.account['Игрок 2'] >= 12:
                print("Игрок 2 выиграл!")
                self.print_score()
                break

if __name__ == "__main__":
    # Создание экземпляра игры и запуск игры.
    game = Checkers()
    game.play()
