package EJERCICIOS;
import java.util.Scanner;
public class ejercicio7 {
	public static void main(String[] args) {
		/*Realizar una función que busque una palabra escondida dentro de un texto. Por
		  ejemplo, si la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”,
		  entonces si se encontrará y deberá devolver True, en caso contrario deberá devolver
		  False. Las letras de la palabra escondida deben aparecer en el orden correcto en la
		  cadena que la oculta:
		  shybaoxlna ⇒ hola: True
		  soybahxlna ⇒ hola: False*/
		
		 Scanner s = new Scanner(System.in);

		    int numCasos = Integer.parseInt(s.nextLine());
		    int count = 0;
		    int contadorBusqueda=0;

		    if (numCasos == 0) {

		    } else {

		        do {

		            String texto = s.nextLine();
		            String buscar = s.nextLine();

		            texto = texto.replaceAll(" ", "");
		            texto = texto.toLowerCase();

		            buscar = buscar.replaceAll(" ", "");
		            buscar = buscar.toLowerCase();
		            int indexUltimoCaracter = 0; 
		            contadorBusqueda = 0;
		            for (int i = 0; i < buscar.length(); i++) { 

		                for (int j = indexUltimoCaracter; j < texto.length(); j++) {
		                    if (buscar.charAt(i) == texto.charAt(j)) {                                                    
		                        contadorBusqueda++;
		                    }
		                }
		            }
		            if (contadorBusqueda == buscar.length()) {
		                System.out.println("SI");
		            } else {
		                System.out.println("NO");
		            }
		        } while (count != numCasos);

		    }
	}
}