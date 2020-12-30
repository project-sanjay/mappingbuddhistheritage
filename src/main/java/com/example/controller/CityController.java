/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.controller;

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
public class CityController {

    @GetMapping("/dashboard/view_City")
    public String viewCity() {
        return "view_City";
    }

    @GetMapping("/dashboard/view_City/showNewCityForm")
    public String showNewStateForm(Model model) {
        // create model attribute to bind form data
        return "new_City";
    }
}
