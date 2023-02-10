package EJERCICIOS;
import java.util.Scanner;
public class ejercicio2 {
	public static void main(String[] args) {
		/*Un número es divisible por 3 si la suma de todas sus cifras reducidas a una cifra es
		igual a 0, 3, 6 ó 9.
		Por ejemplo, 156 ⇒ 1+5+6=12 ⇒ 1+2 = 3 es divisible,
		pero 157 ⇒ 1+5+7 =13 ⇒ 1+3 =4 no lo es.*/
		
		Scanner miScanner = new Scanner(System.in);
        int numero;
        int resultado = 0;
        
        System.out.print("Introduce un número para sumar sus dígitos: ");
        numero = miScanner.nextInt();

        while(numero > 0) {
            resultado += numero % 10;
            numero = numero / 10;
        }

        System.out.println("La suma es: " + resultado);
		
		if (resultado%3==0) {
			System.out.println("Es divisible");
		}else {
			System.out.println("No es divisible");
		}
	}
}