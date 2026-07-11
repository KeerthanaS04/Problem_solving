from typing import List
class Solution:
    def matchPlayerAndTrainer(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        trainer_idx = 0
        num_trainers = len(trainers)

        for player_idx, player_ability in enumerate(players):
            while trainer_idx<num_trainers and trainers[trainer_idx]<player_ability:
                trainer_idx += 1
            
            # if we've exhausted all trainers, we can't match any more players
            if trainer_idx==num_trainers:
                return player_idx
            
            # match the player with the trainer
            trainer_idx += 1
        # all players are matched
        return len(players)