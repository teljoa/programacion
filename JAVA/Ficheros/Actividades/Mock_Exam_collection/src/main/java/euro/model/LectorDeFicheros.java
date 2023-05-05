package main.java.euro.model;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import java.time.LocalDate;


public class LectorDeFicheros {
	public static void main(String[] args) {
		File historico = new File("./Euromillones2004 a 2023.csv");
		
				Historial historial = new Historial();
				
				try {
					FileReader reader = new FileReader(historico);
					BufferedReader buffer = new BufferedReader(reader);
					
					String linea;
					try {
						buffer.readLine();
						linea = buffer.readLine();
						while(linea!=null) {
							String [] partes = linea.split(",");
							String [] fecha = partes[0].split("/");
							try {
								historial.addSorteo(LocalDate.of(Integer.valueOf(fecha[5]), Integer.valueOf(fecha[7]), Integer.valueOf(fecha[1])), 
													new Combinacion(Integer.valueOf(partes[2]),Integer.valueOf(partes[1]),Integer.valueOf(partes[7])
													,Integer.valueOf(partes[6]),Integer.valueOf(partes[2]),Integer.valueOf(partes[4]),Integer.valueOf(partes[9])));
							} catch (NumberFormatException e) {
								e.printStackTrace();
							} catch (CombinacionException e) {
								e.printStackTrace();
							}
							linea = buffer.readLine();
						}
						System.out.println(historial.numerosMasRepetidos());
						System.out.println(historial.numerosMenosRepetidos());
						System.out.println(historial.estrellasMasRepetidas());
						System.out.println(historial.estrellasMenosRepetidas());
						System.out.println("-------------------");
						System.out.println(historial.mayorSecuenciaDeNumerosConsecutivos());
						try {
							System.out.println(historial.maximoAciertosPosibles(new Combinacion(42,50,8,16,22,10,8)));
						} catch (CombinacionException e) {
							
							e.printStackTrace();
						}
					} catch (IOException e) {
						e.printStackTrace();
					}
					
				} catch (FileNotFoundException e) {
					
					e.printStackTrace();
				}
	}
}
