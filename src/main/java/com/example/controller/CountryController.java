/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.controller;

import com.example.model.Country;
import com.example.service.CountryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 *
 * @author Pali
 */
@Controller
@RequestMapping("/view_Country")
public class CountryController {

    @Autowired
    private CountryService countryService;
    
    @GetMapping()
    public String viewCountry(Model model) {  
        model.addAttribute("listCountry", countryService.getAllCountry());
        return "view_Country";
    }  

    @GetMapping("/showNewCountryForm")
    public String showNewCountryForm(Model model) {
        // create model attribute to bind form data
        Country country = new Country();
        model.addAttribute("country", country);
        return "new_Country";
    }
     @PostMapping("/saveCountry")
    public String saveCountry(@ModelAttribute("country") Country country) {
        // save employee to database
        countryService.saveCountry(country);
        return "redirect:/view_Country";
    }
}
