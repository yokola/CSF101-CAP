################################
# Mahindra Rai
# 1ICE
# 02230217
################################
# REFERENCES
#https://www.youtube.com/watch?v=Uc9FTTP-nB4
# https://www.youtube.com/watch?v=fn68QNcatfo
################################
# SOLUTION
# Your Solution Score:50169
# Put your number here :CSF101-CAP/input_7_cap1.txt
def read_input(input_file):
    """
    Read the input file and return a list of tuples containing shape and outcome.

    Args:
        input_file (str): The name of the input file.

    Returns:
        list: A list of tuples, where each tuple contains shape and outcome.
    """
    game_round = []
    with open(input_file, 'r') as file:
        for line in file:
            shape, outcome = line.strip().split()
            game_round.append((shape, outcome))
    return game_round

def calculate_score(game_round):
    """
    Calculate the total score of the game based on the provided rules.

    Args:
        game_round (list): A list of tuples containing shape and outcome for each round.

    Returns:
        int: The total score of the game.
    """
    scores = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6, "CZ": 7}
    total_score = sum(scores.get(shape + outcome, 0) for shape, outcome in game_round)
    return total_score

def main():
    input_file = "CSF101-CAP/input_7_cap1.txt"
    game_round = read_input(input_file)
    total_round_score = calculate_score(game_round)
    print("Total Score:", total_round_score)

if __name__ == "__main__":
    main()