function cadastrarAluno(nome){
    data = JSON.stringify({nome: nome});

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/aluno",
        contentType: 'application/json',
        data: data,
        success: alert("sucesso"),
        dataType: "json"
    });
}

function excluirAluno(id){
    $.ajax({
        url: 'http://127.0.0.1:5000/alunos/'+id,
        contentType: 'application/json',
        dataType: 'json',
        type: 'DELETE',
        success: function(data, textStatus, jqXHR){
        alert("sucesso");
        consultar();
        },
        error: function(XMLHttpRequest, textStatus, errorThrown){
        alert('sucesso');
        consultar();
        }
        }); 
}

function consultar(){
    $("#tabela-aluno").children().html('');
    $.ajax({
        url: 'http://127.0.0.1:5000/aluno',
        contentType: 'application/json',
        dataType: 'json',
        type: 'GET',
    success: function(data, textStatus, jqXHR){
        $("#tabela-aluno").append("<tr><th>id</th><th>nome</th><th>excluir</th><th>editar</th></tr>");
        for(i = 0; i < data.length;i++){
            $("#tabela-aluno").append("<tr> <td>" + data[i].id + "</td> <td>"+data[i].nome +" </td> <td><img src='img/trash.png' class='botao-excluir' onclick='excluirAluno("+data[i].id+")'/></td><td><img src='img/edit.png' class='botao-editar' /> </td></tr>");
        }
    },
    error: function(XMLHttpRequest, textStatus, errorThrown){
        $("#results").append("error");
    }
    });
}


$(document).ready(function(){
    $("#cadastrar_aluno").click(function(){
        nome = $("#nome").val();
        cadastrarAluno(nome);
    });

    $("#consultar").click(function(){
        consultar();
    });
});