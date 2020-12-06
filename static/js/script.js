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

    $('#cadastrar_ajax').on('click', function (e) {
        console.log("apertou")
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
            success: function (json) {
                let total = $('#id_quantidade').val() * $('#id_preco').val()
                let totalpets = parseFloat($('.total-dinheiro').text())
                $('.total-dinheiro').text(totalpets + total)
                $("#ajax_pets").prepend(
                    '<tr>' +
                        '<td class="text-center align-middle">' +
                           nome +
                        '</td>' +
                        '<td class="text-center align-middle">' +
                           preco +
                        '</td>' +
                        '<td class="text-center align-middle">' +
                           quantidade +
                        '</td>' +
                        '<td class="text-center align-middle">' +
                           total +
                        '</td>' +
                        '<td class="text-center align-middle d-inline-flex justify-content-center align-items-center w-100">' +
                            '<button type="button" id="remover-pet" class="text-decoration-none border-0 p-0 confirm-delete" style="background: none ">' +
                            '<i class="fas fa-trash-alt mr-1 ml-1" style="color: var(--danger)"></i>' +
                        '</td>' +
                    '</tr>'
                )
            },

        });

        return false;
    });

    $('#cadastrar_ajax').on('click', function (e) {
        console.log("apertou")
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

    document.getElementById("id_data_nascimento").max = "2007-01-01";


});

