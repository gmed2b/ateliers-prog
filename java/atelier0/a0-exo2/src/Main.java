import java.text.DecimalFormat;

public class Main {
    public static void main(String[] args) {
        Vecteur3D A = new Vecteur3D(3, 2, 5);
        System.out.println("A = " + A);
        System.out.println("||A|| = " + A.norme());

        Vecteur3D B = new Vecteur3D(1, 2, 3);
        System.out.println("B = " + B);
        System.out.println("||B|| = " + B.norme());

        System.out.println("A + B = " + Vecteur3D.somme(A, B));
        System.out.println("A + B = " + A.somme(B));
        System.out.println("A . B = " + Vecteur3D.produitScalaire(A, B));
        System.out.println("A . B = " + A.produitScalaire(B));
    }
}

class Vecteur3D {
    private double x, y, z;

    public Vecteur3D(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public Vecteur3D() {
        this(0, 0, 0);
    }

    public String toString() {
        return "<" + x + ", " + y + ", " + z + ">";
    }

    public double norme() {
        DecimalFormat df = new DecimalFormat("#.##");
        return Double.parseDouble(df.format(Math.sqrt(x * x + y * y + z * z)));
    }

    public static double produitScalaire(Vecteur3D A, Vecteur3D B) {
        return A.x * B.x + A.y * B.y + A.z * B.z;
    }

    public double produitScalaire(Vecteur3D B) {
        return this.x * B.x + this.y * B.y + this.z * B.z;
    }

    public static Vecteur3D somme(Vecteur3D A, Vecteur3D B) {
        return new Vecteur3D(A.x + B.x, A.y + B.y, A.z + B.z);
    }

    public Vecteur3D somme(Vecteur3D B) {
        return new Vecteur3D(this.x + B.x, this.y + B.y, this.z + B.z);
    }
}