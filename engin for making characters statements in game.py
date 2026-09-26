
full_dot = '●'
empty_dot = '○'





def create_character( character_name , strength , intelligense , charisma ):

    if isinstance(character_name , (str)) == False :

        return'The chracter name should be string'

    if len(character_name)== 0 :

        return'The character should have name'

    if len(character_name) > 10 :

        return'The character name is too long'

    if " " in character_name :

        return'The character name should not contain spaces'

    if isinstance(strength , (int)) == False or isinstance(intelligense , (int)) == False or isinstance(charisma , (int)) == False :

        return'All stats should be integers'

    if strength < 1 or intelligense < 1 or charisma < 1 :

        return'All stats should be no less than 1'

    if strength > 4 or intelligense > 4 or charisma > 4 :

        return'All stats should be no more than 4'

    if strength + intelligense + charisma != 7 :

        return'The character should start with 7 points'

    state = (f" {character_name}\n"

            f"STR {strength * full_dot}{(10 - strength) * empty_dot}\n"

            f"INT {intelligense * full_dot}{(10 - intelligense) * empty_dot}\n"

            f"CHA {charisma * full_dot}{(10 - charisma) * empty_dot}"
    )

    return state



character_statement = create_character( 'Amirreza' , 3 , 2 , 2)
print(character_statement)

        
        




