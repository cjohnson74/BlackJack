from p1_random import P1Random

stats = {
    "game_on": True,
    "user_score": 0,
    "dealer_score": 0,
    "player_wins": 0,
    "dealer_wins": 0,
    "ties": 0,
    "total_games_played": 0
}

rng = P1Random()


def hit():
    rnd_num = rng.next_int(13) + 1

    if rnd_num == 1:
        card = 'ACE'
    elif rnd_num == 11:
        card = 'JACK'
        rnd_num = 10
    elif rnd_num == 12:
        card = 'QUEEN'
        rnd_num = 10
    elif rnd_num == 13:
        card = 'KING'
        rnd_num = 10
    else:
        card = str(rnd_num)

    return [rnd_num, card]


def player_turn():
    [curr_draw, card] = hit()
    stats["user_score"] += curr_draw
    print(f'Your card is a {card}!')
    print(f'Your hand is: {stats["user_score"]}\n')
    while stats["user_score"] <= 21:
        if stats["user_score"] == 21:
            print('BLACKJACK! You win!\n')
            stats["player_wins"] += 1
            stats["user_score"] = 0
            stats["dealer_score"] = 0
            stats["total_games_played"] += 1
            return

        else:
            print('1.   Get another card\n'
                  '2.   Hold hand\n'
                  '3.   Print statistics\n'
                  '4.   Exit\n')

            option = input('Choose an option: ')
            print('')

            if option == '1':
                [curr_draw, card] = hit()
                stats["user_score"] += curr_draw
                print(f'Your card is a {card}!')
                print(f'Your hand is: {stats["user_score"]}\n')
            elif option == '2':
                dealer_turn()
                return
            elif option == '3':
                print_stats()
            elif option == '4':
                stats['game_on'] = False
                return
            else:
                print("Invalid input!\n"
                      "Please enter an integer value between 1 and 4.\n")
    print('You exceeded 21! You lose.\n')
    stats["dealer_wins"] += 1
    stats["user_score"] = 0
    stats["dealer_score"] = 0
    stats["total_games_played"] += 1


def dealer_turn():
    stats["dealer_score"] = rng.next_int(11) + 16
    if stats["user_score"] == stats["dealer_score"]:
        print(f"Dealer's hand: {stats['dealer_score']}")
        print(f'Your hand is: {stats["user_score"]}\n')
        print("It's a tie! No one wins!\n")
        stats["ties"] += 1
    elif stats["user_score"] < stats["dealer_score"] <= 21:
        print(f"Dealer's hand: {stats['dealer_score']}")
        print(f'Your hand is: {stats["user_score"]}\n')
        print('Dealer wins!\n')
        stats["dealer_wins"] += 1
    else:
        print(f"Dealer's hand: {stats['dealer_score']}")
        print(f'Your hand is: {stats["user_score"]}\n')
        print('You win!\n')
        stats["player_wins"] += 1
    stats["user_score"] = 0
    stats["dealer_score"] = 0
    stats["total_games_played"] += 1


def print_stats():
    print(f'Number of Player wins: {stats["player_wins"]}\n'
          f'Number of Dealer wins: {stats["dealer_wins"]}\n'
          f'Number of tie games: {stats["ties"]}\n'
          f'Total # of games played is: {stats["total_games_played"]}\n'
          f'Percentage of Player wins: {(stats["player_wins"] / stats["total_games_played"]) * 100:.1f}%\n')


def start_game():
    while stats["game_on"]:
        while stats["game_on"]:
            print(f"START GAME #{stats['total_games_played'] + 1}\n")
            player_turn()


if __name__ == '__main__':
    start_game()
