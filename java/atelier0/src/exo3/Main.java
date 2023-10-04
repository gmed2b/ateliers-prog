package exo3;
import java.text.DecimalFormat;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        System.out.println("PI : " + Math.PI);
        DecimalFormat df = new DecimalFormat("#.##");
        System.out.println("Nombre réel aléatoire [0.0, 1.0[ : " + df.format(Math.random()));

        Random nbRandom = new Random();
        System.out.println("Nombre entier aléatoire [1, 3] : " + nbRandom.nextInt(1, 4));

        int x1 = 1;
        int x2 = 3;
        System.out.println("max(1, 3) : " + Math.max(x1, x2));

        String n1 = "Bonjour";
        String n2 = "Au revoir";
        System.out.println("Ordre alphabétique : ");
        if (n1.compareTo(n2) > 0) {
            System.out.println("- " + n2);
            System.out.println("- " + n1);
        } else if (n1.compareTo(n2) < 0) {
            System.out.println("- " + n1);
            System.out.println("- " + n2);
        } else {
            System.out.println(n1 + " = " + n2);
        }
    }
}
