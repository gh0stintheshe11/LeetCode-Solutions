import random
import string

class Codec:

    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.characters = string.ascii_letters + string.digits
        self.prefix = "http://tinyurl.com/"
    
    def encode(self, longUrl: str) -> str:
        while longUrl not in self.url_to_code:
            code = ''.join(random.choices(self.characters, k=6))
            if code not in self.code_to_url:
                self.code_to_url[code] = longUrl
                self.url_to_code[longUrl] = code
        return self.prefix + self.url_to_code[longUrl]

    def decode(self, shortUrl: str) -> str:
        code = shortUrl.replace(self.prefix, "")
        return self.code_to_url.get(code, "")

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))