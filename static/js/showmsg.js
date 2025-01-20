document.getElementById('form-de-login').onsubmit = async function (event) {
    event.preventDefault();

    const form = event.target; // pega o evento do click no submit 
    const formData = new FormData(form);

    // Fazer a requisição
    const resposta = await fetch(form.action || '/login', { method: 'POST', body: formData });

    const mensagem = document.getElementById('mensagem');
    
    if (resposta.ok) {
        // Se a resposta for 2xx (sucesso), então trata o redirecionamento
        const redirecionamento = resposta.url;  // Pega a URL para o redirecionamento
        window.location.href = redirecionamento;  // Faz o redirecionamento para a URL
    } else {
        // Se a resposta for de erro, mostra a mensagem de erro
        const data = await resposta.json();
        mensagem.textContent = data.message;
        mensagem.style.color = 'red';
    }
};
