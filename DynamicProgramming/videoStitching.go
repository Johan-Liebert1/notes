// You are given a series of video clips from a sporting event that lasted time seconds. These video clips can be overlapping with each other and have varying lengths.
//
// Each video clip is described by an array clips where clips[i] = [starti, endi] indicates that the ith clip started at starti and ended at endi.
//
// We can cut these clips into segments freely.
//
// For example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
// Return the minimum number of clips needed so that we can cut the clips into segments that cover the entire sporting event [0, time]. If the task is impossible, return -1.
//
//
//
// Example 1:
//
// Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
// Output: 3
// Explanation: We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
// Then, we can reconstruct the sporting event as follows:
// We cut [1,9] into segments [1,2] + [2,8] + [8,9].
// Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event [0, 10].
// Example 2:
//
// Input: clips = [[0,1],[1,2]], time = 5
// Output: -1
// Explanation: We cannot cover [0,5] with only [0,1] and [1,2].
// Example 3:
//
// Input: clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
// Output: 3
// Explanation: We can take clips [0,4], [4,7], and [6,9].

package main

import (
	"fmt"
	"math"
)

type ClipsMap = map[int][]*[]int

// check if sent by value or reference
func videoStitchingHelper(
	clips [][]int,
	clipsMap *ClipsMap,
	startTime int,
	endTime int,
    usedIndicies []int,
	depth int,
) int {
	if startTime == endTime {
		return depth
	}

	returnValue := -1

	for index, clip := range clips {
		start := clip[0]

        for _, ii := range usedIndicies {
            if index == ii {
                continue
            }
        }

        // sort.Sort(clips)

        fmt.Println(startTime, endTime, clip)

		if start == startTime {
            usedIndicies = append(usedIndicies, index)
			end := clip[1]

			for i := 0; i <= end; i++ {
                for _, ii := range usedIndicies {
                    if index == ii {
                        continue
                    }
                }

				if val, ok := (*clipsMap)[i]; ok {
					minimumClips := int(math.Pow(2, 31))

					for range val {
						ret := videoStitchingHelper(clips, clipsMap, i, endTime, usedIndicies, depth+1)

						if ret < minimumClips {
							minimumClips = ret
						}
					}

					returnValue = minimumClips
				}
			}
		}
	}

	return returnValue
}

func videoStitching(clips [][]int, time int) int {
	hashMap := ClipsMap{}

	for i := range clips {
		key := clips[i][0]

		if val, ok := hashMap[key]; ok {
			val = append(val, &clips[i])
		} else {
			hashMap[key] = []*[]int{&clips[i]}
		}
	}

	return videoStitchingHelper(clips, &hashMap, 0, time, []int{}, 0)
}

func mainVideo() {
	clips := [][]int{{0, 2}, {4, 6}, {8, 10}, {1, 9}, {1, 5}, {5, 9}}
	time := 10
	print(videoStitching(clips, time))
}
