class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.encrypt_map = {key: value for key, value in zip(keys, values)}
        self.decrypt_map = defaultdict(list)
        for key, value in zip(keys, values):
            self.decrypt_map[value].append(key)

        self.dictionary_set = set(dictionary)
        self.encrypted_dict_count = defaultdict(int)

        for word in self.dictionary_set:
            enc_word = self.encrypt(word)
            self.encrypted_dict_count[enc_word] += 1

    def encrypt(self, word1: str) -> str:
        encrypted_chars = [self.encrypt_map[c] for c in word1 if c in self.encrypt_map]
        return "".join(encrypted_chars) if len(encrypted_chars) == len(word1) else ""

    def decrypt(self, word2: str) -> int:
        return self.encrypted_dict_count.get(word2, 0)