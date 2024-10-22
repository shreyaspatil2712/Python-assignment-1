import numpy as np

def analyze_player_performance(num_players, num_games):

    player_scores = np.random.randint(0, 101, size=(num_players, num_games))
    mean_score = np.mean(player_scores)
    median_score = np.median(player_scores)
    variance_score = np.var(player_scores)
    std_dev_score = np.std(player_scores)

    #results
    print(f"Player performance statistics over {num_games} games for {num_players} players:")
    print(f"Mean Score: {mean_score:.2f}")
    print(f"Median Score: {median_score:.2f}")
    print(f"Variance of Scores: {variance_score:.2f}")
    print(f"Standard Deviation of Scores: {std_dev_score:.2f}")


num_players = 20  
num_games = 30    

analyze_player_performance(num_players, num_games)
