from battle import character_fight
import matplotlib.pyplot as plt

def plot_results(char_1, char_1_win, char_2, char_2_win):
    labels = [char_1, char_2]
    wins = [char_1_win, char_2_win]
    
    plt.bar(labels, wins, color=['blue', 'red'])
    plt.xlabel('Character Type')
    plt.ylabel('Number of Wins')
    plt.title('Battle Results')
    plt.show()

def main():
    char_1 = "fighter"
    char_1_win = 0
    char_2 = "mage"
    char_2_win = 0
    for _ in range(100):
        winner = character_fight(char_1, char_2)
        if winner == char_1:
            char_1_win += 1
        else:
            char_2_win += 1
    print("Results:")
    print(f"{char_1}: {char_1_win}")
    print(f"{char_2}: {char_2_win}")

    # Call plot_results inside the main function.
    plot_results(char_1, char_1_win, char_2, char_2_win)

if __name__ == "__main__":
    main()
