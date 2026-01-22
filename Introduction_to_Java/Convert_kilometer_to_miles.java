package com.company;
import java.util.Scanner;
public class ch1_ps4 {
    static void main() {
        //Write a java program to convert kilometers to miles
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter kilometers =");
        double kilometers=sc.nextDouble();
        double miles=kilometers*0.621371;
        System.out.println("kilometers to miles ="+miles);
    }
}
