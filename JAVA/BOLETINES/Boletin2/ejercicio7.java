package ejercicios;
import java.util.Scanner;
public class ejercicio7 {
	public static void main(String[] args) {
		/*Realizar un método llamado segundosEntre que recibirá seis valores enteros, los
		tres primeros representarán la hora, minuto y segundos de la primera hora y los
		otros tres de la segunda hora. Se deberá devolver el número de segundos que hay
		entre la primera hora y la segunda (el valor debe ser siempre en positivo). Si los
		datos no son correctos se deberá devolver -1000.*/
	
		int h1=4;
		int m1=20;
		int s1=25;
		int h2=7;
		int m2=30;
		int s2=40;
		
		if (h1<h2||m2<m1||s2<s1){
			System.out.println(((h2-h1)*180)+((m2-m1)*60)+(s2-s1));
		}else if (h1<h2||m1<m2||s2<s1) {
			System.out.println(((h2-h1)*180)+((m1-m2)*60)+(s2-s1));
		}else if (h1<h2||m2<m1||s1<s2) {
			System.out.println(((h2-h1)*180)+((m2-m1)*60)+(s1-s2));
		}else if (h1<h2||m1<m2||s1<s1) {
			System.out.println(((h2-h1)*180)+((m1-m2)*60)+(s1-s2));
		
		}else {
			System.out.println(-1000);
		}}
}
