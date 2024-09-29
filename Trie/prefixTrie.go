package trie

import (
	"encoding/json"
	"fmt"
)

type Node struct {
	Val   byte    `json:"val"`
	Next  []*Node `json:"next"`
	IsEnd bool    `json:"isEnd"`
}

type Trie struct {
	Children []*Node `json:"children"`
}

func Constructor() Trie {
	return Trie{}
}

func (node *Node) AddChild(val byte, isEnd bool) *Node {
	newChild := Node{
		Val:   val,
		IsEnd: isEnd,
	}

	node.Next = append(node.Next, &newChild)

	return &newChild
}

func (node *Node) Print() {
	thing, err := json.MarshalIndent(node, "", "  ")

	if err != nil {
		fmt.Printf("Error: %+v\n", err)
		return
	}

	fmt.Println(string(thing))
}

func (trie *Trie) Print() {
	thing, err := json.MarshalIndent(trie, "", "  ")

	if err != nil {
		fmt.Printf("Error: %+v\n", err)
		return
	}

	fmt.Println(string(thing))
}

func (trie *Trie) Insert(word string) {
	var child *Node = nil

	for _, c := range trie.Children {
		if c.Val == word[0] {
			child = c
			break
		}
	}

	if child == nil || child.Val != word[0] {
		child = &Node{
			Val:   word[0],
			IsEnd: len(word) == 1,
		}

		trie.Children = append(trie.Children, child)
	}

	if len(word) == 1 {
		child.IsEnd = true
		return
	}

	prevChild := child

	for i := 1; i < len(word); i++ {
		for _, c := range child.Next {
			if c.Val == word[i] {
				child = c
				break
			}
		}

		if child == prevChild {
			newChild := child.AddChild(word[i], i == len(word)-1)
			child = newChild
		}

        prevChild = child
	}

    child.IsEnd = true
}

func (trie *Trie) Search(word string) bool {
	var child *Node = nil

	for _, c := range trie.Children {
		if c.Val == word[0] {
			child = c
			break
		}
	}

	if child == nil {
		return false
	}

	if len(word) == 1 {
		return child.IsEnd
	}

	prevChild := child

	for i := 1; i < len(word); i++ {
		for _, c := range child.Next {
			if c.Val == word[i] {
				child = c
				break
			}
		}

		if child == prevChild {
			return false
		}

		prevChild = child
	}

	return child.IsEnd == true
}

func (trie *Trie) StartsWith(prefix string) bool {
	var child *Node = nil

	for _, c := range trie.Children {
		if c.Val == prefix[0] {
			child = c
			break
		}
	}

	if child == nil {
		return false
	}

	if len(prefix) == 1 {
		return true
	}

	prevChild := child

	for i := 1; i < len(prefix); i++ {
		for _, c := range child.Next {
			if c.Val == prefix[i] {
				child = c
				break
			}
		}

		if child == prevChild {
			return false
		}

		prevChild = child
	}

	return true
}

func main() {
	trie := Constructor()
	trie.Insert("apple")
	trie.Insert("app")

	apple := trie.Search("apple")
	app := trie.Search("app")
	ape := trie.Search("ape")

    trie.Print()

    fmt.Printf("apple: %v, app: %+v, ape: %+v\n", apple, app, ape)

	fmt.Printf("%+v\n", trie)
}
