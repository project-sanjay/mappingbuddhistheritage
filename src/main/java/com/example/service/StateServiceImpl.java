/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.service;

import com.example.model.State;
import com.example.repository.StateRepository;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;
import org.springframework.beans.factory.annotation.Autowired;

/**
 *
 * @author Pali
 */
@Service
public class StateServiceImpl implements Stateservice {

    @Autowired
    StateRepository stateRepository;

    @Override
    public void saveState(State State) {
        this.stateRepository.save(State);
    }

    @Override
    public List<State> getAllState() {
        this.stateRepository.findAll();
    }

}
