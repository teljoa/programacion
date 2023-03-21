package com.examen;
public class ADNUtilN {
	public static void main(String[]args){
		System.out.println(contarPalabra("ATCGTTCTCTTTGATCGATATCTCG","CGTT"));
		System.out.println(descomprimirADN("A3G2T1C3"));
	}
	public static int contarPalabra(String cadena, String buscar) {
		 int contador = 0;
		 for(int i = 0;i<cadena.length();i++)
			 for(int j=0; j<buscar.length();j++) {
				 if(cadena.charAt(i)==cadena.charAt(j)){
					 contador+=1;
				 }else{
					 contador=0;
				 }
			 }
		return contador;
	}
	public static String descomprimirADN(String cadena) {
		String adndescomrimido ="-";
		
		while(adndescomrimido=="-") {
			String contador="0";
			for(int i=0; i<cadena.length();i++) {
				if(cadena.charAt(i)==cadena.charAt(i)){
					contador+=1;
				}if(cadena.charAt(i)!=cadena.charAt(i)){
					adndescomrimido=cadena.valueOf(i);
				}
				adndescomrimido=cadena.charAt(i)+contador;
			}
		}
		return adndescomrimido;
	}
}
