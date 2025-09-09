"""
This code plays a came of blackjack with the user
"""

from random import shuffle


RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "44"]
SUITS = ["♠", "♥", "♦", "♣"]


def build_deck() -> list[str]:
    return [f"{rank}{suit}" for suit in SUITS for rank in RANKS]


def card_value(card: str) -> int:
    rank = card[:-1]
    if rank in {"J", "Q", "K"}:
        return 10
    if rank == "A":
        return 11
    return int(rank)


def hand_value(cards: list[str]) -> int:
    total = sum(card_value(c) for c in cards)
    aces = sum(1 for c in cards if c[:-1] == "A")
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total


def show_hand(owner: str, cards: list[str], hide_first: bool = False) -> None:
    if hide_first and cards:
        visible = ["??"] + cards[1:]
        print(f"{owner}: {' '.join(visible)}")
    else:
        print(f"{owner}: {' '.join(cards)} ({hand_value(cards)})")


def deal_initial(deck: list[str]) -> tuple[list[str], list[str]]:
    player = [deck.pop(), deck.pop()]
    dealer = [deck.pop(), deck.pop()]
    return player, dealer


def player_turn(deck: list[str], player: list[str], dealer: list[str]) -> tuple[list[str], bool]:
    while True:
        show_hand("Dealer", dealer, hide_first=True)
        show_hand("You", player)
        if hand_value(player) == 21:
            print("Blackjack!")
            return player, False
        if hand_value(player) > 21:
            print("You bust!")
            return player, True
        choice = input("Hit or Stand? [h/s]: ").strip().lower()
        if choice in {"h", "hit"}:
            player.append(deck.pop())
            continue
        if choice in {"s", "stand"}:
            return player, False
        print("Please enter 'h' to hit or 's' to stand.")


def dealer_turn(deck: list[str], dealer: list[str]) -> list[str]:
    while hand_value(dealer) < 17:
        dealer.append(deck.pop())
    return dealer


def decide_winner(player: list[str], dealer: list[str]) -> str:
    player_total = hand_value(player)
    dealer_total = hand_value(dealer)
    if player_total > 21:
        return "Dealer wins (player bust)."
    if dealer_total > 21:
        return "You win! (dealer bust)"
    if player_total > dealer_total:
        return "You win!"
    if player_total < dealer_total:
        return "Dealer wins."
    return "Push (tie)."


def play_round() -> None:
    deck = build_deck()
    shuffle(deck)
    player, dealer = deal_initial(deck)

    player, busted = player_turn(deck, player, dealer)
    if not busted:
        dealer = dealer_turn(deck, dealer)

    print()
    show_hand("Dealer", dealer)
    show_hand("You", player)
    print(decide_winner(player, dealer))


def ask_replay() -> bool:
    while True:
        ans = input("Play again? [y/n]: ").strip().lower()
        if ans in {"y", "yes"}:
            return True
        if ans in {"n", "no"}:
            return False
        print("Please enter 'y' or 'n'.")


def main():
    print("Welcome to Blackjack!")
    try:
        while True:
            play_round()
            if not ask_replay():
                break
            print()
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()
