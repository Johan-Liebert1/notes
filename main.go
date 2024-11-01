package main

import (
	graphs "coding-questions/Graphs"
	"fmt"
)

func main()  {
    board := graphs.Board{ 
        { graphs.EmptyCell, graphs.EmptyCell, graphs.QueenCell, graphs.EmptyCell },
        { graphs.EmptyCell, graphs.EmptyCell, graphs.EmptyCell, graphs.EmptyCell },
        { graphs.EmptyCell, graphs.EmptyCell, graphs.EmptyCell, graphs.EmptyCell },
        { graphs.EmptyCell, graphs.EmptyCell, graphs.EmptyCell, graphs.EmptyCell },
    }

    fmt.Printf("is: %v\n", graphs.IsSquareUnderAttack(1, 3, board))

    graphs.SolveNQueens(4)
}
