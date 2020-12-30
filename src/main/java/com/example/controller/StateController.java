/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.controller;

import com.example.model.State;
import com.example.service.CountryService;
import com.example.service.Stateservice;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

/**
 *
 * @author Pali
 */
@Controller
public class StateController {

    @Autowired
    private Stateservice stateservice;

    @Autowired
    private CountryService countryService;

    @GetMapping("/dashboard/view_State")
    public String viewState(Model model) {
        model.addAttribute("listState", stateservice.getAllState());
        return "view_State";
    }

    @GetMapping("/dashboard/view_State/showNewStateForm")
    public String showNewStateForm(Model model) {
        // create model attribute to bind form data
        State state = new State();
        model.addAttribute("state", state);
        model.addAttribute("listCountry", countryService.getAllCountry());
        return "new_State";
    }

    @PostMapping("/dashboard/view_State/saveState")
    public String saveState(@ModelAttribute("state") State state) {
        // save employee to database
        stateservice.saveState(state);
        return "redirect:/dashboard/view_State";
    }

     @GetMapping("/dashboard/view_State/update_State/{id}")
    public String showFormforUpdate(@PathVariable(value = "id") long id, Model model) {
        // get employee from the service
        State state = stateservice.getStateById(id);

        //set employee as a model attribute to pre-populate the form
        model.addAttribute("state", state);
        model.addAttribute("listCountry", countryService.getAllCountry());
        return "update_State";
    }
    
    @GetMapping("/dashboard/view_State/delete_State/{id}")
    public String deleteState(@PathVariable(value = "id") long id) {
        // call delete employee method
        this.stateservice.deleteStateById(id);
        return "redirect:/dashboard/view_State";
    }

}
