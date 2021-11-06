import stratz
import json

api = stratz.Api(lang=stratz.English)

def main():
    player = api.get_player(id=1258446607)
    player_matches = api.get_player_macthes(id=1258446607)

    json.dump(player, open("player.json", "w", encoding="utf-8"))
    json.dump(player_matches, open("player_matches.json", "w", encoding="utf-8"))


if __name__ == "__main__":
    main()