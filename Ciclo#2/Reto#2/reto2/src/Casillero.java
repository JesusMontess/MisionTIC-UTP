public class Casillero{
    // Constantes
     private static final double PESO = 10.0;
     private static final double TAMANIO = 4.5;
     private static final double PRECIO_BASE = 1000.0;
    // Atributos
     private double peso;
     private double tamanio;
     private double precioBase;
     //Sobrecarga de motodos
    // Constructores
    public Casillero(double peso, double tamanio){
        this.peso = peso;
        this.tamanio = tamanio;
        this.precioBase = PRECIO_BASE;

    }
    public Casillero(double precioBase){
        this.peso = PESO;
        this.tamanio = TAMANIO;
        this.precioBase = precioBase;
    }
    public Casillero(){
        this.peso = PESO;
        this.tamanio = TAMANIO;
        this.precioBase = PRECIO_BASE;
    }
    // Metodos
    public double calcularPrecio(){
    return 0.0;
    }
    // getters/setters de ser necesarios
    public double getPeso(){
        return peso;
    }
    public double getTamanio(){
        return tamanio;    
    }
    public double getPrecioBase(){
        return precioBase;
    }
}
