package com.universidad.modelo;

public class Universidad {
    /**
     * Atributos
     */
    private String nombre;
    private String direccion;
    private String nit;

    /***********
     * Metodos Constructores
     *
     ***********/

     public Universidad(String nombre, String direccion, String nit){
         this.nombre = nombre;
         this.direccion = direccion;
         this.nit = nit;
     }

     public Universidad(String nombre, String direccion){
         this.nombre = nombre;
         this.direccion = direccion;
     }

     public Universidad(){

     }

     /*******
      * Consultores
      *******/

    public String getNombre() {
        return nombre;
    }

    public String getDireccion() {
        return direccion;
    }

    public String getNit() {
        return nit;
    }

    /*******
      * Modificadores
      *******/

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

   

    public void setNit(String nit) {
        this.nit = nit;
    }

    public void crear_facultad(){
        
    }

}
