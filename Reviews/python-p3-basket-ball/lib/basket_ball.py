from statistics import mean


def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }


def all_players ( ) :
    return game_dict()['home']['players'] + game_dict()['away']['players']

def get_player_by_name ( name ) :
    player_by_name = {}
    for player in all_players() :
        if player['name'] == name :
            player_by_name = player
    
    if player_by_name :
        return player_by_name
    else :
        raise Exception( 'Player not found.' )
    

def get_team_by_name ( name ) :
    return [ game_dict()[team] for team in game_dict() if game_dict()[team]['team_name'] == name ][0]
    
    # team_by_name = {}
    # for team in game_dict() :
    #     if game_dict()[team]['team_name'] == name :
    #         team_by_name = game_dict()[team]
    # return team_by_name


# def player_names ( ) :
#     return list( map( lambda player : player['name'], all_players() ) )

def num_points_per_game ( player_name ) :
    return get_player_by_name( player_name )['points_per_game']

def player_age ( player_name ) :
    return get_player_by_name( player_name )['age']

def team_colors ( team_name ) :
    return get_team_by_name( team_name )['colors']

def team_names () :
    return [ game_dict()[team]['team_name'] for team in game_dict() ]
    # return game_dict().map( team => team.team_name )


def player_numbers ( team_name ) :
    return [ player['number'] for player in get_team_by_name( team_name )['players'] ]

    # jersey_numbers = []
    # for player in get_team_by_name( team_name )['players'] :
    #     jersey_numbers.append( player['number'] )
    # return jersey_numbers


def player_stats ( player_name ) :
    return get_player_by_name( player_name )

def average_rebounds_by_shoe_brand () :
    shoe_brands = []
    for player in all_players() :
        shoe_brands.append( player['shoe_brand'] )
    shoe_brands = set( shoe_brands )
    shoe_brands = list( shoe_brands )

    shoe_brands_with_rebounds = []
    for shoe_brand in shoe_brands :
        brand = {}
        brand[shoe_brand] = []
        shoe_brands_with_rebounds.append( brand )
        for player in all_players() :
            if player['shoe_brand'] == shoe_brand :
                brand[shoe_brand].append( player["rebounds_per_game"] )

        brand[shoe_brand] = round( mean( brand[shoe_brand] ), 2 )

    return shoe_brands_with_rebounds


def player_with_most_career_points ( ) :
    players_sorted_by_career_points = all_players()
    players_sorted_by_career_points.sort( key = lambda player: player['career_points'] )
    return players_sorted_by_career_points[-1]

def player_with_longest_name ( ) :
    longest_name = all_players()[0]
    for player in all_players() :
        if len( longest_name['name'] ) < len( player['name'] ) :
            longest_name = player

    return longest_name

def overlapping_jersey_numbers () :
    home_team = player_numbers( game_dict()['home']['team_name'] )
    away_team = player_numbers( game_dict()['away']['team_name'] )
    return set( home_team ) & set( away_team ) if set( home_team ) & set( away_team ) else 'There are no matching jersey numbers. 🙁'
    pass