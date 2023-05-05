package main.java.euro.model;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class Historial {
	
	private Map<LocalDate,Combinacion> sorteos;
	
	public Historial() {
		super();
		sorteos= new HashMap<>();
	}
	
	public boolean addSorteo(LocalDate fecha, Combinacion c1) throws CombinacionException {
		boolean entra=false;
		if(fecha!=null && c1!=null) {
			sorteos.put(fecha, c1);
			entra=true;
		}else {
			throw new CombinacionException();
		}
		return entra;
	}
	
	public boolean adSorteo(int dia, int mes , int ayo, Combinacion c1)  throws CombinacionException {
		boolean entra=false;
		if(c1!=null && LocalDate.of(ayo, mes, dia)!=null) {
			sorteos.put(LocalDate.of(ayo, mes, dia), c1);
			entra=true;
		}else {
			throw new CombinacionException();
		}
		return entra;
	}
	
	public boolean actualizarSorteo(int dia, int mes , int ayo, Combinacion c1) throws CombinacionException {
		boolean actualizar=false;
		if(sorteos.containsKey(LocalDate.of(ayo, mes, dia))) {
			sorteos.replace(LocalDate.of(ayo, mes, dia), c1);
			actualizar=true;
		}else {
			throw new CombinacionException();
		}
		return actualizar;
	}
	
	public boolean actualizarSorteo(LocalDate fecha, Combinacion c1) throws CombinacionException {
		boolean actualizar=false;
		if(sorteos.containsKey(fecha)) {
			sorteos.replace(fecha, c1);
			actualizar=true;
		}else {
			throw new CombinacionException();
		}
		return actualizar;
	}
	
	public boolean borrarSorteo(LocalDate fecha, Combinacion c1) throws CombinacionException {
		boolean borrar=false;
		if(sorteos.containsKey(fecha)) {
			sorteos.remove(fecha);
			borrar=true;
		}else {
			throw new CombinacionException();
		}
		return borrar;
	}
	
	public List<String> listarSorteoDesdeFecha(LocalDate fecha){
		List<String> lista = new ArrayList<String>();
		if(sorteos.containsKey(fecha)) {
			for(LocalDate e : sorteos.keySet()) {
				if(e.isAfter(fecha)) {
					lista.add(e.toString()+": "+sorteos.get(e).toString());
				}
			}
		}
		return lista;
	}
	
	public List<String> mostrarHistorico(){
		List<String> lista = new ArrayList<String>();
		for(LocalDate e : sorteos.keySet()) {
			lista.add(e.toString()+sorteos.get(e));
		}
		return lista;
	}
	
	public Map<String,Integer> comprobarAciertos(LocalDate fecha, Combinacion c1) throws HistorialExcepcion{
		Map<String, Integer> aciertos=new HashMap<String, Integer>();
		if(sorteos.containsKey(fecha)) {
			aciertos.put("En la fecha: "+fecha.toString()+" el numero premiado es: "+sorteos.get(fecha)+", numero que quiere combrobar es: "+c1, sorteos.get(fecha).comprobarCombinacion(c1));
		}else {
			throw new HistorialExcepcion();
		}
		return aciertos;
	}
	
	public Map<Integer, Integer> agruparPorRepeticionNumeros() {
		List<Integer> numeros = new ArrayList<>();
		for(LocalDate e : sorteos.keySet()) {
			numeros.addAll(sorteos.get(e).getNumeros());
		}
		Map<Integer, Integer> m1 =new HashMap<>();
		Iterator<Integer> it = numeros.iterator();
		while(it.hasNext()) {
			Integer Integer = it.next();
			if(!m1.containsKey(Integer)) {
				m1.put(Integer, 1);
			}m1.put(Integer, m1.get(Integer)+1);
		}
		
		return m1;
	}
	
	public Integer mayorRepeticion() {
		Integer numero=-1;
		Map<Integer, Integer> tmp = agruparPorRepeticionNumeros();
		for(Integer e : tmp.keySet()) {
			if(tmp.get(e)>numero) {
				numero=tmp.get(e);
			}
		}
		
		return numero;
	}
	
	public String numerosMasRepetidos() {
		StringBuilder mensaje = new StringBuilder();
		Map<Integer, Integer> tmp = agruparPorRepeticionNumeros();
		Integer mayor = mayorRepeticion();
		for(Integer e : tmp.keySet()) {
			if(tmp.get(e).equals(mayor)) {
				mensaje.append(e+"   ");
			}
		}
		return "Los numeros con mayor repeticion son:\n"+ mensaje.toString() +"\n con un total de: "+mayor+" repeticiones";
	}
	
	public Integer repeticionMenor() {
		Integer numero=mayorRepeticion();
		Map<Integer, Integer> tmp = agruparPorRepeticionNumeros();
		for(Integer e : tmp.keySet()) {
			if(tmp.get(e)<numero) {
				numero=tmp.get(e);
			}
		}
		
		return numero;
	}
	
	public String numerosMenosRepetidos() {
		StringBuilder mensaje = new StringBuilder();
		Map<Integer, Integer> tmp = agruparPorRepeticionNumeros();
		Integer menor = repeticionMenor();
		for(Integer n : tmp.keySet()) {
			if(tmp.get(n).equals(menor)) {
				mensaje.append(n+"   ");
			}
		}
		return "Los numeros con menor repeticion son: \n"+mensaje.toString()+"\n con un total de: "+menor+ " repeticiones";
	}
	
	public Map<Integer, Integer> agruparPorRepeticionEstrellas() {
		List<Integer> estrellas = new ArrayList<>();
		for(LocalDate k : sorteos.keySet()) {
			estrellas.addAll(sorteos.get(k).getEstrellas());
		}
		Map<Integer, Integer> tmp =new HashMap<>();
		Iterator<Integer> it = estrellas.iterator();
		while(it.hasNext()) {
			Integer Integer = it.next();
			if(!tmp.containsKey(Integer)) {
				tmp.put(Integer, 1);
			}tmp.put(Integer, tmp.get(Integer)+1);
		}
		
		return tmp;
	}
	
	public Integer mayorRepeticionEstrellas() {
		Integer numero=-1;
		Map<Integer, Integer> tmp = agruparPorRepeticionEstrellas();
		for(Integer e : tmp.keySet()) {
			if(tmp.get(e)>numero) {
				numero=tmp.get(e);
			}
		}
		
		return numero;
	}
	
	public String estrellasMasRepetidas() {
		StringBuilder mensaje = new StringBuilder();;
		Map<Integer, Integer> tmp = agruparPorRepeticionEstrellas();
		Integer mayor = mayorRepeticionEstrellas();
		for(Integer n : tmp.keySet()) {
			if(tmp.get(n).equals(mayor)) {
				mensaje.append(n+"   ");
			}
		}
		return "Las estrellas que mas se repiten son: \n"+ mensaje.toString() + "\n con un total de: "+mayor+" repeticiones";
	}
	
	public Integer menorRepeticionEstrellas() {
		Integer numero=mayorRepeticionEstrellas();
		Map<Integer, Integer> tmp = agruparPorRepeticionEstrellas();
		for(Integer n : tmp.keySet()) {
			if(tmp.get(n)<numero) {
				numero=tmp.get(n);
			}
		}
		
		return numero;
	}
	
	public String estrellasMenosRepetidas() {
		StringBuilder mensaje = new StringBuilder();;
		Map<Integer, Integer> tmp = agruparPorRepeticionEstrellas();
		Integer mayor = menorRepeticionEstrellas();
		for(Integer n : tmp.keySet()) {
			if(tmp.get(n).equals(mayor)) {
				mensaje.append(n+"   ");
			}
		}
		return "Las estrellas que menos repiten son: \n"+mensaje.toString()+"\n con un total de: "+mayor+" repeticiones";
	}
	
	public int maximoAciertosPosibles(Combinacion c2) {
		int aciertos =-1;
		List<Combinacion> tmp =new ArrayList<>();
		for(LocalDate e : sorteos.keySet()) {
			tmp.add(sorteos.get(e));
		}
		Iterator<Combinacion> it = tmp.iterator();
		while(it.hasNext()) {
			Combinacion tmpC = it.next();
			if(tmpC.comprobarCombinacion(c2)>aciertos) {
				aciertos=tmpC.comprobarCombinacion(c2);
			}
		}
		
		return aciertos;
	}
	
	public String mayorSecuenciaDeNumerosConsecutivos(){
		int mayorRepeticion = 0;
		String mensaje = null;
		for(LocalDate e : sorteos.keySet()) {
			if(sorteos.get(e).numerosConsecutivos()>mayorRepeticion) {
				mayorRepeticion=sorteos.get(e).numerosConsecutivos();
				mensaje=sorteos.get(e).getNumeros()+" => "+mayorRepeticion;
			}
			
				
		}
		return mensaje.substring(8,20)+mensaje.substring(40);
		
	}
}
