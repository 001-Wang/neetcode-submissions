from collections import Counter,defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list) 
        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            group[key].append(s)
        return list(group.values())

          