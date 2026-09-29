import java.util.Scanner;

public class Utiles {
@SuppressWarnings("resource")
    public static String escanerTexto() {//llamarlo asi String miTexto = Utiles.escanerTexto();lo mismo con la de abajo
        Scanner escaner =new Scanner(System.in);
        String texto=escaner.nextLine();
        return texto;
    }
@SuppressWarnings("resource")
    public static int escanerNumero() {
        Scanner escaner = new Scanner(System.in);
        int numero = Integer.parseInt(escaner.nextLine());
        return numero; 
    }
}
