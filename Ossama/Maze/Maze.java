package com.company;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class Maze {
    Node[][] maze;
    int N;
    Queue <Node> queue=new LinkedList<>();
    private boolean canGo(int x, int y) {
        if (x < N && y < N && x >= 0 && y >= 0 && maze[x][y].data == 0&&!maze[x][y].visited)
            return true;
        return false;
    }

    public boolean solve(int x, int y) {
        if (x == N - 1 && y == N - 1) {
            System.out.println("maze solved");
            queue.add(maze[x][y]);
            return true;
        }
        if (canGo(x, y)) {
            maze[x][y].visited = true;
            //System.out.println("maze[" + x + "][" + y + "]: " + maze[x][y].visited);
            queue.add(maze[x][y]);
            if (solve(x+1, y )) {
                return true;
            }
            if (solve(x , y+1)) {
                return true;
            }
            if (solve(x , y-1)) {
                return true;
            }
            if (solve(x-1, y)) {
                return true;
            }
        }
        //System.out.println("Returning false on: maze["+x+"]["+y+"]");
        if(x<N&&x>=0&&y<N&&y>=0)
        {
            if(((LinkedList<Node>) queue).getLast()==maze[x][y])
            ((LinkedList<Node>) queue).removeLast();


        }
        return false;
    }

    public void readData() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter N: ");
        int n = scanner.nextInt();
        N = n;
        maze = new Node[N][N];

        for (int i = 0; i < n; i++) {
            System.out.println("Enter Row(" + i + "):");
            System.out.println("****************");
            for (int j = 0; j < n; j++) {
                System.out.println("Enter Column(" + j + "): ");
                Node node = new Node();
                node.data = scanner.nextInt();
                node.x = i;
                node.y = j;
                maze[i][j] = node;
            }
        }

    }

    public void printMaze() {
        for (int i = 0; i < N; i++) {

            for (int j = 0; j < N; j++) {
                System.out.print(maze[i][j].data + " ");
            }
            System.out.println();
        }
    }
    public void printSolution(){

        System.out.println("Solution");
        while(!queue.isEmpty())
        {
            Node temp=queue.poll();
            System.out.println("["+temp.x+"]["+temp.y+"]");
        }
    }
}