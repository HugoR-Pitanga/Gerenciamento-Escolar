$(document).ready(function(){
    function consultar(){
      $("#tabela-nota").children().html('');
        $.ajax({
          url: 'http://127.0.0.1:5000/notas',
          contentType: 'application/json',
          dataType: 'json',
          type: 'GET',
          success: function(data, textStatus, jqXHR){
            $("#tabela-nota").append("<tr><th>nome</th><th>materia</th><th>nota</th></tr>");
            for(i = 0; i < data.length;i++){
            $("#tabela-nota").append("<tr> <td>" + data[i].aluno_id + "</td> <td>"+data[i].materia +" </td><td>"+data[i].nota +" </td> </tr>");
            }
          },
          error: function(XMLHttpRequest, textStatus, errorThrown){
            $("#results").append("error");
            }
        });
    }
     
      $("#consultar").click(function(){
        consultar();
      });

    function lancarNota(idAluno, materia, nota){
      data = JSON.stringify({aluno_id: idAluno, materia: materia, nota:nota});
      $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/notas",
        contentType: 'application/json',
        data: data,
        success: alert("sucesso"),
        dataType: "json"
      });
    }

      $("#lancar_nota").click(function(){
        idAluno = $("#idAluno").val();
        materia = $("#materia").val();
        nota = $("#nota").val();
        lancarNota(idAluno, materia, nota);
      });
});