package ejercicios;
import java.util.Scanner;
public class ejercicio6 {
	public static void main(String[] args) {
		/*Realizar un método llamado horaMayor que recibirá seis valores enteres, los tres
		primeros representarán la hora, minuto y segundos de la primera hora y los otros
		tres de la segunda hora. Se deberá devolver un 1 si la primera hora es mayor que la
		segunda, un 2 si la segunda hora es mayor que la primera, un 0 si son iguales y un
		-1000 si los datos no son correctos.*/
		
		int h1=4;
		int m1=20;
		int s1=25;
		int h2=7;
		int m2=30;
		int s2=40;
			
		if (h1<h2){
			System.out.println("1");
		}else if (h2<h1) {
			System.out.println("2");
		}else {
			System.out.println(-1000);
		}
	}
}
