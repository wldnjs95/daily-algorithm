# Remove Two Characters - Longest Substring

## Problem
Given a lowercase string `S` and a list of queries `Q = [(c1, c2), ...]`,  
for each query, remove all occurrences of characters `c1` and `c2` from `S`,  
then return the length of the longest remaining contiguous substring.

### Constraints
- 1 ≤ len(S) ≤ 1000  
- `S` contains only lowercase English letters (`a`–`z`)  
- 1 ≤ len(Q) ≤ 100,000  
- Each query contains two **distinct** lowercase letters

---

## Example
```python
solution("abcccacba", [('a', 'b'), ('b', 'c')])
# Output: [3, 1]

solution("intelliaiassistant", [('a', 'i'), ('n', 't')])
# Output: [5, 11]