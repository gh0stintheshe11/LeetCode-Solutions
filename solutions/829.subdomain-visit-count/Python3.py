class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomain_count = {}
        
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            count = int(count)
            fragments = domain.split('.')
            
            for i in range(len(fragments)):
                subdomain = '.'.join(fragments[i:])
                if subdomain in subdomain_count:
                    subdomain_count[subdomain] += count
                else:
                    subdomain_count[subdomain] = count
        
        return [f"{count} {domain}" for domain, count in subdomain_count.items()]