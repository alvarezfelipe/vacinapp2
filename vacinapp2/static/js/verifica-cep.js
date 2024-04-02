function getAddress() {
    var cep = document.getElementById("id_cep")
    var endereco = document.getElementById("id_endereco")
    var estado = document.getElementById("id_estado")
    var cidade = document.getElementById("id_cidade")
    var bairro = document.getElementById("id_bairro")

    fetch(`https://viacep.com.br/ws/${cep.value}/json/`)
        .then(response => response.json())
        .then(data => {
            endereco.value = "logradouro" in data ? data.logradouro : ""
            estado.value = "uf" in data ? data.uf : ""
            cidade.value = "localidade" in data ? data.localidade : ""
            bairro.value = "bairro" in data ? data.bairro : ""
        })
        .catch(() => {
            endereco.value = estado.value = cidade.value = bairro.value = ""
        })
}

// var maskCPF = IMask(document.getElementById('id_cpf'), {
//     mask: '000.000.000-00'
// })

// var maskPostalCode = IMask(document.getElementById('id_cep'), {
//     mask: '00000-000'
// })