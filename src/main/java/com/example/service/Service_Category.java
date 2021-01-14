/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.service;

import com.example.model.Category;
import java.util.List;

/**
 *
 * @author Pali
 */
public interface Service_Category {

    public Category saveCategory(Category category);

    List<Category> getAllCategory();

    void deleteCategoryById(long id);

    public Category getCategoryById(long id);
}
