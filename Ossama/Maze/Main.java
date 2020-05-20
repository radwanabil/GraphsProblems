package com.company;

public class Main {

    public static void main(String[] args) {
        Maze maze=new Maze();
        maze.readData();
        System.out.println("**********");
        maze.printMaze();
        maze.solve(0,0);
        maze.printSolution();

    }
}
