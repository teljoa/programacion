package ejercicios;
import java.util.Scanner;
public class ejercicio3 {
	public static void main(String[] args) {
		/*Diseña una función que, dada una cadena de entrada, comprueba si es una
		contraseña fuerte o no. Se considera que una contraseña es fuerte si contiene 8 o
		más caracteres, y entre ellos al menos hay una mayúscula, una minúscula, un signo
		de puntuación y al menos un dígito.*/
		String valor="REGHRFGDSgf4d:";
		
		String SIGNOS_PUNTUACION=",.!?¿/';:";
		
		int LONGITUD_MINIMA_SEGURA=8;
		boolean existeMayscula=false, existeMinuscula=false;
		boolean existeDigito=false, existeSignopuntuacion=false;
		
		if (valor!=null && valor.length()>=LONGITUD_MINIMA_SEGURA) {
			
			for(int i=0; i<valor.length();i++) {
				if(Character.isUpperCase(valor.charAt(i))) {
					existeMayscula=true;
				}else if(Character.isLowerCase(valor.charAt(i))) {
					existeMinuscula=true;
				}else if(Character.isDigit(valor.charAt(i))) {
					existeDigito=true;
				}else {
					for(int j=0; j<SIGNOS_PUNTUACION.length();j++) {
						if(SIGNOS_PUNTUACION.charAt(j)==valor.charAt(i)) {
							existeSignopuntuacion=true;
						}
					}
				}
			}
		}
		System.out.println(existeMayscula && existeMinuscula && existeDigito && existeSignopuntuacion);
	}
}
