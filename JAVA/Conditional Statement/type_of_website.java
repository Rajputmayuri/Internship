/*Write a Java program to find out the type of website form the url.
.com = commercial website
.org= organization website
.in = indian website*/

package com.company;

import java.util.Scanner;

public class type_of_website {
    static void main() {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter website name =");
        String name=sc.nextLine();
        if (name.endsWith(".com")) {
            System.out.println("Commerical Website ");
        }

        else if(name.endsWith(".org")) {
            System.out.println("Organization Website ");
        }
        else {
            System.out.println("Indian Website");

            }
        }
    }

