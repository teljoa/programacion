package EJERCICIOS;
import java.util.Scanner;
public class ejercicio6 {
	public static void main(String[] args) {
		/*Haciendo uso de la función anterior crea una función esCapicúa que acepte
		  números tanto enteros como decimales.*/
	
		int N, aux, inverso = 0, cifra;
        Scanner sc = new Scanner(System.in);
        do {
            System.out.print("Introduce un número >= 10: ");                                                 
            N = sc.nextInt();
        } while (N < 10);
       
        aux = N;
        while (aux!=0){
            cifra = aux % 10;
            inverso = inverso * 10 + cifra;
            aux = aux / 10;
        }
    
        if(N == inverso){
            System.out.println("Es capicua");
        }else{
            System.out.println("No es capicua");
        }
	}
}
