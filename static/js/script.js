$(window).scroll(function() {
    if ($(this).scrollTop()>100)
     {
        $('#icon-scroll').fadeOut(500);
     }
    else
     {
      $('#icon-scroll').fadeIn(500);
     }
 });

 $(function () {
    $('[data-toggle="popover"]').popover()
  })

  $('.popover-dismiss').popover({
    trigger: 'focus'
  })


$('document').ready(function(){
    $('#id_cpf').mask('000.000.000-00');
    $('#id_rg').mask("99.999.999-9");
    $("#id_telefone").mask("(00) 0000-00009");
    $("#id_cep").mask("00000-000");


    $("#formRegister").validate({
      rules: {  
        password2 : {
					equalTo : "#id_password1"
        },
        cpf :{
          minlength : '14'
        },
        rg :{
          minlength : '12'
        },
        estado :{
          maxlength : '2'
        },
        checkbox :{
          required : true
        },

      }

      
    });

  function limpa_formulário_cep() {
    // Limpa valores do formulário de cep.
    $("#inputDistrict").val("");
    $("#inputCity").val("");
    $("#inputUF").val("");
  }

  $("#id_cep").blur(function() {
    var cep = $(this).val().replace(/\D/g, '');
    if (cep != ""){

      $("#id_cidade").val("...");
      $("#id_estado").val("...");

      //Consulta o webservice viacep.com.br/
      $.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {

          if (!("erro" in dados)) {
              //Atualiza os campos com os valores da consulta.
              $("#id_cidade").val(dados.localidade);
              $("#id_estado").val(dados.uf);
          } //end if.
          else {
              //CEP pesquisado não foi encontrado.
              limpa_formulário_cep();
              alert("CEP não encontrado.");
          }
      });
    }
    else{
      //cep sem valor, limpa formulário.
      limpa_formulário_cep();
    }
  });


  $(".link-like .far.fa-thumbs-up").click(function(){
    let like = $(this).closest('button').find('span').data("like")
    let like_text = $(this).closest('button').find('span').text()
    let dislike = $(this).closest('div').find($(".link-dislike .dislike")).data("dislike")
    let dislike_text = $(this).closest('div').find($(".link-dislike .dislike")).text()
    

    if(like == like_text){ //se não foi apertado o like:
      $(this).closest('button').find('span').text(like + 1)
      $(this).removeClass("far")
      $(this).addClass("fas")

      if(dislike_text != dislike){
        $(this).closest('div').find($(".link-dislike .fa-thumbs-down")).removeClass("fas")
        $(this).closest('div').find($(".link-dislike .fa-thumbs-down")).addClass("far")
        $(this).closest('div').find($(".link-dislike .dislike")).text(dislike)
      }

    }
    else if(like  != like_text){ //se já foi apertado o like:
      $(this).closest('button').find('span').text(like)
      $(this).removeClass("fas")
      $(this).addClass("far")

    }

  })

  $(".link-dislike .far.fa-thumbs-down").click(function(){
    let dislike = $(this).closest('button').find('span').data("dislike")
    let dislike_text = $(this).closest('button').find('span').text()
    let like = $(this).closest('div').find($(".link-like .like")).data("like")
    let like_text = $(this).closest('div').find($(".link-like .like")).text()
    

    if(dislike == dislike_text){ //se não foi apertado o dislike:
      $(this).closest('button').find('span').text(dislike + 1)
      $(this).removeClass("far")
      $(this).addClass("fas")

      if (like_text != like){
        $(this).closest('div').find($(".link-like .fa-thumbs-up")).removeClass("fas")
        $(this).closest('div').find($(".link-like .fa-thumbs-up")).addClass("far")
        $(this).closest('div').find($(".link-like .like")).text(like)
      }

    }
    else if(dislike  != dislike_text){ // se foi apertado o dislike
      $(this).closest('button').find('span').text(dislike)
      $(this).removeClass("fas")
      $(this).addClass("far")
    }

  })



  




});