from typing import List
from collections import defaultdict

class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(reverse=True, key=lambda x: x[0])

        selected_profit = 0
        selected_categories = set()
        profit_by_category = defaultdict(list)
        
        for i in range(k):
            profit, category = items[i]
            selected_profit += profit
            profit_by_category[category].append(profit)
            selected_categories.add(category)

        num_distinct_categories = len(selected_categories)
        current_elegance = selected_profit + num_distinct_categories ** 2
        
        for i in range(k, len(items)):
            profit, category = items[i]
            if category not in selected_categories:
                min_profit_item = None
                min_profit_category = None

                for cat, profits in profit_by_category.items():
                    if len(profits) > 1:
                        min_profit = min(profits)
                        if min_profit_item is None or min_profit < min_profit_item:
                            min_profit_item = min_profit
                            min_profit_category = cat

                if min_profit_item is None:
                    continue

                selected_profit = selected_profit - min_profit_item + profit
                selected_categories.add(category)
                num_distinct_categories += 1

                profit_by_category[min_profit_category].remove(min_profit_item)
                if not profit_by_category[min_profit_category]:
                    del profit_by_category[min_profit_category]

                profit_by_category[category].append(profit)
                
                current_elegance = max(
                    current_elegance,
                    selected_profit + num_distinct_categories ** 2
                )

        return current_elegance