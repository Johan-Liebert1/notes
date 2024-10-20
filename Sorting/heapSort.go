package sorting

import (
	"fmt"
)

type Heap struct {
	heap    []int
	maxHeap bool
}

func NewHeap(maxHeap bool) *Heap {
	return &Heap{
		maxHeap: maxHeap,
	}
}

func (h *Heap) Heapify(array []int) {
	for _, c := range array {
		h.Insert(c)
	}
}

func (h *Heap) Insert(val int) {
	h.heap = append(h.heap, val)

	h.BubbleUp()
}

func (h *Heap) BubbleUp() {
	index := len(h.heap) - 1

	for {
		parent := index / 2

		swap := false

		if h.maxHeap {
			swap = h.heap[parent] < h.heap[index]
		} else {
			swap = h.heap[parent] > h.heap[index]
		}

		if swap {
			h.heap[parent], h.heap[index] = h.heap[index], h.heap[parent]
			index = parent
			continue
		}

		break
	}
}

func (h *Heap) BubbleDown() {
	index := 0

	for index < len(h.heap) {
		leftChildIdx := index*2 + 1
		rightChildIdx := index*2 + 2

		if leftChildIdx >= len(h.heap) {
			break
		}

		childIdxToSwapWith := -1

		if rightChildIdx >= len(h.heap) {
			if h.maxHeap {
				if h.heap[leftChildIdx] <= h.heap[index] {
					break
				}
			} else {
				if h.heap[leftChildIdx] >= h.heap[index] {
					break
				}
			}
		}

		if h.maxHeap {
			if h.heap[leftChildIdx] > h.heap[rightChildIdx] {
				childIdxToSwapWith = leftChildIdx
			} else if h.heap[rightChildIdx] > h.heap[leftChildIdx] {
				childIdxToSwapWith = rightChildIdx
			}
		} else {
			if h.heap[leftChildIdx] < h.heap[rightChildIdx] {
				childIdxToSwapWith = leftChildIdx
			} else if h.heap[rightChildIdx] < h.heap[leftChildIdx] {
				childIdxToSwapWith = rightChildIdx
			}
		}

		if childIdxToSwapWith != -1 {
			h.heap[childIdxToSwapWith], h.heap[index] = h.heap[index], h.heap[childIdxToSwapWith]
			index = childIdxToSwapWith
			continue
		}

		continue
	}
}

func (h *Heap) PeekRoot() int {
	if len(h.heap) == 0 {
		panic("Heap length is zero")
	}

	return h.heap[0]
}

func (h *Heap) GetRoot() int {
	if len(h.heap) == 0 {
		panic("Heap length is zero")
	}

	// get the root at the end
	end := len(h.heap) - 1
	h.heap[0], h.heap[end] = h.heap[end], h.heap[0]

	toRet := h.heap[end]

	h.heap = h.heap[:end]

	h.BubbleDown()

	return toRet
}

func HeapTest() {
	array := []int{4, 7, 10, 23, 30, 45, 1}

	heap := NewHeap(false)
	heap.Heapify(array)

	for range 7 {
		fmt.Println(heap.GetRoot())
	}
}
