package java.model;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class Feria {
	private Set<Caseta> casetas; 
	
	public Feria() {
		this.casetas= new HashSet<>();
	}
	
	public void addCaseta(Caseta caseta) {
		casetas.add(caseta);
	}
	
	public String mostrarCasetasDeUnaCalle(String calle){
		StringBuilder sb = new StringBuilder();
		Iterator<Caseta> it = casetas.iterator();
		while(it.hasNext()) {
			Caseta ct = it.next();
			if(ct.getCalle().toUpperCase().equals(calle.toUpperCase())) {
				sb.append(ct+"\n");
			}
		}
		return sb.toString();
	}
	
	public String mostrarCasetasFamiliares(){
		StringBuilder sb = new StringBuilder();
		Iterator<Caseta> it = casetas.iterator();
		while(it.hasNext()) {
			Caseta ct = it.next();
			if(ct.getClase().equals(Clase.FAMILIAR)) {
				sb.append(ct+"\n");
			}
		}
		return sb.toString();
	}
	
	public String mostrarCasetasTipoDistrito(){
		StringBuilder sb = new StringBuilder();
		Iterator<Caseta> it = casetas.iterator();
		while(it.hasNext()) {
			Caseta ct = it.next();
			if(ct.getClase().equals(Clase.DISTRITO)) {
				sb.append(ct+"\n");
			}
		}
		return sb.toString();
	}
	
	public String mostrarCasetasQueNoSonDistritoNiFamiliar(){
		StringBuilder sb = new StringBuilder();
		Iterator<Caseta> it = casetas.iterator();
		while(it.hasNext()) {
			Caseta ct = it.next();
			if(!ct.getClase().equals(Clase.DISTRITO) && !ct.getClase().equals(Clase.FAMILIAR)) {
				sb.append(ct+"\n");
			}
		}
		return sb.toString();
	}
	
	public String mostrarNumeroCasetasFamiliaresPorCalle() {
		StringBuilder sb = new StringBuilder();
		Map<String, Integer> tmp = new HashMap<>();
		Iterator<Caseta> it = casetas.iterator();
		while(it.hasNext()) {
			Caseta ct = it.next();
			if(ct.getClase().equals(Clase.FAMILIAR)) {
				if(!tmp.containsKey(ct.getCalle())) {
					tmp.put(ct.getCalle(), 0);
				}tmp.put(ct.getCalle(), tmp.get(ct.getCalle())+1);
			}
		}
		for(String c : tmp.keySet()) {
			sb.append("Calle "+c+" "+tmp.get(c)+" caseta/as familiares\n"); 
		}
		return sb.toString();
	}
	
	public String mostrarNumeroCasetasTipoDistritoPorCalle() {
		StringBuilder sb = new StringBuilder();
		Map<String, Integer> tmp = new HashMap<>();
		Iterator<Caseta> it = casetas.iterator();
		while(it.hasNext()) {
			Caseta ct = it.next();
			if(ct.getClase().equals(Clase.DISTRITO)) {
				if(!tmp.containsKey(ct.getCalle())) {
					tmp.put(ct.getCalle(), 0);
				}tmp.put(ct.getCalle(), tmp.get(ct.getCalle())+1);
			}
		}
		for(String c : tmp.keySet()) {
			sb.append("Calle "+c+" "+tmp.get(c)+" caseta/as tipo distrito\n"); 
		}
		return sb.toString();
	}
	
	
	public void borrarCaseta(String calle, int numero) {
		boolean existe =false;
		Iterator<Caseta> it = casetas.iterator();
		while(it.hasNext() && !existe) {
			Caseta ct = it.next();
			if(ct.getCalle().toUpperCase().equals(calle.toUpperCase()) && ct.getNumero()==numero) {
				existe=true;
				casetas.remove(ct);
			}
		}
		if(existe) {
			for(Caseta c : casetas) {
				if(c.getNumero()>numero) {
					int nuevo = c.getNumero()-c.getModulos();
					c.setNumero(nuevo);	
				}
			}
		}
	}
		
	public void menu(int opcion, String calle, int numero) {
		
		while(opcion<8) {
			System.out.println("Opciones:");
			System.out.println("1. Mostrar todas las casetas existentes en una calle.");
			System.out.println("2. Mostrar todas las casetas de tipo familiar.");
			System.out.println("3. Mostrar todas las casetas de tipo Distrito.");
			System.out.println("4. Mostrar todas las casetas que no sean ni familiares ni distritos.");
			System.out.println("5. Mostrar para cada una de las calles del recinto ferial el número de casetas de tipo familiar que existen.");
			System.out.println("6. Mostrar para cada una de las calles del recinto ferial el número de casetas de tipo Distrito que existen.");
			System.out.println("7. Eliminar una caseta. Si se elimina una caseta se considerará que el resto de las casetas"
							  +"posteriores se desplazan, es decir si borro la caseta 5 de una calle, todas las casetas a partir"
							  +"del número 5 deberán descender un número si la caseta borrada tiene un módulo, dos si tiene"
							  +"dos módulos, y así sucesivamente. Se pedirá el nombre de la calle y el número. Si no existe"
							  +"se deberá mostrar un mensaje de error.");
			System.out.println("8. Salir.");
			
			switch (opcion) {
			case 1:
				mostrarCasetasDeUnaCalle(calle);
			case 2:
				mostrarCasetasFamiliares();
			case 3:
				mostrarCasetasTipoDistrito();
			case 4:
				mostrarCasetasQueNoSonDistritoNiFamiliar();
			case 5:
				mostrarNumeroCasetasFamiliaresPorCalle();
			case 6:
				mostrarNumeroCasetasTipoDistritoPorCalle();
			case 7:
				borrarCaseta(calle, numero);
			}
			
		}
		
	}
}
