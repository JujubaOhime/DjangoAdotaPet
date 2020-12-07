$(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
        $('#icon-scroll').fadeOut(500);
    } else {
        $('#icon-scroll').fadeIn(500);
    }
});

$(function () {
    $('[data-toggle="popover"]').popover()
})

$('.popover-dismiss').popover({
    trigger: 'focus'
})


$('document').ready(function () {


    $(document).on("blur", ".quantidade", function(e) {
			let valor = $(this).val()
			if (valor < 0 || valor > 99) {
				console.log(this)
				$(this).focus()
				return
			}
			var serializedData = $(this).parent().serialize();
			var tr = $(this).parent().parent().parent()
            var id = $(this).parent().parent().parent().attr("id")

            console.log(id)
            console.log()
            var quantidade = tr.find('.quantidade').val()
            var token = tr.find('input[name=csrfmiddlewaretoken]').val()
            let url = '/pets/ajax_pet_atualiza/'
			$.ajax({
				type:'POST',
				url: url,
				data: {
				    quantidade: quantidade,
                    csrfmiddlewaretoken: token,
                    pet_id: id
                },
				success:function(data){
				    let preco = $(tr).find('.preco').text().replace(',', '.')
                    let novo_total = preco * parseInt(quantidade)
                    novo_total = parseFloat(novo_total)

                    let preco_removido = $(tr).find('td.preco-total').text().replace(',', '.')
                    preco_removido = parseFloat(preco_removido)

                    $(tr).find('td.preco-total').text(novo_total.toFixed(2).replace('.',','))


                    let totalpets = parseFloat($('.total-dinheiro').text().replace(',','.'))
                    let novo_total_pets = totalpets - preco_removido + novo_total
                    novo_total_pets = novo_total_pets.toFixed(2)
                    novo_total_pets = novo_total_pets.replace(".", ",")
					$('.total-dinheiro').text(novo_total_pets)
				},
			})
		})

    $(document).on('click', '.remover-pet', function () {
        pet_id = $(this).attr("id")
        let urldelete = '/pets/ajax_pet_delete/' + pet_id
        $.ajax({
            data: {
               csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
            },
            url: urldelete,
            type: 'POST',
            dataType: 'json',
            success: function (data){
                let tr = "#" + pet_id
                let preco_removido = parseFloat($(tr).find('td.preco-total').text().replace(',', '.'))
                let totalpets = parseFloat($('.total-dinheiro').text().replace(',', '.'))
                console.log(preco_removido, totalpets)
                $('.total-dinheiro').text((totalpets - preco_removido).toFixed(2).replace('.', ','))
                $(tr).remove()
            }
        })
    });

    $('#cadastrar_ajax').on('click', function (e) {
        let nome = $('#id_nome').val()
        let preco = $('#id_preco').val()
        let quantidade = $('#id_quantidade').val()
        $.ajax({
            data: {
                nome: $('#id_nome').val(),
                preco: $('#id_preco').val(),
                quantidade: $('#id_quantidade').val(),
                action: 'POST',
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            type: 'POST',
            url: $(this).attr('pets/ajax_pet/'),

            success: function (data) {
                let preco = parseFloat($('#id_preco').val().replace(',', '.'))
                quantidade = parseInt(quantidade)
                let total = preco * quantidade
                let totalpets = parseFloat($('.total-dinheiro').text().replace(',', '.'))
                $('.total-dinheiro').text((totalpets + total).toFixed(2).replace('.', ','))
                console.log(data.html)

                $("#ajax_pets").prepend(data.html)



            },

        });

        return false;
    });

    $('#id_cpf').mask('000.000.000-00');
    $('#id_rg').mask("99.999.999-9");
    var options = {
        onKeyPress: function (phone, e, field, options) {
            var masks = ['(00) 0000-00000', '(00) 00000-0000'];
            var mask = (phone.length > 14) ? masks[1] : masks[0];
            $('#id_telefone').mask(mask, options);
        }
    };

    $('#id_telefone').mask('(00) 0000-00000', options);
    $("#id_cep").mask("00000-000");
    $("#id_data_nascimento").mask("00/00/0000");


    function limpa_formulário_cep() {
        // Limpa valores do formulário de cep.
        $("#inputDistrict").val("");
        $("#inputCity").val("");
        $("#inputUF").val("");
    }

    $("#id_cep").blur(function () {
        var cep = $(this).val().replace(/\D/g, '');
        if (cep != "") {

            $("#id_cidade").val("...");
            $("#id_estado").val("...");

            //Consulta o webservice viacep.com.br/
            $.getJSON("https://viacep.com.br/ws/" + cep + "/json/?callback=?", function (dados) {

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
        } else {
            //cep sem valor, limpa formulário.
            limpa_formulário_cep();
        }
    });

    $("#formRegister").validate({
        rules: {
            password2: {
                equalTo: "#id_password1",
                minlength: '5'
            },
            password1: {
                minlength: '5'
            },

            first_name: {
                minlength: '3'
            },
            last_name: {
                minlength: '3'
            },

            last_name: {
                minlength: '3'
            },
            username: {
                minlength: '3'
            },
            cpf: {
                minlength: '14'
            },
            rg: {
                minlength: '12'
            },
            inputUF: {
                maxlength: '2'
            },
            cep: {
                minlength: '9'
            },
            data_nascimento: {
                maxlength: '10'
            },


        },
        onfocusout: function (element) {
            this.element(element); // triggers validation
        },
        onkeyup: function (element, event) {
            this.element(element); // triggers validation
        }
    });


    $(".link-like .far.fa-thumbs-up").click(function () {
        let like = $(this).closest('button').find('span').data("like")
        let like_text = $(this).closest('button').find('span').text()
        let dislike = $(this).closest('div').find($(".link-dislike .dislike")).data("dislike")
        let dislike_text = $(this).closest('div').find($(".link-dislike .dislike")).text()


        if (like == like_text) { //se não foi apertado o like:
            $(this).closest('button').find('span').text(like + 1)
            $(this).removeClass("far")
            $(this).addClass("fas")

            if (dislike_text != dislike) {
                $(this).closest('div').find($(".link-dislike .fa-thumbs-down")).removeClass("fas")
                $(this).closest('div').find($(".link-dislike .fa-thumbs-down")).addClass("far")
                $(this).closest('div').find($(".link-dislike .dislike")).text(dislike)
            }

        } else if (like != like_text) { //se já foi apertado o like:
            $(this).closest('button').find('span').text(like)
            $(this).removeClass("fas")
            $(this).addClass("far")

        }

    })

    $(".link-dislike .far.fa-thumbs-down").click(function () {
        let dislike = $(this).closest('button').find('span').data("dislike")
        let dislike_text = $(this).closest('button').find('span').text()
        let like = $(this).closest('div').find($(".link-like .like")).data("like")
        let like_text = $(this).closest('div').find($(".link-like .like")).text()


        if (dislike == dislike_text) { //se não foi apertado o dislike:
            $(this).closest('button').find('span').text(dislike + 1)
            $(this).removeClass("far")
            $(this).addClass("fas")

            if (like_text != like) {
                $(this).closest('div').find($(".link-like .fa-thumbs-up")).removeClass("fas")
                $(this).closest('div').find($(".link-like .fa-thumbs-up")).addClass("far")
                $(this).closest('div').find($(".link-like .like")).text(like)
            }

        } else if (dislike != dislike_text) { // se foi apertado o dislike
            $(this).closest('button').find('span').text(dislike)
            $(this).removeClass("fas")
            $(this).addClass("far")
        }

    })


});

