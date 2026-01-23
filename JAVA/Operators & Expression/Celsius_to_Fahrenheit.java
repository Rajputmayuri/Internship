//Write a java program to convert temperature from celsius to fahrenheit using expression.
package com.company;
import java.util.Scanner;

public class Celsius_to_Fahrenheit {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter temperature in Celsius =");
        double celsius=sc.nextDouble();
        double fahrenheit=(celsius*9/5)+32;
        System.out.println("Fahrenheit = "+fahrenheit);
    }
}
