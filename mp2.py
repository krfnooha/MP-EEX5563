# Memory block sizes (in KB) and process sizes
memory_blocks = [100, 200, 300, 150]  # Available memory blocks
process_sizes = [120, 250, 90, 350]   # Processes requesting memory

# Function to simulate First Fit memory allocation
def first_fit(memory_blocks, process_sizes):
    n_blocks = len(memory_blocks)
    n_processes = len(process_sizes)
    
    # To keep track of memory block allocation (-1 indicates not allocated)
    allocation = [-1] * n_processes
    
    # Iterate through each process
    for i in range(n_processes):
        # Check each memory block for the current process
        for j in range(n_blocks):
            if memory_blocks[j] >= process_sizes[i]:  # If the block can fit the process
                allocation[i] = j  # Allocate the block to the process
                memory_blocks[j] -= process_sizes[i]  # Reduce the available memory in the block
                break  # Move to the next process
    
    # Print the allocation results
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(n_processes):
        if allocation[i] != -1:
            print(f"{i + 1}\t\t{process_sizes[i]}\t\t{allocation[i] + 1}")
        else:
            print(f"{i + 1}\t\t{process_sizes[i]}\t\tNot Allocated")

# Run the First Fit function
print("Initial Memory Blocks:", memory_blocks)
first_fit(memory_blocks.copy(), process_sizes)
