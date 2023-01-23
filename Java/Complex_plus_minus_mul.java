import java.util.Scanner;

/*
 * Java Program to add and subtract two complex numbers
 * This program will calculate sum and difference of two
 * given a complex number in Java.
 */
public class Main {

  public static void main(String[] args) {

    // first complex number
    Complex c1 = new Complex(2, 4);
    Complex c2 = new Complex(3, 5);

    Complex sum = c1.sum(c2);
    Complex difference = c1.difference(c2);
    Complex multiplication = c1.multiplication(c2);
    System.out.println("first complex number: " + c1);
    System.out.println("second complex number: " + c2);
    System.out.println("sum of two complex numbers: " + sum);
    System.out.println("difference of two complex numbers: " + difference);
    System.out.println("Multiplication of two complex numbers: " + multiplication);

  }
}

/*
 * A class to represent a complex number. A complex number has two parts, real
 * and imaginary. Make this class Immutable as it's a value class.
 */
class Complex {
  private final double real;
  private final double imaginary;

  public Complex(double real, double imaginary) {
    this.real = real;
    this.imaginary = imaginary;
  }

  public Complex sum(Complex other) {
    double r = this.real + other.real;
    double i = this.imaginary + other.imaginary;
    return new Complex(r, i);
  }

  public Complex difference(Complex other) {
    double r = this.real - other.real;
    double i = this.imaginary - other.imaginary;
    return new Complex(r, i);
  }
  public Complex multiplication(Complex other){
      double r = this.real * other.real;
      double i = this.imaginary * other.imaginary;
      return new Complex(r, i);
  }

  public double getReal() {
    return real;
  }

  public double getImaginary() {
    return imaginary;
  }

  @Override
  public String toString() {
    return real + " + " + imaginary + "i";
  }

}