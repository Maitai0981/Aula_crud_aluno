package com.ifam.aula_crud_aluno.models;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDate;
import java.util.Base64;

@Getter
@Setter
@NoArgsConstructor
public class AlunoResponseDTO {

    private Long id;
    private String nome;
    private String serie;
    private String sexo;
    private LocalDate data;
    private String imagemBase64; // Campo para a imagem em Base64


    public AlunoResponseDTO(Aluno aluno) {
        this.id = aluno.getId();
        this.nome = aluno.getNome();
        this.serie = aluno.getSerie();
        this.sexo = aluno.getSexo();
        this.data = aluno.getData();

        if (aluno.getImagem() != null && aluno.getImagem().length > 0) {
            this.imagemBase64 = "data:image/jpeg;base64," + Base64.getEncoder().encodeToString(aluno.getImagem());
        } else {
            this.imagemBase64 = null;
        }
    }
}