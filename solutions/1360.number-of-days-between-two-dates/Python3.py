class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        from datetime import datetime
        
        def parse_date(date_str):
            return datetime.strptime(date_str, "%Y-%m-%d")
        
        date1_parsed = parse_date(date1)
        date2_parsed = parse_date(date2)
        
        return abs((date2_parsed - date1_parsed).days)