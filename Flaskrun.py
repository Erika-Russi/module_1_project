# ### Classes have to add to dictionary function***
#Questions def to_dict for
    # 1) relationships
    # 2)multiple elments i.e. statistics
####1)


# import Flask and jsonify from flask
from flask import Flask, jsonify
# import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import * #Column, Integer, String, ForeignKey, DateTime, create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref


# initialize new flask app
app = Flask(__name__)
# add configurations and database URI
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# connect SQLAlchemy to the configured flask app
db = SQLAlchemy(app)

#define routes and their respective functions that return the correct data
# remember that each function must have a unique name

class Game(db.Model):
    __tablename__ = 'games'
    id = db.Column(db.Integer, primary_key=True)
    venue = db.Column(db.String)
    winner = db.Column(db.String)
    statistics = db.relationship('Statistics', back_populates="game")
    teams = db.relationship(
        'Team',
        secondary='statistics',
        back_populates='games'
    )
    def to_dict(self):
        game = {'id': self.id, 'venue': self.venue, 'winner': self.winner} #'statistics': [tweet.to_dict() for tweet in self.tweets]
        return game

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String)
    statistics = db.relationship('Statistics', back_populates="team")
    games = db.relationship(
        'Game',
        secondary='statistics',
        back_populates='teams'
    )
    def to_dict(self):
        team = {'id': self.id, 'country': self.country,}
        return team

class Statistics(db.Model):
    __tablename__ = 'statistics'
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    name = db.Column(db.String)
    goals = db.Column(db.Integer)
    game = db.relationship('Game', back_populates='statistics')
    team = db.relationship('Team', back_populates='statistics')

    ball_possession=db.Column(db.Integer)
    distance_covered=db.Column(db.Integer)
    on_target=db.Column(db.Integer)
    pass_accuracy=db.Column(db.Integer)
    def to_dict(self):
        tweet = {'id': self.id, 'game_id': self.game_id, 'team_id': self.team_id,'name': self.name,'goals': self.goals}
        return tweet

@app.route('/team/')
def user_index():
    all_teams = db.session.query(Team).all()
    all_teams_dicts = [team.to_dict() for team in all_teams]
    return jsonify(all_teams_dicts)

# run the server
if __name__ == "__main__":
    app.run()


# @app.route('/goals/')
# def return_country_and_its_total_goals():
#     session= session.db.query(Team.country, func.sum(Statistics.goals)).join(Statistics).group_by(Team.country).all()
#     return session

# created JSON routes for our API
# @app.server.route('/api/users')
# def user_index():
#     all_users = db.session.query(User).all()
#     all_users_dicts = [user.to_dict() for user in all_users]
#     return jsonify(all_users_dicts)
#
# @app.server.route('/api/users/<int:id>')
# def find_user(id):
#     user = User.query.filter(User.id == id).first()
#     return jsonify(user.to_dict())
#
#
#
#
# # created routes for the appropriate HTML Templates
# @app.server.route('/users')
# def users_index():
#     all_users = db.session.query(User).all()
#     all_users_dicts = [user.to_dict() for user in all_users]
#     return render_template('users.html', users=all_users_dicts)
















#
# #old Lab below
#
# @app.server.route('/api/users/<name>')
# def find_user_by_name(name):
#     user = User.query.filter(User.username.like(name)).first()
#     return jsonify(user.to_dict())
#
# @app.server.route('/api/tweets')
# def tweet_index():
#     all_tweets = Tweet.query.all()
#     all_tweets_dicts = [tweet.to_dict() for tweet in all_tweets]
#     return jsonify(all_tweets_dicts)
#
# @app.server.route('/api/tweets/<int:id>')
# def find_tweet(id):
#     return jsonify(Tweet.query.filter(Tweet.id == id).first().to_dict())
#
# @app.server.route('/api/users/<int:user_id>/tweets')
# def find_users_tweets(user_id):
#     return jsonify(User.query.filter(User.id == user_id).first().to_dict())
#
# @app.server.route('/api/users/<user_name>/tweets')
# def find_users_tweets_by_user_name(user_name):
#     return jsonify(User.query.filter(User.name == user_name.lower().title()).first().tweets())
#
# @app.server.route('/api/tweets/<int:tweet_id>/user')
# def find_tweets_user(tweet_id):
#     return jsonify(Tweet.query.filter(Tweet.id == tweet_id).first().user.to_dict())
# @app.server.route('/users/<int:id>')
# def user_show_by_id(id):
#     user = User.query.filter(User.id == id).first().to_dict()
#     return render_template('user_show.html', user=user)
#
# @app.server.route('/users/<name>')
# def user_show_by_name(name):
#     user = User.query.filter(User.username.like(name)).first().to_dict()
#     return render_template('user_show.html', user=user)
#
# @app.server.route('/tweets')
# def tweets_index():
#     all_tweets = Tweet.query.all()
#     all_tweets_dicts = [tweet.to_dict() for tweet in all_tweets]
#     return render_template('tweets.html', tweets=all_tweets_dicts)
#
# @app.server.route('/tweets/<int:id>')
# def tweet_show_by_id(id):
#     tweet = Tweet.query.filter(Tweet.id == id).first().to_dict()
#     return render_template('tweet_show.html', tweet=tweet)
#
# @app.server.route('/users/<int:user_id>/tweets')
# def find_tweets_by_user_id(user_id):
#     user_tweets = User.query.filter(User.id == user_id).first().to_dict()
#     return render_template('tweets.html', tweets=user_tweets['tweets'])
#
# @app.server.route('/users/<user_name>/tweets')
# def find_tweets_by_username(user_name):
#     user_tweets = User.query.filter(User.username == user_name.lower().title()).first().to_dict()
#     return render_template('tweets.html', tweets=user_tweets['tweets'])
#
# @app.server.route('/tweets/<int:tweet_id>/user')
# def find_user_by_tweet(tweet_id):
#     tweet = Tweet.query.filter(Tweet.id == tweet_id).first().to_dict()
#     user = User.query.filter(User.id == tweet['user_id']).first().to_dict()
#     return render_template('user_show.html', user=user)
