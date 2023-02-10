package EJERCICIOS;
import java.util.Scanner;
import java.util.StringTokenizer;
public class ejercicio3 {
	public static void main(String[] args) {
		/*Diseña un programa que cuente el número de veces que aparece una palabra en
		una cadena de texto.*/
		
		       Scanner sc = new Scanner(System.in);
		       String frase;
		       System.out.print("Introduce una frase: ");
		       frase = sc.nextLine();
		       StringTokenizer st = new StringTokenizer(frase);
		       System.out.println("Número de palabras: " + st.countTokens());                                             
		    }
		
	}

