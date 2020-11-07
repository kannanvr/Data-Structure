# s1="AXYZ", s2="BAZ"
# we can start from begin or end of the strings
def lcs_recursive(s1, s2, m, n):  # m is length of string s1 and n is length of string s2
    if m == 0 or n == 0:
        return 0
    if s1[m - 1] == s2[
        n - 1]:  # if last character of string matches then length of lcs is at least 1, now recur of rest of the strings
        return 1 + lcs_recursive(s1, s2, m - 1, n - 1)
    else:
        # if last character doesn't match the we can remove the last of either s1 or s2, will take the max of removal of s1 or s2
        return max(lcs_recursive(s1, s2, m - 1, n), max(s1, s2, m, n - 1))
