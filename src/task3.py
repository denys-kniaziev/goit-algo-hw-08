import heapq


def min_cable_connection_cost(cables):
    """
    Find the minimum cost to connect all cables using a greedy approach with min-heap.
    
    The algorithm always connects the two shortest cables first, which minimizes
    the total cost. This is optimal because shorter cables contribute to the cost
    multiple times when used in subsequent connections.
    
    Args:
        cables: list of int/float - lengths of individual cables
        
    Returns:
        int/float - minimum total cost to connect all cables
    """
    if not cables:
        return 0
    
    if len(cables) == 1:
        return 0  # No connection needed for single cable
    
    # Create a min-heap from cable lengths
    heap = cables.copy()
    heapq.heapify(heap)
    
    total_cost = 0
    
    # Connect cables until only one remains
    while len(heap) > 1:
        # Take two shortest cables
        cable1 = heapq.heappop(heap)
        cable2 = heapq.heappop(heap)
        
        # Cost of connecting these two cables
        connection_cost = cable1 + cable2
        total_cost += connection_cost
        
        # Put the connected cable back into heap
        heapq.heappush(heap, connection_cost)
    
    return total_cost


def min_cable_connection_cost_detailed(cables):
    """
    Same algorithm as above but with detailed step-by-step output for demonstration.
    
    Args:
        cables: list of int/float - lengths of individual cables
        
    Returns:
        int/float - minimum total cost to connect all cables
    """
    if not cables:
        return 0
    
    if len(cables) == 1:
        print("Only one cable, no connection needed.")
        return 0
    
    print(f"Initial cables: {cables}")
    
    heap = cables.copy()
    heapq.heapify(heap)
    
    total_cost = 0
    step = 1
    
    while len(heap) > 1:
        cable1 = heapq.heappop(heap)
        cable2 = heapq.heappop(heap)
        connection_cost = cable1 + cable2
        total_cost += connection_cost
        
        print(f"Step {step}: Connect cables {cable1} + {cable2} = {connection_cost}, Total cost: {total_cost}")
        
        heapq.heappush(heap, connection_cost)
        step += 1
    
    return total_cost


def main():
    # Test case 1: Example from the problem
    cables1 = [4, 3, 2, 6]
    print("Test case 1:")
    print(f"Cables: {cables1}")
    cost1 = min_cable_connection_cost_detailed(cables1)
    print(f"Minimum cost: {cost1}")
    print()
    
    # Test case 2: Another example
    cables2 = [20, 4, 8, 2]
    print("Test case 2:")
    print(f"Cables: {cables2}")
    cost2 = min_cable_connection_cost(cables2)
    print(f"Minimum cost: {cost2}")
    print()
    
    # Test case 3: Edge cases
    print("Edge cases:")
    print(f"Empty list: {min_cable_connection_cost([])}")
    print(f"Single cable: {min_cable_connection_cost([10])}")
    print(f"Two cables: {min_cable_connection_cost([3, 7])}")


if __name__ == "__main__":
    main()