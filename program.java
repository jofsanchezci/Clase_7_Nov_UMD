import java.util.Scanner;

public class program{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Ingrese un número entero positivo: ");
        long numero = scanner.nextLong();
        
        if (numero < 0) {
            System.out.println("El factorial no está definido para números negativos.");
        } else {
            long n = 1;
            
            for (long i = 1; i <= numero; i++) {
                n *= i; 
            }
            
            System.out.println("El factorial de " + numero + " es " + n);
        }
        
        scanner.close();
    }
}