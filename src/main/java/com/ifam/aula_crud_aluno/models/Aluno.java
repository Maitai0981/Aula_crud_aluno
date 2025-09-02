package com.ifam.aula_crud_aluno.models;

import jakarta.persistence.*;
import lombok.*;


@Entity(name= "tb_alunos")
@Getter
@Setter
public class Aluno {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String nome;
    private String serie;
    private String sexo;
}
