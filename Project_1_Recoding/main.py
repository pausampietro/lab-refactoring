
import logic as lo
import plot as p


# definition/initialization of global variables
global plg, actual_turn, max_turns
max_turns_defined = 9
max_turns = min(max_turns_defined, 9)   # getting sure we do not exceed max possible turns (9)
actual_turn = 1
plg = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# initialize turn 1
st_one = lo.starting_one()
win = False


if st_one == 'user':

    p.plot_plg(plg)           # 1st turn for the user (randomly selected)(not checking a victory, it is impossible by now)

    user_x, user_y = lo.user_move()
    while not lo.empty_cell(plg, 2 - user_y, user_x):
        print('The selected cell is already filled')
        user_x, user_y = lo.user_move()

    plg = lo.update_plg(plg, 1, 2 - user_y, user_x)  # update the playground (plg matrix) placing a 1
    p.plot_plg(plg)
    print(f'Remaining turns: {max_turns - actual_turn}')
    print(f'Winner: {lo.who_wins(plg)}')
    actual_turn += 1

    while actual_turn < max_turns and not win:    # 2nd to 8th turns or until a victory
        pc_x, pc_y = lo.pc_move(plg)           # PC's TURN
        plg = lo.update_plg(plg, -1, pc_x, pc_y)  # update the playground (plg matrix) placing a -1

        p.plot_plg(plg)

        print(f'PC move was: ({pc_y + 1},{2 - pc_x + 1})')
        print(f'Remaining turns: {max_turns - actual_turn}')
        print(f'Winner: {lo.who_wins(plg)}')
        actual_turn += 1

        if lo.who_wins(plg) == 'pc':  # If pc wins with its move, the game ends.
            print("You have lost against Python...Try again!")
            win = True

        else:
            user_x, user_y = lo.user_move()     # USER'S TURN
            while not lo.empty_cell(plg, 2 - user_y, user_x):
                print('The selected cell is already filled')
                user_x, user_y = lo.user_move()

            plg = lo.update_plg(plg, 1, 2 - user_y, user_x)  # update the playground (plg matrix) placing a 1

            p.plot_plg(plg)

            print(f'Remaining turns: {max_turns - actual_turn}')
            print(f'Winner: {lo.who_wins(plg)}')
            actual_turn += 1

            if lo.who_wins(plg) == 'user':  # If pc wins with its move, the game ends.
                print("You have win...Congratulations 'Master of Strategy'!!!")
                win = True


elif st_one == 'pc':

    print("PC has started playing. Now it's your turn!")
    pc_x, pc_y = lo.pc_move(plg)           # 1st turn for the pc (randomly selected)(not checking a victory)
    plg = lo.update_plg(plg, -1, pc_x, pc_y)           # update the playground (plg matrix) placing a -1

    p.plot_plg(plg)

    print(f'PC move was: ({pc_y + 1},{2 - pc_x + 1})')
    print(f'Remaining turns: {max_turns - actual_turn}')
    print(f'Winner: {lo.who_wins(plg)}')
    actual_turn += 1

    while actual_turn < max_turns and not win:      # 2nd to 8th turns or until a victory
        user_x, user_y = lo.user_move()        # USER'S TURN
        while not lo.empty_cell(plg, 2 - user_y, user_x):
            print('The selected cell is already filled')
            user_x, user_y = lo.user_move()

        plg = lo.update_plg(plg, 1, 2 - user_y, user_x)        # update the playground (plg matrix) placing a 1

        p.plot_plg(plg)

        print(f'Remaining turns: {max_turns - actual_turn}')
        print(f'Winner: {lo.who_wins(plg)}')
        actual_turn += 1

        if lo.who_wins(plg) == 'user':  # If pc wins with its move, the game ends.
            print("You have win...Congratulations 'Master of Strategy'!!!")
            win = True
        else:
            pc_x, pc_y = lo.pc_move(plg)         # PC's TURN
            plg = lo.update_plg(plg, -1, pc_x, pc_y)          # update the playground (plg matrix) placing a -1

            p.plot_plg(plg)

            print(f'PC move was: ({pc_y + 1},{2 - pc_x + 1})')
            print(f'Remaining turns: {max_turns - actual_turn}')
            print(f'Winner: {lo.who_wins(plg)}')
            actual_turn += 1

            if lo.who_wins(plg) == 'pc':  # If pc wins with its move, the game ends.
                print("You have lost against Python...Try again!")
                win = True

if not win:
    print("The game ended in a tie. Do you want to play again?")

