package boletin1EDA.Ejercicio1;

import java.util.Arrays;

public class Principal {
public static void main(String[] args) {
		
	Integer[] numeros = new Integer[5];
	
	numeros[0]=10;
	numeros[1]=20;
	numeros[2]=30;
	numeros[3]=40;
	numeros[4]=50;
	
	System.out.println(Arrays.toString(numeros));
	System.out.println(Arrays.toString(riversada(numeros)));
	
	
}
	
	public static <T> T[] riversada ( T[] arrayOriginal) {
		T[] arrayRiverse = arrayOriginal.clone();
		
		for(int i=0; i<arrayOriginal.length; i++) {
			arrayRiverse[i]=arrayOriginal[arrayOriginal.length-1-i];
		}
		
		
		return arrayRiverse;
	}	
}