class FrequencyTracker:

    def __init__(self):
        self.num_freq = {}
        self.freq_count = {}

    def add(self, number: int) -> None:
        if number in self.num_freq:
            old_freq = self.num_freq[number]
            self.num_freq[number] += 1
            new_freq = self.num_freq[number]

            self.freq_count[old_freq] -= 1
            if self.freq_count[old_freq] == 0:
                del self.freq_count[old_freq]

            if new_freq in self.freq_count:
                self.freq_count[new_freq] += 1
            else:
                self.freq_count[new_freq] = 1
        else:
            self.num_freq[number] = 1
            if 1 in self.freq_count:
                self.freq_count[1] += 1
            else:
                self.freq_count[1] = 1

    def deleteOne(self, number: int) -> None:
        if number in self.num_freq:
            old_freq = self.num_freq[number]
            self.num_freq[number] -= 1
            if self.num_freq[number] == 0:
                del self.num_freq[number]
            else:
                new_freq = self.num_freq[number]

                if new_freq in self.freq_count:
                    self.freq_count[new_freq] += 1
                else:
                    self.freq_count[new_freq] = 1
            
            self.freq_count[old_freq] -= 1
            if self.freq_count[old_freq] == 0:
                del self.freq_count[old_freq]

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq_count and self.freq_count[frequency] > 0