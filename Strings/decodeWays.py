class Solution:
    def count(self, s: str, start: int, cache):
        print(f"{start = }, {cache = }")
        if start in cache:
            return cache[start]

        if s[start] == "0":
            return 0

        total = self.count(s, start + 1, cache)

        if start < len(s) - 1 and (int(s[start] + s[start + 1]) <= 26):
            total += self.count(s, start + 2, cache)

        cache[start] = total

        print(cache)

        return total

    def numDecodingsBetter(self, s: str) -> int:
        if s[0] == "0":
            return 0

        prev_1, prev_2 = 1, 1

        for i in range(1, len(s)):
            curr = 0
            # if current index is number in 1->9 range, we can make dp[i] = dp[i-1]
            if s[i] != "0":
                curr += prev_2

            # if current index and the prev index make a number in 0 -> 26 range, we can add dp[i-2]
            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                if i > 1:
                    curr += prev_1
                else:
                    curr += 1

            print(f"{prev_1 = }, {prev_2 = }, {curr = }")

            prev_1 = prev_2
            prev_2 = curr

        return prev_2

    def numDecodings(self, s: str) -> int:
        if s[0] == "0" or (len(s) < 2 and int(s[0]) > 2):
            return 0

        cache = {len(s): 1}
        return self.count(s, 0, cache)


print(Solution().numDecodingsBetter("23215"))
