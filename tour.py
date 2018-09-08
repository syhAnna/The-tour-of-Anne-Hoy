"""
functions to run TOAH tours.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "main":'
import time
from toah_model import TOAHModel


def move_of_three_stools(model, n, stool_tuple, delay=0.5):
    """
    Move the tower starting the nth disk from source to target, using helper,
    and following the rules of the Tower of Hanoi game

    @param TOAHModel model:
    @param int n: the number of cheese to be moved
    @param tuple[int] stool_tuple:
    @param int delay: the second of the dalay between each moves
    @rtype: None
    """
    if n > 0:
        stool_tuple1 = (stool_tuple[0], stool_tuple[2], stool_tuple[1])
        move_of_three_stools(model, n - 1, stool_tuple1, delay)
        model.move(stool_tuple[0], stool_tuple[1])
        print(model)
        time.sleep(delay)
        stool_tuple2 = (stool_tuple[2], stool_tuple[1], stool_tuple[0])
        move_of_three_stools(model, n - 1, stool_tuple2, delay)


def move_of_four_stools(model, n, stool_tuple, delay=0.5):
    """
    Move the tower starting the nth disk from source to target, using helper,
    and following the rules of the Tower of Hanoi game

    @param TOAHModel model:
    @param int n: the number of cheese to be moved
    @param tuple[int] stool_tuple:
    @param int delay: the second of the delay between each moves
    @rtype: None
    """
    if n == 1:
        move_of_three_stools(model, 1, stool_tuple[:-1], delay)
    else:
        i = split_index(n)[1]
        stool_tuple1 = (stool_tuple[0], stool_tuple[2], stool_tuple[1],
                        stool_tuple[3])
        move_of_four_stools(model, n - i, stool_tuple1, delay)

        stool_tuple2 = (stool_tuple[0], stool_tuple[1], stool_tuple[3])
        move_of_three_stools(model, i, stool_tuple2, delay)

        stool_tuple3 = (stool_tuple[2], stool_tuple[1], stool_tuple[0],
                        stool_tuple[3])
        move_of_four_stools(model, n - i, stool_tuple3, delay)


def split_index(number_of_cheeses):
    """ Return the minimum tuple with (moves, index)

    @param int number_of_cheeses:
    @rtype: tuple[int]
    """
    if number_of_cheeses == 1:
        return 1, 0
    moves = []
    for i in range(1, number_of_cheeses):
        move_ = 2 * split_index(number_of_cheeses - i)[0] + 2 ** i - 1
        moves.append((move_, i))
    return min(moves)


def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    """
    if animate:
        n = model.get_number_of_cheeses()
        stool_tuple = (0, 3, 1, 2)
        move_of_four_stools(model, n, stool_tuple, delay_btw_moves)


if __name__ == '__main__':
    num_cheeses = 5
    delay_between_moves = 0.5
    console_animate = True

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheeses=num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())
    # Leave files below to see what python_ta checks.
    # File tour_pyta.txt must be in same folder
    import python_ta
    python_ta.check_all(config="tour_pyta.txt")
