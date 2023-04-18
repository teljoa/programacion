package boletin1EDA.Ejercicio8;

public interface ComparaNombre {
	
	public default int compare(Alumno a1, Alumno a2) {
		int resultado;
		if(a1==null) {
			resultado=-1;
		}else if(a2==null) {
			resultado=1;
		}else if(a1==null) {
			resultado=0;
		}else {
			resultado=a1.nombre.compareTo(a2.nombre);
		}
		
		return resultado;
	}
}
