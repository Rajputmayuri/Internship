//Write a program to print multiplication table of 10 in reverse order.

package com.company;

public class reverse_table {
    static void main() {
        int n=10;
        for(int i=10;i>=1;i--){
            System.out.println(+ n + " X " + i + " = " +(n*i));
        }
    }
}
