class Solution:
    def maskPII(self, s: str) -> str:
        def mask_email(email: str) -> str:
            local, domain = email.split('@')
            return local[0].lower() + "*****" + local[-1].lower() + "@" + domain.lower()
        
        def mask_phone(number: str) -> str:
            digits = [c for c in number if c.isdigit()]
            local = "***-***-" + "".join(digits[-4:])
            country_len = len(digits) - 10
            if country_len == 0:
                return local
            else:
                return "+" + "*" * country_len + "-" + local
        
        if '@' in s:
            return mask_email(s)
        else:
            return mask_phone(s)