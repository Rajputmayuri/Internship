//Write a java program to detect double and triple spaces in a string.

package com.company;

public class IndexOf {
    static void main() {
        String str="This string contain  double and   triple spaces";
        System.out.println(str.indexOf("  "));
        System.out.println(str.indexOf("   "));
    }
}
