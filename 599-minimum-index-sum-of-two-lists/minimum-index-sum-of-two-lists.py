class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        str_to_idx1 = {}
        str_to_idx2 = {}
        for i, word in enumerate(list1):
            if word in str_to_idx1:
                str_to_idx1[word] = min(str_to_idx1[word], i)
            else:
                str_to_idx1[word] = i
        
        for i, word in enumerate(list2):
            if word in str_to_idx2:
                str_to_idx2[word] = min(str_to_idx2[word], i)
            else:
                str_to_idx2[word] = i
        
        holder = defaultdict(list)
        for k, v in str_to_idx1.items():
            if k in str_to_idx2:
                tmp = str_to_idx2[k]
                holder[v + tmp].append(k)
        
        min_key = float("inf")
        for k, v in holder.items():
            min_key = min(min_key, k)
        
        return holder[min_key]
