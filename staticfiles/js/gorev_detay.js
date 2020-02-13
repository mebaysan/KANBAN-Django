$(".custom-control-label").on('click', function () {
    let islem_pk = $(this).attr('data-pk');
    let url = $("#ajax_url").val();
    let form_data = new FormData(); // FormData instance oluşturduk
    form_data.append('islem_pk', islem_pk); // form data'ya  değer ekledik (key-value)
    form_data.append('islem_tipi', 'gorev_islem_tipi_degistir');
    $.ajax({
        url: url,
        type: "post",
        data: form_data,
        contentType: false,
        processData: false,
        success: function (data) {
            if (data.success === true) {
                location.reload();
            } else {
                alert("Hata");
            }
        }
    });
});