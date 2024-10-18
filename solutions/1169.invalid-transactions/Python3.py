class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        mapped_transactions = collections.defaultdict(lambda: collections.defaultdict(set))
   
        for transaction in transactions:
            name, time, amount, city = Solution.parse_transaction(transaction)
            mapped_transactions[name][time].add(city)
        
        result = []
        for transaction in transactions:

            name, time, amount, city = Solution.parse_transaction(transaction)
            
            if amount > 1000:
                result.append(transaction)
                continue
            
            if name not in mapped_transactions:
                continue
            
            for time_point in range(time-60, time+61):

                if time_point not in mapped_transactions[name]:
                    continue

                if len(mapped_transactions[name][time_point]) > 1 or (city not in mapped_transactions[name][time_point]):
                    result.append(transaction)
                    break
                                        
        return result
    
    @staticmethod
    def parse_transaction(transaction: str) -> Tuple[str, int, int, str]:
        name, time, amount, city = transaction.split(',')
        time = int(time)
        amount = int(amount)
        return name, time, amount, city