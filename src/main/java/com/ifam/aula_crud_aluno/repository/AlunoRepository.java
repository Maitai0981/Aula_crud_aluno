package com.ifam.aula_crud_aluno.repository;

import com.ifam.aula_crud_aluno.models.Aluno;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AlunoRepository extends JpaRepository<Aluno, Long> {
}