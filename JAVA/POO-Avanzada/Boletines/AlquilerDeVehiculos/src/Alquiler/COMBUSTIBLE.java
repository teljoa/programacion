package Alquiler;

public enum COMBUSTIBLE {
	GASOLINA(3.50), DIESEL(2.00);
	private double precio;
	
	COMBUSTIBLE(double v){
		this.precio=precio;
	}
	
	public double getPrecio() {
		return this.precio;
	}
}
