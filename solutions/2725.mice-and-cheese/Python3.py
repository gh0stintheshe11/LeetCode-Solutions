class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        # Calculate the total rewards assuming the second mouse eats all the cheese
        total_reward = sum(reward2)
        
        # Calculate the difference between reward1 and reward2
        differences = [reward1[i] - reward2[i] for i in range(len(reward1))]
        
        # Sort the differences in descending order to maximize the reward for the first mouse
        differences.sort(reverse=True)
        
        # Add the top k differences to the total reward
        total_reward += sum(differences[:k])
        
        return total_reward