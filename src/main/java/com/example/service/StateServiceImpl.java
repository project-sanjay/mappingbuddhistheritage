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
        return stateRepository.findAll();
    }

    @Override
    public void deleteStateById(long id) {
        this.stateRepository.deleteById(id);
    }

    @Override
    public State getStateById(long id) {
        Optional<State> optional = stateRepository.findById(id);
        State state = null;
        if (optional.isPresent()) {
            state = optional.get();
        } else {
            throw new RuntimeException("Country not found for id::" + id);
        }
        return state;
    }

}
