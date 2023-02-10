package EJERCICIOS;
import java.util.Scanner;
public class ejercicio4 {
	public static void main(String[] args) {
		/*Crea tres funciones cuyo comportamiento sea como el de los métodos de String
       	startsWirth, contains y endsWith, pero sin utilizar ninguno de ellos.*/
	
		System.out.println(empiezaPor("hola buenos dias", "hola"));
		System.out.println(empiezaPor("hola buenos dias", "helo"));
		System.out.println(terminaPor("hola buenos dias", "dias"));
		System.out.println(terminaPor("hola buenos dias", "dia"));
		System.out.println(contiene("hola buenos dias", "buenos"));
		System.out.println(contiene("hola buenos dias", "buenas"));
	}
		
		public static boolean empiezaPor(String cadena, String palabra) {
			boolean mensaje = false;
			if (cadena.indexOf(palabra)==0) {
				mensaje=true;
			}
			return mensaje;
		}
		
		public static boolean terminaPor(String cadena, String palabra) {
			boolean mensaje = false;
			if (cadena.indexOf(palabra)==(cadena.length())-palabra.length()) {
				mensaje=true;
			}
			return mensaje;
		}
		public static boolean contiene(String cadena, String palabra) {
			boolean mensaje = false;
			for(int i=0; i<cadena.length(); i++) {
				if (cadena.indexOf(palabra)==i) {
					mensaje = true;
				}
			}
			
			return mensaje;
	}
}