from classes import Statistics,Game,Team
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

all_games = requests.get('http://worldcup.sfg.io/matches').json()
engine = create_engine('sqlite:///games.db')
Session = sessionmaker(bind=engine)
session = Session()

#todolist
# 1)games only loads with ID and Venue
#2)stats doenst have game_id or team1_id
# 3)teams load with id and country
    #) all_games_objects[1].teams[1].country
    #all_games[1]["home_team_country"]

# game = all_games[0]
#stats below
def find_home_team_objects():
    home_team_stats_objects=[]
    for game in all_games:
        country=game['home_team']['country']
        ball_poss= game["home_team_statistics"]["ball_possession"]
        goals=game['home_team']['goals']
        distance= game["home_team_statistics"]["distance_covered"]
        pass_accur= game["home_team_statistics"]["pass_accuracy"]
        on_net=game["home_team_statistics"]["on_target"]
        game_stats = Statistics(name = country,ball_possession=ball_poss, goals=goals,distance_covered=distance,pass_accuracy=pass_accur,on_target=on_net)
        home_team_stats_objects.append(game_stats)
    return home_team_stats_objects

def find_away_team_objects():
    aaway_team_stats_objects=[]
    for game in all_games:
        country=game['away_team']['country']
        ball_poss= game["away_team_statistics"]["ball_possession"]
        goals=game['away_team']['goals']
        distance= game["away_team_statistics"]["distance_covered"]
        pass_accur= game["away_team_statistics"]["pass_accuracy"]
        on_net=game["away_team_statistics"]["on_target"]
        game_stats = Statistics(name = country,ball_possession=ball_poss, goals=goals,distance_covered=distance,pass_accuracy=pass_accur,on_target=on_net)
        away_team_stats_objects.append(game_stats)
    return away_team_stats_objects
all_stats=find_home_team_objects()+find_away_team_objects()
# session.add_all(all_stats)
# session.commit()

#team objects  below
all_games_tuples= [(game['venue'], game['home_team_country'], game['away_team_country']) for game in all_games]
h_teams = set([t[1] for t in all_games_tuples])
a_teams = set([t[2] for t in all_games_tuples])
teams = h_teams.union(a_teams)
team_objects = [Team(country = t) for t in teams]
# session.add_all(team_objects)
# session.commit()
# session.query(Team).filter(Team.country == 'Russia').one()

#game objects
all_game_objects = []
for game in all_games:
    h_team = session.query(Team).filter(Team.country == game['home_team_statistics']['country']).one()
    a_team = session.query(Team).filter(Team.country == game['away_team_statistics']['country']).one()
    game_object = Game(venue= game['venue'],
                       teams = [h_team, a_team],
                       winner = game['winner'])
    all_game_objects.append(game_object)
# session.add_all(all_game_objects)
# session.commit()












# all_games_objects[1].teams[1].country = "Uruguay"

# session.add_all(all_stats)
# session.commit()
# print(all_stats)

# all_games_tuples= [(game['venue'], game['home_team_country'], game['away_team_country']) for game in all_games]
# all_games_objects= [Game(venue=t[0], teams = [Team(country=t[1]),Team(country = t[2])]) for t in all_games_tuples]
# print(vars(all_games_objects[1][teams]))

# session.add_all(all_stats)
# session.add_all(all_games_objects)
# session.commit()
# print((vars(all_stats[1])))

















# total_stats = session.query(all_stats).all()
# print(total_stats)
# def assign_stats():
#     total_stats = session.query(all_stats).all()
#     for stat in total_stats:
#         name = stat.country_name
#         team = session.query(Team).filter_by(name=name)
#         stat.team_id = team.id
#         # stat.team = team
#         stat.append(stat.team_id)
#         return total_stats







# game_stats = findgamestats()
# print(game_stats)

    # if game['away_team']['country']==game[teams].country:
        # country=game['away_team']['country']
        # ball_poss= game["away_team_statistics"]["ball_possession"]
        # goals= game['away']['goals']
        # distance= game["away"]["distance_covered"]
        # pass_accur= game["away"]["pass_accuracy"]
        # on_net=game["away"]["on_target"]
        # game_stats = Statistics(county = country,ball_possession=ball_poss, goals=goals,distance_covered=distance,pass_accuracy=pass_accur,on_target=on_net)

        # return game_stats
    # else:
    #     return "Broken"


# looop
# 2) loop and get team id
# 3) Sttatlitcs.team_id= team_id
# #


# def all_team_game_goals():
# #     for game in games:
# #         # if game['status'] in ('completed', 'in progress'):
# #         print (game['home_team']['country'], game['home_team']['goals'], 'x',
#                # game['away_team']['country'], game['away_team']['goals'], game["datetime"],game["winner"])
# game=games[1]
#
# Games:
#     belongs_to :team1, class_name: 'Team', foreign_key: 'team1_id'
#     belongs_to :team2, class_name: 'Team', foreign_key: 'team2_id'
#
# Team:
#     has_many :home_games, class_name: 'Game', foreign_key: 'team1_id'
#     has_many :away_games, class_name: 'Game', foreign_key: 'team2_id'
#     def games
#     Game.where( 'team1_id = ? or team2_id = ?', id, id ).order( 'play_at' )
# Stats:
#     belongs_to :team

# print(all_team_game_goals())
# def away_team_statistics():
#     list=[]
#     for game in all_games:
#         country=game['home_team']['country']
#         ball_poss= game["away_team_statistics"]["ball_possession"]
#         goals= game['away_team']['goals']
#         distance= game["away_team_statistics"]["distance_covered"]
#         pass_accur= game["away_team_statistics"]["pass_accuracy"]
#         on_net=game["away_team_statistics"]["on_target"]
#         game_stats = country,ball_poss, goals,distance,pass_accur,on_net
#         list.append(game_stats)
#         game=Game()
#     return list
#         # game_stats= {"posession":ball_poss, "goals":goals,"distance_covered":distance,"pass_accuracy":pass_accur,"shots_on_net":on_net}
#
#     # dict.append(game_stats)
# print(away_team_statistics()[1])
# print(away_team_statistics())

# def home_team_statistics():
#     for game in games:
#         return (game["home_team_statistics"])
