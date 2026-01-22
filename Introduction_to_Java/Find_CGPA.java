package com.company;
import java.util.Scanner;
public class ch1_ps2 {
    static void main() {
        //Write a program to calculate CGPA using marks of three subjects out of 100
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter marks for subject 1=");
        float subject_1=sc.nextFloat();
        System.out.print("Enter marks for subject 2=");
        float subject_2=sc.nextFloat();
        System.out.print("Enter marks for subject 3=");
        float subject_3=sc.nextFloat();
        float CGPA=(subject_1+subject_2+subject_3)/30;
        System.out.println("CGPA = "+CGPA);
    }
}
