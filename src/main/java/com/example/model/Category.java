/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.model;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Lob;
import javax.persistence.Table;

/**
 *
 * @author Pali
 */
@Entity
@Table(name = "Category")
public class Category {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id_category;

    @Column(nullable = false, unique = true)
    private String categoryname;

    @Column(nullable = false, unique = true)
    private byte[] categorypic;

    /**
     * @return the id_category
     */
    public Long getId_category() {
        return id_category;
    }

    /**
     * @param id_category the id_category to set
     */
    public void setId_category(Long id_category) {
        this.id_category = id_category;
    }

    /**
     * @return the categoryname
     */
    public String getCategoryname() {
        return categoryname;
    }

    /**
     * @param categoryname the categoryname to set
     */
    public void setCategoryname(String categoryname) {
        this.categoryname = categoryname;
    }


    /**
     * @return the categorypic
     */
    public byte[] getCategorypic() {
        return categorypic;
    }

    /**
     * @param categorypic the categorypic to set
     */
    public void setCategorypic(byte[] categorypic) {
        this.categorypic = categorypic;
    }

}
