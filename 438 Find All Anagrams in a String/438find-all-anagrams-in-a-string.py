class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        windowLeft = 0
        windowRight = 0
        anagram_indices = []
        correct_counter = {}
        counter = {}
        reset_counter = {}

        for letter in p:
            if letter not in correct_counter:
                correct_counter[letter] = 1
            else:
                correct_counter[letter] += 1

            counter[letter] = 0
            reset_counter[letter] = 0

        while windowRight < len(s):
            if (
                s[windowRight] in p
                and counter[s[windowRight]] < correct_counter[s[windowRight]]
            ):
                counter[s[windowRight]] += 1
                windowRight += 1
            elif s[windowRight] not in p:
                if counter == correct_counter:
                    anagram_indices.append(windowLeft)
                counter = reset_counter.copy()
                windowLeft = windowRight + 1
                windowRight += 1
            elif (
                s[windowRight] in p
                and counter[s[windowRight]] >= correct_counter[s[windowRight]]
            ):
                if counter == correct_counter:
                    anagram_indices.append(windowLeft)
                counter[s[windowLeft]] -= 1
                windowLeft += 1

        if counter == correct_counter:
            anagram_indices.append(windowLeft)

        return anagram_indices