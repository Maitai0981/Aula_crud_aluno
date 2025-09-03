package com.ifam.aula_crud_aluno.models;

import jakarta.persistence.*;
import lombok.*;
import java.time.LocalDate;

@Entity(name = "tb_alunos")
@Getter
@Setter
@ToString(exclude = "imagem")
public class Aluno {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nome;
    private String serie;
    private String sexo;

    @Lob
    @Column(columnDefinition = "LONGBLOB")
    private byte[] imagem;

    private LocalDate data;

    public boolean temImagem() {
        return imagem != null && imagem.length > 0;
    }

    @PrePersist
    public void prePersist() {
        if (this.data == null) {
            this.data = LocalDate.now();
        }
    }
}