
def initialize():
    # definition of global variables
    global plg, actual_turn, max_turns

    max_turns_defined = 9
    max_turns = min(max_turns_defined, 9)   # getting sure we do not exceed max possible turns (9)
    actual_turn = 1
    plg = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
