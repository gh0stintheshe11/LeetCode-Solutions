from urllib.parse import urlparse

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_hostname(url):
            return urlparse(url).hostname
        
        start_hostname = get_hostname(startUrl)
        visited = set([startUrl])
        queue = [startUrl]
        
        while queue:
            current_url = queue.pop(0)
            for url in htmlParser.getUrls(current_url):
                if url not in visited and get_hostname(url) == start_hostname:
                    visited.add(url)
                    queue.append(url)
                    
        return list(visited)