package ejercicios;
import java.util.Scanner;
public class ejercicio8 {
	public static void main(String[] args) {
		/*Realiza un método llamado toBinary que reciba un número decimal como
		argumento y devuelva un String con el número binario correspondiente.*/
		
		Scanner entrada = new Scanner(System.in);
    String bin = ""; 
    int numero; 

    System.out.print("Ingrese un numero: ");
    numero = entrada.nextInt();

    while (numero > 0) {
        if (numero % 2 == 0) {
            bin = "0" + bin;
        } else {
            bin = "1" + bin;
        }
        numero = numero / 2;
    }
    System.out.println(bin);	
}
}
