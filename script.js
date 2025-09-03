document.addEventListener('DOMContentLoaded', () => {

    const apiUrl = 'http://localhost:3000/curriculo';



    // Faz a requisição para a nossa API

    fetch(apiUrl)

        .then(response => {

            if (!response.ok) {

                throw new Error('Erro na requisição: ' + response.statusText);

            }

            return response.json();

        })

        .then(data => {

            preencherCurriculo(data);

        })

        .catch(error => {

            console.error('Falha ao buscar dados do currículo:', error);

            document.body.innerHTML = `<p>Não foi possível carregar as

             informações do currículo. Tente novamente mais tarde.</p>`;

        });

});



function preencherCurriculo(data) {

    document.getElementById('nome').textContent = data.nome;

    document.getElementById('cargo').textContent = data.cargo;

    document.getElementById('resumo').textContent = data.resumo;



    const contatoLista = document.getElementById('contato-lista');

    contatoLista.innerHTML = `

        <li>Email: <a href="mailto:${data.contato.email}">${data.contato.email}</a></li>

        <li>Telefone: ${data.contato.telefone}</li>

        <li>LinkedIn: <a href="${data.contato.linkedin}" target="_blank">${data.contato.linkedin}</a></li>

        <li>GitHub: <a href="${data.contato.github}" target="_blank">${data.contato.github}</a></li>

    `;



    // Preenche a lista de experiências

    const experienciaLista = document.getElementById('experiencia-lista');

    data.experiencia.forEach(exp => {

        const expDiv = document.createElement('div');

        expDiv.innerHTML = `

            <h4>${exp.cargo} na ${exp.empresa}</h4>

            <p><i>${exp.periodo}</i></p>

            <p>${exp.descricao}</p>

        `;

        experienciaLista.appendChild(expDiv);

    });



    // Preenche a formação acadêmica

    const educacaoLista = document.getElementById('educacao-lista');

    data.educacao.forEach(edu => {

        const eduDiv = document.createElement('div');

        eduDiv.innerHTML = `

            <h4>${edu.curso}</h4>

            <p>${edu.instituicao} (${edu.periodo})</p>

        `;

        educacaoLista.appendChild(eduDiv);

    });



    // Preenche a lista de habilidades

    const habilidadesLista = document.getElementById('habilidades-lista');

    data.habilidades.forEach(habilidade => {

        const li = document.createElement('li');

        li.textContent = habilidade;

        habilidadesLista.appendChild(li);

    });

}
