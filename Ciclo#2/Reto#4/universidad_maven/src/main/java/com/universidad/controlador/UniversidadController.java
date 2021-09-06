package com.universidad.controlador;

import com.universidad.modelo.Universidad;

public class UniversidadController {
    /*******
     * Atributos
     */
    
    public Universidad[] universidades;

    /****************
   * Contructor
   **************/
  public UniversidadController(){
      this.universidades = new Universidad[5];
  }

  /************************
   * Getters and Setters
   * **********************/
  public Universidad[] getUniversidades() {
      return universidades;
  }

  public Universidad getUniversidad(int pos){
      return this.universidades[pos];
  }

  //public Universidad getUniversidad(String nit){
      //Recorrer el arreglo
      //for(int i = 0; i < this.universidades.length; i++){
          //if(this.universidades[i] != null){
              //this.universidades[i].get
          //}
      //}
  //}

  public void setUniversidades(Universidad[] universidades) {
      this.universidades = universidades;
  }


  /************************
   * Sobrecarga de métodos
   * *********************/

  //Método que me permite crear una universidad
  public void crear_universidad(String nombre, String direccion, String nit){
      this.universidades[0] = new Universidad(nombre, direccion, nit);
  }

  public void crear_universidad(String nombre, String direccion){
      this.universidades[0] = new Universidad(nombre, direccion);
  }

  public void crear_universidad(){
      this.universidades[0] = new Universidad();
  }
}
