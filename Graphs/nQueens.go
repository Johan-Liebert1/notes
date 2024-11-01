package graphs

import "fmt"

func printBoard[T int | string](board [][]T) {
	for _, row := range board {
		fmt.Printf("%+v\n", row)
	}

	fmt.Println("------------------------------------------")
}


func printAnswerBoard(board []string) {
	for _, row := range board {
		fmt.Printf("%+v\n", row)
	}

	fmt.Println("------------------------------------------")
}


var rowAddersChess = []int{
	-1, // top
	1,  // down
	0,  // left
	0,  // right
	-1, // top left
	-1, // top right
	1,  // bottom left
	1,  // bottom right
}

var colAddersChess = []int{
	0,  // top
	0,  // down
	-1, // left
	1,  // right
	-1, // top left
	1,  // top right
	-1, // bottom left
	1,  // bottom right
}

const (
	EmptyCell = iota
	QueenCell
)

type Board = [][]int

func IsSquareUnderAttack(row, col int, board Board) bool {
	for idx, ra := range rowAddersChess {
		r := row + ra
		c := col + colAddersChess[idx]

		for ; r >= 0 && c >= 0 && r < len(board) && c < len(board); r, c = r+ra, c+colAddersChess[idx] {
			if board[r][c] == QueenCell {
				return true
			}
		}
	}

	return false
}

func solveIterativeDoesNotGiveAllSolutions(board Board) []string {
	// this holds the last queen position
	stack := Board{}

	row := 1
	col := 0

	for row < len(board) {
		for col < len(board) {
			if !IsSquareUnderAttack(row, col, board) {
				// we can place queen
				board[row][col] = QueenCell
				stack = append(stack, []int{row, col})

				// placed a queen on a row, can't place another on the same row
				// so we break
				break
			}

			col++
		}

		// we went through the entire row but couldn't place a single queen
		// time to backtrack
		if col == len(board) {
            if len(stack) == 0 {
                // we cannot place a queen without it attacking another
                // break the loop
                break
            }

			lastQueen := stack[len(stack)-1]
			lastRow, lastCol := lastQueen[0], lastQueen[1]

			row = lastRow
			col = lastCol + 1

			board[lastRow][lastCol] = EmptyCell

            stack = stack[:len(stack) - 1]

			continue
		}

		row++
		col = 0
	}

    var boardCopy []string

    if row == len(board) {
        // make a copy of the board
        boardCopy = make([]string, 0, len(board))

        for _, row := range board {
            s := ""

            for _, c := range row {
                if c == QueenCell {
                    s += "Q"
                } else {
                    s += "."
                }
            }

            boardCopy = append(boardCopy, s)
        }
    }

	// reset the board for next queens
	for i := len(stack) - 1; i >= 0; i-- {
		lastQueen := stack[i]
		lastRow, lastCol := lastQueen[0], lastQueen[1]
		board[lastRow][lastCol] = EmptyCell
	}

    return boardCopy
}

func solveRecursive(board Board, row int) [][]string {
    answerBoard := [][]string{}

    if row >= len(board) {
        // make a copy of the board
        boardCopy := make([]string, 0, len(board))

        for _, row := range board {
            s := ""

            for _, c := range row {
                if c == QueenCell {
                    s += "Q"
                } else {
                    s += "."
                }
            }

            boardCopy = append(boardCopy, s)
        }

        answerBoard = append(answerBoard, boardCopy)

        return answerBoard
    }

    for col := 0; col < len(board); col++ {
        if !IsSquareUnderAttack(row, col, board) {
            board[row][col] = QueenCell

            retBoard := solveRecursive(board, row + 1)

            answerBoard = append(answerBoard, retBoard...)

            board[row][col] = EmptyCell
        }
    }

    return answerBoard
}

func SolveNQueensRecursive(n int) [][]string {
    answer := [][]string{}

	board := Board{}

	for range n {
		row := make([]int, n)
		board = append(board, row)
	}

	// what we'll do

	// iterate over the first row and keep filling a Queen on each column
	// for each column that we fill a queen, go through the 2nd row to the
	// end and keep filling queens whereever we can

	for col := 0; col < len(board); col++ {
		// row is 0 here
		board[0][col] = QueenCell

        retBoard := solveRecursive(board, 1)

        if len(retBoard) > 0 {
            answer = append(answer, retBoard...)
        }

		board[0][col] = EmptyCell
	}

    for _, board := range answer {
        printAnswerBoard(board)
    }

    return answer
}
