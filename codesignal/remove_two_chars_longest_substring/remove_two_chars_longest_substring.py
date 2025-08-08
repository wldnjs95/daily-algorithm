from typing import List, Tuple

def _precompute_longest_without_pairs(S: str) -> List[List[int]]:
    """
    ans[i][j] = length of the longest substring of S without characters
                (chr(ord('a')+i), chr(ord('a')+j))
    """
    K = 26
    ans = [[0] * K for _ in range(K)]

    for i in range(K):
        forbid1 = chr(ord('a') + i)
        for j in range(i, K):
            forbid2 = chr(ord('a') + j)
            best = cur = 0
            for ch in S:
                if ch == forbid1 or ch == forbid2:
                    best = max(best, cur)
                    cur = 0
                else:
                    cur += 1
            best = max(best, cur)
            ans[i][j] = ans[j][i] = best  # symmetric
    return ans

def solution(S: str, Q: List[Tuple[str, str]]) -> List[int]:
    """
    For each (c1, c2) in Q, return the length of the longest substring
    of S after removing all c1 and c2.
    """
    table = _precompute_longest_without_pairs(S)

    def idx(c: str) -> int:
        return ord(c) - ord('a')

    return [table[idx(c1)][idx(c2)] for (c1, c2) in Q]


# Example usage:
if __name__ == "__main__":
    print(solution("abcccacba", [('a', 'b'), ('b', 'c')]))  # [3, 1]
    print(solution("intelliaiassistant", [('a', 'i'), ('n', 't')]))  # [5, 11]