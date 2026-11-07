/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.odev1;

/**
 *
 * @author Muhammet Fatih
 */
public class  ödev1 
{ 
    private String model;
    private int yil;
    private double fiyat;
    
    public static final int KAPASITE = 5;
    
    // parametresiz yapıcı
    public Audi() {
        model = "";
        yil = 0;
        fiyat = 0.0;
    }
    
    // parametreli yapıcı
    public Audi(String model, int yil, double fiyat) {
        this.model = model;
        this.yil = yil;
        this.fiyat = fiyat;
    }
    
    // getter ve setter metodları
    public String getModel() {
        return model;
    }
    
    public void setModel(String model) {
        this.model = model;
    }
    
    public int getYil() {
        return yil;
    }
    
    public void setYil(int yil) {
        this.yil = yil;
    }
    
    public double getFiyat() {
        return fiyat;
    }
    
    public void setFiyat(double fiyat) {
        this.fiyat = fiyat;
    }
 
}
