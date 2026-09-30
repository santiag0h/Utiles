
import java.io.BufferedReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Scanner;

public class Utiles {

    public static String escanerTexto() {//llamarlo asi String miTexto = Utiles.escanerTexto();lo mismo con la de abajo
        Scanner escaner =new Scanner(System.in);
        String texto=escaner.nextLine();
        escaner.close();
        return texto;
    }

    public static int escanerNumero() {
        Scanner escaner = new Scanner(System.in);
        int numero = Integer.parseInt(escaner.nextLine());
        escaner.close();
        return numero; 
    }
     public static void LeerArchivo(Path ruta){//posiblemente se deba de cambiar
         try(BufferedReader entrada=Files.newBufferedReader(ruta, StandardCharsets.UTF_8)){
                String lineas;
                 while ((lineas=entrada.readLine())!=null){
                     System.out.println(lineas);
                 }
             }catch(IOException e){
                 System.err.println("No se pudo leer el archivo");
             }
     }
}