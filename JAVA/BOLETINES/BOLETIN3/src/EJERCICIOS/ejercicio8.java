package EJERCICIOS;
import java.util.Scanner;
public class ejercicio8 {
	public static void main(String[] args) {
		/*Diseñar una función que reciba como parámetro tres cadenas, la primera será una
		frase y deberá buscar si existe la palabra que recibe como segundo parámetro y
		reemplazarla por la tercera.*/
	
		String frase1="buenos dias a todos";
		String palabra1="dias";
		String palabra2="noches";
		
		String cadenaRemplazada = frase1.replace(palabra1, palabra2);
        System.out.printf("Cadena: %s\n", cadenaRemplazada);
		      
	}
}
