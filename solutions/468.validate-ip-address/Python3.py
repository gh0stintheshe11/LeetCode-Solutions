class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4(IP: str) -> bool:
            parts = IP.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit() or not (0 <= int(part) <= 255) or str(int(part)) != part:
                    return False
            return True
        
        def isIPv6(IP: str) -> bool:
            parts = IP.split(':')
            if len(parts) != 8:
                return False
            hex_digits = '0123456789abcdefABCDEF'
            for part in parts:
                if not (1 <= len(part) <= 4) or not all(c in hex_digits for c in part):
                    return False
            return True

        if '.' in queryIP and isIPv4(queryIP):
            return "IPv4"
        elif ':' in queryIP and isIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"