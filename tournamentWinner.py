# Author : Ondřej Maceška
# Date : 4.6.2022
# Task : https://www.algoexpert.io/questions/tournament-winner


# O(n) time, O(k) space, where n is the number of competitions and k is the number of teams
def tournamentWinner(competitions, results):
    """ visit https://www.algoexpert.io/questions/tournament-winner for the assignment

    Args:
        array (int[ ]) : competitions
        target_sum (int) : results

    Returns:
        string : name of the winning team
    """
    team_scores = {}
    for index, competition in enumerate(competitions):
        
        winning_team = competition[1 - results[index]]
        if(winning_team in team_scores):
            team_scores[winning_team] += 3
        else:
            team_scores[winning_team] = 3
        
    return max(team_scores, key = team_scores.get)
