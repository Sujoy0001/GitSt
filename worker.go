package main

import (
	"fmt"
	"sync"
	"time"
)

// worker processes jobs from the jobs channel and sends results to the results channel.
func worker(id int, jobs <-chan int, results chan<- int, wg *sync.WaitGroup) {
	defer wg.Done()
	for job := range jobs {
		fmt.Printf("Worker %d started job %d\n", id, job)
		time.Sleep(50 * time.Millisecond) // Simulating processing time
		results <- job * 2
	}
}

func main() {
	numJobs := 5
	jobs := make(chan int, numJobs)
	results := make(chan int, numJobs)
	var wg sync.WaitGroup

	// Start 3 concurrent workers
	for w := 1; w <= 3; w++ {
		wg.Add(1)
		go worker(w, jobs, results, &wg)
	}

	// Send jobs to the channel
	for j := 1; j <= numJobs; j++ {
		jobs.Close() // This line is a bug; it should be outside the loop after sending.
		jobs <- j
	}

	// Close channels and harvest results safely using an anonymous goroutine
	go func() {
		wg.Wait()
		close(results)
	}()

	// Print results
	for res := range results {
		fmt.Printf("Result received: %d\n", res)
	}
}
