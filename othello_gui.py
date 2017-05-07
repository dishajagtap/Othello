# Disha Jagtap. 86199478.

import tkinter
import othello_game

DEFAULT_FONT = ('Helvetica',18)

class Startscreen:
    '''Class containing all of the attributes of the startscreen of Othello, asking the user
    about the parameters of the game to be played'''
    def __init__(self)->None:
        '''Creates the main window and canvas where the widgets will lie'''
        self._dialog_window = tkinter.Tk()
        self._dialog_window.title('Othello')
        self._bottom_canvas = tkinter.Canvas(master = self._dialog_window,width = 500,
                                      height = 500, background = '#ffffff')
        self._bottom_canvas.grid(row=0,column=0,
                                 sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._canvas = tkinter.Canvas(master = self._dialog_window,width = 500,
                                      height = 500, background = '#80d4ff')
        self._canvas.grid(row = 0, column = 0, padx = 0, pady = 0,
                          sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        self._rows = 4
        self._cols = 4

        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(0, weight = 1)

        self._canvas.rowconfigure(0, weight = 1)
        self._canvas.rowconfigure(1, weight = 1)
        self._canvas.rowconfigure(2, weight = 1)
        self._canvas.rowconfigure(3, weight = 1)
        self._canvas.rowconfigure(4, weight = 1)
        self._canvas.rowconfigure(5, weight = 1)

        self._canvas.columnconfigure(0, weight = 1)
        self._canvas.columnconfigure(1, weight = 1)
        self._canvas.columnconfigure(2, weight = 1)
        self._canvas.columnconfigure(3, weight = 1)

    def init_widgets(self)->None:
        '''Creates the widgets which register user input on the parameters of the game'''

        '''Dimensions'''
        row_label = tkinter.Label(master = self._canvas, text = 'Rows: ',font = DEFAULT_FONT,bg = '#80d4ff')
        row_label.grid(row =0, column = 0)

        self._row_input = tkinter.Spinbox(master = self._canvas, from_ = 4,to = 16,
                                          increment = 2, width = 2, wrap = True, state = 'readonly',
                                          font = DEFAULT_FONT,command = self._on_row_buttons_clicked,
                                          highlightbackground = '#80d4ff')
        self._row_input.grid(row=0,column=1,sticky=tkinter.W)

        col_label = tkinter.Label(master = self._canvas, text = 'Columns: ',font = DEFAULT_FONT,bg = '#80d4ff')
        col_label.grid(row = 1,column = 0)

        self._col_input = tkinter.Spinbox(master = self._canvas, from_ = 4,to = 16,
                                          increment = 2, width = 2, wrap = True, state = 'readonly',
                                          font = DEFAULT_FONT, command = self._on_col_buttons_clicked,
                                          highlightbackground = '#80d4ff')
        self._col_input.grid(row=1,column=1,sticky=tkinter.W)

        '''first player'''
        fplayer_label = tkinter.Label(master=self._canvas,text = 'First Player: ',font = DEFAULT_FONT,
                                      bg = '#80d4ff')
        fplayer_label.grid(row=2,column=0)

        self._fplayer_var = tkinter.IntVar()
        first_player_W = tkinter.Radiobutton(master = self._canvas,text = 'W',
                                             variable = self._fplayer_var,value =1,font = DEFAULT_FONT,
                                             bg = '#80d4ff')
        first_player_W.grid(row=2,column=1,sticky=tkinter.W)

        first_player_B = tkinter.Radiobutton(master = self._canvas,text ='B',
                                             variable = self._fplayer_var, value=2,font = DEFAULT_FONT,
                                             bg = '#80d4ff')
        first_player_B.grid(row=2,column=2,sticky=tkinter.W)

        '''top left'''
        top_left_label = tkinter.Label(master=self._canvas,text='Top Left Player: ',
                                       font = DEFAULT_FONT,bg = '#80d4ff')
        top_left_label.grid(row=3,column=0)
        self._top_left_player = tkinter.IntVar()
        top_left_W = tkinter.Radiobutton(master = self._canvas,text = 'W',
                                                   variable = self._top_left_player,value =1,font = DEFAULT_FONT,
                                         bg = '#80d4ff')
        top_left_W.grid(row=3,column=1,sticky = tkinter.W)

        top_left_B = tkinter.Radiobutton(master = self._canvas,text = 'B',
                                         variable = self._top_left_player,value =2,font = DEFAULT_FONT,
                                         bg = '#80d4ff')
        top_left_B.grid(row=3,column=2,sticky = tkinter.W)

        '''winning method'''
        winning_method_label = tkinter.Label(master=self._canvas,text = 'Who Wins?',font = DEFAULT_FONT,
                                             bg = '#80d4ff')
        winning_method_label.grid(row=4,column=0)

        self._winning_method = tkinter.IntVar()
        winning_method_most = tkinter.Radiobutton(master = self._canvas,text = 'Most Tiles Wins',font = DEFAULT_FONT,
                                                   variable = self._winning_method,value =1,bg = '#80d4ff')
        winning_method_most.grid(row=4,column=1,sticky=tkinter.W)

        winning_method_least = tkinter.Radiobutton(master = self._canvas,text = 'Least Tiles Wins',font = DEFAULT_FONT,
                                                   variable = self._winning_method,value =2,bg = '#80d4ff')
        winning_method_least.grid(row=4,column=2,sticky=tkinter.W)

        '''play button'''
        play_button = tkinter.Button(master = self._canvas, text = 'Play Othello!',font = DEFAULT_FONT,bg = '#80d4ff',
                                     command = self._on_button_pressed,highlightbackground = '#80d4ff')
        play_button.grid(row=5,column=0,columnspan=3)

    def _on_row_buttons_clicked(self) -> None:
        '''Assigns the value of row spinbox to row attribute of class'''
        self._rows = int(self._row_input.get())

    def _on_col_buttons_clicked(self) -> None:
        '''Assigns the value of column spinbox to column attribute of class'''
        self._cols = int(self._col_input.get())

    def _on_button_pressed(self)-> None:
        '''Creates Gamescreen object to start playing the game'''
        self._fplayer = self._fplayer_var.get()
        self._top_left = self._top_left_player.get()
        winning_method = self._winning_method.get()
        self._winning_method = '>' if winning_method == 1 else '<'
        self._quit_window()

        self._start_gamescreen()

    def start(self) -> None:
        '''Start the mainloop'''
        self._dialog_window.mainloop()

    def _quit_window(self)->None:
        '''Quits the startscreen window'''
        self._dialog_window.destroy()

    def _start_gamescreen(self)->None:
        '''Creates and runs Gamescreen object in a new window using user inputs'''
        gamescreen = Gamescreen(self._rows,self._cols,self._fplayer,self._top_left,self._winning_method)
        gamescreen.init_game()
        gamescreen.start()

class Gamescreen:
    def __init__(self,rows:int,cols:int,fplayer:int,top_left:int,winning_method:str)->None:
        '''Initialize Gamescreen object with user input parameters'''
        self._root_window = tkinter.Tk()
        self._root_window.title('Othello - FULL')

        self._rows = rows
        self._cols = cols
        self._fplayer = fplayer
        self._top_left = top_left
        self._winning_method = winning_method

        self._stats_canvas_bottom = tkinter.Canvas(master = self._root_window, width = 600, height = 40)
        self._stats_canvas_bottom.grid(row=0,column=0,sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E,padx=5)

        self._stats_canvas_top = tkinter.Canvas(master = self._root_window, width = 600, height = 40, background = '#000000',
                                                highlightbackground='black')
        self._stats_canvas_top.grid(row=0,column=0,sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E,padx=5)


        self._white_count = tkinter.StringVar()
        self._white_count.set('White: {}'.format(2))
        self._white_label = tkinter.Label(master = self._stats_canvas_top,textvariable = self._white_count,font = DEFAULT_FONT,
                                          bg = '#000000',fg = '#ffffff')
        self._white_label.grid(row=0,column=0)

        self._black_count = tkinter.StringVar()
        self._black_count.set('Black: {}'.format(2))
        self._black_label = tkinter.Label(master = self._stats_canvas_top,textvariable = self._black_count,font = DEFAULT_FONT,
                                          bg = '#000000',fg='#ffffff')
        self._black_label.grid(row=0,column=2)

        self._turn = tkinter.StringVar()
        self._turn.set('Turn: {}'.format(self.int_to_player(self._fplayer)))
        self._turn_label = tkinter.Label(master = self._stats_canvas_top,textvariable = self._turn,font = DEFAULT_FONT,
                                         bg = '#000000',fg='#ffffff')
        self._turn_label.grid(row=0,column=1)


        self._canvas = tkinter.Canvas(master = self._root_window,width = 600,
                                      height = 600, background = '#ffffff',highlightbackground='black')

        self._canvas.grid(row = 1, column = 0, padx = 5, pady = 5,
                         sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self._canvas.update()

        self._width = self._canvas.winfo_width()
        self._height = self._canvas.winfo_height()

        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

        self._stats_canvas_top.rowconfigure(0,weight = 1)
        self._stats_canvas_top.columnconfigure(0,weight = 1)
        self._stats_canvas_top.columnconfigure(1,weight = 1)
        self._stats_canvas_top.columnconfigure(2,weight = 1)

    def _set_count_tiles(self)->None:
        '''Counts the tiles of each player and sets it to its corresponding StringVar object variables'''
        self.gamestate.count_tiles()
        self._white_count.set('White: {}'.format(self.gamestate.w_count))
        self._black_count.set('Black: {}'.format(self.gamestate.b_count))

    '''Event Handlers'''
    def _on_canvas_resized(self,event:tkinter.Event)->None:
        '''whenever the canvas' size changes, redraws all of the tiles and the board on the screen'''
        self._canvas.delete(tkinter.ALL)

        self._width = self._canvas.winfo_width()
        self._height = self._canvas.winfo_height()

        self._display_board()

    def _on_canvas_clicked(self,event:tkinter.Event)->None:
        '''Gets the pixel coordinates of where the click occured and handles it'''
        click_point = event.x, event.y
        self._handle_click(click_point)

    '''Game Handlers'''
    def init_game(self)->None:
        '''Initializes Othello game'''
        self.gamestate = othello_game.new_game()
        othello_game.create_gameboard(self.gamestate, self._rows, self._cols)
        try:
            self.gamestate.init_turn(self._fplayer)
        except:
            raise SystemExit
        try:
            othello_game.init_gameboard(self.gamestate,self._top_left)
        except:
            raise SystemExit

        self._display_board()

    def _handle_click(self,click_point:(int,int))->None:
        '''Converts click point to row and col input and plays the game'''
        row , col = self._from_pixel(click_point)
        try:
            if not othello_game.game_over(self.gamestate):
                self._play_Othello(row,col)
                if othello_game.game_over(self.gamestate):
                    self._winner_popup()
            else:
                self._winner_popup()
        except othello_game.StalemateError:
            self._winner_popup()

    def _play_Othello(self, row:int, col:int)->None:
        '''Makes a move'''
        try:
            self.gamestate = othello_game.make_move(self.gamestate, row, col)
        except othello_game.InvalidMove:
            pass
        except IndexError:
            pass
        else:
            self._display_board()
            othello_game.flip_turn(self.gamestate)
            othello_game.game_over(self.gamestate)
            self._turn.set('Turn: {}'.format(self.int_to_player(self.gamestate.turn)))

    def _winner_popup(self)->None:
        '''Creates a separate window that is generated when the game is over and displays the winner'''
        self._popup = tkinter.Toplevel()

        bottom_canvas = tkinter.Canvas(master = self._popup, width = 300, height = 300,background = '#80d4ff')
        bottom_canvas.grid(row=0,column=0,sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        top_canvas = tkinter.Canvas(master = self._popup, width = 300, height = 300, background = '#80d4ff')
        top_canvas.grid(row=0,column=0,sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        game_over_label = tkinter.Label(master = top_canvas,text = 'Game Over!',bg = '#80d4ff',font=DEFAULT_FONT)
        game_over_label.grid(row=0,column=0)

        winner_var = tkinter.StringVar()
        winner_var.set('Winner: {}'.format(self.int_to_player(othello_game.winner(self.gamestate,self._winning_method))))
        winner_label = tkinter.Label(master = top_canvas,textvariable = winner_var,bg = '#80d4ff',
                                     font = DEFAULT_FONT)
        winner_label.grid(row=1,column=0)

        done_button = tkinter.Button(master = top_canvas, text = 'Exit',command = self._on_window_exit,
                                     highlightbackground= '#80d4ff',font = DEFAULT_FONT)
        done_button.grid(row=2,column=0)

        self._popup.protocol('WM_DELETE_WINDOW',self._on_window_exit)

        self._popup.rowconfigure(0, weight = 1)
        self._popup.columnconfigure(0, weight = 1)

        top_canvas.rowconfigure(0,weight=1)
        top_canvas.rowconfigure(1,weight=1)
        top_canvas.rowconfigure(2,weight=1)
        top_canvas.columnconfigure(0,weight=1)

    def _on_window_exit(self)->None:
        '''Exits the winner window and Othello game window'''
        self._popup.destroy()
        self._root_window.destroy()

    '''Drawing Board Methods'''
    def _draw_empty_board(self)->None:
        ''' Draws rectangles on canvas simulating an empty board'''
        self._rec_width = self._width/self._cols
        self._rec_height = self._height/self._rows

        self._x_gap = 0.2*self._rec_width
        self._y_gap = 0.2*self._rec_height
        self._diameter_x = self._rec_width - self._x_gap
        self._diameter_y = self._rec_height - self._y_gap

        i = -1+self._rec_width
        j = -1+self._rec_height
        start_i = 0
        start_j = 0

        count = 0
        light_green = '#008000'
        green = '#004d00'
        while i<self._width:
            while j<self._height:
                color = green if count % 2 == 0 else light_green
                self._canvas.create_rectangle(start_i,start_j,i,j,fill = color,width=0)
                start_j=j
                j+=self._rec_height
                count+=1
            count+=1
            start_j=0
            j=-1+self._rec_height
            start_i=i
            i+=self._rec_width

    def _display_board(self)->None:
        '''Displays board's tiles on canvas simulating the gameboard'''
        self._draw_empty_board()
        self._set_count_tiles()
        for i in range(len(self.gamestate.board)):
            for j in range(len(self.gamestate.board[i])):
                if self.gamestate.board[i][j] == othello_game.WHITE:
                    self._draw_tile(i,j,'white')
                elif self.gamestate.board[i][j] == othello_game.BLACK:
                    self._draw_tile(i,j,'black')

    def _draw_tile(self,i:int,j:int,color:str)->None:
        '''Draws a tile in specified row and col with 'color' color'''
        start_x = j*self._rec_width + self._x_gap/2
        start_y = i*self._rec_height + self._y_gap/2

        end_x = start_x + self._diameter_x
        end_y = start_y + self._diameter_y

        self._canvas.create_oval(start_x,start_y,end_x,end_y,fill = color,outline = 'black')

    def _from_pixel(self,click_point:(int,int))->(int,int):
        '''Returns pixel on canvas as a tuple of row and col of the gameboard'''
        x,y = click_point
        x = int(x/self._rec_width)
        y = int(y/self._rec_height)
        return y,x

    def int_to_player(self,player: int)->str:
        '''Given the player's integer,
        returns the string representing the player
        '''
        int_dict = {othello_game.NONE: 'None', othello_game.WHITE: 'White', othello_game.BLACK: 'Black'}
        return int_dict[player]

    def start(self)->None:
        '''Starts the mainloop'''
        self._root_window.mainloop()

def start_game()->None:
    '''Starts the GUI by creating and running a Startscreen object'''
    screen = Startscreen()
    screen.init_widgets()
    screen.start()

if __name__ == '__main__':
    start_game()

