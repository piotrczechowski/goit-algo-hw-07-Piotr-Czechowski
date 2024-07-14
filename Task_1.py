import heapq

def min_cost_to_connect_cables(cables):
    
    heapq.heapify(cables)
    
    total_cost = 0
    
  
    while len(cables) > 1:
        
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
       
        combined_length = first + second
        total_cost += combined_length
        
      
        heapq.heappush(cables, combined_length)
    
    return total_cost


cables = [4, 3, 2, 6]
min_cost = min_cost_to_connect_cables(cables)
print(f"The minimum cost to connect all cables is: {min_cost}")
