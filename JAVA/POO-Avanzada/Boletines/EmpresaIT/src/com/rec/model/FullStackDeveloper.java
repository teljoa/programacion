package com.rec.model;

import java.time.LocalDate;
import java.time.LocalDateTime;

public class FullStackDeveloper extends Candidate {

	public FullStackDeveloper(LocalDate dateOfBirth, LocalDateTime startDate, String dni, String name, String surname,
			ContractType ct, boolean inProject) {
		super(dateOfBirth, startDate, dni, name, surname, ct, inProject);
	}
	
	public double computeWebDesingCost() {
		return 0;
		
	}
	
	public double computeFEMaintenanceCost() {
		return 0;
		
	}
	
	public double createWebAPIAndDBConnectionCost() {
		return 0;
		
	}
	
	public double maintenanceCost() {
		return 0;
		
	}

	@Override
	public double computeGrossSalary() {

		return 0;
	}

}
