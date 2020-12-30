/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.service;

import com.example.model.City;
import java.util.List;

/**
 *
 * @author Pali
 */
public interface Service_City {

    public void saveCity(City City);

    List<City> getAllCity();

    void deleteCityById(long id);
}
