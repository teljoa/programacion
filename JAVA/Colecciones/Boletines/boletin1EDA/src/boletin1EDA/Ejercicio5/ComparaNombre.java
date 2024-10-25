package boletin1EDA.Ejercicio5;

public interface ComparaNombre {
	
	public default int compare(Mensaje m1, Mensaje m2)  {
		int resultado=0;
		if(m1==null) {
			resultado=-1;
		}else if(m2==null) {
			resultado=1;
		}else if(m1==null && m2==null) {
			resultado=0;
		}else {
			resultado= m1.getRemitente().getUsername().compareTo(m2.getRemitente().getUsername());
		}

		return resultado;
	}
}
