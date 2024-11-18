package main

import (
	"fmt"
	"strconv"
)

func printOperators(operators *[]byte) {
    fmt.Printf("[ ")
    for _, o := range *operators {
        fmt.Printf("'%c', ", o)
    }

    fmt.Printf("]\n")
}

func operate(operands *[]int, operators *[]byte) {
    printOperators(operators)
    fmt.Printf("operands: %+v\n", *operands)

	right := (*operands)[len(*operands)-1]
	op := (*operators)[len(*operators)-1]

    (*operators) = (*operators)[:len(*operators) - 1]

	if op == '+' {
		left := (*operands)[len(*operands)-2]
		(*operands) = (*operands)[:len(*operands)-2]

		*operands = append(*operands, right+left)
	} else {
		if len(*operands) > 1 {
			left := (*operands)[len(*operands)-2]
			(*operands) = (*operands)[:len(*operands)-2]
			*operands = append(*operands, left - right)
		} else {
			(*operands) = (*operands)[:len(*operands)-1]
			*operands = append(*operands, -right)
		}
	}
}

func constructNumber(i *int, s string) int {
    numStr := ""

    for *i < len(s) {
        if s[*i] >= '0' && s[*i] <= '9' {
            numStr += string(s[*i])
            *i++
            continue
        }

        *i--

        break
    }

    val, _ := strconv.Atoi(numStr)

    return val
}

func calculate(s string) int {
	// convert infix to postfix
	operands := []int{}
	operators := []byte{}

	for i := 0; i < len(s); i++ {
		char := s[i]

		if char == ' ' {
			continue
		}

		if char >= '0' && char <= '9' {
			operands = append(operands, constructNumber(&i, s))
			continue
		}

		if char == '+' || char == '-' {
			if len(operators) > 0 && operators[len(operators) - 1] != '(' {
				// pop from the operands and perform the operation
				operate(&operands, &operators)
			} 

			operators = append(operators, char)

			continue
		}

		if char == '(' {
			operators = append(operators, char)
			continue
		}

		if char == ')' {
			// start popping from the operands until we find (
			for {
				op := operators[len(operators)-1]

				if op == '(' {
					operators = operators[:len(operators)-1]
					break
				}

				operate(&operands, &operators)
			}
		}
	}

	// now we basically evaluate all remaining expressions
	for len(operators) > 0 {
		operate(&operands, &operators)
	}

	return operands[0]
}
