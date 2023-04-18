package boletin1EDA.Ejercicio7;

public class Cliente {
	private int numeroCliente;
	private static int siguiente;
	
	
	public Cliente() {
		super();
		this.numeroCliente=++siguiente;
	}

	
	public int getNumeroCliente() {
		return this.numeroCliente;
	}
}
