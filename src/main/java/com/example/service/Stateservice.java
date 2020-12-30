/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.service;
import com.example.model.State;
import java.util.List;
/**
 *
 * @author Pali
 */
public interface Stateservice {

    public void saveState(State State);
    List<State> getAllState();
    void deleteStateById(long id);
    State getStateById(long id);
}
