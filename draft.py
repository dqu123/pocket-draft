import random
import time
import json

from data.a1 import genetic_apex, mythical_island


def combine_data(datasets):
    combined = {}
    for dataset in datasets:
        for key, value in dataset.items():
            if key not in combined:
                combined[key] = []
            combined[key] += value
    return combined


class Draft:
    def __init__(self, opts):
        card_pool = combine_data([genetic_apex, mythical_island])

        packs = []
        for rarity in opts["rounds"]:
            cards_per_pack = opts["cards_per_rarity"][rarity]
            possible_cards = card_pool[rarity]
            random.shuffle(possible_cards)
            packs.append(
                [
                    possible_cards[i * cards_per_pack : (i + 1) * cards_per_pack]
                    for i in range(len(opts["players"]))
                ]
            )

        self.opts = opts
        self.packs = packs

    def export(self):
        name = time.strftime("%Y-%m-%d_PokemonPocketDraft")
        with open("output/{}.json".format(name), "w") as f:
            f.write(json.dumps(self.packs, indent=2))


if __name__ == "__main__":
    Draft(
        {
            "players": ["red", "blue", "yellow"],
            "rounds": ["2s+", "1s", "4d", "3d", "2d", "1d", "t"],
            "cards_per_rarity": {
                "2s+": 3,
                "1s": 3,
                "4d": 3,
                "3d": 8,
                "2d": 10,
                "1d": 12,
                "t": 4,
            },
        }
    ).export()
