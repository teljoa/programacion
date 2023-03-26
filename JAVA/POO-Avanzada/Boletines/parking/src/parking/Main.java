package parking;
import java.time.LocalDate;
import java.time.LocalTime;
public class Main {
	public static void main(String[] args) {
		Parking brenes = new Parking();
		
		try {
			Vehiculo uno = new Vehiculo(new Marca("Ford"), new Modelo("Focus"), new Matricula("ABC",1234), 
					Combustible.Gasoil, new FechaEntrada(LocalDate.now(), LocalTime.now()),Tipo.Automovil );
		
			Vehiculo dos = new Vehiculo(new Marca("Citroen"), new Modelo("C4"), new Matricula("ZZZA",9992), 
					Combustible.Electrico, new FechaEntrada(LocalDate.now(), LocalTime.now()),Tipo.Automovil );
		
			Vehiculo tres = new Vehiculo(new Marca("Kawasaki"), new Modelo("Ninja"), new Matricula("IMKL",9012), 
					Combustible.Gasolina, new FechaEntrada(LocalDate.now(), LocalTime.now()),Tipo.Ciclomotor );
		
			Vehiculo cinco = new Vehiculo(new Marca("Audi"), new Modelo("A4"), new Matricula("PJRS",7890), 
					Combustible.Gasolina, new FechaEntrada(LocalDate.now(), LocalTime.now()),Tipo.Automovil );
			
			Vehiculo cuatro = new Vehiculo(new Marca("Peugeot"), new Modelo("207"), new Matricula("MNÑC",3456), 
					Combustible.Hibrido, new FechaEntrada(LocalDate.now(), LocalTime.now()),Tipo.Automovil );
		
			
			System.out.println(brenes.addVehiculo(uno));
			System.out.println(brenes.addVehiculo(dos));
			System.out.println(brenes.addVehiculo(tres));
			System.out.println(brenes.addVehiculo(cuatro));
			System.out.println(brenes.addVehiculo(cinco));
			
			
			System.out.println("Por defecto");
			System.out.println(brenes);
			
			System.out.println("Marca y modelo");
			System.out.println(brenes.ordenarPorMarcayModelo());
			
			System.out.println(brenes.removeVehiculo("ZZZA9992"));
			System.out.println("Matricula");
			System.out.println(brenes.ordenarPorMatricula());
			
			System.out.println(brenes.removeVehiculo("IMKL9012"));
			System.out.println("Tipo y Combustible");
			System.out.println(brenes.ordenarPorTipoyCombustible());
			
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			System.out.println("Done!");
		}
	}
}
