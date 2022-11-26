window.addEventListener('load', function() {
    let buttonAdd= $('#add-to-favorite');
    let buttonRemove = $('#remove-from-favorite');

    buttonAdd.on('click', function(evt) {
        const pk = $('button[data-pk]').data('pk')
        $('button[data-pk]').data('pk').remove()

        let url = 'http://localhost:8000/photos/';

            url : url + `${pk}/like/`,


        $.ajax({
            type: 'POST',
            url : url + `${pk}/to-favorite/`,
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