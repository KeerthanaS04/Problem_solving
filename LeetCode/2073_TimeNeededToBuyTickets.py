from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = 0

        for i, ticket_count in enumerate(tickets):
            # for people before or at position k, they can buy atmost tickets[k] before person k finishes
            if i<=k:
                total_time+=min(ticket_count, tickets[k])
            else:
                # for people position after k, they can buy atmost tickets[k]-1 beofre person k finishes
                total_time+=min(ticket_count, tickets[k]-1)
        return total_time