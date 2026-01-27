/*Write a program to find out whether a student is pass or fail.
if it requires total 40% and at least 33% in each subject to pass.
Assume 3 subjects and take marks as an input from the user.*/

package com.company;
import java.util.Scanner;

public class pass_or_fail {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter marks for subject 1=");
        int subject1=sc.nextInt();
        System.out.print("Enter marks for subject 2=");
        int subject2=sc.nextInt();
        System.out.print("Enter marks for subject 3=");
        int subject3=sc.nextInt();
        int total=subject1+subject2+subject3;
        float percentage=(total/300.0f)*100;

        if(percentage>=40 && subject1>=33 && subject2>=33 && subject3>=33) {
            System.out.println("Result :Pass");
        }else{
            System.out.println("Result :Fail");
        }
        System.out.println("Percentage :"+percentage);
    }
}
