package strings

import "sort"

// Two strings are considered close if you can attain one from the other using the following operations:
// 
// Operation 1: Swap any two existing characters.
// For example, abcde -> aecdb

// Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
// For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

// You can use the operations on either string as many times as necessary.

// Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

// This is basically like frequency analysis

func CloseStrings(word1 string, word2 string) bool {
	// Check if the lengths of both words are equal
	if len(word1) != len(word2) {
		return false
	}

	// Create slices to store the frequency of characters for both words
	freq1 := make([]int, 26)
	freq2 := make([]int, 26)

	// Populate the frequency slices for word1
	for _, char := range word1 {
		freq1[char-'a']++
	}

	// Populate the frequency slices for word2
	for _, char := range word2 {
		freq2[char-'a']++
	}

	// Check if the sets of characters (keys) in both words are the same
	for i := 0; i < 26; i++ {
		if (freq1[i] > 0 && freq2[i] == 0) || (freq1[i] == 0 && freq2[i] > 0) {
			return false
		}
	}

	// Sort the frequency slices in ascending order
	sort.Ints(freq1)
	sort.Ints(freq2)

	// Compare the sorted frequency slices
	for i := 0; i < 26; i++ {
		if freq1[i] != freq2[i] {
			return false
		}
	}

	return true
}
