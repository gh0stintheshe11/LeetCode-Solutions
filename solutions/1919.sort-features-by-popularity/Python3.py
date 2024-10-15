from typing import List

class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:
        # Initialize a dictionary to count the number of appearances of each feature in responses.
        feature_count = {feature: 0 for feature in features}
        
        # Go through each response and count the unique appearance of features in the response.
        for response in responses:
            # Use a set to avoid duplicating counts of the same feature within one response
            words = set(response.split())
            for feature in features:
                if feature in words:
                    feature_count[feature] += 1

        # Sort features first by the count (descending) and then by their original order (which is natural for the list)
        # by using the feature list index
        sorted_features = sorted(features, key=lambda x: (-feature_count[x], features.index(x)))

        return sorted_features