package EJERCICIOS;
import java.util.Scanner;
public class ejercicio1 {
	public static void main(String[] args) {
		/*Escribe una función que reciba una cadena de texto y una variable bandera
		(par/impar) e imprima solo los caracteres que se encuentran situados en las
		posiciones pares o impares (según indique la variable bandera).
		Desarrolla el código con un bucle for y después modifica el código para que utilice
		una estructura while y do-while.*/
		
		String bandera= "par";
		String flase= "Buenos dias";
		
		for (int i=0; i<flase.length(); i++){
			
			if (bandera.equals("par")){
				if (i%2==0) {
					String letra=String.valueOf(i);
					System.out.println(flase.charAt(i));
				}}
			else if (bandera.equals("impar")) {
				if (i%2==1) {
					String letra=String.valueOf(i);
					System.out.println(flase.charAt(i));
					}
				}
			}
	}
}

