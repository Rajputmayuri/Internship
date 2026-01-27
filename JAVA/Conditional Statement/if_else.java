//write a java program to check whether a person is eligible for voting or not.

package com.company;
import java.util.Scanner;

public class if_else {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter age of the person =");
        int age=sc.nextInt();
        if(age>=18) {
            System.out.println("Eligible for voting");
        }else{
            System.out.println("Not eligible for voting");
        }
    }
}
