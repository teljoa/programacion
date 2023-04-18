package boletin1EDA.Ejercicio7;

public interface ComparaNumClienteANDnumCaja{
	
	public default int compare(Caja c1, Caja c2) {
		int resultado;
		if(c1==null) {
			resultado=1;
		}else if(c2==null) {
			resultado=-1;
		}else if(c1==null) {
			resultado=0;
		}else {
			resultado= c1.numeroClientes()-c2.numeroClientes()==0? 
						c1.getNumeroCaja()-c2.getNumeroCaja():
						c1.numeroClientes()-c2.numeroClientes();
		}
		
		return resultado;
	}
}
