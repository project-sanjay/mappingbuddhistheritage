/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.service;

import com.example.model.Country;
import java.util.List;

/**
 *
 * @author Pali
 */
public interface CountryService {

    public void saveCountry(Country country);

    List<Country> getAllCountry();

    void deleteCountryById(long id);
    
    Country getCountryById(long id);
}
