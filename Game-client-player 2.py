import sys
import socket
from GAME_Functions import Game_Rules
## Client ##
if __name__ == "__main__":
    from_addr = (socket.gethostname(),9988)
    to_addr = (socket.gethostname(),9999)
    
    game_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    game_sock.bind(from_addr)
    print("Game has started running on :",socket.gethostname())
    game = Game_Rules(type="client", socket=game_sock, to_addr=to_addr)
    
    player=1
    game.instructions(player)
    game.client_loop()

    
