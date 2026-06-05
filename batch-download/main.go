package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
	"sync"
)

func download(
	allData [][]byte,
	index int,
	total int,
	url string,
	sem chan struct{},
	wg *sync.WaitGroup,
) {
	defer func() {
		wg.Done()
		<-sem
	}()

	fmt.Printf("Downloading %s... Index: %d/%d\n", url[:108], index, total)

	client := &http.Client{}

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		fmt.Printf("Error creating request: %+v\n", err)
		return
	}

	req.Header.Set("User-Agent", "Mozilla/5.0")

	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error while sending request: %+v\n", err)
		return
	}
	defer resp.Body.Close()

	b, err := io.ReadAll(resp.Body)

	if err != nil {
		fmt.Printf("Error reading request body: %+v\n", err)
		return
	}

	fmt.Printf("Index: %d/%d, Read: %d bytes\n", index, total, resp.ContentLength)

	allData[index] = b
}

func main() {
	if len(os.Args) < 3 {
		fmt.Println(
			"Usage: ./executable <file with urls> <filename to write the contents to>",
		)
		os.Exit(1)
	}

	file, err := os.ReadFile(os.Args[1])

	if err != nil {
		fmt.Printf("Failed to read file '%s': %+v\n", os.Args[1], err)
		os.Exit(1)
	}

	filePath := os.Args[2]

	fileContents := string(file)
	lines := strings.Split(fileContents, "\n")

	sem := make(chan struct{}, 10)
	wg := sync.WaitGroup{}

	// tmpdir := os.TempDir()

	// filePath := fmt.Sprintf("%s/%s", tmpdir, filename)
	fileToWrite, err := os.Create(filePath)

	if err != nil {
		fmt.Printf("Failed to create file %s\n", filePath)
		os.Exit(1)
	}

	newLines := []string{}

	for _, line := range lines {
		if !strings.HasPrefix(line, "https://") {
			continue
		}

		newLines = append(newLines, line)
	}

	allData := make([][]byte, len(newLines))

	for i, line := range newLines {
		if !strings.HasPrefix(line, "https://") {
			continue
		}

		sem <- struct{}{}

		wg.Add(1)
		go download(allData, i, len(newLines), strings.TrimSpace(line), sem, &wg)

		i++
	}

	wg.Wait()

	for _, b := range allData {
		n, err := fileToWrite.Write(b)

		if err != nil {
			fmt.Printf("Error writing to file %s: %+v\n", fileToWrite.Name(), err)
			os.Exit(1)
		}

		if n != len(b) {
			fmt.Printf(
				"Error writing to file %s. Could not write all bytes: %+v\n",
				fileToWrite.Name(),
				err,
			)
			os.Exit(1)
		}
	}
}
