//Write a program using do-while loop to display a menu-driven program.
package com.company;
import java.util.Scanner;

public class MenuDrivenProgram {
    static void main() {
        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\n--- MENU ---");
            System.out.println("1. Addition");
            System.out.println("2. Subtraction");
            System.out.println("3. Multiplication");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");

            choice = sc.nextInt();

            if (choice == 1) {
                System.out.print("Enter two numbers: ");
                int a = sc.nextInt();
                int b = sc.nextInt();
                System.out.println("Sum = " + (a + b));
            }
            else if (choice == 2) {
                System.out.print("Enter two numbers: ");
                int a = sc.nextInt();
                int b = sc.nextInt();
                System.out.println("Difference = " + (a - b));
            }
            else if (choice == 3) {
                System.out.print("Enter two numbers: ");
                int a = sc.nextInt();
                int b = sc.nextInt();
                System.out.println("Product = " + (a * b));
            }
            else if (choice == 4) {
                System.out.println("Exiting program...");
            }
            else {
                System.out.println("Invalid choice!");
            }

        } while (choice != 4);
    }
}
