# #Solution with recursion

# def isPalindrome(x):
#     return x == x[::-1]
 
 
# def minPalPartion(string, i, j):
#     if i >= j or isPalindrome(string[i:j + 1]):
#         return 0
#     ans = float('inf')
#     for k in range(i, j):
#         count = (
#             1 + minPalPartion(string, i, k)
#             + minPalPartion(string, k + 1, j)
#         )
#         ans = min(ans, count)
#     return ans



# Dynamic Programming Solution for
# Palindrome Partitioning Problem
import sys
 
# Returns the minimum number of cuts
# needed to partition a string such
# that every part is a palindrome
def minPalPartion(str1):
     
    # Get the length of the string
    n = len(str1);
     
    # Create two arrays to build the solution
    # in bottom up manner
    # C[i] = Minimum number of cuts needed
    # for palindrome partitioning of
    # substring str[0..i]
    # P[i][j] = true if substring str[i..j]
    # is palindrome, else false
    # Note that C[i] is 0 if P[0][i] is true
    C = [0]*(n + 1);
    P = [[False for x in range(n + 1)] for y in range(n + 1)];
     
    # Every substring of length 1 is
    # a palindrome
    for i in range(n):
        P[i][i] = True;
     
    # L is substring length. Build the solution
    # in bottom up manner by considering all
    # substrings of length starting from 2 to n.
    for L in range(2, n + 1):
         
        # For substring of length L, set
        # different possible starting indexes
        for i in range(n - L + 1):
            j = i + L - 1;
             
            # Set ending index
            # If L is 2, then we just need to
            # compare two characters. Else need
            # to check two corner characters and
            # value of P[i + 1][j-1]
            if (L == 2):
                P[i][j] = (str1[i] == str1[j]);
            else:
                P[i][j] = ((str1[i] == str1[j]) and P[i + 1][j - 1]);
    for i in range(n):
        if (P[0][i] == True):
            C[i] = 0;
        else:
            C[i] = sys.maxsize;
            for j in range(i):
                if(P[j + 1][i] == True and 1 + C[j] < C[i]):
                    C[i] = 1 + C[j];
     
    # Return the min cut value for complete
    # string. i.e., str[0..n-1]
    return C[n - 1];

class Solution:

    def minCut(self, s: str) -> int:       
        return minPalPartion(s)
        
    # def first_isPalindrome(self, s):  
#         if s == s[::-1]:
#             return s
#         else:
#             return ""

#     def isPalindrome(self, s):      
#         return s == s[::-1]

    # def minCut(self, s: str) -> int:
        
#         #Partition string in a list
#         res = [self.first_isPalindrome(s[i: j]) for i in range(len(s))
#           for j in range(i + 1, len(s) + 1)]
        
#         #Remove extra ""
#         while "" in res:
#             res.remove("")

#         print(res)
#         print("-------")
        
#         #Find palindromes within the list, and take out the others
#         # for string in res:
#         #     if self.isPalindrome(string) == False:
#         #         res.remove(string)
        
#         #Start from the largest palindrome, then subtract it from the main string. count each subtraction until the main string is empty
#         res.sort(key = len)
#         res.reverse()
        
#         count = -1 #count number of times there is a subtraction
        
#         while s != "":
#             for i in range(len(res)):
#                 print(s)
#                 print(res[i])
#                 print("------")
#                 if res[i] in s:
#                     print(res[i])
#                     print("--")
#                     s = s.replace(res[i],"",1)
#                     count += 1
                    
#         return count