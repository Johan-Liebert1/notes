/*
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
*/

package main

func doesDivide(str string, subStr string) bool {
	for i := 0; i < len(str); i += len(subStr) {
		if str[i:i+len(subStr)] != subStr {
			return false
		}
	}

	return true
}

func gcdOfStrings(str1 string, str2 string) string {
	maxI := 0
	i := 0

	for i < len(str1) && i < len(str2) {
		if str1[i] != str2[i] {
			break
		}

		i++

		// whereever i ends, is the longest prefix
		if len(str1)%i != 0 || len(str2)%i != 0 {
			continue
		}

		if doesDivide(str1, str1[:i]) && doesDivide(str2, str2[:i]) {
			maxI = i
		}
	}

	return str1[:maxI]
}
