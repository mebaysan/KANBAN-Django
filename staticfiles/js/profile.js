$("#takim_yonet_btn").on('click', function () {
    let takim_slug = $(this).attr('data-slug');
    let url = $("#ajax_url").val();
    let form_data = new FormData(); // FormData instance oluşturduk
    form_data.append('takim_slug', takim_slug); // form data'ya  değer ekledik (key-value)
    form_data.append('islem_tipi', 'takim_detay_getir');
    $.ajax({
        url: url, // url'e istek atıyoruz
        type: "post", // post request
        data: form_data, // veri olarak form_data değişkenini yolluyoruz
        contentType: false,
        processData: false,
        success: function (data) {
            if (data.success === true) {
                $("#guncelle_takim_ad").val(data.takim_ad);
                $("#guncelle_takim_aciklama").val(data.takim_aciklama);
                $("#takim_guncelle_slug").val(takim_slug);
            }
        }
    });
});


$("#takim_guncelle_btn").on('click', function (e) {
    e.preventDefault();
    let takim_ad = $("#guncelle_takim_ad").val();
    let takim_aciklama = $("#guncelle_takim_aciklama").val();
    let takim_slug = $("#takim_guncelle_slug").val();
    let url = $("#ajax_url").val();
    let form_data = new FormData(); // FormData instance oluşturduk
    form_data.append('takim_ad', takim_ad); // form data'ya  değer ekledik (key-value)
    form_data.append('takim_aciklama', takim_aciklama); // form data'ya  değer ekledik (key-value)
    form_data.append('takim_slug', takim_slug); // form data'ya  değer ekledik (key-value)
    form_data.append('islem_tipi', 'takim_guncelle');
    $.ajax({
        url: url, // url'e istek atıyoruz
        type: "post", // post request
        data: form_data, // veri olarak form_data değişkenini yolluyoruz
        contentType: false,
        processData: false,
        success: function (data) {
            if (data.success === true) {
                location.reload();
            }
        }
    });
});