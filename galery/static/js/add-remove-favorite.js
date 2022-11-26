window.addEventListener('load', function() {
    let buttonAdd= $('#add-to-favorite');
    let buttonRemove = $('#remove-from-favorite');

    buttonAdd.on('click', function(evt) {
        buttonRemove.remove()

        $.ajax({
            type: 'POST',
            url : 'photos/to-favorite/',
            data: {

                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                action:'post',
            },
            success: function(data) {

                alert('Опыт работы добавлен!')
            }
        })


    });
}