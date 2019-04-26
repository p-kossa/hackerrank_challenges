package main

import (
	"fmt"
	"math"
)

func main() {
	arr := make([][]int, 6)

	for i := 0; i < 6; i++ {
		arr[i] = make([]int, 6)
		for j := 0; j < 6; j++ {
			fmt.Scan(&arr[i][j])
		}
	}
	max := math.MinInt32
	j := 0
	i := 0

	for j < 4 {
		tmp := arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
		if tmp > max {
			max = tmp
		}
		i++
		if i == 4 {
			i = 0
			j++
		}
	}
	fmt.Println(max)
}
