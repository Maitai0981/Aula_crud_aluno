package com.ifam.aula_crud_aluno.controller;


import com.ifam.aula_crud_aluno.models.Aluno;
import com.ifam.aula_crud_aluno.repository.AlunoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/alunos")
public class AlunoController {
    @Autowired
    private AlunoRepository alunoRepository;

    @PostMapping("/cadastrar")
    public Aluno cadastrar(@RequestBody Aluno obj) {
       return alunoRepository.save(obj);
    }

    @GetMapping("/listar")
    public Iterable<Aluno> listar() {
        return alunoRepository.findAll();
    }
}
