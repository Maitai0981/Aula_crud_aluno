const API  = '';
const BASE = '/api/alunos';

const formulario       = document.querySelector('form');
const Inome            = document.querySelector('.nome');
const Iserie           = document.querySelector('.serie');
const Isexo            = document.querySelector('.sexo');
const Idata            = document.querySelector('.data');
const Iid              = document.getElementById('id');
const limparBtn        = document.getElementById('limparBtn');
const recarregarBtn    = document.getElementById('recarregarBtn');
const tbody            = document.querySelector('#tabela tbody');
const msg              = document.getElementById('msg');
const imageInput       = document.getElementById('imageInput');
const imagePreview     = document.getElementById('imagePreview');
const imagePlaceholder = document.getElementById('imagePlaceholder');
const removeImageBtn   = document.getElementById('removeImageBtn');
const imageModal       = document.getElementById('imageModal');
const modalImage       = document.getElementById('modalImage');

function setMsg(t, err=false){
    msg.textContent = t || '';
    msg.className   = err ? 'err' : '';
}
function formatDate(v){
    if(!v) return '';
    const d = new Date(v);
    return isNaN(d) ? v : d.toISOString().slice(0,10);
}

async function handleResponse(res) {
    if (!res.ok) {
        const errorBody = await res.text();
        throw new Error(`HTTP ${res.status}: ${errorBody}`);
    }
    const contentType = res.headers.get("content-type");
    if (contentType && contentType.indexOf("application/json") !== -1) {
        return res.json();
    }
    return null;
}

function listar(){
    fetch(API + BASE + '/listar', { headers: { 'Accept': 'application/json' } })
        .then(handleResponse)
        .then(renderTabela)
        .catch(err => setMsg('Erro ao listar: ' + err, true));
}

function salvar(formData, method = 'POST', url = API + BASE + '/cadastrar'){
    return fetch(url, { method: method, body: formData }).then(handleResponse);
}

function obter(id){
    return fetch(`${API}${BASE}/${id}`, { headers: { 'Accept': 'application/json' } })
        .then(handleResponse);
}

function excluir(id){
    return fetch(`${API}${BASE}/${id}`, { method: 'DELETE' }).then(handleResponse);
}

function removerImagemAluno(alunoId){
    return fetch(`${API}${BASE}/remover-imagem/${alunoId}`, { method: 'DELETE' })
        .then(handleResponse);
}

function renderTabela(lista){
    tbody.innerHTML = '';
    if(!lista || !lista.length){
        tbody.innerHTML = '<tr><td colspan="6">Nenhum aluno.</td></tr>';
        return;
    }
    lista.forEach(a => {
        const tr = document.createElement('tr');
        let imagemHtml = '';
        if(a.imagemBase64){
            imagemHtml = `<img src="${a.imagemBase64}" class="table-image" alt="Foto de ${a.nome}" onclick="ampliarImagem('${a.imagemBase64.replace(/'/g, '&#39;')}')" title="Clique para ampliar">`;
        } else {
            const inicial = a.nome ? a.nome.charAt(0).toUpperCase() : '?';
            imagemHtml = `<div class="table-placeholder">${inicial}</div>`;
        }
        tr.innerHTML = `
            <td>${imagemHtml}</td>
            <td>${a.nome || ''}</td>
            <td>${a.serie || ''}</td>
            <td>${a.sexo || ''}</td>
            <td>${formatDate(a.data) || ''}</td>
            <td>
                <a class="action" data-act="edit" data-id="${a.id}">Editar</a>
                <a class="action" data-act="del"  data-id="${a.id}">Excluir</a>
            </td>`;
        tbody.appendChild(tr);
    });
}

function limpar(){
    formulario.reset();
    Iid.value = '';
    setMsg('');
    limparPreviewImagem();
}

function mostrarPreview(base64) {
    imagePreview.src = base64;
    imagePreview.style.display = 'block';
    imagePlaceholder.style.display = 'none';
    removeImageBtn.style.display = 'inline-block';
}

function limparPreviewImagem() {
    imagePreview.src = '';
    imagePreview.style.display = 'none';
    imagePlaceholder.style.display = 'flex';
    removeImageBtn.style.display = 'none';
    imageInput.value = '';
}

function handleImageSelect(file) {
    if(!file) return;
    if(!file.type.startsWith('image/')){
        setMsg('Por favor, selecione apenas arquivos de imagem.', true);
        return;
    }
    if(file.size > 10 * 1024 * 1024){ // 10MB
        setMsg('A imagem deve ter no máximo 10MB.', true);
        return;
    }
    const reader = new FileReader();
    reader.onload = e => mostrarPreview(e.target.result);
    reader.readAsDataURL(file);
}

function ampliarImagem(base64) {
    modalImage.src = base64.replace(/&#39;/g, "'");
    imageModal.style.display = 'block';
}

function fecharModal() {
    imageModal.style.display = 'none';
}

formulario.addEventListener('submit', function(event){
    event.preventDefault();

    const dadosAluno = {
        nome:  Inome.value.trim(),
        serie: Iserie.value.trim(),
        sexo:  Isexo.value,
        data:  Idata.value || null
    };

    if(!dadosAluno.nome){
        setMsg('O nome é obrigatório.', true);
        return;
    }

    const formData = new FormData();
    formData.append('aluno', new Blob([JSON.stringify(dadosAluno)], { type: 'application/json' }));

    if (imageInput.files[0]) {
        formData.append('imagem', imageInput.files[0]);
    }

    let promise;
    if (Iid.value) {
        dadosAluno.id = Number(Iid.value);
        formData.set('aluno', new Blob([JSON.stringify(dadosAluno)], { type: 'application/json' }));
        promise = salvar(formData, 'PUT', API + BASE);
    } else {
        promise = salvar(formData, 'POST', API + BASE + '/cadastrar');
    }

    promise.then(() => {
        setMsg('Aluno salvo com sucesso!');
        limpar();
        listar();
    }).catch(err => {
        setMsg('Erro ao salvar: ' + err.message, true);
    });
});

tbody.addEventListener('click', function(ev){
    const a = ev.target.closest('a.action');
    if(!a) return;

    const id  = a.getAttribute('data-id');
    const act = a.getAttribute('data-act');

    if(act === 'edit'){
        obter(id).then(aluno => {
            Iid.value    = aluno.id   || '';
            Inome.value  = aluno.nome || '';
            Iserie.value = aluno.serie|| '';
            Isexo.value  = aluno.sexo || '';
            Idata.value  = formatDate(aluno.data);

            if (aluno.imagemBase64) {
                mostrarPreview(aluno.imagemBase64);
            } else {
                limparPreviewImagem();
            }
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }).catch(err => setMsg('Erro ao carregar aluno: ' + err.message, true));
    }

    if(act === 'del'){
        if(confirm('Tem certeza que deseja excluir este aluno?')){
            excluir(id)
                .then(() => {
                    setMsg('Aluno excluído com sucesso.');
                    listar();
                })
                .catch(err => setMsg('Erro ao excluir: ' + err.message, true));
        }
    }
});

limparBtn.addEventListener('click', limpar);
recarregarBtn.addEventListener('click', listar);

imageInput.addEventListener('change', e => handleImageSelect(e.target.files[0]));
removeImageBtn.addEventListener('click', () => {
    limparPreviewImagem();

    if(Iid.value){
        if(confirm("Deseja remover a imagem salva deste aluno também?")){
            removerImagemAluno(Iid.value)
                .then(() => {
                    setMsg("Imagem removida do servidor.");
                    listar(); // Atualiza a tabela
                })
                .catch(err => setMsg("Erro ao remover imagem do servidor: " + err, true));
        }
    }
});

imageModal.addEventListener('click', e => { if (e.target === imageModal) fecharModal() });
document.addEventListener('keydown', e => { if (e.key === 'Escape') fecharModal() });

listar();