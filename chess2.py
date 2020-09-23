class Board:
    def __init__(self):
        self.board_state = [[(None, None) for j in range(8)] for i in range(8)]
        
    def put_pieces_on_board(self, initial_pieces_list):
        for piece in initial_pieces_list:
            self.board_state[piece.position[0]][piece.position[1]] = (piece.name,piece.color)
        return self.board_state

b1 = Board()
print(b1.board_state)

class Piece:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position


class Find_Possible_positions:
    def __init__(self, piece, board):
        self.possible_positions = []
        self.piece_name = piece.name
        self.color = piece.color
        self.position = piece.position
        self.board_state = board.board_state
    def north_direction(self):
        north = []
        for j in range(self.position[1],0,-1):
            if self.board_state[self.position[0]][j] == (None, None):
                north.append(self.position[0],j)
            elif self.board_state[self.position[0]][j][1] == self.color:
                break
            else:
                north.append(self.position[0],j)
                break
        return north
    def south_direction(self):
        south = []
        for j in range(self.position[1],8):
            if self.board_state[self.position[0]][j] == (None, None):
                south.append(self.position[0],j)
            elif self.board_state[self.position[0]][j][1] == self.color:
                break
            else:
                south.append(self.position[0],j)
                break
        return south
            
    def east_direction(self):
        east = []
        for i in range(self.position[0],8):
            if self.board_state[i[self.position[1]] == (None, None):
                east.append(i, self.position[1])
            elif self.board_state[i][self.position[1]][1] == self.color:
                break
            else:
                east.append(i, self.position[1])
                break
        return east
            
    def west_direction(self):
        west = []
        for i in range(self.position[0],0,-1):
            if self.board_state[i][self.position[1]] == (None, None):
                west.append(i, self.position[1])
            elif self.board_state[i][self.position[1]][1] == self.color:
                break
            else:
                west.append(i, self.position[1])
                break
        return west

    def north_east_direction(self):
        north_east = []
        for i in range(self.position[0],8):
            for j in range(self.position[1],0,-1):
                if self.board_state[i][j] == (None, None):
                    north_east.append(i,j)
                elif self.board_state[i][j][1] == self.color:
                    break
                else:
                    north_east.append(i,j)
                    break
        return north_east

    def south_east_direction(self):
        south_east = []
        for i in range(self.position[0],8):
            for j in range(self.position[1],8):
                if self.board_state[i][j] == (None, None):
                    south_east.append(i,j)
                elif self.board_state[i][j][1] == self.color:
                    break
                else:
                    south_east.append(i,j)
                    break
        return south_east    
    
            
    def north_west_direction(self):
        north_west = []
        for i in range(self.position[0],0,-1):
            for j in range(self.position[1],0,-1):
                if self.board_state[i][j] == (None, None):
                    north_west.append(i,j)
                elif self.board_state[i][j][1] == self.color:
                    break
                else:
                    north_west.append(i,j)
                    break
        return north_west
    
    def south_west_direction(self):
        south_west = []
        for i in range(self.position[0],0,-1):
            for j in range(self.position[1],8):
                if self.board_state[i][j] == (None, None):
                    south_west.append(i,j)
                elif self.board_state[i][j][1] == self.color:
                    break
                else:
                    south_west.append(i,j)
                    break
        return south_west
    
    def get_possible_positions(self):
        
        if self.piece_name == 'king':
            self.possible_positions = [(self.position[0] + 1,self.position[1] + 1),(self.position[0],self.position[1] + 1),(self.position[0] - 1,self.position[1] + 1),(self.position[0] + 1,self.position[1]),self.position,
             (self.position[0] - 1,self.position[1]),(self.position[0] + 1,self.position[1] - 1),(self.position[0],self.position[1] - 1),(self.position[0] - 1,self.position[1] - 1)]
            return self.possible_positions
        
        elif self.piece_name == 'knight':
            self.possible_positions = [(self.position[0] + 1,self.position[1] + 2),(self.position[0] + 2,self.position[1] + 1),(self.position[0] + 2,self.position[1] - 1),(self.position[0] + 1,self.position[1] - 2),self.position,
             (self.position[0] - 1,self.position[1] + 2),(self.position[0] - 2,self.position[1] + 1),(self.position[0] - 2,self.position[1] - 1),(self.position[0] - 1,self.position[1] - 2)]
            return self.possible_positions
        
        elif self.piece_name == 'pawn':
            if (self.position[0]) == 1:
                self.possible_positions = [(self.position[0] + 2 ,self.position[1]),(self.position[0] + 1 ,self.position[1] - 1),(self.position[0] + 1 ,self.position[1]),(self.position[0] + 1 ,self.position[1] + 1)]
            else:
                self.possible_positions = [(self.position[0] + 1 ,self.position[1] - 1),(self.position[0] + 1 ,self.position[1]),(self.position[0] + 1 ,self.position[1] + 1)]
            return self.possible_positions
        
        elif self.piece_name == 'queen':
            self.possible_positions = north_direction() + south_direction() + east_direction() + west_direction() + north_east_direction() + north_west_direction() + south_east_direction() + south_west_direction()
            return self.possible_positions
        
        elif self.piece_name == 'rook':
            self.possible_positions = north_direction() + south_direction() + east_direction() + west_direction()
            return self.possible_positions
        
        elif self.piece_name == 'bishop':
            self.possible_positions = north_east_direction() + north_west_direction() + south_east_direction() + south_west_direction()
            return self.possible_positions     

               



class Move:
    def __init__(self,current_position,next_position):
        self.current_position = current_position
        self.next_position = next_position
    def do_move(self, possible_positions_list):
        if self.next_position in possible_positions_list:
            self.current_position = self.next_position
        else:
            print("Invalid movement")
            



def initialize_game():
    KW = Piece('king','W',(0,3))
    QW = Piece('queen','W',(0,4))
    R1W = Piece('rook','W',(0,0))
    R2W = Piece('rook','W',(0,7))
    K1W = Piece('knight','W',(0,1))
    K2W = Piece('knight','W',(0,6))
    B1W = Piece('bishop','W',(0,2))
    B2W = Piece('bishop','W',(0,5))
    P1W = Piece('pawn','W',(1,0))
    P2W = Piece('pawn','W',(1,1))
    P3W = Piece('pawn','W',(1,2))
    P4W = Piece('pawn','W',(1,3))
    P5W = Piece('pawn','W',(1,4))
    P6W = Piece('pawn','W',(1,5))
    P7W = Piece('pawn','W',(1,6))
    P8W = Piece('pawn','W',(1,7))
    KB = Piece('king','B',(7,3))
    QB = Piece('queen','B',(7,4))
    R1B = Piece('rook','B',(7,0))
    R2B = Piece('rook','B',(7,7))
    K1B = Piece('knight','B',(7,1))
    K2B = Piece('knight','B',(7,6))
    B1B = Piece('bishop','B',(7,2))
    B2B = Piece('bishop','B',(7,5))
    P1B = Piece('pawn','B',(6,0))
    P2B = Piece('pawn','B',(6,1))
    P3B = Piece('pawn','B',(6,2))
    P4B = Piece('pawn','B',(6,3))
    P5B = Piece('pawn','B',(6,4))
    P6B = Piece('pawn','B',(6,5))
    P7B = Piece('pawn','B',(6,6))
    P8B = Piece('pawn','B',(6,7))
    initial_pieces = [KW, QW, R1W, R2W, K1W, K2W, B1W, B2W, P1W, P2W, P3W, P4W, P5W, P6W, P7W, P8W, KB, QB, R1B, R2B, K1B, K2B, B1B, B2B, P1B, P2B, P3B, P4B, P5B, P6B, P7B, P8B]
    return initial_pieces
initial_pieces = initialize_game()
print(initial_pieces[0].position)
b1.put_pieces_on_board(initial_pieces)
print(b1.board_state)
