package exo1;

import java.util.Random;

/**
 * The {@code De} class represents a dice with a specified number of faces.
 * Each dice has a name and can be rolled to produce a random number between 1 and the number of faces.
 */
public class De {
    public static final int NB_FACES_MIN = 3;
    public static final int NB_FACES_MAX = 120;
    public static final int NB_FACES_DEFAUT = 6;
    public static final int BORNE_MIN_DEFAUT = 1;
    private static final Random nbRandom = new Random();
    private static int nbDes = 0;
    private String nom;
    private int nbFaces;

    /**
     * Constructs a dice with the specified number of faces and a name.
     *
     * @param nbFaces the number of faces on the dice
     * @param nom     the name of the dice
     */
    public De(int nbFaces, String nom) {
        nbDes++;
        this.setNbFaces(nbFaces);
        this.setNom(nom);
    }

    /**
     * Constructs a dice with the specified number of faces and a default name.
     *
     * @param nbFaces the number of faces on the dice
     */
    public De(int nbFaces) {
        this(nbFaces, "");
    }

    /**
     * Constructs a dice with a default number of faces and the specified name.
     *
     * @param nom the name of the dice
     */
    public De(String nom) {
        this(NB_FACES_DEFAUT, nom);
    }

    /**
     * Constructs a dice with a default number of faces and a default name.
     */
    public De() {
        this(NB_FACES_DEFAUT, "De");
    }

    /**
     * Prints the total number of dice objects created.
     */
    public static void getNbDes() {
        System.out.println("Nombre de dés : " + nbDes);
    }

    /**
     * Returns a string representation of the dice.
     *
     * @return a string representing the name and number of faces of the dice
     */
    @Override
    public String toString() {
        return "Nom: " + this.getNom() + " - Faces: " + this.getNbFaces();
    }

    /**
     * Compares this dice to the specified object.
     *
     * @param o the object to compare this dice against
     * @return {@code true} if the given object represents a dice equivalent to this dice, {@code false} otherwise
     */
    @Override
    public boolean equals(Object o) {
        if (o instanceof De de) {
            return this.nbFaces == de.nbFaces && this.nom.equals(de.nom);
        } else {
            return false;
        }
    }

    /**
     * Returns the name of this dice.
     *
     * @return the name of this dice
     */
    public String getNom() {
        return this.nom;
    }

    public void setNom(String nom) {
        if (nom.isEmpty()) {
            this.nom = "De n°" + nbDes;
        } else {
            this.nom = nom;
        }
    }

    /**
     * Returns the number of faces on this dice.
     *
     * @return the number of faces on this dice
     */
    public int getNbFaces() {
        return this.nbFaces;
    }

    /**
     * Sets the number of faces on this dice, if it is within the valid range.
     *
     * @param nbFaces the number of faces to set
     */
    public void setNbFaces(int nbFaces) {
        if (nbFaces >= NB_FACES_MIN && nbFaces <= NB_FACES_MAX) {
            this.nbFaces = nbFaces;
        } else {
            this.nbFaces = NB_FACES_DEFAUT;
            System.err.println("(" + this + ") Le nombre de faces doit être compris entre 3 et 120");
        }
    }

    /**
     * Rolls the dice and returns the result.
     *
     * @return a random number between 1 and the number of faces on this dice
     */
    int lancer() {
        return nbRandom.nextInt(BORNE_MIN_DEFAUT, this.nbFaces + 1);
    }

    /**
     * Rolls the dice the specified number of times and returns the highest result.
     *
     * @param nb the number of times to roll the dice
     * @return the highest number rolled
     */
    int lancer(int nb) {
        int best = this.lancer();
        for (int i = 0; i < nb; i++) {
            int lancer = this.lancer();
            if (lancer > best) {
                best = lancer;
            }
        }
        return best;
    }
}

