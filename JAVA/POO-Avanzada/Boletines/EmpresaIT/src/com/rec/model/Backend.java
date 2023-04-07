package com.rec.model;

public interface Backend {
	public static final double WEB_DB_COST=2200.00;
	public static final double BE_MAINTENANCE_COST=500.00;
	
	public double createWebAPIAndDBConnectionCost();
	
	public double maintenanceCost();
}
