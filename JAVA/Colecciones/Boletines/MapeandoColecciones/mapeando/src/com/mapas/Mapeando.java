package com.mapas;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.Random;
import java.util.TreeMap;
import java.util.LinkedHashMap;
import com.mapas.*;

public class Mapeando {

	
	
	
	/**
	 * Recibe una colección de personas y las agrupa por género
	 * @param personas
	 * @return Mapa con la colección de personas clasificadas por género
	 */
	public Map<Genero, Persona> mapearPersonasPorGenero(Collection<Persona> personas) {
		Genero g = null;
		Map<Genero, Persona> pg = new TreeMap<Genero, Persona>();
		pg.put(g, (Persona) personas);
		return pg;
	}
	
	
	/**
	 * Recibe una colección de números y cuenta cuantas ocurrencias hay de cada uno de ellos
	 * creando un mapa en el que aparece cada número junto a su frecuencia de aparición
	 * @param numeros
	 * @return Tabla de frecuencias de los números facilitados
	 */
	public Map<Integer, Integer> contarNumeros(Collection<Integer> numeros){
		Map<Integer, Integer> ocurrencias= new LinkedHashMap<Integer, Integer>();
		for (int n : numeros) {
            if (ocurrencias.containsKey(n)) {
            	ocurrencias.put(n, ocurrencias.get(n) + 1);
            } else {
            	ocurrencias.put(n, 1);
            }
        }
        
        for (Map.Entry<Integer, Integer> ocurrencia : ocurrencias.entrySet()) {
            System.out.printf("%d -> %d%n", ocurrencia.getKey(), ocurrencia.getValue());
        }
		return ocurrencias;
	}
	
	
	
	/**
	 * Genera una lista de números aleatorios entre 0 y 20 del tamaño indicado
	 * @param size tamaño de la lista
	 * @return lista de size números aleatorios
	 */
	public static Collection<Integer> generarNumerosAleatorios(int size){
		List<Integer> numeros = new ArrayList<>() {{
			for(int i=0; i<size; i++) {
				add(new Random().nextInt(0, 20));
			}
		}};
		
		return numeros;
	}
}
