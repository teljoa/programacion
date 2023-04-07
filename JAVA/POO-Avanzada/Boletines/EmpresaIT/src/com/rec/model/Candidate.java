package com.rec.model;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.Objects;

public abstract class Candidate {
	private LocalDate dateOfBirth;
	private LocalDateTime startDate;
	private String dni;
	private String name;
	private String surname;
	private ContractType ct;
	private boolean inProject;
	
	
	
	public abstract double computeGrossSalary();

	public Candidate(LocalDate dateOfBirth, LocalDateTime startDate,String dni, String name, String surname, ContractType ct,
			boolean inProject) {
		super();
		this.dateOfBirth = dateOfBirth;
		this.startDate = startDate;
		this.setDni(dni);
		this.name = name;
		this.surname = surname;
		this.ct = ct;
		this.inProject = inProject;
	}
	
	public boolean darAlta() {
		boolean alta=false;
		Candidate a = null;
		if(!this.equals(a)) {
			alta=true;
		}
		
		return alta;
	}
	
	public int compareTo() {
		int i=0;
		if(startDate.compareTo(startDate)>0) {
			i=1;
		}else if(startDate.compareTo(startDate)<0) {
			i=-1;
		}else if(startDate.compareTo(startDate)==0) {
			i=0;
		}
		return i;
	}
	
	public double calcularSueldo() {
		double sueldo=0;
			if(ct.equals(ContractType.PARTIAL)) {
				sueldo=sueldo*0.67;
				if(startDate.compareTo(startDate)>0) {
					sueldo=(sueldo*0.05)+sueldo;
				}
			}
		return sueldo;
	}

	public LocalDate getDateOfBirth() {
		return dateOfBirth;
	}

	public void setDateOfBirth(LocalDate dateOfBirth) {
		this.dateOfBirth = dateOfBirth;
	}

	public LocalDateTime getStartDate() {
		return startDate;
	}

	public void setStartDate(LocalDateTime startDate) {
		this.startDate = startDate;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getSurname() {
		return surname;
	}

	public void setSurname(String surname) {
		this.surname = surname;
	}

	public ContractType getCt() {
		return ct;
	}

	public void setCt(ContractType ct) {
		this.ct = ct;
	}

	public boolean isInProject() {
		return inProject;
	}

	public void setInProject(boolean inProject) {
		this.inProject = inProject;
	}
	
	public int compareTo(Candidate i) {
		return 0;
		
	}

	public String getDni() {
		return dni;
	}

	public void setDni(String dni) {
		this.dni = dni;
	}

	@Override
	public int hashCode() {
		return Objects.hash(ct, dateOfBirth, dni, inProject, name, startDate, surname);
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Candidate other = (Candidate) obj;
		return ct == other.ct && Objects.equals(dateOfBirth, other.dateOfBirth) && Objects.equals(dni, other.dni)
				&& inProject == other.inProject && Objects.equals(name, other.name)
				&& Objects.equals(startDate, other.startDate) && Objects.equals(surname, other.surname);
	}

	public String toString(String dni) {
		return "Candidate [dateOfBirth=" + dateOfBirth + ", startDate=" + startDate + ", dni=" + dni + ", name=" + name
				+ ", surname=" + surname + ", ct=" + ct + ", inProject=" + inProject + "]";
	}
}
