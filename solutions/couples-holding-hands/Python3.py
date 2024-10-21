class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def findPartner(x):
            return x ^ 1

        pos = {num: i for i, num in enumerate(row)}
        swaps = 0

        for i in range(0, len(row), 2):
            partner = findPartner(row[i])
            if row[i + 1] != partner:
                swaps += 1
                partner_index = pos[partner]

                # Swap the incorrect person with the partner
                row[i + 1], row[partner_index] = row[partner_index], row[i + 1]

                # Update positions in the dictionary
                pos[row[i + 1]] = i + 1
                pos[row[partner_index]] = partner_index

        return swaps