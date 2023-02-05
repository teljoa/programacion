package ejercicios;
import java.util.Scanner;
public class ejercicio2 {
	public static void main(String[] args) {
		/*Realiza un programa que pida un número por teclado y que después muestre ese
		número al revés.*/
		
		System.out.print("Introduzca un número entero: ");
	    int numeroIntroducido = Integer.parseInt(System.console().readLine());

	    int numero = numeroIntroducido;
	    int volteado = 0;
	    
	    while (numero > 0) {
	      volteado = (volteado * 10) + (numero % 10);
	      numero /= 10;
	    } // while
	    
	    System.out.print("Si le damos la vuelta al " + numeroIntroducido);
	    System.out.println(" tenemos el " + volteado + ".");
	}
}
