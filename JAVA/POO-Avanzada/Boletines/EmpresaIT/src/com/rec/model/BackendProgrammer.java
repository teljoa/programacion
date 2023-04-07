package com.rec.model;

import java.time.LocalDate;
import java.time.LocalDateTime;

public class BackendProgrammer extends Candidate {

	public BackendProgrammer(LocalDate dateOfBirth, LocalDateTime startDate,String dni, String name, String surname,
			ContractType ct, boolean inProject) {
		super(dateOfBirth, startDate, dni,name, surname, ct, inProject);
		
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
