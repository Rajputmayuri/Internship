package com.company;
import java.util.Scanner;

public class Exercise_1 {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter marks for subject1 =");
        int subject1=sc.nextInt();
        System.out.print("Enter marks for subject2=");
        int subject2=sc.nextInt();
        System.out.print("Enter marks for subject3=");
        int subject3=sc.nextInt();
        System.out.print("Enter marks for subject4=");
        int subject4 =sc.nextInt();
        System.out.print("Enter marks for subject5=");
        int subject5 =sc.nextInt();
        float total=subject1+subject2+subject3+ subject4 + subject5;
        float percentage=(total/500)*100;
        System.out.println("Total marks of the student ="+total);
        System.out.print("Percentage of the student is ="+percentage);
    }
}
