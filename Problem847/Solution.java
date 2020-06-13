
// Problem 847: Shortest Path visiting all nodes (HARD)
// Had to look at the solutions
// Note this is an NP problem, runtime is O(N*2^N) and space is O(N*2^N)
// Runtime: 7ms, faster than 71.95% of submissions and Memory usage is 39.4 MB
//          , less than 77.43% of submission
// Also note this problem assumes there are at most 32 nodes in the graph so 
//          java's int data type can be used as a bit set.

class Solution {
    // G = (V,E)

    // S:= visited set (bit vector)
    // OPT(S, v) := min nodes traversed to have visited each node in the visited set and be at node v
    // Degenerate case: OPT(S={v}, v) = 0 for all v in V
    // Inductive case: OPT(S,v) = min {1+OPT(S+v,w)}{for all w in neighbors(v)}
    
    // Want to find min(V, v) for all v in V
    static int[][] distances; //1st index is bit vector, 2nd is current vertex
    static int UNEXPLORED; // haven't calculcated yet, assigning max weight possible
    static int[][] global_graph;

    public static void shortestPath_dp(int N, int visited_set){
        boolean shouldRecalculate= true;
        while(shouldRecalculate){
            shouldRecalculate=false; // for now assume we don't need to
            for(int v = 0; v < N; v++){
                // System.out.println("looking at vs="+visited_set+ " , v="+v);
                int distance = distances[visited_set][v];
                for(int neighbor : global_graph[v]){
                    int new_visited_set = visited_set | (1 << neighbor);
                    
                    // We've found a new shortest path to cover
                    // new_visited_set and have a current node of w
                    if(distance + 1 < distances[new_visited_set][neighbor]){
                        distances[new_visited_set][neighbor] = distance+1;

                        // Determined that our shorter path found affects 
                        // others calculated for this visited set, recompute
                        if(visited_set == new_visited_set) shouldRecalculate = true;
                    }
                }
            }
        }
    }


    public static int shortestPathLength(int[][] graph) {
        // Initialization
        int N = graph.length;
        int bitvector_length = 1<<N;
        distances = new int[bitvector_length][N];
        global_graph = graph;
        UNEXPLORED = N*N;
        for(int i = 0; i < bitvector_length; i++){
            for(int j = 0; j < N; j++){
                distances[i][j]= UNEXPLORED;
            }
        }

        for(int v = 0; v < N; v++){
            distances[1<<v][v] = 0;
        }
        
        // Dynamic Programming, computation
        for(int visited_set = 0; visited_set < (1<<N); visited_set++){
            shortestPath_dp(N, visited_set);
        }


        // Determine best optimal for final soln
        final int ALL_VISITED = (1<<N)-1;
        int min = distances[ALL_VISITED][0];
        for(int v = 0; v < N; v++){
            if(distances[ALL_VISITED][v] < min){
                min = distances[ALL_VISITED][v];
            }
        }
        return min;
    }
}