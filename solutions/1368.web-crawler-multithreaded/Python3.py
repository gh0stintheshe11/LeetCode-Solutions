from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse
import threading
from typing import List

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname = urlparse(startUrl).hostname
        visited = set()
        lock = threading.Lock()

        def crawl_url(url):
            if url in visited or urlparse(url).hostname != hostname:
                return

            with lock:
                if url in visited:
                    return
                visited.add(url)

            future_urls = htmlParser.getUrls(url)
            with ThreadPoolExecutor(max_workers=10) as executor:
                for future_url in future_urls:
                    executor.submit(crawl_url, future_url)

        crawl_url(startUrl)
        return list(visited)