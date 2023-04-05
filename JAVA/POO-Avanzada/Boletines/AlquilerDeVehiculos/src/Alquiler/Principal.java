package Alquiler;
import java.util.Scanner;
public class Principal {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int opcion=0;
		Vehiculo empresa[]=new Vehiculo[200];
		String matricula;
		String tipo;
		String dato;
		String datos[]=new String[200];
		
		while(opcion!=3) {
			System.out.println("Introduzca opcion:");
			opcion=sc.nextInt();
			if(opcion==1) {
				System.out.println("Introduzca matricula:");
				matricula=sc.nextLine();
				System.out.println("Introduzca tipo de vehiculo:");
				tipo=sc.nextLine();
				System.out.println("Intrdusca su dato identificativo:");
				dato=sc.nextLine();
				for(int i=0;i<empresa.length;i++) {
					if(empresa[i].DarAlta()==true) {
						empresa[i].setMatricula(matricula);;
						for(int j=0;i<datos.length;i++) {
							datos[j]=dato;
						}
					}
				}
			}else if(opcion==2) {
				System.out.println("Introduzca matricula:");
				matricula=sc.nextLine();
				for(int i=0;i<empresa.length;i++) {
					if(empresa[i].equals(true)) {
						empresa[i].toString();
					}
				}
			}else {
				System.out.println("Opcion incorecta.Vuelve a introducirla.");
			}
		}
	}
}
