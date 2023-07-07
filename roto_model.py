class Roto:
    def __init__(self, players, cube_text_file):
        self.players = players
        self.cube_list = self.load_cube_from_file(cube_text_file)
        self.pick_list = []

    def __str__(self):
        return f'Players: {" ".join(self.players)}\nlen(cube_list): {len(self.cube_list)}\npick_list: {self.pick_list}'

    def load_cube_from_file(self, file):
        with open(file) as f:
            #remove empty lines
            lines = [l for l in f.readlines() if l]
        #remove comments
        return [l for l in lines if '#' not in l]

    def pick(self, player, card_name):
        if card_name not in self.cube_list:
            return "Card not in cube"
        self.pick_list.append((player, card_name))
        self.cube_list.remove(card_name)
        return f'{player} picked {card_name}'


if __name__ == '__main__':
    players = ['a', 'b', 'c']
    file_path = '/Users/elliotmartin/Downloads/EastBayCubingPeasantRotisserieDraft.txt'
    my_roto = Roto(players, file_path)

