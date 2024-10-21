class ProductOfNumbers:

    def __init__(self):
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1]
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        n = len(self.prefix_products)
        if k >= n:
            return 0
        return self.prefix_products[-1] // self.prefix_products[-k - 1]