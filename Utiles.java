import java.io.BufferedReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.Scanner;

public class Utiles {

    public static String escanerTexto() {//llamarlo asi String miTexto = Utiles.escanerTexto();lo mismo con la de abajo
        Scanner escaner =new Scanner(System.in);
        String texto=escaner.nextLine();
        return texto;
    }

    public static int escanerNumero() {
        Scanner escaner = new Scanner(System.in);
        int numero = Integer.parseInt(escaner.nextLine());
        return numero; 
    }
    public static void LeerArchivo(){
        try(BufferedReader entrada=Files.newBufferedReader(ruta, StandardCharsets.UTF_8)){//Aqui esta el reader
                String lineas;
                while ((lineas=entrada.readLine())!=null){//vemos si las lineas si esta en blanco paramos de leer
                    System.out.println(lineas);
                }
            }catch(IOException e){
                System.err.println("No se pudo leer el archivo");
            }
    }
}
