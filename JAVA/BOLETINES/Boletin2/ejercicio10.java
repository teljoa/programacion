package ejercicios;
import java.util.Scanner;
public class ejercicio10 {
	public static void main(String[] args) {
		/*Realiza un método llamado gcd (greaterCommonDivisor) que recibirá dos números y
		devuelva el máximo común divisor según el algoritmo de Euclides.*/
	
	int a=54;  
	int b=120;
    int temporal;
    while (b != 0) {
        temporal = b;
        b = a % b;
        a = temporal;
    }
    System.out.println("La solucion es"+a);
}
}

