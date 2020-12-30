/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.service;

import com.example.model.City;
import com.example.repository.CityRepository;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;

/**
 *
 * @author Pali
 */
@Service
public class CityServiceImpl implements Service_City {

    @Autowired
    CityRepository cityRepository;
    
    @Override
    public void saveCity(City City) {
        this.cityRepository.save(City);
    }

    @Override
    public List<City> getAllCity() {
        return cityRepository.findAll();
    }

    @Override
    public void deleteCityById(long id) {
        this.cityRepository.deleteById(id);
    }
   
}
