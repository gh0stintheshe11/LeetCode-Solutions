class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict, Counter
        
        food_items = set()
        table_orders = defaultdict(Counter)
        
        for _, table, food in orders:
            food_items.add(food)
            table_orders[table][food] += 1
        
        food_items = sorted(food_items)
        header = ["Table"] + food_items
        result = [header]
        
        for table in sorted(table_orders, key=int):
            row = [table] + [str(table_orders[table][food]) for food in food_items]
            result.append(row)
        
        return result