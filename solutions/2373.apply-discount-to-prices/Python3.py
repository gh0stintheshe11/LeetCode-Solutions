class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        discount_factor = (100 - discount) / 100
        result = []

        for word in words:
            if word.startswith('$') and word[1:].isdigit():
                price = float(word[1:])
                discounted_price = price * discount_factor
                result.append(f"${discounted_price:.2f}")
            else:
                result.append(word)

        return ' '.join(result)