/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

/**
 *
 * @author Pali
 */
@Controller
@RequestMapping("/view_City")
public class CityController {

    @GetMapping()
    public String viewCity() {
        return "view_City";
    }
}
