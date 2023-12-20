import pytest
from checkers import Checkers

@pytest.fixture
def checkers_game():
    return Checkers()

def test_initialization(checkers_game):
    assert checkers_game.turn == 'w'
    assert checkers_game.account == {'Игрок 1': 0, 'Игрок 2': 0}

def test_valid_move(checkers_game):
    assert checkers_game.is_valid_move(5, 0, 4, 1)

def test_invalid_move(checkers_game):
    assert not checkers_game.is_valid_move(5, 0, 4, 2)

def test_make_move(checkers_game):
    checkers_game.make_move(5, 0, 4, 1)
    assert checkers_game.board[5][0] == ' '
    assert checkers_game.board[4][1] == 'w'

def test_parse_move(checkers_game):
    move = 'a5 b4'
    parsed_move = checkers_game.parse_move(move)
    assert parsed_move == (4, 0, 3, 1)
