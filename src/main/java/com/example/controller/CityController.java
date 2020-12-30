/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.controller;

import com.example.model.City;
import com.example.service.Stateservice;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import com.example.service.Service_City;

/**
 *
 * @author Pali
 */
@Controller
public class CityController {

    @Autowired
    private Service_City Service_City;

    @Autowired
    private Stateservice stateservice;

    @GetMapping("/dashboard/view_City")
    public String viewCity(Model model) {
        model.addAttribute("listCity", Service_City.getAllCity());
        return "view_City";
    }

    @GetMapping("/dashboard/view_City/showNewCityForm")
    public String showNewStateForm(Model model) {
        // create model attribute to bind form data
        City city = new City();
        model.addAttribute("city", city);
        model.addAttribute("listState", stateservice.getAllState());
        return "new_City";
    }

    @PostMapping("/dashboard/view_City/saveCity")
    public String saveState(@ModelAttribute("city") City city) {
        // save employee to database
        Service_City.saveCity(city);
        return "redirect:/dashboard/view_City";
    }

    @GetMapping("/dashboard/view_State/update_State/{id}")
    public String showFormforUpdate(@PathVariable(value = "id") long id, Model model) {
        // get employee from the service
        City city = Service_City.getCityById(id);
        model.addAttribute("city", city);
        model.addAttribute("listState", stateservice.getAllState());
        return "update_State";
    }

    @GetMapping("/dashboard/view_City/delete_City/{id}")
    public String deleteState(@PathVariable(value = "id") long id) {
        // call delete employee method
        this.Service_City.deleteCityById(id);
        return "redirect:/dashboard/view_City";
    }
}
