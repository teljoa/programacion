package ejercicios;
import java.util.Scanner;
public class ejercicio9 {
	public static void main(String[] args) {
		/*Realiza un método llamado toDecimal que reciba un String con un valor decimal
		como argumento y devuelva un número con el número decimal correspondiente.*/
	
		String decimal="93.54";
		System.out.println("String value: "+decimal);
        float f_Val = Float.valueOf(decimal);
        System.out.println("Float value: "+f_Val);
	}
}
