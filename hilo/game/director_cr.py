from game.card import Card

# Hi all - I started this Director file and I don't think I am doing it correctly. I am realizing now that I may have put some of the 
# code meant for the Card class in this file... 
# I am having a hard time separating the code into the different class files in my mind and am getting confused. 
# Feel free to make suggestions on how I can fix this :)

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """

        self.card = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args: 
            self (Director): an instance of Director.
        """

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to draw.
        
        Args:
            self (Director): an instance of Director.
        """

        draw_card = input("Draw card? (y/n) ")
        self.is_playing = (draw_card =="y")


    def do_updates(self):
        """Updates the player's score. 
        
        Args: 
            self (Director): an instance of Director.
        """

        if not self.is_playing:
            return

        score = 300
        # add new code with the instance card     

    def do_outputs(self):
        """Displays the card and the score. 
            Also asks the player if they want to draw again.
            
        Args: 
            self (Director): An instance of Director.
        """

        if not self.is_playing:
            return
        
        print(f"Your score is: {score}")

    

            