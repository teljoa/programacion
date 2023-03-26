package parking;
import java.util.Comparator;
public class ComparaMatricula implements Comparator<Vehiculo>{
	@Override
	public int compare(Vehiculo v1, Vehiculo v2) {
		int resultado;
		if(v1==null) {
			resultado =-1;
		}else if(v2==null) {
			resultado = 1;
		}else if(v1==null && v2==null) {
			resultado=0;
		}else {
			resultado=v1.getMatricula().compareTo(v2.getMatricula());
		}
		return resultado;
	}
}
