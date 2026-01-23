//Write a Java program to perform bitwise AND, OR, XOR, left shift, and right shift operations on two integers.
package com.company;

import java.util.Scanner;

class BitwiseOperators {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println("AND = " + (a & b));
        System.out.println("OR = " + (a | b));
        System.out.println("XOR = " + (a ^ b));
        System.out.println("Left Shift = " + (a << 1));
        System.out.println("Right Shift = " + (a >> 1));
    }
}
