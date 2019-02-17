Team.query.all(), Team.country, Team.query[1].country = Team name "Iceland"
        vars(Team.query[1])
        Out[27]:
        {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState at 0x111d14e48>,
         'id': 2,
         'country': 'Iceland'}

Game.query.all()
        vars(Game.query[1])
        Out[25]:
        {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState at 0x111d7f080>,
         'winner': 'Uruguay',
         'id': 2,
         'venue': 'Ekaterinburg'}

Statistics.query.all()
    ---vars(Statistics.query[1])
                Out[23]:
                {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState at 0x111d4d048>,
                 'distance_covered': 105,
                 'goals': 0,
                 'team_id': 25,
                 'id': 2,
                 'on_target': 0,
                 'ball_possession': 60,
                 'name': 'Saudi Arabia',
                 'game_id': 1,
                 'pass_accuracy': 86}


vars(Team)
mappingproxy({'__module__': 'ourpackage.models', '__tablename__':
 'teams', 'id': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x103dbc888>,
 'country': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x103dbc938>,
 'statistics': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x103dbc780>,
  'games': <sqlalchemy.orm.attributes.InstrumentedAttribute object at 0x103dbc830>,
  'to_dict': <function Team.to_dict at 0x1032f52f0>, '__doc__': None,
  '__table__': Table('teams', MetaData(bind=None), Column('id', Integer(), table=<teams>, primary_key=True, nullable=False),
  Column('country', String(), table=<teams>), schema=None), '_sa_class_manager': <ClassManager of <class 'ourpackage.models.Team'> at 103dbc678>,
   '__init__': <function __init__ at 0x1032f5d08>, '__mapper__': <Mapper at 0x103da56a0; Team>})
>>>
