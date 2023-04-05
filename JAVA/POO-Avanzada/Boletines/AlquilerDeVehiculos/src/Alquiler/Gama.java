package Alquiler;

public enum Gama {
	ALTA(50.00), MEDIA(40.00), BAJA(30.00);
	private double precio;
	
	Gama(double v){
		this.precio=precio;
	}
	
	public double getPrecio() {
		return this.precio;
	}
}
