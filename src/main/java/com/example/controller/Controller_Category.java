/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.controller;

import com.example.model.Category;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

/**
 *
 * @author Pali
 */
@Controller
public class Controller_Category {

    @GetMapping("/dashboard/view_Category")
    public String viewCategory(Model model) {

        return "view_Category";
    }

    @GetMapping("/dashboard/view_Category/showNewCategoryForm")
    public String showNewCountryForm(Model model) {
        // create model attribute to bind form data
        Category Category = new Category();
        model.addAttribute("category", Category);
        return "new_Category";
    }
}
