/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.controller;

import com.example.model.Category;
import com.example.service.Service_Category;
import java.io.IOException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.util.StringUtils;

/**
 *
 * @author Pali
 */
@Controller
public class Controller_Category {

    @Autowired
    private Service_Category Service_Category;

    @GetMapping("/dashboard/view_Category")
    public String viewCategory(Model model) {

        return "view_Category";
    }

    @GetMapping("/dashboard/view_Category/showNewCategoryForm")
    public String showNewCategoryForm(Model model) {
        // create model attribute to bind form data
        Category Category = new Category();
        model.addAttribute("category", Category);
        return "new_Category";
    }

    @PostMapping("/dashboard/view_Category/saveCategory")
    public String saveCategory(@ModelAttribute("category") Category category, @RequestParam("categorypic") MultipartFile MultipartFile) throws IOException {
        // save category to database
        Service_Category.saveCategory(category);
        Category Category = new Category();
        Category.setCategorypic(MultipartFile.getBytes());
        Service_Category.saveCategory(Category);
        return "redirect:/dashboard/view_Category";
    }
}
