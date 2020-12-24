/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

/**
 *
 * @author Pali
 */
@Controller
public class StateController {

    @GetMapping("/dashboard/view_State")
    public String viewState() {
        return "view_State";
    }
}
