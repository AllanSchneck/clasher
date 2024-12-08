


const URL = 'https://api-clash-royale.onrender.com/';

function esconderLoading() {
    const loadingElement = document.querySelector('h1');
    loadingElement.classList.add('hide');
  }

async function getTropaByIndex(index,index2) {
    const resp = await fetch(URL);
    if (resp.status === 200){
        esconderLoading();
    }
    const data = await resp.json();
    if (index < 0 || index >= data.length) {
        console.log("Índice inválido ou item não encontrado.");
        return null;
    }
    const item = data[index];
    const title = document.createElement("h2");
    const title1 = document.createElement("h2");
    const title2 = document.createElement("h2");
    const title3 = document.createElement("h2");
    const title4 = document.createElement("h2");
    const title5 = document.createElement("h2");
    const title6 = document.createElement("h2");
    const title7 = document.createElement("h2");
    const title8 = document.createElement("h2");
    const title9 = document.createElement("h2");
    const title10 = document.createElement("h2");
    const title11 = document.createElement("h2");
    const title12 = document.createElement("h2");
    const div = document.createElement("div");
    const postContainer = document.querySelector("#container_post"+index2);
    console.log(data);
    // Renderiza o item no DOM // Assumindo que 'carta' é o título
    title.innerText = 'ID    :   '+item.id;
    title1.innerText = 'Carta    :   '+item.carta;
    title2.innerText =  'Tipo   :   '+item.tipo;
    title3.innerText =  'Raridade   :   '+item.raridade;
    title4.innerText =  'Elixir     :   '+item.elixir;  
    title5.innerText =  'Vida   :   '+item.vida;
    title6.innerText =  'Dano   :   '+item.dano;
    title7.innerText =  'Velocidade de Impacto  :   '+item.velocidade_de_impacto;
    title8.innerText = 'Alvo    :   '+item.alvo;
    title9.innerText =  'Velocidade :   '+item.velocidade;
    title10.innerText = 'Alcance    :   '+item.alcance;
    title11.innerText =  'Unidades  :   '+item.unidades;
    title12.innerText =  'Especial  :   '+item.especial;
    div.appendChild(title);
    div.appendChild(title1);
    div.appendChild(title2);
    div.appendChild(title3);
    div.appendChild(title4);
    div.appendChild(title5);
    div.appendChild(title6);
    div.appendChild(title7);
    div.appendChild(title8);
    div.appendChild(title9);
    div.appendChild(title10);
    div.appendChild(title11);
    div.appendChild(title12);
    postContainer.appendChild(div);
}

// Chama a função para exibir o item com índice 0


async function getConstrucaoByIndex(index,index2) {
    const resp = await fetch('https://api-clash-royale.onrender.com/construcoes');
    if (resp.status === 200){
        esconderLoading();
    }
    const data = await resp.json();
    if (index < 0 || index >= data.length) {
        console.log("Índice inválido ou item não encontrado.");
        return null;
    }
    const item = data[index];
    const title = document.createElement("h2");
    const title1 = document.createElement("h2");
    const title2 = document.createElement("h2");
    const title3 = document.createElement("h2");
    const title4 = document.createElement("h2");
    const title5 = document.createElement("h2");
    const title6 = document.createElement("h2");
    const title7 = document.createElement("h2");
    const title8 = document.createElement("h2");
    const div = document.createElement("div");
    const postContainer = document.querySelector("#container_post"+index2);
    console.log(data);
    // Renderiza o item no DOM // Assumindo que 'carta' é o título
    title.innerText = 'ID    :   '+item.id;
    title1.innerText = 'Carta    :   '+item.carta;
    title2.innerText =  'Tipo   :   '+item.tipo;
    title3.innerText =  'Raridade   :   '+item.raridade;
    title4.innerText =  'Elixir     :   '+item.elixir; 
    title5.innerText = 'Vida   :   '+item.vida;
    title6.innerText = 'Dano    :   '+item.dano;
    title7.innerText = 'Tempo de Invocação  :   '+item.tempo_de_invocacao;
    title8.innerText =  'Especial :   '+item.especial;
    div.appendChild(title);
    div.appendChild(title1);
    div.appendChild(title2);
    div.appendChild(title3);
    div.appendChild(title4);
    div.appendChild(title5);
    div.appendChild(title6);
    div.appendChild(title7);
    div.appendChild(title8); 
    postContainer.appendChild(div);
}





// Chama a função para exibir o item com índice 0

async function getFeiticoByIndex(index,index2) {
    const resp = await fetch('https://api-clash-royale.onrender.com/feitico');
    if (resp.status === 200){
        esconderLoading();
    }
    const data = await resp.json();
    if (index < 0 || index >= data.length) {
        console.log("Índice inválido ou item não encontrado.");
        return null;
    }
    const item = data[index];
    const title = document.createElement("h2");
    const title1 = document.createElement("h2");
    const title2 = document.createElement("h2");
    const title3 = document.createElement("h2");
    const title4 = document.createElement("h2");
    const title5 = document.createElement("h2");
    const title6 = document.createElement("h2");
    const title7 = document.createElement("h2");
    const title8 = document.createElement("h2");
    const div = document.createElement("div");
    const postContainer = document.querySelector("#container_post"+index2);
    console.log(data);
    // Renderiza o item no DOM // Assumindo que 'carta' é o título
    title.innerText = 'ID    :   '+item.id;
    title1.innerText = 'Carta    :   '+item.carta;
    title2.innerText =  'Tipo   :   '+item.tipo;
    title3.innerText =  'Raridade   :   '+item.raridade;
    title4.innerText =  'Elixir     :   '+item.elixir; 
    title5.innerText = 'Dano em Área    :   '+item.dano_em_area;
    title6.innerText = 'Dano à Torre    :   '+item.dano_a_torre;
    title6.innerText =  'Raio   :   '+item.raio;
    title8.innerText =  'Especial :   '+item.especial;
    div.appendChild(title);
    div.appendChild(title1);
    div.appendChild(title2);
    div.appendChild(title3);
    div.appendChild(title4);
    div.appendChild(title5);
    div.appendChild(title6);
    div.appendChild(title7);
    div.appendChild(title8); 
    postContainer.appendChild(div);
}