package miscellaneous

import (
	"container/heap"
)

// [processing time, original index]
type Task [][]int

func (t Task) Len() int { return len(t) }

func (t Task) Less(i, j int) bool {
	pt1, i1 := t[i][0], t[i][1]
	pt2, i2 := t[j][0], t[j][1]

	if pt1 == pt2 {
		return i1 < i2
	}

	return pt1 < pt2
}

func (t Task) Swap(i, j int) { t[i], t[j] = t[j], t[i] }

func (t *Task) Push(x any) {
	*t = append(*t, x.([]int))
}

func (t *Task) Pop() any {
	old := *t
	n := len(old)
	x := old[n-1]
	*t = (*t)[0 : n-1]
	return x
}

// [enqueue time, processing time]
func getOrder(tasks [][]int) []int {
	order := []int{}

	heapTasks := &Task{}

	heap.Init(heapTasks)

	time := 1

	mapp := make([]bool, len(tasks))
	idx := 0

	for idx < len(tasks) {
		for i, t := range tasks {
			if mapp[i] {
				continue
			}

			value := []int{t[1], i}

			if t[0] <= time {
				mapp[i] = true
				idx++
				heap.Push(heapTasks, value)
			}
		}

		// process task
		if heapTasks.Len() > 0 {
			taskToProcess := heapTasks.Pop().([]int)
			time += taskToProcess[0]
			order = append(order, taskToProcess[1])
		} else {
			time++
		}
	}

	for heapTasks.Len() > 0 {
		taskToProcess := heapTasks.Pop().([]int)
		order = append(order, taskToProcess[1])
	}

	return order
}

func SingleThreadedCPU(tasks [][]int) []int {
	return getOrder(tasks)
}
