/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.service;

import com.example.model.Category;
import com.example.repository.Repository_Category;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 *
 * @author Pali
 */
@Service
public class Implement_Service_Category implements Service_Category {

    @Autowired
    Repository_Category Repository_Category;

    @Override
    public void saveCategory(Category Category) {
        this.Repository_Category.save(Category);
    }

}
