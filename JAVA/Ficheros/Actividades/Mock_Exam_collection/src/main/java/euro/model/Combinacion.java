package main.java.euro.model;

import java.util.Collection;
import java.util.Objects;
import java.util.Set;
import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;


public class Combinacion {
	protected static final int VALOR_MINIMO=1;
	protected static final int VALOR_MAXIMO_NUMEROS=50;
	protected static final int VALOR_MAXIMO_ESTRELLAS=12;
	protected static final int TOTAL_NUMEROS=5;
	protected static final int TOTAL_ESTRELLAS=2;
	private Set<Integer> numeros;
	private Set<Integer> estrellas;
	
	public Combinacion(int n1, int n2, int n3, int n4, int n5, int e1, int e2) throws CombinacionException {
		int[] numeros= {n1,n2,n3,n4,n5};
		int[] estrellas= {e1,e2};
		
	}

	public Combinacion(int[] numeros, int[] estrellas) {
		super();
		
	}

	public Collection<Integer> getNumeros() {
		for(int n: numeros) {
			if(n>VALOR_MAXIMO_NUMEROS || n<VALOR_MINIMO) {
				
			}
		}
		return numeros;
		
	}

	public Collection<Integer> getEstrellas() {
		for(int e: estrellas) {
			if(e>VALOR_MAXIMO_ESTRELLAS || e<VALOR_MINIMO) {
				
			}
		}
		return estrellas;
		
	}
	
	public int comprobarCombinacion(Combinacion c1) {
		int naciertosdeN=0;
		int naciertosdeE=0;
		
		Set<Integer> listanumero1 = new HashSet<>();
		Set<Integer> listanumero2 = new HashSet<>();
		Set<Integer> listaestrellas1 = new HashSet<>();
		Set<Integer> listaestrellas2 = new HashSet<>();
			
		for(int n : this.getNumeros()) {
			listanumero1.add(n);
		}
		for(int n : this.getEstrellas()) {
			listaestrellas1.add(n);
		}
		for(int n : c1.getNumeros()) {
			listanumero2.add(n);
		}
		for(int n : c1.getEstrellas()) {
			listaestrellas2.add(n);
		}
		listanumero1.retainAll(listanumero2);
		naciertosdeN=listanumero1.size();
		listanumero1.retainAll(listaestrellas2);
		naciertosdeE=listanumero1.size();
		
		return naciertosdeN+naciertosdeE;
	}

	@Override
	public int hashCode() {
		return Objects.hash(estrellas, numeros);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Combinacion other = (Combinacion) obj;
		return Objects.equals(estrellas, other.estrellas) && Objects.equals(numeros, other.numeros);
	}

	@Override
	public String toString() {
		return "Combinacion [numeros=" + numeros + ", estrellas=" + estrellas + "]";
	}
	
	public boolean numerosCorrectos(int[] numeros, int[]estrellas){
		boolean numeroEstrellasCorrecto = true;
		Set<Integer> tmpEstrellas = new HashSet<>();
		for(int e : estrellas) {
			tmpEstrellas.add(e);
			if(e>VALOR_MAXIMO_ESTRELLAS || e<VALOR_MINIMO) {
				numeroEstrellasCorrecto=false;
			}
		}if(tmpEstrellas.size()!=TOTAL_ESTRELLAS) {
			numeroEstrellasCorrecto=false;
		}
											
		boolean numeroNumerosCorrecto = true;		
		Set<Integer> tmpNumeros = new HashSet<>();
		for(int n : numeros) {
			tmpNumeros.add(n);
			if(n>VALOR_MAXIMO_NUMEROS || n<VALOR_MINIMO) {
				numeroNumerosCorrecto=false;
			}
		}if(tmpNumeros.size()!=TOTAL_NUMEROS) {
			numeroNumerosCorrecto=false;
		}
											
		return numeroEstrellasCorrecto && numeroNumerosCorrecto;
	}
	
	public int numerosConsecutivos() {
		int contador=1;
		boolean stop = true;
		List<Integer> tmp = new ArrayList<>();
		tmp.addAll(numeros);
		for(int i=1; i<5 ; i++) {
			if(tmp.get(i)==tmp.get(i-1)+1 && stop) {
				contador++;
			}else {
				stop=false;
			}
		}
		
		
		return contador;
	}
}
