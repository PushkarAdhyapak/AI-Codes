import java.util.Scanner;
public class A3 {
    int minDistance(int dist[], Boolean sptSet[]) {
        int min = Integer.MAX_VALUE, min_index = -1;
        for (int v = 0; v < dist.length; v++)
            if (sptSet[v] == false && dist[v] <= min) {
                min = dist[v];
                min_index = v;
            }

        return min_index;
    }

    void printSolution(int dist[]) {
        System.out.println("Vertex \t\t Distance from Source");
        for (int i = 0; i < dist.length; i++)
            System.out.println(i + " \t\t " + dist[i]);
    }

    void dijkstra(int graph[][], int src) {
        int dist[] = new int[graph.length];
        Boolean sptSet[] = new Boolean[graph.length];

        for (int i = 0; i < graph.length; i++) {
            dist[i] = Integer.MAX_VALUE;
            sptSet[i] = false;
        }
    
        dist[src] = 0;
    
        for (int count = 0; count < graph.length - 1; count++) {
            int u = minDistance(dist, sptSet);
            sptSet[u] = true;
    
            for (int v = 0; v < graph.length; v++)
                if (!sptSet[v] && graph[u][v] != 0
                        && dist[u] != Integer.MAX_VALUE
                        && dist[u] + graph[u][v] < dist[v])
                    dist[v] = dist[u] + graph[u][v];
        }
    
        printSolution(dist);
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number of rows/columns");
        int V = sc.nextInt();
        int graph[][] = new int[V][V];
        A3 t = new A3();
    
        System.out.println("Enter the adjacency matrix of the graph:");
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                graph[i][j] = sc.nextInt();
            }
        }
    
        System.out.println("The adjacency matrix is:");
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                System.out.print(graph[i][j] + " ");
            }
            System.out.println();
        }
    
        System.out.print("Enter the source vertex: ");
        int src = sc.nextInt();
    
        // Function call
        t.dijkstra(graph, src);
    }
}    