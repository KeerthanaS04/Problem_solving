from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(customer_accounts) for customer_accounts in accounts)