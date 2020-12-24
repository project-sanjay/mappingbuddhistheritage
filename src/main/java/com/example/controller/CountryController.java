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
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

// this is new import here
import com.example.repository.CountryRepository;
import java.util.List;

/**
 *
 * @author Pali
 */
@Controller
public class CountryController {

    @Autowired
    private CountryService countryService;

//    this is new thing 
    @Autowired
    private CountryRepository countryRepository;

    @GetMapping("/dashboard/view_Country")
    public String viewCountry(Model model) {
//        model.addAttribute("listCountry", countryService.getAllCountry());
        List<Country> listCountry = countryRepository.findAll();
        model.addAttribute("listCountry", listCountry);
        return "view_Country";
    }

    @GetMapping("/dashboard/view_Country/showNewCountryForm")
    public String showNewCountryForm(Model model) {
        // create model attribute to bind form data
        Country country = new Country();
        model.addAttribute("country", country);
        return "new_Country";
    }

    @PostMapping("/dashboard/view_Country/saveCountry")
    public String saveCountry(@ModelAttribute("country") Country country) {
        // save employee to database
        countryService.saveCountry(country);
        return "redirect:/dashboard/view_Country";
    }

    @GetMapping("/dashboard/view_Country/update_Country/{id}")
    public String showFormforUpdate(@PathVariable(value = "id") long id, Model model) {
        // get employee from the service
        Country country = countryService.getCountryById(id);

        //set employee as a model attribute to pre-populate the form
        model.addAttribute("country", country);
        return "update_Country";
    }

    @GetMapping("/dashboard/view_Country/delete_Employee/{id}")
    public String deleteCountry(@PathVariable(value = "id") long id) {
        // call delete employee method
        this.countryService.deleteCountryById(id);
        return "redirect:/dashboard/view_Country";
    }
}
