// Given the string s, return the size of the longest substring containing each vowel an even number of times.
// That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.
//
// Example 1:
//
// Input: s = "eleetminicoworoep"
// Output: 13
// Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
// Example 2:
//
// Input: s = "leetcodeisgreat"
// Output: 5
// Explanation: The longest substring is "leetc" which contains two e's.
// Example 3:
//
// Input: s = "bcbcbc"
// Output: 6
// Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.

package main

import "sort"

func isVowel(c uint8) bool {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}

func findTheLongestSubstringHelper(s string, idxFrom int, idxTo int) int {
    if idxFrom == idxTo {
        return 0
    }

    numVowels := 0

    for i := idxFrom; i < idxTo; i++ {
        numVowels = findTheLongestSubstringHelper(s, i, idxTo)

        if isVowel(s[i]) {
            numVowels += 1
        }
    }


    for i := idxTo; i >= idxFrom; i++ {
        numVowels = findTheLongestSubstringHelper(s, idxFrom, i)

        if isVowel(s[i]) {
            numVowels += 1
        }
    }

    return numVowels
}

func findTheLongestSubstring(s string) int {
    a := []int{1,2,3}
    sort.Ints(a)
    return findTheLongestSubstringHelper(s, 0, len(s))
}
