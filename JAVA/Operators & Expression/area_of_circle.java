//Write a program to calculate area of circle using formula
package com.company;
import java.util.Scanner;
public class area_of_circle {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter radius of circle =");
        double radius=sc.nextFloat();
        double area=Math.PI*radius*radius;
        System.out.println("Area of circle ="+area);
    }
}
