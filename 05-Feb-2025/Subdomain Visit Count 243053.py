# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains_dict = defaultdict(int)
        ans = []
        for domain in cpdomains:
            domain = domain.split()
            count = domain[0]
            domain[1] = domain[1].split(".")
            for i in range(len(domain[1])):
                subdomain = ".".join(domain[1][i:])
                domains_dict[subdomain] += int(count)
        
        for subdomain,count in domains_dict.items():
            ans.append(f"{count} {subdomain}")
        return ans