package ___Hashing
// https://leetcode.com/problems/group-anagrams

/*
   def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       # about default dict: https://www.geeksforgeeks.org/defaultdict-in-python/
       ans=collections.defaultdict(list)
       for i in strs:
           ans[tuple(sorted(i))].append(i)
       return ans.values()
*/
