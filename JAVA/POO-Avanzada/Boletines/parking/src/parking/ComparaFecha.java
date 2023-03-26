package parking;

import java.time.temporal.ChronoUnit;
import java.util.Comparator;
public class ComparaFecha implements Comparator {
		
		@Override
		public int compare(Object o1, Object o2) {
			return (int)ChronoUnit.YEARS.between(((Vehiculo)o1).getFechaEntrada().getFecha(),((Vehiculo)o2).getFechaEntrada().getFecha());
		}
}
