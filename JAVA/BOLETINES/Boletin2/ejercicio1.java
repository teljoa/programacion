package ejercicios;
import java.util.Scanner;
public class ejercicio1 {
	public static void main(String[] args) {
		/*Realizar un método llamado numeroSolucionesEcuacionSegundoGrado que reciba
		los coeficientes de una ecuación de segundo grado y devuelva el número de
		soluciones que tiene. Si los argumentos no son válidos (el primer coeficiente tiene
		que ser distinto de cero) debe devolver un -1.*/
		
		System.out.println("x^2 - 5x + 6"); 
        double resultados[] = ecuacion2Grado(1, -5, 6);
 
        if (resultados == null) {
            System.out.println("No tiene solucion");
        } else {
            for (int i = 0; i < resultados.length; i++) {
                System.out.println(resultados[i]);
            }
        }
 
        System.out.println("x^2 - 2x + 1"); 
        resultados = ecuacion2Grado(1, -2, 1);
 
        if (resultados == null) {
            System.out.println("No tiene solucion");
        } else {
            for (int i = 0; i < resultados.length; i++) {
                System.out.println(resultados[i]);
            }
        }
 
        System.out.println("x^2 - x + 1"); 
        resultados = ecuacion2Grado(1, 1, 1);
 
        if (resultados == null) {
            System.out.println("No tiene solucion");
        } else {
            for (int i = 0; i < resultados.length; i++) { System.out.println(resultados[i]); } } } public static double[] ecuacion2Grado(int a, int b, int c) { double discriminante = (Math.pow(b, 2) - (4 * a * c)); if (discriminante >= 0) {
 
            double soluciones[];
 
       
            if (discriminante == 0) {
 
                soluciones = new double[1];
 
                soluciones[0] = ((-b) - (4 * a * c)) / (2 * a);
 
              
            } else {
 
                soluciones = new double[2];
 
                soluciones[0] = ((-b) + Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
 
                soluciones[1] = ((-b) - Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
 
            }
 
            return soluciones;
        } else {
        
            return null;
        }
 
	}
}