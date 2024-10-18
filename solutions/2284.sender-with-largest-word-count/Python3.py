class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        from collections import defaultdict
        
        word_count = defaultdict(int)
        
        for message, sender in zip(messages, senders):
            count = len(message.split())
            word_count[sender] += count
        
        max_words = -1
        result_sender = ""
        
        for sender in word_count:
            if word_count[sender] > max_words or (word_count[sender] == max_words and sender > result_sender):
                max_words = word_count[sender]
                result_sender = sender
        
        return result_sender