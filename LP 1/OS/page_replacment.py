from collections import deque

def fifo_page_replacement(pages, capacity):
    page_queue = deque(maxlen=capacity)
    page_set = set()
    page_faults = 0
    page_hits = 0

    for page in pages:
        if page in page_set:
            page_hits += 1
        else:
            page_faults += 1

            if len(page_queue) == capacity:
                removed_page = page_queue.popleft()
                page_set.remove(removed_page)

            page_queue.append(page)
            page_set.add(page)

        
        print("Current Page Queue (FIFO):", list(page_queue))

    return page_faults, page_hits

def lru_page_replacement(pages, capacity):
    page_queue = deque(maxlen=capacity)
    page_set = set()
    page_faults = 0
    page_hits = 0

    for page in pages:
        if page in page_set:
            page_hits += 1
            page_queue.remove(page)
            page_queue.append(page)
        else:
            page_faults += 1

            if len(page_queue) == capacity:
                removed_page = page_queue.popleft()
                page_set.remove(removed_page)

            page_queue.append(page)
            page_set.add(page)

        print("Current Page Queue (LRU):", list(page_queue))

    return page_faults, page_hits

def optimal_page_replacement(pages, capacity):
    page_queue = deque(maxlen=capacity)
    page_set = set()
    page_faults = 0
    page_hits = 0

    for i, page in enumerate(pages):
        if page in page_set:
            page_hits += 1
        else:
            page_faults += 1

            if len(page_queue) == capacity:
                farthest_used = -1
                farthest_idx = -1

                for idx, item in enumerate(page_queue):
                    if item not in pages[i + 1:]:
                        farthest_used = item
                        farthest_idx = idx
                        break

                if farthest_used == -1:
                    farthest_used = page_queue[0]

                page_queue.remove(farthest_used)
                page_set.remove(farthest_used)

            page_queue.append(page)
            page_set.add(page)

        print("Current Page Queue (Optimal):", list(page_queue))

    return page_faults, page_hits

if __name__ == "__main__":
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    capacity = 3

    print("Input Page Reference Sequence:", pages)
    print("Number of Frames (Capacity):", capacity)

    fifo_faults, fifo_hits = fifo_page_replacement(pages, capacity)
    print("Total Page Faults (FIFO):", fifo_faults)
    print("Total Page Hits (FIFO):", fifo_hits)

    lru_faults, lru_hits = lru_page_replacement(pages, capacity)
    print("Total Page Faults (LRU):", lru_faults)
    print("Total Page Hits (LRU):", lru_hits)

    optimal_faults, optimal_hits = optimal_page_replacement(pages, capacity)
    print("Total Page Faults (Optimal):", optimal_faults)
    print("Total Page Hits (Optimal):", optimal_hits)
