/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

/**
 *
 * @author Pali
 */
@Entity
@Table(name="Country")
public class Country {

    /**
     * @return the id_country
     */
    public long getId_country() {
        return id_country;
    }

    /**
     * @param id_country the id_country to set
     */
    public void setId_country(long id_country) {
        this.id_country = id_country;
    }

    /**
     * @return the countryname
     */
    public String getCountryname() {
        return countryname;
    }

    /**
     * @param countryname the countryname to set
     */
    public void setCountryname(String countryname) {
        this.countryname = countryname;
    }

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id_country;
    
    private String countryname;
}
