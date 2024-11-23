import random

# Blackjack strategy table (fixed for doubling on 11)
STRATEGY_TABLE = {
    "hard": {
        8: {"dealer": range(2, 12), "action": "h", "reason": "You need to build a stronger hand to compete with the dealer."},
        9: {"dealer": range(3, 7), "action": "d", "reason": "The dealer is weak, so doubling here maximizes your advantage."},
        10: {"dealer": range(2, 10), "action": "d", "reason": "Doubling is optimal when the dealer likely won't beat 20."},
        11: {"dealer": range(2, 12), "action": "d", "reason": "Your chance of hitting 21 is high, so doubling is optimal."},  # Fixed
        12: {"dealer": range(4, 7), "action": "st", "reason": "Standing avoids risking a bust against a weak dealer hand."},
        13: {"dealer": range(2, 7), "action": "st", "reason": "The dealer has a weak card, so let them risk busting."},
        14: {"dealer": range(2, 7), "action": "st", "reason": "The dealer is likely to bust, so standing is safest."},
        15: {"dealer": range(2, 7), "action": "st", "reason": "Standing here takes advantage of the dealer's weak card."},
        16: {"dealer": range(2, 7), "action": "st", "reason": "Standing avoids busting while the dealer risks failure."},
        17: {"dealer": range(2, 12), "action": "st", "reason": "With 17 or more, standing minimizes risk of busting."},
    },
    "soft": {
        13: {"dealer": range(5, 7), "action": "d", "reason": "You have flexibility to improve against a weak dealer hand."},
        14: {"dealer": range(5, 7), "action": "d", "reason": "Doubling increases your odds against a vulnerable dealer."},
        15: {"dealer": range(4, 7), "action": "d", "reason": "Maximize value when the dealer is weak."},
        16: {"dealer": range(4, 7), "action": "d", "reason": "Doubling here is an aggressive move against a weak dealer."},
        17: {"dealer": range(3, 7), "action": "d", "reason": "Capitalize on the flexibility of your soft total."},
        18: {"dealer": range(3, 7), "action": "d", "reason": "The dealer is vulnerable, so take advantage with a double."},
        19: {"dealer": range(6, 7), "action": "d", "reason": "This is a rare opportunity to double with a high soft total."},
    },
    "pairs": {
        2: {"dealer": range(2, 8), "action": "sp", "reason": "Splitting here maximizes your chances to build winning hands."},
        3: {"dealer": range(2, 8), "action": "sp", "reason": "Splitting gives you two chances to capitalize on weak cards."},
        4: {"dealer": range(5, 7), "action": "sp", "reason": "Splitting takes advantage of the dealer's weak position."},
        6: {"dealer": range(2, 8), "action": "sp", "reason": "Splitting is the best play when the dealer is weak."},
        7: {"dealer": range(2, 8), "action": "sp", "reason": "Splitting increases your chance of building winning hands."},
        8: {"dealer": range(2, 12), "action": "sp", "reason": "Splitting eights avoids a weak 16 and gives you two solid hands."},
        9: {"dealer": range(2, 10), "action": "sp", "reason": "Splitting maximizes winning potential against most dealer hands."},
    },
}


def get_strategy(player_total, dealer_card, is_soft, is_pair):
    """Returns the optimal strategy and reason based on player hand and dealer card."""
    category = "hard"
    if is_pair:
        category = "pairs"
    elif is_soft:
        category = "soft"
    
    if player_total in STRATEGY_TABLE[category]:
        if dealer_card in STRATEGY_TABLE[category][player_total]["dealer"]:
            return STRATEGY_TABLE[category][player_total]["action"], STRATEGY_TABLE[category][player_total]["reason"]
    return "h", "Hitting is the safest move when no clear advantage exists."


def simulate_hand():
    """Simulates a blackjack hand and asks the user for their decision."""
    player_card1 = random.randint(1, 10)
    player_card2 = random.randint(1, 10)
    dealer_card = random.randint(2, 11)
    player_total = player_card1 + player_card2
    is_soft = 1 in [player_card1, player_card2] and player_total <= 11
    is_pair = player_card1 == player_card2

    print(f"\nYour cards: {player_card1} and {player_card2} (Total: {player_total})")
    print(f"Dealer's visible card: {dealer_card}")

    # Get the correct strategy and reason
    correct_action, reason = get_strategy(player_total, dealer_card, is_soft, is_pair)

    # Get user input
    user_action = input("What is your move? (h = hit, st = stand, d = double, sp = split): ").strip().lower()

    # Evaluate user's decision
    if user_action == correct_action:
        print("Correct! You played optimally.")
    else:
        print(f"Wrong! The correct move was: {correct_action}.")
        print(f"Reason: {reason}")


def main():
    print("Welcome to the Blackjack Strategy Trainer!")
    print("Enter your moves using: h = hit, st = stand, d = double, sp = split")
    print("Press Ctrl+C to quit.\n")
    
    while True:
        simulate_hand()


if __name__ == "__main__":
    main()
