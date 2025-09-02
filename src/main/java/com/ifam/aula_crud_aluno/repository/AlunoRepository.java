package com.ifam.aula_crud_aluno.repository;

import com.ifam.aula_crud_aluno.models.Aluno;
import org.springframework.data.repository.CrudRepository;

public interface AlunoRepository extends CrudRepository<Aluno, Long> {

}
