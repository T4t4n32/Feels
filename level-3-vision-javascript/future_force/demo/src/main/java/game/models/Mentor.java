package game.models;

public class Mentor {

    private String nombre;
    private String titulo;
    private String descripcion;

    public Mentor(String nombre, String titulo, String descripcion) {
        this.nombre = nombre;
        this.titulo = titulo;
        this.descripcion = descripcion;
    }

    public String getNombre() {
        return nombre;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getDescripcion() {
        return descripcion;
    }
}
