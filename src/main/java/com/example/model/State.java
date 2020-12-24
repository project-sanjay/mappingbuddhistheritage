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
@Table(name = "State")
public class State {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id_state;

    @Column(nullable = false, unique = true)
    private String statename;

    @ManyToOne
    @JoinColumn(name = "id_country")
    private Country country;

    /**
     * @return the id_state
     */
    public long getId_state() {
        return id_state;
    }

    /**
     * @param id_state the id_state to set
     */
    public void setId_state(long id_state) {
        this.id_state = id_state;
    }

    /**
     * @return the statename
     */
    public String getStatename() {
        return statename;
    }

    /**
     * @param statename the statename to set
     */
    public void setStatename(String statename) {
        this.statename = statename;
    }

    /**
     * @return the country
     */
    public Country getCountry() {
        return country;
    }

    /**
     * @param country the country to set
     */
    public void setCountry(Country country) {
        this.country = country;
    }

}
