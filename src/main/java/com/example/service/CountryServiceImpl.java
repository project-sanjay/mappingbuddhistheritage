/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.service;

import com.example.model.Country;
import com.example.repository.CountryRepository;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 *
 * @author Pali
 */
@Service
public class CountryServiceImpl implements CountryService {

    @Autowired
    CountryRepository countryRepository;

    @Override
    public void saveCountry(Country country) {
        this.countryRepository.save(country);
    }
     @Override
    public List<Country> getAllCountry() {
        return countryRepository.findAll();
    }

    @Override
    public void deleteCountryById(long id) {
       this.countryRepository.deleteById(id);
    }

}
