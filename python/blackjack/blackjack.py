#
# Blackjack
#
# Python tutoring exercise.
# Sean Midford, 2020
#
from typing import List
from hand import Hand

def get_bet(balance: int) -> int:
    """This function gets the user's bet for the hand. The bet must be less than or equal to
        the player's balance. The bet is also invalid if the user enters an invalid character,
        or if the bet is less than or equal to zero (a bet must be at least 1). If the bet is 
        not valid for any reason, the function should ask the user to re-enter the bet.

    Parameters
    ----------
    balance : int
        The amount of money the player can bet.
    Returns
    -------
    int
        The bet amount.
    """
    pass

def add_to_balance(balance: int, bet: int) -> int:
    """This function adds the bet amount to the balance and returns the result.

    Parameters
    ----------
    balance : int
        The amount of money the player has.
    bet : int
        The amount of money the player has bet.
    Returns
    -------
    int
        The total balance amount after adding the bet.
    """
    pass

def subtract_from_balance(balance: int, bet: int) -> int:
    """This function subtracts the bet amount from the balance and returns the result.

    Parameters
    ----------
    balance : int
        The amount of money the player has.
    bet : int
        The amount of money the player has bet.
    Returns
    -------
    int
        The total balance amount after subtracting the bet.
    """
    pass

def print_balance(balance: int):
    """This function prints the current balance.

    Parameters
    ----------
    balance : int
        The player's balance.
    """
    pass

def check_for_win(player: Hand, dealer: Hand) -> bool:
    """This function checks if the player has won the hand. The player wins if
    they have a higher hand total than the dealer, and have not gone over 21. If
    the player and dealer tie, the player loses. However, if the player reaches
    exactly 21 they win even in a tie.

    Parameters
    ----------
    player : Hand
        The player's hand.
    dealer : Hand
        The dealer's hand.
    Returns
    -------
    bool
        If the player has won the hand or not.
    """
    pass

def check_for_bankruptcy(balance: int) -> bool:
    """This function checks if the player has gone bankrupt (balance is 0).

    Parameters
    ----------
    balance : int
        The player's balance.
    Returns
    -------
    bool
        If the player has gone bankrupt.
    """
    pass

def get_hit_choice() -> bool:
    """This function asks the player if they want to 'hit'. Input should be 'H' for
    hitting and 'P' for pass. Invalid choices should be ignored and the user should
    be prompted for a new choice.

    Returns
    -------
    bool
        If the player hit.
    """
    pass

def run_player_hand(hand: Hand):
    """This function continually asks the player if they want to 'hit'. If the
    player hits, a card is added to their hand. If the hand total is ever greater
    than 21, the player can not hit again.

    Hint: Use get_hit_choice()

    Parameters
    ----------
    hand : Hand
        The player's hand.
    """
    pass

def run_dealer_hand(hand: Hand):
    """This function runs through the dealers hand. The dealer must always hit if
    the hand total is less than or equal to 16.

    Parameters
    ----------
    hand : Hand
        The dealer's hand.
    """
    pass

def play_hand(balance: int) -> int:
    bet = get_bet(balance)

    player = Hand()
    dealer = Hand()

    dealer.print_hand(dealer = True)

    run_player_hand(player)
    run_dealer_hand(dealer)

    if check_for_win(player, dealer):
        print("You win!")
        return add_to_balance(balance, bet)
    else:
        print("You lose!")
        return subtract_from_balance(balance, bet)

def play_game():
    balance = 1000

    while not check_for_bankruptcy(balance):
        print_balance(balance)
        balance = play_hand(balance)

    print("Bankrupt!")

def main():
    print("Welcome to Blackjack!")
    play_game()


if __name__ == "__main__":
    main()
