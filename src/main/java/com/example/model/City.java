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
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

/**
 *
 * @author Pali
 */
@Entity
@Table(name = "City")
public class City {

    /**
     * @return the id_city
     */
    public long getId_city() {
        return id_city;
    }

    /**
     * @param id_city the id_city to set
     */
    public void setId_city(long id_city) {
        this.id_city = id_city;
    }

    /**
     * @return the cityname
     */
    public String getCityname() {
        return cityname;
    }

    /**
     * @param cityname the cityname to set
     */
    public void setCityname(String cityname) {
        this.cityname = cityname;
    }

    /**
     * @return the state
     */
    public State getState() {
        return state;
    }

    /**
     * @param state the state to set
     */
    public void setState(State state) {
        this.state = state;
    }

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id_city;

    @Column(nullable = false, unique = true)
    private String cityname;

    @ManyToOne
    @JoinColumn(name = "id_State")
    private State state;

}
