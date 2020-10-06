import socket
from GAME_Functions import Game_Rules

if __name__ == "__main__":
    name=socket.gethostname()
    from_addr = (name,9999)
    to_addr = (name,9988)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind(from_addr)
    
    
    print("Game has started running on :",socket.gethostname())
    game = Game_Rules(type="server", socket=s, to_addr=to_addr)
    
    
    player=0
    game.instructions(player)
    print("Waiting for other players to connect...")
    game.server_loop()
    
    
