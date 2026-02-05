class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counter = defaultdict(lambda: 0)

        for domain in cpdomains:
            count, topdomain = domain.split(" ")
            count = int(count)
            subdomains = topdomain.split(".")
            for i in range(len(subdomains)):
                counter[".".join(subdomains[i:])] += count
        
        res = []
        for k, v in counter.items():
            res.append(f"{v} {k}")
        
        return res
