/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.service;

import com.example.model.Employee;
import java.util.List;

/**
 *
 * @author Pali
 */
public interface EmployeeService {

    List<Employee> getAllEmployees();

    public void saveEmployee(Employee employee);

    Employee getEmployeeById(long id);

    void deleteEmployeeById(long id);

}
