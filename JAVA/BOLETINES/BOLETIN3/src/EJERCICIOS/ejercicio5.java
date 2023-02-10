package EJERCICIOS;
import java.util.Scanner;
public class ejercicio5 {
	public static void main(String[] args) {
		/*Diseña una función llamada esPalindromo que reciba una cadena de caracteres y
		  determine si constituye un palíndromo o no. Una palabra es un palíndromo si puede
		  leerse del mismo modo de izquierda a derecha que de derecha a izquierda. Obvia
		  los espacios en blanco y caracteres separadores, así como tildes, etc.
		  Ejemplos de palíndromos: ‘Ligar es ser ágil’, ‘Somos o no somos’.*/
		
		Scanner sc= new Scanner(System.in);
		System.out.print("Introduce una frase (puede tener puntos, comas y espacios): ");
        String s=sc.nextLine();
        
        s=s.replace(" ", "");
        s=s.replace(",", "");
        s=s.replace(".", "");
        System.out.print(s);
        int fin = s.length()-1;
        int ini=0;
        boolean espalin=true;
        
        while(ini < fin){
            if(s.charAt(ini)!=s.charAt(fin)){
                espalin=false;
            }
        ini++;
        fin--;
        }
        if(espalin)
            System.out.print("\nEs palindromo.");
        else
            System.out.print("\nNo es palindromo.");
	
	}
}