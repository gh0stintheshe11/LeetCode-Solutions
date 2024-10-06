class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.prices = {product: price for product, price in zip(products, prices)}
        self.customer_count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.customer_count += 1
        total_bill = sum(self.prices[p] * a for p, a in zip(product, amount))
        
        if self.customer_count % self.n == 0:
            total_bill *= (100 - self.discount) / 100
        
        return total_bill