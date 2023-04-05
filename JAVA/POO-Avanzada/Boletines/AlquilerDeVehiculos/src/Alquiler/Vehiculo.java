package Alquiler;

import java.util.Objects;

public class Vehiculo {
	private String matricula;
	private Gama gama;
	private TipoVehiculo tipo;
	private COMBUSTIBLE combustible;
	private double plazas;
	private double PMA;
	private double diasAlquiler;
	
	public Vehiculo(String matricula, Gama gama, TipoVehiculo tipo, COMBUSTIBLE combustible, double plazas, double pMA,
			double diasAlquiler) {
		super();
		this.matricula = matricula;
		this.gama = gama;
		this.tipo = tipo;
		this.combustible = combustible;
		this.plazas = plazas;
		PMA = pMA;
		this.diasAlquiler = diasAlquiler;
	}
	
	public double CalcularAlquiler() {
		double precio=0;
		if(!this.matricula.equals(matricula)) {
			if(tipo.equals(tipo.COCHE)) {
				if(combustible.equals(combustible.GASOLINA)) {
					precio=(diasAlquiler*combustible.getPrecio())+gama.getPrecio();
				}if(tipo.equals(tipo.FURGONETA)){
					precio=diasAlquiler*((0.5*PMA)+gama.getPrecio());
				}if(tipo.equals(tipo.MICROBUS)) {
					precio=diasAlquiler*((5*plazas)+gama.getPrecio());
				}
			}
		}
		
		return precio;
	}
	
	public boolean DarAlta() {
		boolean alta=false;
		if(!this.matricula.equals(matricula)) {
			alta=true;
		}
		return alta;
	}

	public String getMatricula() {
		return matricula;
	}

	public void setMatricula(String matricula) {
		this.matricula = matricula;
	}

	public Gama getGama() {
		return gama;
	}

	public void setGama(Gama gama) {
		this.gama = gama;
	}

	public TipoVehiculo getTipo() {
		return tipo;
	}

	public void setTipo(TipoVehiculo tipo) {
		this.tipo = tipo;
	}

	public COMBUSTIBLE getCombustible() {
		return combustible;
	}

	public void setCombustible(COMBUSTIBLE combustible) {
		this.combustible = combustible;
	}

	public double getPlazas() {
		return plazas;
	}

	public void setPlazas(double plazas) {
		this.plazas = plazas;
	}

	public double getPMA() {
		return PMA;
	}

	public void setPMA(double pMA) {
		PMA = pMA;
	}

	public double getDiasAlquiler() {
		return diasAlquiler;
	}

	public void setDiasAlquiler(double diasAlquiler) {
		this.diasAlquiler = diasAlquiler;
	}

	@Override
	public int hashCode() {
		return Objects.hash(matricula);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Vehiculo other = (Vehiculo) obj;
		return Objects.equals(matricula, other.matricula);
	}

	@Override
	public String toString() {
		return "Vehiculo [matricula=" + matricula + ", diasAlquiler=" + diasAlquiler + ", CalcularAlquiler()="
				+ CalcularAlquiler() + "]";
	}
}
