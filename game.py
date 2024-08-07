import sys

def display_tokens(red_tokens, blue_tokens):
    print(f"Red tokens: {red_tokens}, Blue tokens: {blue_tokens}")

def player_turn(player, red_tokens, blue_tokens):
    print(f"Player {player}'s turn")
    color = input("Choose a color (red/blue): ").strip().lower()
    while color not in ["red", "blue"]:
        color = input("Invalid color. Choose a color (red/blue): ").strip().lower()
    count = int(input(f"How many {color} tokens to remove? "))
    if color == "red":
        red_tokens -= count
    else:
        blue_tokens -= count
    return red_tokens, blue_tokens

def computer_turn(red_tokens, blue_tokens, version, depth):
    # Implement MinMax with Alpha Beta Pruning
    # For simplicity, let's just remove one red token in this placeholder function
    if version == "standard":
        if red_tokens > 0:
            red_tokens -= 1
        else:
            blue_tokens -= 1
    else:  # Misère version
        if blue_tokens > 0:
            blue_tokens -= 1
        else:
            red_tokens -= 1
    return red_tokens, blue_tokens

def check_winner(red_tokens, blue_tokens, version):
    if version == "standard":
        return red_tokens == 0 or blue_tokens == 0
    elif version == "misere":
        return red_tokens == 0 and blue_tokens == 0

def red_blue_nim_game(red_tokens, blue_tokens, version, first_player, depth):
    current_player = first_player
    
    while True:
        display_tokens(red_tokens, blue_tokens)
        if current_player == "human":
            red_tokens, blue_tokens = player_turn(current_player, red_tokens, blue_tokens)
        else:
            red_tokens, blue_tokens = computer_turn(red_tokens, blue_tokens, version, depth)
        
        if check_winner(red_tokens, blue_tokens, version):
            print(f"Player {current_player} wins!")
            break
        
        current_player = "computer" if current_player == "human" else "human"

def main():
    if len(sys.argv) < 5 or len(sys.argv) > 6:
        print("Usage: python3 game.py <7-red> <5-blue> <version> <first-player> [<depth>]")
        sys.exit(1)

    try:
        red_tokens = int(sys.argv[1])
        blue_tokens = int(sys.argv[2])
        version = sys.argv[3].lower()
        first_player = sys.argv[4].lower()
        if version not in ["standard", "misere"]:
            raise ValueError("Version must be 'standard' or 'misere'.")
        if first_player not in ["human", "computer"]:
            raise ValueError("First player must be 'human' or 'computer'.")
        depth = int(sys.argv[5]) if len(sys.argv) == 6 else None
    except ValueError as e:
        print(f"Error: {e}")
        print("Usage: python3 game.py <7-red> <5-blue> <version> <first-player> [<depth>]")
        sys.exit(1)

    red_blue_nim_game(red_tokens, blue_tokens, version, first_player, depth)

if __name__ == "__main__":
    main()
