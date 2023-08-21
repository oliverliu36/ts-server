from hello.models import Player
# entry_list is "LASTNAME, FISTNAME"
def get_new_players_list(entry_list):
    final_list = [] #final_list is the players that we need to look up.
    for entry in entry_list:
        new_last_name = entry.split(', ')[0]
        new_first_name = entry.split(', ')[1]
        res = Player.objects.filter(last_name=new_last_name).filter(first_name=new_first_name)
        lst = list(res)
        if(len(lst) == 0):
            final_list.append(entry)
    return final_list


def look_up_players(entry_list):
    final_list = []
    for entry in entry_list:
        new_last_name = entry.split(', ')[0]
        new_first_name = entry.split(', ')[1]
        res = Player.objects.filter(last_name=new_last_name).filter(first_name=new_first_name)
        lst = list(res)
        if(len(lst) > 0):
            new_player = {
                "last_name": new_last_name,
                "first_name": new_first_name,
                "info": lst[0].info,
                "utr": lst[0].utr
            }
            # p = {}
            # p["info"] = lst[0].info
            final_list.append(new_player)
    return final_list

