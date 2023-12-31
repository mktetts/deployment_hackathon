package org.codeshift.service;

import java.util.List;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import jakarta.transaction.Transactional;

import org.codeshift.dao.PatientDao;
import org.codeshift.model.Patient;

@ApplicationScoped
@Transactional
public class PatientServiceImpl implements PatientService {
	
	@Inject
	PatientDao patientDao;
	
	@Override
	public List<Patient> findAll() {
		return this.patientDao.listAll();
	}
	
	@Override
	public Patient findById(Long personId) {
		return this.patientDao.findById(personId);
	}

	@Override
	public Patient findByEmail(String email) {
		return this.patientDao.findByEmail(email);
	}
	
	@Override
	public void save(Patient person) {
		this.patientDao.persist(person);
	}
	
	@Override
	public void update(Patient person) {
		this.patientDao.persist(person);
	}
	
	@Override
	public void deleteById(Long personId) {
		this.patientDao.deleteById(personId);
	}
	@Override
	public void deleteByEmail(String email) {
		this.patientDao.deleteByEmail(email);
	}
}





