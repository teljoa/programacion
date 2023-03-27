package cadenaUtil;
import static org.junit.jupiter.api.Assertions.*;

class Test {

	
	void testtomayscula() {
		CadenaUtil cadena=new CadenaUtil("Antonio");
		
		//Comprueba que la cadena se almacena y muestra en mayuscula.
		assertEquals("Antonio".toUpperCase(),cadena.toMayuscula());
		//Comprueba que la cadena introducida se almacena en mayusculas y no contiene minusculas.
		assertNotEquals("Antonio".toUpperCase(),cadena.toMayuscula());
		//Comprueba que se almacena la cadena.
		assertTrue(!cadena.toMayuscula().isBlank());
		assertTrue(cadena.toMayuscula().isEmpty());
		
	}
	
	void testtominuscula() {
		CadenaUtil cadena=new CadenaUtil("Antonio");
		
		//Comprueba que la cadena se almacena y muestra en minuscula.
		assertEquals("Antonio".toLowerCase(),cadena.toMinuscula());
		//Comprueba que la cadena introducida se almacena en miniscula y no contiene minusculas.
		assertNotEquals("Antonio".toLowerCase(),cadena.toMinuscula());
		//Comprueba que se almacena la cadena.
		assertTrue(!cadena.toMinuscula().isBlank());
		assertTrue(cadena.toMinuscula().isEmpty());
		
	}
	
	void testesmayscula() {
		CadenaUtil cadena=new CadenaUtil("ANTONIO");
		
		assert("ANTONIO".equals(cadena.esMayuscula()));
	}
	
	void testesminuscula() {
		CadenaUtil cadena=new CadenaUtil("antonio");
		
		assert("antonio".equals(cadena.esMinuscula()));
	}
	
	void testescapicua() {
		CadenaUtil cadena=new CadenaUtil("12344321");
		
		assert("12344321".equals(cadena.esCapicua()));
	}
	
	void testespalimdromo() {
		CadenaUtil cadena=new CadenaUtil("aaa");
		
		assert("aaa".equals(cadena.esPalindromo()));
	}
	
	void testesdecimal() {
		CadenaUtil cadena=new CadenaUtil("1,0");
		
		assert("aaa".equals(cadena.esDecimal()));
	}
	
	void testesentero() {
		CadenaUtil cadena=new CadenaUtil("1,0");
		
		assert("aaa".equals(cadena.esEntero()));
	}
}
