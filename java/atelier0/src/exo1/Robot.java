package exo1;

public class Robot {
    public final static int NORD = 1;
    public final static int EST = 2;
    public final static int SUD = 3;
    public final static int OUEST = 4;
    static int nbRobot = 0;
    String reference;
    String name;
    int x;
    int y;
    int orientation;

    public Robot(String name, int x, int y, int orientation) {
        this.reference = "ROB" + nbRobot;
        this.name = name;
        this.x = x;
        this.y = y;
        this.setOrientation(orientation);
        nbRobot++;
    }

    public Robot(String name) {
        this(name, 0, 0, NORD);
    }

    public String toString() {
        return "Je suis " + this.reference + " alias " + this.name + ". Je me situe en (" + this.x + ", " + this.y + ") " + this.printOrientation(this.orientation);
    }

    public void afficheToi() {
        System.out.println("Je suis " + this.reference + " alias " + this.name + ". Je me situe en (" + this.x + ", " + this.y + ") " + this.printOrientation(this.orientation));
    }

    public void setOrientation(int orientation) {
        if (orientation >= NORD && orientation <= OUEST) {
            this.orientation = orientation;
        }
    }

    public String printOrientation(int orientation) {
        return switch (orientation) {
            case EST -> "EST";
            case SUD -> "SUD";
            case OUEST -> "OUEST";
            default -> "NORD";
        };
    }

    public void deplacer() {
        if (this.orientation == NORD) {
            this.y++;
        } else if (this.orientation == EST) {
            this.x++;
        } else if (this.orientation == SUD) {
            this.y--;
            if (this.y < 0) {
                this.y = 0;
            }
        } else if (this.orientation == OUEST) {
            this.x--;
            if (this.x < 0) {
                this.x = 0;
            }
        }
    }
}
