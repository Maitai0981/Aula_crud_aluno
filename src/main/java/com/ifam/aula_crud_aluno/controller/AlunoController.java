package com.ifam.aula_crud_aluno.controller;

import com.ifam.aula_crud_aluno.models.Aluno;
import com.ifam.aula_crud_aluno.models.AlunoResponseDTO;
import com.ifam.aula_crud_aluno.repository.AlunoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

@RestController
@RequestMapping("/api/alunos")
@CrossOrigin(origins = "*")
public class AlunoController {

    @Autowired
    private AlunoRepository alunoRepository;

    private void setImagem(Aluno aluno, MultipartFile arquivo) {
        if (arquivo != null && !arquivo.isEmpty()) {
            try {
                aluno.setImagem(arquivo.getBytes());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    @PostMapping("/cadastrar")
    public ResponseEntity<AlunoResponseDTO> cadastrar(
            @RequestPart("aluno") Aluno aluno,
            @RequestPart(value = "imagem", required = false) MultipartFile imagem) {

        if (aluno.getNome() == null || aluno.getNome().trim().isEmpty()) {
            return ResponseEntity.badRequest().build();
        }
        setImagem(aluno, imagem);
        Aluno alunoSalvo = alunoRepository.save(aluno);
        return ResponseEntity.ok(new AlunoResponseDTO(alunoSalvo));
    }

    @GetMapping("/listar")
    public List<AlunoResponseDTO> listar() {
        return StreamSupport.stream(alunoRepository.findAll().spliterator(), false)
                .map(AlunoResponseDTO::new)
                .collect(Collectors.toList());
    }

    @GetMapping("/{id}")
    public ResponseEntity<AlunoResponseDTO> buscarPorId(@PathVariable Long id) {
        return alunoRepository.findById(id)
                .map(aluno -> ResponseEntity.ok(new AlunoResponseDTO(aluno)))
                .orElse(ResponseEntity.notFound().build());
    }

    @PutMapping
    public ResponseEntity<AlunoResponseDTO> atualizar(
            @RequestPart("aluno") Aluno dadosAtualizados,
            @RequestPart(value = "imagem", required = false) MultipartFile imagem) {

        return alunoRepository.findById(dadosAtualizados.getId())
                .map(aluno -> {
                    aluno.setNome(dadosAtualizados.getNome());
                    aluno.setSerie(dadosAtualizados.getSerie());
                    aluno.setSexo(dadosAtualizados.getSexo());
                    aluno.setData(dadosAtualizados.getData());

                    setImagem(aluno, imagem);

                    Aluno alunoSalvo = alunoRepository.save(aluno);
                    return ResponseEntity.ok(new AlunoResponseDTO(alunoSalvo));
                })
                .orElse(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> excluir(@PathVariable Long id) {
        if (!alunoRepository.existsById(id)) {
            return ResponseEntity.notFound().build();
        }
        alunoRepository.deleteById(id);
        return ResponseEntity.noContent().build();
    }

    @DeleteMapping("/remover-imagem/{id}")
    public ResponseEntity<Object> removerImagem(@PathVariable Long id) {
        return alunoRepository.findById(id)
                .map(aluno -> {
                    aluno.setImagem(null);
                    alunoRepository.save(aluno);
                    return ResponseEntity.noContent().build();
                })
                .orElse(ResponseEntity.notFound().build());
    }
}