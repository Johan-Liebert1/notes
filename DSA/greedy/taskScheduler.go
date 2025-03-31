package greedy

import "container/heap"

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

// Push and Pop use pointer receivers to modify the slice
func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = (*h)[0 : n-1]
	return x
}

type Task struct {
    frequency int
    timeAvailable int
}

func leastInterval(tasks []byte, n int) int {
    mapp := map[byte]int{}

    for _, t := range tasks {
        mapp[t]++
    }

    intHeap := &IntHeap{}

    heap.Init(intHeap)

    for _, v := range mapp {
        heap.Push(intHeap, v)
    }

    time := 0

    queue := []Task{}

    for intHeap.Len() > 0 || len(queue) > 0 {
        time += 1

        if intHeap.Len() > 0 {
            // we pick up a task
            // and then decrement the frequency of the task
            // and add it back to the heap if the frequency > 0

            count := heap.Pop(intHeap).(int)
            count -= 1

            if count > 0 {
                queue = append(queue, Task { frequency: count, timeAvailable: time + n })
            }
        }

        if len(queue) > 0 && queue[0].timeAvailable == time {
            thingy := queue[0]
            queue = queue[1:]

            if thingy.frequency > 0 {
                heap.Push(intHeap, thingy.frequency)
            }
        }
    }

    return time
}
