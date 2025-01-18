import random
import time

from data.a1 import genetic_apex

class Draft:
    def __init__(self, opts):
        card_pool = genetic_apex

        packs = []
        for rarity in opts['rounds']:
            cards_per_pack = opts['cards_per_rarity'][rarity]
            possible_cards = card_pool[rarity]
            random.shuffle(possible_cards)
            packs.append([
                possible_cards[i*cards_per_pack:(i + 1)*cards_per_pack]
                for i in range(len(opts['players']))
            ])

        self.opts = opts
        self.packs = packs

    def export(self):
        name = time.strftime('%Y-%m-%d: Pokemon Pocket Draft')
        print(name, self.packs)

if __name__ == '__main__':
    Draft({
        'players': ['red', 'blue', 'yellow'],
        'rounds': ['2s', '1s', '4d', '3d', '2d', '1d', 't'],
        'cards_per_rarity': {
            '2s': 3,
            '1s': 3,
            '4d': 6,
            '3d': 8,
            '2d': 10,
            '1d': 12,
            't': 4,
        },
    }).export()
