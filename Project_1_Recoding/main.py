
import logic as l
import plot as p
import globals as g


g.initialize()

# initialize turn 1
st_one = l.starting_one()
win = False

# todo change calling of functions in logic and in plot, pass as a first variable PLG
if st_one == 'user':

    p.plot_plg()           # 1st turn for the user (randomly selected)(not checking a victory, it is impossible by now)

    user_x, user_y = l.user_move()
    while not l.empty_cell(2 - user_y, user_x):
        print('The selected cell is already filled')
        user_x, user_y = l.user_move()

    l.update_plg(1, 2 - user_y, user_x)  # update the playground (plg matrix) placing a 1
    p.plot_plg()
    print(f'Remaining turns: {max_turns - actual_turn}')
    print(f'Winner: {l.who_wins()}')
    actual_turn += 1

    while actual_turn < max_turns and not win:    # 2nd to 8th turns or until a victory
        pc_x, pc_y = l.pc_move()           # PC's TURN
        l.update_plg(-1, pc_x, pc_y)  # update the playground (plg matrix) placing a -1

        p.plot_plg()

        print(f'PC move was: ({pc_y + 1},{2 - pc_x + 1})')
        print(f'Remaining turns: {max_turns - actual_turn}')
        print(f'Winner: {l.who_wins()}')
        actual_turn += 1

        if l.who_wins() == 'pc':  # If pc wins with its move, the game ends.
            print("You have lost against Python...Try again!")
            win = True

        else:
            user_x, user_y = l.user_move()     # USER'S TURN
            while not l.empty_cell(2 - user_y, user_x):
                print('The selected cell is already filled')
                user_x, user_y = l.user_move()

            l.update_plg(1, 2 - user_y, user_x)  # update the playground (plg matrix) placing a 1

            p.plot_plg()

            print(f'Remaining turns: {max_turns - actual_turn}')
            print(f'Winner: {l.who_wins()}')
            actual_turn += 1

            if l.who_wins() == 'user':  # If pc wins with its move, the game ends.
                print("You have win...Congratulations 'Master of Strategy'!!!")
                win = True


elif st_one == 'pc':

    print("PC has started playing. Now it's your turn!")
    pc_x, pc_y = l.pc_move()           # 1st turn for the pc (randomly selected)(not checking a victory)
    l.update_plg(-1, pc_x, pc_y)           # update the playground (plg matrix) placing a -1

    p.plot_plg()

    print(f'PC move was: ({pc_y + 1},{2 - pc_x + 1})')
    print(f'Remaining turns: {max_turns - actual_turn}')
    print(f'Winner: {l.who_wins()}')
    actual_turn += 1

    while actual_turn < max_turns and not win:      # 2nd to 8th turns or until a victory
        user_x, user_y = l.user_move()        # USER'S TURN
        while not l.empty_cell(2 - user_y, user_x):
            print('The selected cell is already filled')
            user_x, user_y = l.user_move()

        l.update_plg(1, 2 - user_y, user_x)        # update the playground (plg matrix) placing a 1

        p.plot_plg()

        print(f'Remaining turns: {max_turns - actual_turn}')
        print(f'Winner: {l.who_wins()}')
        actual_turn += 1

        if l.who_wins() == 'user':  # If pc wins with its move, the game ends.
            print("You have win...Congratulations 'Master of Strategy'!!!")
            win = True
        else:
            pc_x, pc_y = l.pc_move()         # PC's TURN
            l.update_plg(-1, pc_x, pc_y)          # update the playground (plg matrix) placing a -1

            p.plot_plg()

            print(f'PC move was: ({pc_y + 1},{2 - pc_x + 1})')
            print(f'Remaining turns: {max_turns - actual_turn}')
            print(f'Winner: {l.who_wins()}')
            actual_turn += 1

            if l.who_wins() == 'pc':  # If pc wins with its move, the game ends.
                print("You have lost against Python...Try again!")
                win = True

if not win:
    print("The game ended in a tie. Do you want to play again?")

