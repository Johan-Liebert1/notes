package graphs

const (
    Empty int = iota
    Fresh 
    Rotten
)

type Pos struct {
    row int
    col int
}

func inBounds(row, col int, grid [][]int) bool {
    return row >= 0 && col >= 0 && row < len(grid) && col < len(grid[0])
}

func orangesRotting(grid [][]int) int {
    queue := []Pos{}
    dirs := [][]int{ { -1, 0 }, { 1, 0 }, { 0, 1 }, { 0, -1 } }

    freshExist := false

    for row := range len(grid) {
        for col := range len(grid[0]) {
            if grid[row][col] == Rotten {
                queue = append(queue, Pos { row: row, col: col })
            }

            if grid[row][col] == Fresh {
                freshExist = true
            }
        }
    }

    if len(queue) == 0 {
        if freshExist {
            return -1
        }
        
        return 0
    }

    iter := 0

    for len(queue) > 0 {
        queueLen := len(queue)

        for i := 0; i < queueLen; i++ {
            pos := queue[i]

            for _, dir := range dirs {
                newRow := pos.row + dir[0]
                newCol := pos.col + dir[1]

                if !inBounds(newRow, newCol, grid) {
                    continue
                }

                if grid[newRow][newCol] != Fresh {
                    continue
                }

                grid[newRow][newCol] = Rotten

                queue = append(queue, Pos { row: newRow, col: newCol })
            }
        }

        queue = queue[queueLen:]

        iter++
    }

    for row := range len(grid) {
        for col := range len(grid[0]) {
            if grid[row][col] == Fresh {
                return -1
            }
        }
    }

    return iter - 1
}
